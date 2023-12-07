from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class chkboxcourse(models.Model):
    coursename=models.CharField(max_length=100)


    def __str__(self):
        return self.coursename



class Students(models.Model):
    name = models.CharField(max_length=124)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10)  # New field
    phone_number = models.CharField(max_length=20)  # New field
    mail_id = models.EmailField(blank=True, null=True, default="default@example.com")  # New field
    address = models.TextField(blank=True, null=True, default="No address provided")  # New field
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)

    purpose = models.CharField(max_length=20, choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'),
                                                        ('return', 'Return')])  # New field
    materials_provide=models.CharField(max_length=100, blank=True, null=True)
    # materials_provide = models.ManyToManyField(Material, blank=True)

    def __str__(self):
        return self.name






