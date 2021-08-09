from django.db import models

# Create your models here.
class utilisateurs(models.Model):
    username = models.CharField(max_length=30, default='NULL')
    password =  models.CharField(max_length=35 , default='NULL')
    full_name = models.CharField(max_length=40, default='NULL')
    departement = models.CharField(max_length=40, default='NULL')
    def __str__(self):
        return ''+self.full_name+''
    
    

class chargehoraire(models.Model):
    user= models.ForeignKey(utilisateurs, on_delete=models.CASCADE)
    nbrheures = models.IntegerField()
    module = models.CharField(max_length=30, default='NULL')
    matiere = models.CharField(max_length=40, default='NULL')
    cc = models.CharField(max_length=4,default='NULL')
    departement = models.CharField(max_length=40, default='NULL')
    
    def __str__(self):
        return ''+self.user.full_name+''
   
class annonce(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    titre = models.CharField(max_length=30, default='NULL')
    texte = models.CharField(max_length=1000, default='NULL')
    def __str__(self):
        return ''+self.titre+''
    
    
  #  lastname = models.CharField(max_length=30)
   # login = models.CharField(max_length=15)
   # password = models.CharField(max_length=15)
 #class annonce(models.Model):
   # date=models.DateTimeField()
    #texte=models.TextField()
 