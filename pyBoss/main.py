#Import modules
import os
import csv
#import us_states

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Set Paths
employee_data_path = os.path.join('..','Resources', 'employee_data.csv')
output_data_file = os.path.join('..','Output',"new_employee_data.csv")

#Define Variables
myEmp_ID = []
myFirstName = []
myFirst = "TBD"
myLastName = []
myLast = "TBD"
myDOB = []
mySSN = []
myState = []
myStateLookup = "XXX"

#Read employees data into cvsreader
with open(employee_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #Append Employer Id to the Emp_Id list
        myEmp_ID.append(row[0])
        #Splint the Name in first and last name, then add to both lists
        myFirst = row[1].split()[0]
        myFirstName.append(myFirst)
        myLast = row[1].split()[1]
        myLastName.append(myLast)
        #Convert date format from YYYY-MM-DD to MM/DD/YYYY then add to list for DOB
        myDOBcheck = row[2]
        myDOByear = row[2][0:4]
        myDOBmonth = row[2][5:7]
        myDOBday = row[2][8:10]
        myDOBnew = (myDOBmonth + "/" + myDOBday + "/" + myDOByear)
        myDOB.append(myDOBnew)
        #Hide first 7 characters from SSN then add to list SSN
        mySSNnew = row[3][7:12]
        mySSNreplace = ('***-**-' + mySSNnew)
        mySSN.append(mySSNreplace)
        #Finally lookup the abbreviated state
        #from us_states import us_state_abbrev as ussa
        myStateLookup = (us_state_abbrev[row[4]])
        myState.append(myStateLookup)

#Zip results into new table and write to new_employee_data.cvs
cleaned_employee_data = zip(myEmp_ID,myFirstName,myLastName,myDOB,mySSN,myState)

with open(output_data_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    # Write in zipped rows
    writer.writerows(cleaned_employee_data)