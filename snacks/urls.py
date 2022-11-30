from django.urls import path
from .views import HomePage,AboutPage,ThingListView
urlpatterns = [
    path('',HomePage.as_view(),name="home"),
    path('about', AboutPage.as_view(),name="about"),
    path('snacks/',ThingListView.as_view(), name='snacks' )
]