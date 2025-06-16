from django.db import models
from datetime import datetime

# HR Users (managers)
class HR(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    password=models.CharField(max_length=1000)
    profile_picture = models.ImageField(upload_to='employee_hr/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateField()


    def __str__(self):
        return self.name


# Department
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    hr = models.ForeignKey(HR, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    employee_id = models.CharField(max_length=10, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    Bank_Account_No=models.CharField(max_length=1000)
    IFSC_CODE=models.CharField(max_length=1000)
    phone = models.CharField(max_length=15, null=True, blank=True)
    position = models.CharField(max_length=100)
    date_joined = models.DateField()
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='employee_profiles/', null=True, blank=True)
    is_active = models.BooleanField(default=True) 

    def save(self, *args, **kwargs):
        if not self.employee_id:
            year = datetime.now().year
            prefix = str(year)
            last_employee = Employee.objects.filter(employee_id__startswith=prefix).order_by('employee_id').last()
            if last_employee and last_employee.employee_id:
                last_id = int(last_employee.employee_id[-3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.employee_id = f"{prefix}{new_id:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
       return f"{self.employee_id} - {self.first_name} {self.last_name}"


# Attendance
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=(
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'SickLeave'),
        ('Leave', 'CasualLeave'),
    ))

    def __str__(self):
        return f"{self.employee} - {self.date}"


# Leave
class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=(
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ), default='Pending')

    def __str__(self):
        return f"{self.employee} Leave from {self.start_date} to {self.end_date}"



# Job Position
class JobPosition(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
