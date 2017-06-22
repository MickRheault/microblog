from django.conf import settings
from rest_framework import serializers

from article.models import Article
from tag.models import Tag


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'desc', 'author', 'creation_date', 'tags')


class ArticleAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ('image', 'author')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title', 'created_by', 'creation_date')


class TagAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('created_by',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('id', 'username', 'first_name', 'last_name')