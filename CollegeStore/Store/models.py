from django.db import models

class Department(models.Model):
    departmentname = models.CharField(max_length=250)

    def __str__(self):
        return self.departmentname


class Course(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.CharField(max_length=250)

    def __str__(self):
        return self.course



class Order(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=(('Male', 'Male'), ('Female', 'Female'),))
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50)
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.name
