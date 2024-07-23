import authentication
import operations
from getpass import getpass
from Employee_data import add_employee,new_employee,Edit_Employee

def Employee_Services():
        print("Select an option:")
        print("1.Display Employee Information")
        print("2.Calculate Bouns")
        print("3.Calculate Discount")
        print("4.Remind Legal Holidays")
        print("5.Exit")    

def Admin_Services():
        print("Select an option:")
        print("1.Add New Employee")
        print("2.Update Employee Details")
        print("3.Remove Employee")
        print("4.Exit") 


if __name__ == "__main__":
    print("Welcome To Employee Managment System")
    print("Please Login To Continue")

    ID = input("Enter Your Employee ID: ")

    Password = getpass("Enter Your Password: ")

    user = authentication.Authrnticate(ID,Password)

    if (user["Name"] == "admin" or user["Name"] == "Admin"):
        while(1):
            Admin_Services()
            option = input("Enter your Choice: ")
            match(option):
                case "1": 
                    for key in new_employee:
                        new_employee[key] = input(f"Enter The Employee {key}: ")                                  
                    add_employee(ID,new_employee)
                case "2":
                    Employee_ID = input("Please Enter The Employee ID To Modify the data: ")
                    Edit_Employee(ID,Employee_ID)
                case "3":
                    pass

                case "4":
                    print("Thank you for using Employee Managment System. Goodbye!")
                    exit(0) 
    else:
        while(1):
            Employee_Services()
            option = input("Enter your choice: ")
            match(option):
                case "1":
                    print("--------------- Employee Information ------------------")
                    for key in user:
                        print(f"{key}: {user[key]}")
                    print("-------------------------------------------------------")    

                case "2":
                    print("--------------- Employee Bouns ------------------")                    
                    print(f"Bouns = {operations.Bouns( int (user["Salary"][1:] ) )}")
                    print("-------------------------------------------------------")    

                case "3":
                    print("--------------- Employee Discount ------------------")
                    print(f"Discount = {operations.Discount( int (user["Salary"][1:] ) )}")
                    print("-------------------------------------------------------")    

                case "4":
                    print("--------------- Employee Holidays ------------------")
                    print(f"Remind Legal Holidays = {operations.RemindLegalHolidays( user["Days Of Absence"])}")
                    print("-------------------------------------------------------")    

                case "5":
                    print("Thank you for using Employee Managment System. Goodbye!")
                    exit(0)      

                case _:
                    print("-------------------------------------------------------")    
                    print("Invalid Choice please choose a service from [1 to 5]")
                    print("-------------------------------------------------------")    

