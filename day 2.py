"""
QUESTION 1:
------------
Description: Using datatype intialize the below details
             emp_Id
             emp_Name
             emp_Email
             emp_Phone_No
             emp_Salary
             emp_Gender
             emp_City
"""

emp_Id          = 1201
emp_Name        = "MahendraN"
emp_Email       = "mahe@gmail.com"
emp_Phone_No    = 0987654321
emp_Salary      = 23021.40
emp_Gender      = "Male"
emp_City        = "Chennai"

print("\nEmployee Details")
print("================")
print("Employee id:",emp_Id)
print("Employee Name:",emp_Name)
print("Employee Email id:",emp_Email)
print("Employee Phone Number:",emp_Phone_No)
print("Employee Salary:",emp_Salary)
print("Employee Gender:",emp_Gender)
print("Employee City:",emp_City)



"""
QUESTION 2:
-------------
Description: Using input() method get the below details
        studentId
        studentName
        Mark_1
        Mark_2
        Mark_3
        Mark_4
        Mark_5
        :Find the total and average of marks

"""

studentId    = int(input("\nEnter Student Id:"))
studentName  = input("Enter Student Name:")
Mark_1       = int(input("Enter Mark_1:"))
Mark_2       = int(input("Enter Mark_2:"))
Mark_3       = int(input("Enter Mark_3:"))
Mark_4       = int(input("Enter Mark_4:"))
Mark_5       = int(input("Enter Mark_5:"))
total        = Mark_1 + Mark_2 + Mark_3 + Mark_4 + Mark_5
average      = Mark_1 + Mark_2 + Mark_3 + Mark_4 + Mark_5 / 5

print("\nStudent Mark Details")
print("=================")
print("Student Id is:",studentId)
print("Student Name is:",studentName)
print("Student Mark_1 is:",Mark_1)
print("Student Mark_2 is:",Mark_2)
print("Student Mark_3 is:",Mark_3)
print("Student Mark_4 is:",Mark_4)
print("Student Mark_5 is:",Mark_5)
print("Total:",total)
print("Average is:",average)


"""
QUESTION 3:
------------
Description: Using input() method get the below details
        student_Id
        student_Name
        student_Email
        student_Phoneno
        student_Dept
        student_Gender
        student_City

"""

student_Id = int(input("Enter Student ID: "))
student_Name = input("Enter Student Name: ")
student_Email = input("Enter Student Email: ")
student_Phoneno = int(input("Enter Student Phone Number: "))
student_Dept = input("Enter Student Department: ")
student_Gender = input("Enter Student Gender: ")
student_City = input("Enter Student City: ")

print("\nStudent Details")
print("===============")
print("Student Id:",student_Id)
print("Student Name:",student_Name)
print("Student Email id:",student_Email)
print("Student Phone Number:",student_Phoneno)
print("Student Department:",student_Dept)
print("Student Gender:",student_Gender)
print("Student City:",student_City)


"""
QUESTION 4:
------------
Description: Using datatype intialize the below details
        clg_Id
        clg_Name
        clg_Email
        clg_Phone_No
        clg_Code
        clg_Dept_Count
        clg_Address

"""

clg_Id         = 121
clg_Name       = "Sri Vasavi College"
clg_Email      = "info@svc.edu.in"
clg_Phone_No   = 9876543210
clg_Code       = 1001
clg_Dept_Count = 13
clg_Address    = "Erode"

print("\n College Details")
print("==================")
print("College Id is:",clg_Id)
print("College Name is:",clg_Name)
print("College Email is:",clg_Email)
print("College Phone number is:",clg_Phone_No)
print("College Code is:",clg_Code)
print("College Department Count is:",clg_Dept_Count)
print("College Address is:",clg_Address)


"""
QUESTION 5:
------------
Description: Using datatype intialize the below details
             com_Id
             com_Name
             com_Email
             com_Phone_No
             com_Employee_Count
             com_Location
             com_Revenue
             com_CEO
             com_Founded_Date
"""

company_Id = 101                        
company_Name = "Solutions Ltd."    
company_Email = "contact@techsolutions.com"  
company_Phone_No = "0123456789"         
company_Employee_Count = 250            
company_Location = "Bangalore, India"   
company_Revenue = 5000000.00            
company_CEO = "John "                
company_Founded_Date = "2010-05-15"     


print("\nCompany Details:")
print("================")
print(f"ID: {company_Id}")
print(f"Name: {company_Name}")
print(f"Email: {company_Email}")
print(f"Phone Number: {company_Phone_No}")
print(f"Employee Count: {company_Employee_Count}")
print(f"Location: {company_Location}")
print(f"Revenue: ${company_Revenue}")
print(f"CEO: {company_CEO}")
print(f"Founded Date: {company_Founded_Date}")


"""
QUESTION 6:
------------
Description: Using input() method get 15 bankdetails [15 variables]

"""

bank_Name = input("Enter Bank Name: ")
bank_Branch = input("Enter Bank Branch: ")
bank_IFSC = input("Enter Bank IFSC Code: ")
bank_MICR = input("Enter Bank MICR Code: ")
bank_Account_Number = int(input("Enter Bank Account Number: "))
bank_Account_Holder_Name = input("Enter Account Holder's Name: ")
bank_Account_Type = input("Enter Account Type (e.g., Savings, Current): ")
bank_Phone_Number = input("Enter Bank Phone Number: ")
bank_Email = input("Enter Bank Email Address: ")
bank_Address = input("Enter Bank Address: ")
bank_City = input("Enter Bank City: ")
bank_State = input("Enter Bank State: ")
bank_Country = input("Enter Bank Country: ")
bank_PIN_Code = int(input("Enter Bank PIN/ZIP Code: "))
bank_Customer_Service_Number = int(input("Enter Bank Customer Service Number: "))


print("\nBank Details:")
print(f"Bank Name: {bank_Name}")
print(f"Branch: {bank_Branch}")
print(f"IFSC Code: {bank_IFSC}")
print(f"MICR Code: {bank_MICR}")
print(f"Account Number: {bank_Account_Number}")
print(f"Account Holder's Name: {bank_Account_Holder_Name}")
print(f"Account Type: {bank_Account_Type}")
print(f"Phone Number: {bank_Phone_Number}")
print(f"Email: {bank_Email}")
print(f"Address: {bank_Address}")
print(f"City: {bank_City}")
print(f"State: {bank_State}")
print(f"Country: {bank_Country}")
print(f"PIN/ZIP Code: {bank_PIN_Code}")
print(f"Customer Service Number: {bank_Customer_Service_Number}")


"""
QUESTION 7:
------------
Description: Using input() method enter all state name in India

"""

state_1 = input("Enter the name of state 1: ")
state_2 = input("Enter the name of state 2: ")
state_3 = input("Enter the name of state 3: ")
state_4 = input("Enter the name of state 4: ")
state_5 = input("Enter the name of state 5: ")
state_6 = input("Enter the name of state 6: ")
state_7 = input("Enter the name of state 7: ")
state_8 = input("Enter the name of state 8: ")
state_9 = input("Enter the name of state 9: ")
state_10 = input("Enter the name of state 10: ")
state_11 = input("Enter the name of state 11: ")
state_12 = input("Enter the name of state 12: ")
state_13 = input("Enter the name of state 13: ")
state_14 = input("Enter the name of state 14: ")
state_15 = input("Enter the name of state 15: ")
state_16 = input("Enter the name of state 16: ")
state_17 = input("Enter the name of state 17: ")
state_18 = input("Enter the name of state 18: ")
state_19 = input("Enter the name of state 19: ")
state_20 = input("Enter the name of state 20: ")
state_21 = input("Enter the name of state 21: ")
state_22 = input("Enter the name of state 22: ")
state_23 = input("Enter the name of state 23: ")
state_24 = input("Enter the name of state 24: ")
state_25 = input("Enter the name of state 25: ")
state_26 = input("Enter the name of state 26: ")
state_27 = input("Enter the name of state 27: ")
state_28 = input("Enter the name of state 28: ")

# Displaying the state names entered
print("\nList of States in India:")
print(f"1. {state_1}")
print(f"2. {state_2}")
print(f"3. {state_3}")
print(f"4. {state_4}")
print(f"5. {state_5}")
print(f"6. {state_6}")
print(f"7. {state_7}")
print(f"8. {state_8}")
print(f"9. {state_9}")
print(f"10. {state_10}")
print(f"11. {state_11}")
print(f"12. {state_12}")
print(f"13. {state_13}")
print(f"14. {state_14}")
print(f"15. {state_15}")
print(f"16. {state_16}")
print(f"17. {state_17}")
print(f"18. {state_18}")
print(f"19. {state_19}")
print(f"20. {state_20}")
print(f"21. {state_21}")
print(f"22. {state_22}")
print(f"23. {state_23}")
print(f"24. {state_24}")
print(f"25. {state_25}")
print(f"26. {state_26}")
print(f"27. {state_27}")
print(f"28. {state_28}")


"""
QUESTION 8:
------------
Description: Using input() method get below details
             district_State
             district_Name
             district_Area
             district_population
             district_Captial
             district_Urban_Count
             district_Rural_Count

"""


district_State = input("Enter the State of the District: ")
district_Name = input("Enter the District Name: ")
district_Area = input("Enter the District Area (in square kilometers): ")
district_Population = int(input("Enter the District Population: "))
district_Capital = input("Enter the District Capital: ")
district_Urban_Count = int(input("Enter the Number of Urban Areas in the District: "))
district_Rural_Count = int(input("Enter the Number of Rural Areas in the District: "))

print("\nDistrict Details:")
print(f"State: {district_State}")
print(f"District Name: {district_Name}")
print(f"Area: {district_Area} sq km")
print(f"Population: {district_Population}")
print(f"Capital: {district_Capital}")
print(f"Urban Area Count: {district_Urban_Count}")
print(f"Rural Area Count: {district_Rural_Count}")


# ------------------------------ End -----------------------------------------