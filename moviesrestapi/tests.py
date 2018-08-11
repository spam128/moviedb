from django.test import TestCase
from .models import Movie, Comment


class TestMoviesReastApi(TestCase):
    def test_save_movie(self):
        self.assertEqual(Movie.objects.count(), 0)
        resp = self.client.post('/movies/', {'title': 'game of thrones'})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Movie.objects.count(), 1)

    def test_get_movie(self):
        self.client.post('/movies/', {'title': 'game of thrones'})
        resp = self.client.get('/movies/')
        self.assertEqual('Game of Thrones', resp.data[0]['title'])

# class TestCommentsReastApi(TestCase):
#     def test_add_comments(self):
#         self.client.post('comments/', {'name': 's'})
#
#         self.assertFalse()
#
#     def test_get_comments(self):
#         resp = self.client.get('comments/', {'name': 's'})
#
#         self.assertFalse()
#
#     def test_filtered_comment(self):
#         self.assertFalse()
