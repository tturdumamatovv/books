from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Robinson Crusoe', price=25,
                                     author_name='Author 1')
        book_2 = Book.objects.create(name="Five's Wave", price=55,
                                     author_name='Author 2')
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Robinson Crusoe',
                'price': '25.00',
                'author_name': 'Author 1'
            },
            {
                'id': book_2.id,
                'name': "Five's Wave",
                'price': '55.00',
                'author_name': 'Author 2'
            }
        ]
        self.assertEqual(expected_data, data)
