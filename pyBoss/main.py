# Define Variables
import os
import csv

#import pandas as pd

employee_data_path = os.path.join('..','Resources', 'employee_data.csv')
output_data_file = os.path.join('..','Output',"new_employee_data.csv")

myEmp_ID = []
myFirstName = []
myFirst = "TBD"
myLastName = []
myLast = "TBD"
myDOB = []
#myDOBnew = "TBD"
mySSN = []
myState = []

# def type_convert(var):
#     if len(var) == 10:                 
#         return pd.to_datetime(var, format='%m/%d/%Y').date()

with open(employee_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        myEmp_ID.append(row[0])
        myFirst = row[1].split()[0]
        myFirstName.append(myFirst)
        myLast = row[1].split()[1]
        myLastName.append(myLast)
        myDOBcheck = row[2]
        myDOByear = row[2][0:4]
        myDOBmonth = row[2][5:7]
        myDOBday = row[2][8:10]
        myDOBnew = (myDOBmonth + "/" + myDOBday + "/" + myDOByear)
        myDOB.append(myDOBnew)
        mySSNnew = row[3][7:12]
        mySSNreplace = ('***-**-' + mySSNnew)
        mySSN.append(mySSNreplace)
        myState.append(row[4])

cleaned_employee_data = zip(myEmp_ID,myFirstName,myLastName,myDOB,mySSN,myState)

with open(output_data_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    # Write in zipped rows
    writer.writerows(cleaned_employee_data)