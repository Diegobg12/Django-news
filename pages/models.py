from django.db import models

# Create your models here.


class Quote(models.Model):
    quote = models.TextField(default="I can give you my loneliness, my darkness, the hunger of my heart, I am trying to bribe you with uncertainty, with danger, with defeat")
    author = models.TextField(default="Jorge Luis Borges", null=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.author
