from django.db import models
from django.core.exceptions import ValidationError


def validate_title(value):
    if len(value.split(" ")) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, blank=False, validators=[validate_title]
    )
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
        "Users", on_delete=models.CASCADE, null=False, blank=False
    )
    created_at = models.DateField(null=False, blank=False)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
