from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is a book.')
    
    def test_text_contest(self):
        post = Post.objects.get(id=1)
        expect_object_name = f'{post.text}'
        self.assertEqual(expect_object_name, 'This is a book.')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text= 'This is the other test.')
    
    def test_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_use_correct_templates(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')