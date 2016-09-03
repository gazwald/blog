from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User

from .views import index


class TestPosts(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
                username="my_user",
                password="ALackOfSecurity",
                email="root@localhost.localdomain")


    def test_view_about_user(self):
       request = self.factory.get('/posts/')
       request.user = self.user
       response = index(request)
       self.assertEqual(response.status_code, 200)


    def test_view_about_anon(self):
       request = self.factory.get('/posts/')
       request.user = AnonymousUser()
       response = index(request)
       self.assertEqual(response.status_code, 200)
