# Student ADT using Dictionary

student = {}

# Create Record
student["Roll No"] = int(input("Enter Roll Number: "))
student["Name"] = input("Enter Name: ")
student["Age"] = int(input("Enter Age: "))
student["Marks"] = float(input("Enter Marks: "))

print("\nStudent Record Created")
print(student)

# Menu
print("\nChoose an Operation")
print("1. Create (Add New Field)")
print("2. Update")
print("3. Delete")
print("4. Display Record")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    
    key = input("Enter New Field Name: ")
    value = input("Enter Value: ")
    student[key] = value
    print("\nField Added Successfully!")

elif choice == 2:
    key = input("Enter Field to Update: ")
    if key in student:
        value = input("Enter New Value: ")
        student[key] = value
        print("\nRecord Updated Successfully!")
    else:
        print("Field not found!")

elif choice == 3:
    key = input("Enter Field to Delete: ")
    if key in student:
        del student[key]
        print("\nField Deleted Successfully!")
    else:
        print("Field not found!")

elif choice == 4:
    print("\nStudent Record")
    print(student)

else:
    print("Invalid Choice!")

print("\nFinal Student Record")
print(student)
