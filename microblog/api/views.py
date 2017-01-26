from django.contrib.auth.models import User

from rest_framework.views import APIView

from article.models import Article
from tag.models import Tag

from .serializers import ArticleSerializer, TagSerializer, UserSerializer
from .mixins import ListSerializerMixin, LastListSerializerMixin, DetailSerializerMixin


class ArticleList(ListSerializerMixin, APIView):
    http_method_names = ['get']
    model = Article
    serializer = ArticleSerializer


class ArticleListLast(LastListSerializerMixin, APIView):
    http_method_names = ['get']
    model = Article
    serializer = ArticleSerializer


class ArticleDetail(DetailSerializerMixin, APIView):
    http_method_names = ['get']
    model = Article
    serializer = ArticleSerializer


class TagList(ListSerializerMixin, APIView):
    http_method_names = ['get']
    model = Tag
    serializer = TagSerializer


class TagListLast(LastListSerializerMixin, APIView):
    http_method_names = ['get']
    model = Tag
    serializer = TagSerializer


class TagDetail(DetailSerializerMixin, APIView):
    http_method_names = ['get']
    model = Tag
    serializer = TagSerializer


class UserListView(ListSerializerMixin, APIView):
    http_method_names = ['get']
    model = User
    serializer = UserSerializer
