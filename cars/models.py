from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# sahibi model 
# maşın model
# rentacar model

# Maşınlarımız var hər şəxsin 1-dən artıq maşını olabilməz. 
# Yəni bu maşın 1 dən artıq şəxsə aid olabilməz və ya eyni şəxsin 2 maşını olabilməz (onetoonefield). 
# Daha sonra isə bu maşınları kirayə verən bir  şirkət var və seçilmiş maşın sadəcə bir kirayə şirkətinə aid olabilər.
# Eyni anda 2 kirayə  şirkətində olabilməz (foreignkey).

class Owner(models.Model):
    owner = models.OneToOneField("auth.User", verbose_name=("Sahib"), on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.owner)
    

class Rentacar(models.Model):
    company_name = models.CharField(max_length=50, verbose_name=("Şirkət adı"))
   
    def __str__(self):
       return str(self.company_name)

 
class Car(models.Model):
    owner = models.OneToOneField(Owner, verbose_name=("Sahib"), on_delete=models.CASCADE)
    rentacar = models.ForeignKey(Rentacar, on_delete=models.CASCADE,verbose_name="Rentacar",)
    name = models.CharField(max_length=50, verbose_name="Maşın adı")
    year = models.DateField(verbose_name="İli")
    
    def __str__(self):
        return f"{self.name} ({self.year.year}) - {self.owner.owner.username}"
    
