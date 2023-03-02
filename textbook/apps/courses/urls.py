
from django.urls import path
from apps.courses import views


urlpatterns = [
    path("", views.IndexPage.as_view(), name="index"),
    path("courses/list/", views.CourseListView.as_view(), name="courses_list"),
    path("course/<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),

    path("blog/create/", views.PostCreateView.as_view(), name="create_blog"),
    path("post/list", views.PostListView.as_view(), name="blog_display"),
    path("teachers/list", views.TeachersListView.as_view(), name="teachers_list"),

    path("enrollment/<int:course_id>/", views.subscribe_course, name="subscribe_course"),
    path("teacher/courses", views.TeacherCourseListView.as_view(), name="teacher_course"),

    path("module/<int:pk>", views.ModuleDetailView.as_view(), name="module"),
    path("my/courses/", views.get_my_enrollments, name="my_courses"),
    path("progress/<int:module_id>/", views.finish_module, name="progress"),
    path("books/", views.BookList.as_view(), name="books"),
    path("blog/detail/<int:pk>", views.BlogDetail.as_view(), name="blog_detail")






]