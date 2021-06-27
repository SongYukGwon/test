from django import forms
from . import models


class CreateReview(forms.ModelForm):

    class Meta:
        modle = models.Review
        fields = (
            "created_by",
            "text",
            "movie",
            "book",
            "rating",
        )

    def save(self):
        review = super().save(commit=False)
        return review
