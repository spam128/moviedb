# moviedb
simple REST API - basic movie database interacting with external APi http://www.omdbapi.com/

[app deployed on heroku](https://moviedb-restapi.herokuapp.com/)

### functionalities:
ordering, searching movie by name and year(movies), searching by user name(commets)
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
