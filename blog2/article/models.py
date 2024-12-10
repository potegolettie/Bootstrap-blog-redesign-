from django.db import models

# Create your models here.

class Topic(models.Model):

  topic_name = models.CharField(max_length = 256)
  Choose_image = models.ImageField(upload_to='images/' , default='default.jpg')

  def _str_(self):
      return self.topic_name


class Article(models.Model):

   title = models.CharField(max_length = 256)
   topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='articles')
   article = models.TextField()
   Choose_image = models.ImageField(upload_to='images/' , default='default.jpg')
   created_at = models.DateTimeField(auto_now_add=True)


   def _str_(self):
       return self.title
