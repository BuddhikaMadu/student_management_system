import csv
from dataclasses import field

# Write header 
with open("Student_privet_data.csv" , "w") as file_header:
    file_header.write("student name , mother name , father name , address , phone number")

# This is a student data insert section 
while True:
    still_work = input("Still have to add students : Yes / No ").title()
    if still_work == "yes":
        student_name = input("Student Name : ").strip()
        mother_name = input("Mother Name : ").strip()
        father_name = input("Father Name : ").strip()
        address = input("Student Address : ").strip()
        phone_number = int(input("Phone Number : "))

        with open("Student_privet_data.csv" , "a") as insert_data:
            writer = csv.DictWriter(insert_data , fieldnames= ["student name" , "mother name" , "father name" , "address" , "phone number"])
            writer.writerow({"student name":student_name.title() , "mother name":mother_name.title() , "father name" : father_name.title() , "address":address.title() , "phone number":phone_number})
    else:
        exit()
  