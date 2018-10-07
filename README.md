# moviedb
simple REST API in django - basic movie database interacting with external APi http://www.omdbapi.com/ and loading movies data from https://www.imdb.com/interfaces/ tsv files.


## Instalation
```pipenv install``` it's sufficient to provide all packages

## IMDB
### Functionalities:

Getting movies ordered by movie title with given genre, series start year or cast person name
Main cons:
-during using importer command loadimdbtsv, database is blocked and there is no posibility to reach end points 

Python command to load TSV data from https://www.imdb.com/interfaces/
python manage.py loadimdbtsv title.basics.tsv.gz name.basics.tsv.gz 

### Endpoints:

```imdb/titles/``` all titles ordered by primary title, pagination is set to 25 values per page
```imdb/titles/?search=searched_phrase``` return movies by given criteria (genre, series start year or cast person name)

```imdb/names/``` all staff, pagination is set to 25 values per page.


## OMDB:
### Functionalities:
Ordering, searching movie by name and year(movies), searching by user name(commets)
There is no posibility to login to keep the same user name

### Endpoints
##### GET:
```/movies/``` get all movies
```/movies/?search=name``` where name is title of movie or date
```/movies/?ordering=att``` where att is the attribute that is going to be use to order response (-att if descending ordering)

```/comments/?search=user_name``` searching by username only
```/comments/?ordering=att``` where att is the attribute that is going to be use to order response (-att if descending ordering)

##### POST:
```/movies/ {'title':'movie_title_name'}```to add movie from omdbapi (on heroke are more atrributes to write because django rest framework adds them by default but they are ignored)

```/comments/ {'user_name':'your_user_name', 'comment':'your comment', 'movie':'movie title'}``` movie has to be in database before adding a comment
