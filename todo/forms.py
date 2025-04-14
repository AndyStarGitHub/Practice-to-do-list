from django.forms import forms

from todo.models import Tag


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
