from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Done Item')
        self.assertFalse(item.done)

    def test_fields_name(self):
        item = Item.objects.create(name='Test Field Name')
        self.assertEqual(str(item), 'Test Field Name')


