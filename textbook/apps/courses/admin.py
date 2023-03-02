from django.contrib import admin
# from django import forms

from apps.courses.models import Tag, Course, Module, Content, Post, Enrollment, Progress, Book
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "teacher", "description", "created", "updated",]
    list_filter = ["created", "updated"]
    filter_horizontal = ["tags"]

class ContentInline(admin.TabularInline):
    model = Content

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ContentInline]
    list_display = ["course", "title", "description", "order_id"]
    list_filter = ["course"]
    search_fields = ["title"]



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ["title",
                    "description",
                    "image",
                    "file",
                    "created",
                    "updated",
                    "is_draft",]
    list_filter = ["tags"]
    search_fields = ["title"]
    filter_horizontal = ["tags"]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["student",
                    "course",
                    "date_enrolled",
                    "status"]
    list_editable = ["status"]


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = [
                    "user",
                    "module", ]




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "file",
        "image"
    ]

