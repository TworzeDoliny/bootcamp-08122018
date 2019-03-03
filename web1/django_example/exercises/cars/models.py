from django.db import models



# Create your models here\
BODY_TYPE_CHOICE =(
    ("sedan", "sedan")
    ("combi", "combi")
    ("hatchback", "hatchback")
    ("cabriolet", "cabriolet")

)

ENGINE_TYPE_CHOICE =(
    ("benz", "benz")
    ("diesel", "diesel")
    ("steam", "steam")
    ("hybrid", "hybrid")

)





class Engine(models.Model):
    type = models.CharField(max_length=20, choices=ENGINE_TYPE_CHOICE, null=True, blank=True)
    power = models.IntegerField()
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.type}, | {self.power}"



class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=50)
    production_year = models.IntegerField()
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICE, null=True, blank=True)
    engine = models.ForeignKey(Engine, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} | {self.model} | {self.production_year}"