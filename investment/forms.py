from django import forms
from .models import StockMarketItem, Blog

class StockForm(forms.ModelForm):

    class Meta:
        model = StockMarketItem
        fields = ('phase', 'investment_segment', 'name', 'profit', 'portion', 'description','comment_before','chosen')

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('category','title', 'text')
