from django.urls import path
from . import views

app_name = "views"

urlpatterns = [
    path("", views.ReviewsView.as_view(), name="list"),
    path("<int:pk>", views.DetailReview.as_view(), name="review"),
    path("create/<int:pk>", views.CraeteReview.as_view(), name="create"),
    path("<int:pk>/delete", views.DeleteReview.as_view(), name="delete"),
]
