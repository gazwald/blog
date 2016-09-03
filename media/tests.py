from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.core.paginator import EmptyPage
from django.utils.crypto import get_random_string
from django.core.files.uploadedfile import SimpleUploadedFile

from .views import media_list, media_add, media_del
from .models import UploadedFile
from .forms import UploadedFileForm


class TestPosts(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="my_user",
            password="ALackOfSecurity",
            email="root@localhost.localdomain")

    def test_view_media_list_logged(self):
        request = self.factory.get('/media/')
        request.user = self.user
        response = media_list(request)
        self.assertEqual(response.status_code, 200)

    def test_view_media_list_anon(self):
        request = self.factory.get('/media/')
        request.user = AnonymousUser()
        response = media_list(request)
        self.assertEqual(response.status_code, 302)

    def test_add_media_logged_in(self):
        request = self.factory.get('/media/add/')
        request.user = self.user
        response = media_add(request)
        self.assertEqual(response.status_code, 302)

    def test_add_media_anonymous(self):
        request = self.factory.get('/posts/add/', follow=True)
        request.user = AnonymousUser()
        response = media_add(request)
        self.assertEqual(response.status_code, 302)

