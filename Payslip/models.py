from django.db import models
from Login.models import Employee

# Create your models here.
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_month = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    pf=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee} - {self.salary_month}"