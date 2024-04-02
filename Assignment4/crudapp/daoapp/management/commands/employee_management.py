# your_app/management/commands/employee_management.py

from django.core.management.base import BaseCommand
from daoapp.dao import empDAO

class Command(BaseCommand):
    help = 'Manage employees'

    def handle(self, *args, **kwargs):
        while True:
            self.stdout.write("1. Create an employee")
            self.stdout.write("2. Read all employees")
            self.stdout.write("3. Update an employee")
            self.stdout.write("4. Delete an employee")
            self.stdout.write("5. Exit")
            
            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                designation = input("Enter designation: ")
                name = input("Enter name: ")
                joining_date = input("Enter joining date(YYYY-MM-DD): ")
                empDAO.create_emp(designation, name, joining_date)
                self.stdout.write(self.style.SUCCESS('Employee created successfully!'))

            elif user_choice == '2':
                employees = empDAO.show_emp()
                for emp in employees:
                    self.stdout.write(str(emp))
            
            elif user_choice == '3':
                emp_id = int(input("Enter the id of the employee you want to update: "))
                self.stdout.write("Leave fields blank if you want to keep unchanged")
                designation = input("Enter updated designation: ")
                name = input("Enter updated name: ")
                joining_date = input("Enter updated joining date: ")
                empDAO.update_emp(emp_id=emp_id, designation=designation, name=name, joining_date=joining_date)
                self.stdout.write(self.style.SUCCESS('Employee updated successfully!'))
            
            elif user_choice == '4':
                emp_id = int(input("Enter the id of the employee you want to delete: "))    
                empDAO.delete_emp(emp_id=emp_id)
                self.stdout.write(self.style.SUCCESS('Employee deleted successfully!'))
            
            elif user_choice == '5':
                self.stdout.write("Exiting")
                break
            
            else: 
                self.stdout.write("Invalid Choice. Try again")
