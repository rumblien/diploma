from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, FormView, TemplateView,  CreateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.core.paginator import Paginator

from apps.courses.models import Tag, Course, Module, Post, Enrollment, Progress, Book
from apps.accounts.models import User




class IndexPage(TemplateView):
    template_name = "index.html"




class CourseListView(ListView):
    paginate_by = 4
    model = Course
    template_name = "courses.html"
    queryset = Course.objects.all()


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"
    queryset = Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        if self.request.user.is_authenticated:
            context["is_subscribed"] = Enrollment.objects.filter(
                student=self.request.user,
                course=course
            ).exists()
        else:
            context["is_subscribed"] = False
        module_ids = Progress.objects.filter(
            module_id__course__id=course.id,
            user=self.request.user,
        ).values_list("module_id__id")
        # left_modules = course.modules.exclude(id__in=module_ids)
        completed_module_count = len(module_ids)
        total = len(course.modules.all())
        if completed_module_count == 0:
            context["percent"] = 0
        else:
            percent = completed_module_count * 100 / total
            context["percent"] = percent



        return context




from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostCreateForm


class PostCreateView(LoginRequiredMixin, FormView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('create_blog')
    login_url = reverse_lazy('login')
    template_name = "blog_create.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostListView(ListView):
    paginate_by = 2
    model = Post
    template_name = "blog_display.html"
    queryset = Post.objects.all()


class BlogDetail(DetailView):
    model = Post
    template_name = "blog_detail.html"
    queryset = Post.objects.all()


class TeachersListView(ListView):
    paginate_by = 2
    model = User
    template_name = "t_list.html"
    queryset = User.objects.filter(role=User.ROLE_MENTOR)


class TeacherCourseListView(ListView):
    paginate_by = 4
    model = Course
    template_name = "teacher_courses.html"
    queryset = Course.objects.all()


class BookList(ListView):
    paginate_by = 7
    model = Book
    template_name = "books.html"
    queryset = Book.objects.all()





from django.shortcuts import render, redirect
from .models import Course, Enrollment
from django.shortcuts import get_object_or_404


@login_required
def subscribe_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user = request.user
    if not Enrollment.objects.filter(course=course, student=user).exists():
        Enrollment.objects.create(
            course=course,
            student=user,
            status=Enrollment.PENDING_STATUS
        )

    return redirect(reverse_lazy("course_detail", kwargs={"pk": course.id}))


@login_required
def get_my_enrollments(request):

    enrollments = Enrollment.objects.filter(student=request.user)

    context = {'enrollments': enrollments, }
    return render(request, 'student_courses.html', context)

from django.shortcuts import get_object_or_404
class ModuleDetailView(UserPassesTestMixin, DetailView):

    model = Module
    template_name = "module.html"
    def test_func(self):
        module = self.get_object()
        course = module.course
        enrollment = get_object_or_404(Enrollment, student=self.request.user, course=course)
        if enrollment.status.lower() == 'approved':

            return True
        else:
            return False


@login_required
def finish_module(request, module_id):


    module = get_object_or_404(Module, pk=module_id)
    progress = Progress.objects.create(
        user=request.user,
        module=module,
        )
    return redirect(reverse_lazy("course_detail", kwargs={"pk": module.course.id}))



















