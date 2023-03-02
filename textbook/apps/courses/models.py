from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from apps.accounts.models import User




class Tag(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField("Название", max_length=255)
    teacher = models.ForeignKey(User,
                                related_name='course_created',
                                on_delete=models.CASCADE)
    image = models.ImageField("Фото", null=True)
    description = models.TextField("Описание")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="tg_posts")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


    def __str__(self):
       return self.title

class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    video = models.URLField(max_length=200)
    file = models.FileField("Файл", null=True)
    order_id = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"
        ordering = ["order_id"]

    def __str__(self):
        return self.title








class Post(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Фото")
    file = models.FileField("Файл")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    is_draft = models.BooleanField("Черновик", default=True)
    tags = models.ManyToManyField(Tag,
            related_name="posts_tag")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    PENDING_STATUS = "pending"
    APPROVED_STATUS = "approved"
    REJECTED_STATUS = "rejected"
    STATUS_CHOICES = (
        (PENDING_STATUS, 'Pending'),
        (APPROVED_STATUS, 'Approved'),
        (REJECTED_STATUS, 'Rejected')
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    date_enrolled = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
    def __str__(self):
        return f"{self.student.email}-{self.course.title}"



class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    file = models.FileField(upload_to="module/course/")

    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контенты"





class Progress(models.Model):
    module = models.ForeignKey(Module,
                               related_name="finished_module",
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             related_name="progress_module",
                             on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Пргоресс"
        verbose_name_plural = "Прогрессы"

    def __str__(self):
        return self.name



class Book(models.Model):
    name = models.CharField("Название", max_length=255, null=True)
    image = models.ImageField("Фото")
    file = models.FileField("Файл")
    description = models.TextField("Описание", null=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name

