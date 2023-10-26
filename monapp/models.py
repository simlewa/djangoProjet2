from django.db import models
class Info(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    commentaire = models.TextField()

    #pour specifié explicitement le nom de la table
    class Meta:
        db_table = 'info'
# Create your models here.
