from django.db import models

# Create your models here.




class Employee(models.Model):
    empid = models.CharField(max_length = 30)
    empname = models.CharField(max_length = 30)
    salary = models.CharField(max_length = 30,default=0)
    # address = models.OneToOneField(Address,on_delete=models.CASCADE,related_name="address")

    def __str__(self) -> str:
        return "Empid: "+self.empid+" , Ename: "+self.empname+", salary: "+self.salary
    



class Address(models.Model):
    city = models.CharField(max_length = 30)
    pincode = models.CharField(max_length = 30)
    # employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee",default=0)
    
    employee = models.ManyToManyField(Employee)

    def __str__(self) -> str:
        return "city: "+self.city+" with pincode: "+self.pincode+" of employee" + str(self.employee)



