import authentication
import operations
from getpass import getpass
from Employee_data import Check_Existing_ID,add_employee,new_employee,Edit_Employee,Show_Employee_data,Delete_Employee,Promot_Password


def Handle_User_Inputs():
    Edit_Field_names = []
    valid_fields = ["Name", "Department", "Salary","Password", "Days_Of_Absence"]
    user_input = input("Enter The Field Names To Update separated by space (Name - Department - Salary - Password - Days Of Absence): ")
    Edit_Field_names = user_input.split(' ')
    
    for item in Edit_Field_names:
        if '' in Edit_Field_names:
            Edit_Field_names.remove('')
        else:
            continue    
    for item in Edit_Field_names:
        if item in valid_fields:
            continue
        else:
            raise Exception (f"Invalid Field Name {item} Please Enter a valid Field Name")
            exit()

    return Edit_Field_names

def Employee_Services():
        print("----------------------------------------")
        print("Select an option:")
        print("1.Display Employee Information")
        print("2.Calculate Bouns")
        print("3.Calculate Discount")
        print("4.Remind Legal Holidays")
        print("5.Exit")
        print("----------------------------------------")    

def Admin_Services():
        print("----------------------------------------")
        print("Select an option:")
        print("1.Add New Employee")
        print("2.Update Employee Details")
        print("3.Remove Employee")
        print("4.Exit")
        print("----------------------------------------") 

if __name__ == "__main__":
    print("\033[1m\033[34m----------------------------- Welcome To Employee Managment System  ---------------------------------\033[0m")
    print("\033[1m\033[34m----------------------------- Please Login To Continue ----------------------------------------------\033[0m")

    ID = input("Enter Your Employee ID: ")

    Password = Promot_Password(ID)

    user = authentication.Authrnticate(ID,Password)

    if (user["Name"] == "admin" or user["Name"] == "Admin"):
        while(1):
            Admin_Services()
            option = input("Enter your Choice: ")
            match(option):
                case "1": 
                    for key in new_employee:
                                                          
                        if (key == "ID"):
                            Checking_ID = input(f"Enter The Employee {key}: ")                                  
                            new_employee[key] = Check_Existing_ID(Checking_ID)
                        else:
                            new_employee[key] = input(f"Enter The Employee {key}: ")    
                    add_employee(ID,new_employee)

                case "2":
                    new_data = []                    
                    Employee_ID = input("Please Enter The Employee ID To Modify the data: ")
                    Show_Employee_data(Employee_ID)
                    EditFieldNames = Handle_User_Inputs()
                    for key in EditFieldNames:
                        new_value = input(f"Enter The new {key}: ")
                        new_data.append(new_value)                        
                    Edit_Employee(Employee_ID,EditFieldNames,new_data)
                    print("---------- Employee After Modification ---------")
                    Show_Employee_data(Employee_ID)

                case "3":
                    Employee_id = input("Please Enter The Employee ID To delete the data: ")
                    Delete_Employee(Employee_id)

                case "4":
                    print("\033[1m\033[34mThank you for using Employee Managment System. Goodbye!\033[0m")
                    exit(0) 

                case _:
                    print("-------------------------------------------------------")    
                    print("\033[1m\033Invalid Choice please choose a service from [1 to 4]\033[0m")
                    print("-------------------------------------------------------")   

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
                    print(f"Remind Legal Holidays = {operations.RemindLegalHolidays( int(user["Days Of Absence"]) )}")
                    print("-------------------------------------------------------")    

                case "5":
                    print("\033[1m\033[34mThank you for using Employee Managment System. Goodbye!\033[0m")
                    exit(0)      

                case _:
                    print("-------------------------------------------------------")    
                    print("\033[1m\033[31mInvalid Choice please choose a service from [1 to 5]\033[0m")
                    print("-------------------------------------------------------")    

