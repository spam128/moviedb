from rest_framework import routers
from moviesrestapi import views

router = routers.DefaultRouter()
router.register(r'movies', views.MoviesViewSet)
router.register(r'comments', views.CommentsViewSet)

urlpatterns = router.urls
