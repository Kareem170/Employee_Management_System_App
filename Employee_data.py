import csv

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

            print("New employee data has been added")
            break
    else:
        print("You should Login as admin to add an employee")       

#------------------------------------------------------------------------------------------------#

#---------------------------------- Modify Employee Data ---------------------------------------#

def Edit_Employee (AdminID , EmployeeID):
    pass


#---------  Module Test -----------#

if __name__ == "__main__":
    new_employee = {
           "ID" : 20,
            "Name" : "Esraa Mohamed",
            "Department" : "UI & UX Engineer",
            "Salary" :  "$800",
            "Password" : "SM522000@",
            "Days Of Absence" : 7
    }    
    add_employee('111',new_employee)
    Show_Employee_data(new_employee["ID"])

