from .models import Employee

class empDAO:
    @staticmethod
    def create_emp(title, name, joining_date):
        return Employee.objects.create(designation =title, name = name, joining_date = joining_date)
    
    @staticmethod
    def show_emp():
        return Employee.objects.all()
    
    @staticmethod
    def update_emp(emp_id, designation = None, name = None, joining_date = None):
        employee = Employee.objects.get(id = emp_id)
        if designation:
            employee.designation = designation
        if name:
            employee.name = name
        if joining_date:
            employee.joining_date = joining_date
        
        employee.save()
        return employee
    
    @staticmethod
    def delete_emp(emp_id):
        employee = Employee.objects.get(id = emp_id)
        employee.delete()
