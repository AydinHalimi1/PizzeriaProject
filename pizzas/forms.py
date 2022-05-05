from django import forms

from .models import Pizza, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':''}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_name']
        labels = {'comment_name':''}
        widgets = {'comment_name': forms.Textarea(attrs={'cols':80})}