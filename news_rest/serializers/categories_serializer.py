from rest_framework import serializers
from news.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id", "name"]
