from django.db import models

class Postagem(models.Model):
  tag = models.CharField(max_length=50)
  title = models.CharField(max_length=64)
  content = models.TextField()

  def __str__(self):
    return self.title
