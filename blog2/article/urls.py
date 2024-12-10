from django.urls import path, include
from .views import showarticle,show_topics,send_input_data,create_topic

app_name = 'article'

urlpatterns = [
                path('',showarticle,name='show'),
                path('topics',show_topics,name='topics'),
                path('input',send_input_data),
                path('topic/add',create_topic,name = 'add_topic'),
]
