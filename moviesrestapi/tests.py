from django.test import TestCase
from unittest.mock import patch

from .models import Movie


def mocked_requests_get(data):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(data, 201)


class TestMoviesReastApi(TestCase):
    """TODO: corner cases, movie does not exist"""

    @patch('moviesrestapi.views.requests.get', return_value=mocked_requests_get(data={"Title": "Game of Thrones"}))
    def test_save_movie(self, mock_requests):
        self.assertEqual(Movie.objects.count(), 0)
        resp = self.client.post('/movies/', {'title': 'game of thrones'})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Movie.objects.count(), 1)

    def test_get_movie(self):
        self.client.post('/movies/', {'title': 'game of thrones'})
        resp = self.client.get('/movies/')
        self.assertEqual('Game of Thrones', resp.data[0]['title'])

    def test_filter_movie(self):
        with patch('moviesrestapi.views.requests.get',
                   return_value=mocked_requests_get(data={'Title': 'Game of Thrones'})):
            self.client.post('/movies/', {'title': 'game of thrones'})
        with patch('moviesrestapi.views.requests.get', return_value=mocked_requests_get(data={'Title': 'blow'})):
            self.client.post('/movies/', {'title': 'blow'})

        resp = self.client.get('/movies/?search=blow')
        self.assertEqual(len(resp.data), 1)
        self.assertEqual('blow', resp.data[0]['title'])


class TestCommentsReastApi(TestCase):
    def test_add_comments(self):
        with patch('moviesrestapi.views.requests.get',
                   return_value=mocked_requests_get(data={'Title': 'Game of Thrones'})):
            self.client.post('/movies/', {'title': 'game of thrones'})
        self.client.post('/comments/', {'comment': 'some long comment', 'user_name': 'user1', 'movie': 1})
        resp = self.client.get('/comments/')
        self.assertEqual(resp.data[0]['user_name'], 'user1')
        self.assertEqual(resp.data[0]['comment'], 'some long comment')
