from django import forms
from stripe import Review
from core.models import ProductReveiw

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Write review"}))

    class Meta:
        model = ProductReveiw
        fields = ['review', 'rating']
