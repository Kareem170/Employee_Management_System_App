import csv
from getpass import getpass
import time


csv_file = "Employees_database.csv"

new_employee = {
    "ID" : 0,
    "Name" : "",
    "Department" : "",
    "Salary" :  "",
    "Password" : "",
    "Days Of Absence" : 0
}    

#------------------------------------------------------------------------------------------#
#-------------------------------- Check if ID exists or not -------------------------------#
def Check_Existing_ID(ID):
    # Open CSV file to read Employee Data From it
    file = open(csv_file,"r")

    # create an object that reads lines from a CSV file and maps the information into a dictionary
    Employees = csv.DictReader(file)

    for employee in Employees:
        while f'{ID}' == employee["ID"]:
            ID = input("ID already exists ,Please Enter another ID: ")

    return ID        

#------------------------------------------------------------------------------------------#
#------------------------------------- Password Attempts ----------------------------------#

def Promot_Password(ID,max_attempts=3,block_time=10):
    Password_attempt = 1

    Correct_Password = ""

    Entered_Password = ""

    # Open CSV file to read Employee Data From it
    file = open(csv_file,"r")

    # create an object that reads lines from a CSV file and maps the information into a dictionary
    Employees = csv.DictReader(file)

    # Get the correct password for the employee ID
    for employee in Employees:
        if(f'{ID}' == employee["ID"]):
            Correct_Password = employee["Password"]
            break
        else:
            continue
    else:
        print("The ID isn't registered ,Please Contact the admin")
        exit(1)    
    
    Entered_Password = getpass("Enter Your Password: ")

    while (1):
        
        while Entered_Password != Correct_Password:
            
            if(Password_attempt == max_attempts):
                print(f"You Enter The Password {Password_attempt} Wrong Times please wait for {block_time} Seconds and try again")                
                time.sleep(block_time)
                Entered_Password = getpass("\033[43mPlease Re-Enter The Password For one last time\033[0m: ")
                if Entered_Password == Correct_Password:
                    break 
                else:
                    print("\033[1m\033[31mYou have exceeded the max number of allowed trials ,Please Contact the admin\033[0m")
                    exit(1)    
            else:
                Password_attempt+=1
                Entered_Password = getpass("Incorrect Password ,Please Re-Enter The Password: ")

        else:
            print("\033[32mCorrect Password! Access Granted\033[0m")
            return Entered_Password


#------------------------------------------------------------------------------------------#
#---------------------------------- Print Employee Data ----------------------------------#

def Show_Employee_data(EmployeeID):
    
    # Open CSV file to read Employee Data From it
    file = open(csv_file,"r")

    # create an object that reads lines from a CSV file and maps the information into a dictionary
    Employees = csv.DictReader(file)

    for employee in Employees:
        if (f'{EmployeeID}' == employee["ID"]):
            print(f"--------------{employee["Name"]} Data ------------")
            for key in employee:
                print(f"{key}: {employee[key]}")
            print("---------------------------------------------------")
            file.close()    
            break
        else:
            continue
    else:
        print("Employee ID isn't Registered")




#------------------------------------------------------------------------------------------#
#---------------------------------- Add New Employee --------------------------------------#

def add_employee(Admin_ID,new_Employee_data):

    # Open CSV file to read Employee Data From it
    file = open(csv_file,"r")

    # create an object that reads lines from a CSV file and maps the information into a dictionary
    Employees = csv.DictReader(file)

    for employee in Employees:
        if (Admin_ID == employee["ID"]) and (employee["Name"] == "Admin" or employee["Name"] == "admin"):

            new_employee = {
            "ID" : new_Employee_data ["ID"],
            "Name" : new_Employee_data ["Name"],
            "Department" : new_Employee_data ["Department"],
            "Salary" : new_Employee_data ["Salary"],
            "Password" : new_Employee_data ["Password"],
            "Days Of Absence" : new_Employee_data ["Days Of Absence"]
            }

            employee_data = open(csv_file,"a",newline='')

# This creates a dict object named "write_new_employee" that will be used to write dictionaries to the CSV file.
            write_new_employee = csv.DictWriter(employee_data, fieldnames=new_employee.keys())
            
# Checks if the file is empty. If it is, the file pointer will be at position 0 to write the header "Dictionary Keys".
            if employee_data.tell() == 0:
                write_new_employee.writeheader()

# write the dictionary value --> new employee data
            write_new_employee.writerow(new_employee)

            print("\033[32m ------ New employee data has been added ------\033[0m")
            file.close()
            break
    else:
        print("You should Login as admin to add an employee")       

#------------------------------------------------------------------------------------------------#

#---------------------------------- Modify Employee Data ---------------------------------------#

def Edit_Employee (EmployeeID, Field_To_Modify, new_data ):
    
    # Open CSV file to read Employee Data From it
    file = open(csv_file,"r")

    # create an object that reads lines from a CSV file and maps the information into a dictionary
    Employees = csv.DictReader(file)    

    # create a  List of dictionaries
    Employees_List =  list(Employees)

    # read the header "Keys" and store it
    headers = Employees.fieldnames

    Data_Updated =  False

    for employee in Employees_List:

        if(employee["ID"] == f'{EmployeeID}'):
            
            for index,key in enumerate(Field_To_Modify):
                if key in employee:
                    employee[key] = new_data[index]
                else:
                    print(f"Invalid Attribute Field Name --> {key}")    
        
        else:
            continue            
        
        Data_Updated = True
        break

    if Data_Updated:
        print("Employee Data is Updated Successfully")
        
        employee_data = open(csv_file,"w",newline='')

        #  This creates a dict object named "write_new_employee" that will be used to write dictionaries to the CSV file.
        write_new_employee = csv.DictWriter(employee_data, fieldnames=headers)
        
        write_new_employee.writeheader()
    
        # write the dictionary value --> new employee data
        write_new_employee.writerows(Employees_List)        
 
    else:
        print("The Entered ID isn't Registered")


#------------------------------------------------------------------------------------------------#

#---------------------------------- Delete Employee Data ---------------------------------------#

def Delete_Employee(Employee_id):
    rows_to_keep = []
    
    Employee_deleted =  False

    Delete_confirmation = ""

    # Lambda Fn to Detect the row with the corresponding ID
    condition = lambda row : row["ID"] == f'{Employee_id}'

    # Open CSV file to read Employee Data From it
    file = open(csv_file,"r")

    # create an object that reads lines from a CSV file and maps the information into a dictionary
    Employees = csv.DictReader(file)    

    # create a  List of dictionaries
    Employees_List =  list(Employees)

    # read the header "Keys" and store it
    headers = Employees.fieldnames

    for employee in Employees_List:
        if condition(employee):
            Employee_deleted = True
            print("---------- Employee Data To Be Deleted -------------")
            print(f"-------------- {employee["Name"]} Data ------------")
            for key in employee:
                print(f"{key}: {employee[key]}")
            continue
        else:
            rows_to_keep.append(employee)

    if Employee_deleted:

        print("-------------------------------------")

        Delete_confirmation =  input("\033[44mAre you sure that you want to delete the employee data [Y/N]:\033[0m ")

        if (Delete_confirmation  ==  "Y"  or Delete_confirmation == "y"):
                
            print("Employee Data is Deleted Successfully")
                
            employees_data = open(csv_file,"w",newline='')

            #  This creates a dict object named "Remove_employee" that will be used to write dictionaries to the CSV file.
            Remove_employee = csv.DictWriter(employees_data, fieldnames=headers)
            
            Remove_employee.writeheader()

            # write the dictionary value --> without the deleted employee
            Remove_employee.writerows(rows_to_keep)

        elif (Delete_confirmation == "N" or Delete_confirmation == "n"):
            print("OK Employee Data Still Exist")

        else:
            print("You entered invalid delete confirmation letter [Y/N]")
  
    else:  
        print("The ID isn't Registered or maybe deleted")








#---------  Module Test -----------#

if __name__ == "__main__":
    new_employee = {
           "ID" : 9,
            "Name" : "Esraa Mohamed",
            "Department" : "UI & UX Engineer",
            "Salary" :  "$800",
            "Password" : "SM522000@",
            "Days Of Absence" : 7
    }    
    add_employee('111',new_employee)
    Show_Employee_data(new_employee["ID"])
    
    edit_employee = [
    "Alaa Samy",
    "5"
    ]

    Edit_Employee(16,["Name","Days Of Absence"],edit_employee)

    Delete_Employee(9)
    print(Promot_Password(1,5))
    print(Check_Existing_ID(1))
