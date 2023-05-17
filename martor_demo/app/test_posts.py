from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="Django", description="Testing", wiki="Post Body")
        self.assertEqual(post.title, "Django")
        self.assertEqual(post.description, "Testing")
        self.assertEqual(post.wiki, "Post Body")
