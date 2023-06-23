import pandas as pd
from tabulate import tabulate

# CSV file path
CSV_FILE = "records.csv"

# Create an empty DataFrame or load existing CSV file
try:
    records_df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    records_df = pd.DataFrame(columns=["Name", "Age", "Address", "Phone Number", "Email"])

def add_record():
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    address = input("Enter the address: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email: ")
    record = {"Name": name, "Age": age, "Address": address, "Phone Number": phone_number, "Email": email}
    records_df.loc[len(records_df)] = record
    records_df.to_csv(CSV_FILE, index=False)
    print("Record added successfully!")

def delete_record():
    name = input("Enter the name of the record you want to delete: ")
    records_df.drop(records_df[records_df["Name"] == name].index, inplace=True)
    records_df.to_csv(CSV_FILE, index=False)
    print("Record deleted successfully!")

def update_record():
    name = input("Enter the name of the record you want to update: ")
    field = input("Enter the field you want to update (Name, Age, Address, Phone Number, Email): ")
    new_value = input("Enter the new value: ")
    records_df.loc[records_df["Name"] == name, field] = new_value
    records_df.to_csv(CSV_FILE, index=False)
    print("Record updated successfully!")

def view_records():
    if records_df.empty:
        print("No records found.")
    else:
        print(tabulate(records_df, headers="keys", tablefmt="fancy_grid"))

def main():
    while True:
        print("\n1. Add a record")
        print("2. Delete a record")
        print("3. Update a record")
        print("4. View records")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_record()
        elif choice == "2":
            delete_record()
        elif choice == "3":
            update_record()
        elif choice == "4":
            view_records()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
