from django.db import models

class faculte(models.Model):
    codeFac=models.CharField(max_length=10)
    denomination_extact=models.TextField()
    
    class Meta:
        ordering=['codeFac']
        
    def __str__(self):
        return self.codeFac
    