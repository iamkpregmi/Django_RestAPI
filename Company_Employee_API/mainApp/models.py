from django.db import models

class Company(models.Model):
    comp_type = [
        ('IT', 'IT'),
        ('Other', 'Other')
    ]
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    company_type = models.CharField(max_length=20,choices = comp_type)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    Company_Name = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()


