from django.db import models

class Company(models.Model):
    Company_Tpye = [
        ('Account','Account'),
        ('IT','IT'),
        ('Other','Other')
    ]
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=20, choices=Company_Tpye)
    added_date = models.DateTimeField(auto_now=True)
    
