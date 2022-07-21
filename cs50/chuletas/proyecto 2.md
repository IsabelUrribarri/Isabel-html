Crear un modelo

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()


Naming Your Models

E.g. User , Permission , ContentType , etc. For the model's attributes use snake_case. E.g. first_name , last_name , etc. Always name your models using singular.