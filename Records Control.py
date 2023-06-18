def add_record():
    record = input("Enter the record you want to add: ")
    with open("records.txt", "a") as file:
        file.write(record + "\n")
    print("Record added successfully!")

def delete_record():
    record = input("Enter the record you want to delete: ")
    with open("records.txt", "r") as file:
        lines = file.readlines()
    with open("records.txt", "w") as file:
        for line in lines:
            if line.strip() != record:
                file.write(line)
    print("Record deleted successfully!")

def update_record():
    old_record = input("Enter the record you want to update: ")
    new_record = input("Enter the new record: ")
    with open("records.txt", "r") as file:
        lines = file.readlines()
    with open("records.txt", "w") as file:
        for line in lines:
            if line.strip() == old_record:
                file.write(new_record + "\n")
            else:
                file.write(line)
    print("Record updated successfully!")

def view_records():
    with open("records.txt", "r") as file:
        records = file.readlines()
        if not records:
            print("No records found.")
        else:
            print("Records:")
            for record in records:
                print(record.strip())

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