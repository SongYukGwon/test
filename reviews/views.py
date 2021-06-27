from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from . import models
# Create your views here.


class DetailReview(DetailView):
    model = models.Review
    context_object_name = 'review'


class CraeteReview(CreateView):
    model = models.Review
    fields = (
        "text",
        "movie",
        "book",
        "rating",
    )


class DeleteReview(DeleteView):
    model = models.Review
    success_url = "/"


class ReviewsView(ListView):

    model = models.Review
    paginate_by = 15
    paginate_orphans = 5
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Reviews"
        return context
