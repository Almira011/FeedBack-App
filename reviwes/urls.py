from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()), 
    path("thank-page", views.ThankYou.as_view()),
    path("list-reviews", views.ListReviews.as_view()),
    path("list-reviews/liked_id", views.AddLikeView.as_view()),
    path("list-reviews/<int:pk>", views.SingleReviews.as_view()),
]