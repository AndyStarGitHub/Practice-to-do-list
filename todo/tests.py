from django.test import TestCase

from todo.models import Tag


# Create your test here.
class ModelTests(TestCase):
    def test_tag_name(self):
        tag = Tag.objects.create(
            name="test tag",)
        self.assertEqual(tag.name, "test tag")
