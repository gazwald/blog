from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User

from .views import index, post_add
from .models import Post


class TestPosts(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
                username="my_user",
                password="ALackOfSecurity",
                email="root@localhost")


    def test_view_post_index(self):
       request = self.factory.get('/posts/')
       response = index(request)
       self.assertEqual(response.status_code, 200)


    def test_add_post(self):
        new_post = Post(
                    author=self.user,
                    title="Hello world",
                    body="I am a test post, isn't this great")
        self.assertEqual(new_post.title, "Hello world")


    def test_add_post_logged_in(self):
        request = self.factory.get('/posts/add/')
        request.user = self.user
        response = post_add(request)
        self.assertEqual(response.status_code, 200)


    def test_add_post_anonymous(self):
        request = self.factory.get('/posts/add/', follow=True)
        request.user = AnonymousUser()
        response = post_add(request)
        self.assertEqual(response.status_code, 302)
