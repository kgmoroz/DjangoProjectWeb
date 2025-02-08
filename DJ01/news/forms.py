from django import forms
from .models import News_post

class News_postForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        label="Дата и время публикации"
    )

    class Meta:
        model = News_post
        fields = ["title", "short_description", "text", "pub_date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите заголовок"}),
            "short_description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите краткое описание"}),
            "text": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Введите текст новости"}),
            "pub_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        }
