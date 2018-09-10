from django.test import TestCase
from unittest.mock import patch

from .models import Movie

REQUESTS_GET = 'moviesrestapi.omdbapi.requests.get'


def mocked_requests_get(data):
    """Mock GET response from requests"""

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(data, 201)


class TestMoviesReastApi(TestCase):
    """Test movies rest api"""

    @patch(REQUESTS_GET, return_value=mocked_requests_get(data={"Title": "Game of Thrones"}))
    def test_save_movie(self, mock_requests):
        """Test post new movie is saved to database"""
        self.assertEqual(Movie.objects.count(), 0)
        resp = self.client.post('/movies/', {'title': 'game of thrones'})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Movie.objects.count(), 1)

    def test_get_movie(self):
        """Check if added movie is retrieved in GET"""
        self.client.post('/movies/', {'title': 'game of thrones'})
        resp = self.client.get('/movies/')
        self.assertEqual('Game of Thrones', resp.data[0]['title'])

    def test_filter_movie(self):
        """Check filtering movies"""
        with patch(REQUESTS_GET, return_value=mocked_requests_get(data={'Title': 'Game of Thrones'})):
            self.client.post('/movies/', {'title': 'game of thrones'})
        with patch(REQUESTS_GET, return_value=mocked_requests_get(data={'Title': 'blow'})):
            self.client.post('/movies/', {'title': 'blow'})

        resp = self.client.get('/movies/?search=blow')
        self.assertEqual(len(resp.data), 1)
        self.assertEqual('blow', resp.data[0]['title'])


class TestCommentsReastApi(TestCase):
    """Test comments rest api"""

    def test_add_comments(self):
        """Test POST comment is added to database"""
        with patch(REQUESTS_GET, return_value=mocked_requests_get(data={'Title': 'Game of Thrones'})):
            self.client.post('/movies/', {'title': 'game of thrones'})
        self.client.post('/comments/', {'comment': 'some long comment', 'user_name': 'user1', 'movie': 1})
        resp = self.client.get('/comments/')
        self.assertEqual(resp.data[0]['user_name'], 'user1')
        self.assertEqual(resp.data[0]['comment'], 'some long comment')
