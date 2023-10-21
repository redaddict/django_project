from django.db import models


# Create your models here.
class Nifty(models.Model):
    # create fields
    BANKNIFTY = models.CharField("BANKNIFTY",max_length=(255))
    DATE = models.DateField("DATE")
    TIME = models.TimeField("TIME")
    OPEN = models.DecimalField("OPEN",max_digits=6,decimal_places=2)
    HIGH = models.DecimalField("HIGH",max_digits=6,decimal_places=2)
    LOW = models.DecimalField("LOW",max_digits=6,decimal_places=2)
    CLOSE = models.DecimalField("CLOSE",max_digits=6,decimal_places=2)
    VOLUME = models.BigIntegerField("VOLUME")

    def __str__ (self):
        return self.BANKNIFTY
    
    




  