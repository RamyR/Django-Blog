from django.urls import path
from . import views

# fmt: off
urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]

# fmt: on
