from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from article.models import Article
from tag.models import Tag

from .serializers import ArticleSerializer, ArticleAddSerializer, TagSerializer, TagAddSerializer, UserSerializer
from .mixins import ListSerializerMixin, LastListSerializerMixin, DetailSerializerMixin, \
    CreationMixin, DeleteMixin, ArticleListSerializerMixin, ArticleLastListSerializerMixin, \
    ArticleDetailSerializerMixin


class ArticleList(ArticleListSerializerMixin, APIView):
    http_method_names = ['get']
    model = Article
    serializer = ArticleSerializer


class ArticleListLast(ArticleLastListSerializerMixin, APIView):
    http_method_names = ['get']
    model = Article
    serializer = ArticleSerializer


class ArticleDetail(ArticleDetailSerializerMixin, APIView):
    http_method_names = ['get']
    model = Article
    serializer = ArticleSerializer


class ArticleCreateView(CreationMixin, APIView):
    model = Article
    http_method_names = ['put']
    serializer = ArticleAddSerializer
    permission_classes = (IsAuthenticated,)
    author_field_name = 'author'


class ArticleDeleteView(DeleteMixin, APIView):
    model = Article
    http_method_names = ['delete']
    permission_classes = (IsAuthenticated, )
    author_field_name = 'author'


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


class TagCreateView(CreationMixin, APIView):
    model = Tag
    http_method_names = ['put']
    serializer = TagAddSerializer
    permission_classes = (IsAuthenticated,)
    author_field_name = 'created_by'


class TagDeleteView(DeleteMixin, APIView):
    model = Tag
    http_method_names = ['delete']
    permission_classes = (IsAuthenticated,)
    author_field_name = 'created_by'


class UserListView(ListSerializerMixin, APIView):
    http_method_names = ['get']
    model = settings.AUTH_USER_MODEL
    serializer = UserSerializer
