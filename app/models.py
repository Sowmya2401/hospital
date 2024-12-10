from django.db import models

class Department(models.Model):
    dep_title=models.CharField(max_length=50)
    dep_desc=models.TextField(max_length=200)

    def __str__(self):
        return self.dep_title
    
class Doctor(models.Model):
    doc_name=models.CharField(max_length=50)
    doc_desc=models.TextField(max_length=200)
    doc_image=models.TextField(max_length=500)
    doc_department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_name
class Booking(models.Model):
    p_name=models.CharField(max_length=50)
    p_email=models.CharField(max_length=50)
    p_phone=models.CharField(max_length=50)
    p_department=models.CharField(max_length=50)
    p_doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    p_date=models.DateField()
    p_msh=models.TextField(max_length=500)

    def __str__(self):
        return self.p_name