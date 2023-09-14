from django import forms
from .models import Categories, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields["author"].widget = forms.Select(
            attrs={"class": "form-control"}
        )
        self.fields["categories"].widget = forms.CheckboxSelectMultiple()
