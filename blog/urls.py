from django.urls import path

from blog import views

urlpatterns = [
    path("", views.PostList.as_view(), name="index"),
    path("home/", views.home, name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
