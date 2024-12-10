from django import forms
from .models import Article,Topic


class InputForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()

class TopicForm(forms.ModelForm):

    class Meta():

        model = Topic
        fields = ("topic_name",
                  "Choose_image",)

class ArticleForm(forms.ModelForm):

    class Meta():

        model = Article
        exclude = ['created_at',]
