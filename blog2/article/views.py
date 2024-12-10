from django.shortcuts import render,redirect
from .models import Topic,Article
from .import forms

# Create your views here.

def create_topic(request):

    if request.method == "POST":
         form = forms.TopicForm(request.POST)
         if form.is_vaild():
             form.save()
             return redirect('articles:topics')
         else:
             print("an error has occurred")

             form = forms.TopicForm()
             return render(request,'input.html',{'form':form})



def send_input_data(request):

    form = forms.InputForm()

    if request.method == "POST":

        form = forms.InputForm(request.POST)
        if form.is_valid():

            print("form valid")
        else:
            print("form not valid!!!")

    return render(request,'input.html',{form:form})

def show_topics(request):

    topics = Topic.objects.all()
    return render(request,'topics.html',{'topics':topics})

def showarticle(request):

    title = 'My first article'
    author ='Mark'
    article_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
    qui officia deserunt mollit anim id est laborum.
    """

    return render(request,'article/article.html',{'title':title,'author':author,'article_text':article})
