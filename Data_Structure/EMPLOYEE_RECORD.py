# Employee ADT using Dictionary

employee = {}

# Create Employee Record
employee["Emp ID"] = int(input("Enter Employee ID: "))
employee["Name"] = input("Enter Employee Name: ")
employee["Department"] = input("Enter Department: ")
employee["Salary"] = float(input("Enter Salary: "))

print("\nEmployee Record Created")
print(employee)

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
    employee[key] = value
    print("\nField Added Successfully!")

elif choice == 2:
    key = input("Enter Field to Update: ")
    if key in employee:
        value = input("Enter New Value: ")
        employee[key] = value
        print("\nRecord Updated Successfully!")
    else:
        print("Field not found!")

elif choice == 3:
    key = input("Enter Field to Delete: ")
    if key in employee:
        del employee[key]
        print("\nField Deleted Successfully!")
    else:
        print("Field not found!")

elif choice == 4:
    print("\nEmployee Record")
    print(employee)

else:
    print("Invalid Choice!")

print("\nFinal Employee Record")
print(employee)
