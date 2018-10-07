from rest_framework import routers
from imdbapi import views

router = routers.DefaultRouter()
router.register(r'titles', views.TitlesViewSet)
router.register(r'names', views.NamesViewSet)

