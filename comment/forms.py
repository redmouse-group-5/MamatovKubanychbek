from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(label='Comment Body', max_length=100, widget=forms.Textarea)