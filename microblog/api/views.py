from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from article.models import Article
from tag.models import Tag

from .serializers import ArticleSerializer, ArticleAddSerializer, TagSerializer, UserSerializer
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


class ArticleCreateView(APIView):
    model = Article
    http_method_names = ['put']
    serializer = ArticleAddSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


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