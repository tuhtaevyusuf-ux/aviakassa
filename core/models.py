from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()

    def __str__(self):
        return self.name
    
class Flight(models.Model):
    date = models.DateField()
    from_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='froms')
    to_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='tos')

    def __str__(self):
        return f"{self.date}: {self.from_country} - {self.to_country}"