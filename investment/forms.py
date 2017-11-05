from django import forms
from .models import StockMarketItem, Blog, Goal

class StockForm(forms.ModelForm):

    class Meta:
        model = StockMarketItem
        fields = ('phase', 'investment_segment', 'name', 'profit', 'portion', 'description','comment_before','chosen')

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('category','title', 'text')

class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ('goal_date','title', 'text')
