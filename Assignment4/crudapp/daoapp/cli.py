from .dao import empDAO

def main():
    while True:
        print("1. Create a book")
        print("2. Read all books")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")
        
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            designation = input("Enter role: ")
            name = input("Enter name: ")
            joining_date = input("Enter joining date(YYYY-MM-DD): ")
            empDAO.create_emp(designation,name, joining_date)

        elif user_choice == '2':
            employees = empDAO.show_emp()
            for emp in employees:
                print(emp)
        
        elif user_choice == '3':
            emp_id = int(input("Enter the id of employee you want to update: "))
            print("Leave fields blank if want to keep unchanged")
            designation = input("Enter updated designation: ")
            name = input("Enter updated name: ")
            joining_date = input("Enter updated joining date: ")
            empDAO.update_emp(emp_id = emp_id, designation = designation, name = name, joining_date= joining_date)
        
        elif user_choice == '4':
            emp_id = int(input("Enter the id of employee you want to delete: "))    
            empDAO.delete_emp(emp_id= emp_id)
        elif user_choice == '5':
            print("Exiting")
            break
        else: 
            print("Invalid Choice. Try again")

if __name__ == '__main__':
    main()

