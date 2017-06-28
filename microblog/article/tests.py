import factory

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from factory.django import DjangoModelFactory
from django.utils.crypto import get_random_string

from account.models import User
from tag.models import Tag

from .models import Article
from .views import ArticleListView, ArticleDetailView, SearchView, ArticleAuthorListView


class LoginError(Exception):
    pass


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    title = factory.Sequence(lambda n: "tag_{0}".format(n))
    slug = factory.Sequence(lambda n: "tag{0}".format(n))


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_{0}".format(n))


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Sequence(lambda n: "title_{0}".format(n))
    slug = factory.Sequence(lambda n: "title{0}".format(n))
    status = Article.PUBLISHED


class ArticleViewTestCase(TestCase):
    def setUp(self):
        passw = get_random_string(32)
        staff = AuthorFactory.build()
        staff.set_password(passw)
        staff.is_staff = True
        setattr(staff, 'ps', passw)
        staff.save()
        self.staff = staff

        passw = get_random_string(32)
        user = AuthorFactory.build()
        user.set_password(passw)
        setattr(user, 'ps', passw)
        user.save()
        self.user = user

        tag = TagFactory(created_by=user)

        for _ in range(20):
            ArticleFactory(author=user)

        for _ in range(4):
            a = ArticleFactory(author=user)
            a.tags.add(tag)
            a.save()

    @staticmethod
    def if_logged(login):
            if not login:
                raise LoginError

    def test_article_preview_view_as_author(self):
        passw = get_random_string(32)
        client = Client()

        author = AuthorFactory.build()
        author.set_password(passw)
        author.save()

        article = ArticleFactory(author=author)

        author = article.author
        self.if_logged(client.login(username=author.username, password=passw))

        resp = client.get(reverse("article:preview", kwargs={
            'pk': article.pk
        }))
        self.assertEqual(resp.status_code, 200)

    def test_article_preview_view_as_staff(self):
        client = Client()

        author = AuthorFactory.build()
        author.set_password(get_random_string(32))
        author.save()

        article = ArticleFactory(author=author)
        self.if_logged(client.login(username=self.staff.username, password=self.staff.ps))

        resp = client.get(reverse("article:preview", kwargs={
            'pk': article.pk
        }))
        self.assertEqual(resp.status_code, 200)

    def test_article_preview_view_as_user(self):
        client = Client()

        author = AuthorFactory.build()
        author.set_password(get_random_string(32))
        author.save()

        article = ArticleFactory(author=author)
        self.if_logged(client.login(username=self.user.username, password=self.user.ps))

        resp = client.get(reverse("article:preview", kwargs={
            'pk': article.pk
        }))
        self.assertEqual(resp.status_code, 403)

    def test_article_preview_view_as_anonymous(self):
        client = Client()

        author = AuthorFactory.build()
        author.set_password(get_random_string(32))
        author.save()

        article = ArticleFactory(author=author)

        resp = client.get(reverse("article:preview", kwargs={
            'pk': article.pk
        }))
        self.assertEqual(resp.status_code, 403)

    def test_article_list_view(self):
        client = Client()

        resp = client.get(reverse("article:list"))
        self.assertEqual(resp.status_code, 200)

    def test_article_list_view_pagination(self):
        client = Client()

        resp = client.get(reverse("article:list"), {"page": 2})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context[ArticleListView.context_object_name]), ArticleListView.paginate_by)

        resp = client.get(reverse("article:list"), {"page": 20})
        self.assertEqual(resp.status_code, 404)

    def test_article_detail_view(self):
        client = Client()
        article = Article.objects.first()
        slug = article.slug

        resp = client.get(reverse("article:detail", kwargs={'slug': slug}))
        self.assertEqual(article.pk, resp.context[ArticleDetailView.context_object_name].pk)
        self.assertEqual(resp.status_code, 200)

    def test_search_view(self):
        client = Client()
        article = Article.objects.first()
        tag = Tag.objects.first()

        resp = client.get(reverse("article:search"), {'q': article.title})
        self.assertEqual(len(resp.context[SearchView.context_object_name]), 1)

        resp = client.get(reverse("article:search"), {'q': "none"})
        self.assertEqual(len(resp.context[SearchView.context_object_name]), 0)

        resp = client.get(reverse("article:search"), {'q': tag.title})
        self.assertEqual(len(resp.context[SearchView.context_object_name]), 4)

    def test_author_view(self):
        client = Client()

        resp = client.get(reverse("article:author-list", kwargs={
            'slug': self.user.username
        }))
        self.assertEqual(len(resp.context[ArticleAuthorListView.context_object_name]), 7)

        resp = client.get(reverse("article:author-list", kwargs={
            'slug': 'none'
        }))
        self.assertEqual(len(resp.context[ArticleAuthorListView.context_object_name]), 0)

    def test_change_article_status_view(self):
        client = Client()

        id = 2
        url = reverse("article:list")
        trans_method = '___hidden'

        resp = client.post(reverse("article:change_status"), {
            'id': id,
            'url': url,
            trans_method: ""
        })
        self.assertEqual(resp.status_code, 302)

        # wrong id
        resp = client.post(reverse("article:change_status"), {
            'id': 1002,
            'url': url,
            trans_method: ""
        })
        self.assertEqual(resp.status_code, 404)

        # wrong trans method
        resp = client.post(reverse("article:change_status"), {
            'id': id+1,
            'url': url,
            '___looooooolloooo': ""
        })
        self.assertEqual(resp.status_code, 404)

        # try to hack model
        resp = client.post(reverse("article:change_status"), {
            'id': id + 1,
            'url': url,
            'title': ""
        })
        self.assertEqual(resp.status_code, 404)
