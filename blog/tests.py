from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        testuser1 = User.objects.create_user(username='testuser1', password='12345')
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1,
            title='Test Post',
            body='Test Post Body'
        )
        test_post.save()

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        self.assertEqual(expected_object_title, 'Test Post')

    def test_body_content(self):
        post = Post.objects.get(id=1)
        expected_object_body = f'{post.body}'
        self.assertEqual(expected_object_body, 'Test Post Body')

    def test_author_content(self):
        post = Post.objects.get(id=1)
        expected_object_author = f'{post.author}'
        self.assertEqual(expected_object_author, 'testuser1')
