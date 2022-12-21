from django.db import models

# Create your models here.
class User(models.Model):
    nom=models.CharField('Nom',max_length=255)
    prenom=models.CharField('Prenom',max_length=255)
    email=models.EmailField()
    def __str__(self):
        #return "le nom est :"+self.nom+"le prenom est :"+self.prenom
        return f"le nom est :{self.nom}le prenom est :{self.prenom}"
class etudiant(User):
    groupe=models.CharField('Groupe',max_length=255)
class coach(User):
    pass 

class projet(models.Model):
    nom_projet=models.CharField(max_length=255)
    duree_projet=models.IntegerField("Duree Estime",default=0)
    etat=models.BooleanField(default=False)
    temps_alloue=models.IntegerField()
    membres=models.ManyToManyField(
        'etudiant',
        related_name='les_projets',
        through = 'MemberShipinProject'
       )
    createur=models.OneToOneField(
        etudiant,
        on_delete=models.SET_NULL,
        null=True
    )
    suprviseur=models.ForeignKey(
        coach,
        on_delete=models.CASCADE
    )    

class MemberShipinProject(models.Model):
    projet=models.ForeignKey(projet,on_delete=models.CASCADE)
    etudiant=models.ForeignKey(etudiant,on_delete=models.CASCADE)
    time_allocated=models.IntegerField()
