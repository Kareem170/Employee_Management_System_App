import csv

csv_file = "Employees_database.csv"

def Authrnticate(ID , Password):

    # Open CSV file to read Employee Data From it
    file = open(csv_file,"r")

    # create an object that reads lines from a CSV file and maps the information into a dictionary
    Employees = csv.DictReader(file)

    for employee in Employees:
        #print(employee)
        if (ID == employee["ID"]) and (employee["Name"] == "Admin" or employee["Name"] == "admin"):
            if(Password == employee["Password"]):
                print("Welcome Admin!")
                print("Login Successful!")
                return employee
            else:
                print("Wrong Admin Password")
                break

        elif (ID == employee["ID"]):
            if(Password == employee["Password"]):
                print(f"Welcome {employee["Name"]}")
                print("Login Successful!")
                return employee
            else:
                print(f"{employee["Name"]},The Password is incorrect")
                break
    else:
        print("The ID isn't Registered Please, Contact The Admin")    

    file.close()     


# -------- Module Test ----------#
if __name__ ==  "__main__":
    ID = input("Enter Your ID: ")
    Authrnticate (ID,"KM522000@")  
    Authrnticate ('111',"CEO@")
    Authrnticate ('111',"CompanyCO@admin")  
    Authrnticate ('2',"AE522000@")  
    Authrnticate ('200',"CompanyCEO@admin")                         