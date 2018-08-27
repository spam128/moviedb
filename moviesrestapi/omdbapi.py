"""
This module get movie data from omdbapi and returns movie object
"""
from django.template.defaultfilters import slugify
import requests


def get_movie(title):
    """Returns movie from omdbapi by given title.

    Keyword arguments:
    title -- movie title
    """
    name = slugify(title).replace('-', '+')
    resp = requests.get('http://www.omdbapi.com/?apikey=7b85cd2d&t={}'.format(name))
    data = resp.json()
    movie_data = {key.lower(): data[key] for key in data}
    return movie_data
