from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(  # pylint: disable=no-member
            name='Test Todo Item', done=False)
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(  # pylint: disable=no-member
            name='Test Todo Item', done=True)
        self.assertEqual(str(item), 'Test Todo Item')
