from django import forms
from .models import Course, Post, Enrollment



class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title',
                  'image',
                  'description',
                  'tags',)



class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
                  'image',
                  'file',
                  'description',
                  'tags',
                  'is_draft',
                  )
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "file":forms.FileInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "is_draft":forms.CheckboxInput(attrs={"class":"form-control"}),
            "tags":forms.SelectMultiple(attrs={"class":"form-control"})
        }