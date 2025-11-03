# Name - Harshit Raut
# Enrolment number - 2502140026

import sys

clients = [
{
        'id': 101,
        'name': 'John Dean',
        'dob': '31-03-1977',
        'contact': '9810541010',
        'policies': [
            ('LIC_123', 'Life', 500000, 35000),
            ('HI_001', 'Health', 300000, 15000)
]},
{        'id': 102,
        'name': 'Hugo Bumo',
        'dob': '22-09-1992',
        'contact': '9884577777',
        'policies': [
            ('VI_077', 'Vehicle', 810000, 21000)
]}]

next_client_id = 103

POLICY_TYPES = {"Life", "Health", "Vehicle"}

SYSTEM_PASSWORD = "admin#22"

def find_client_by_id(client_id):
    for client in clients:
        if client['id'] == client_id:
            return client
    return None

def add_client():
    global next_client_id
    print("\n--- Add a New Client ---")

    name = input("Enter client's full name: ")
    dob = input("Enter client's date of birth (DD-MM-YYYY): ")
    contact = input("Enter client's contact number: ")

    new_client = {
        'id': next_client_id,
        'name': name,
        'dob': dob,
        'contact': contact,
        'policies': []
    }
    while True:
        add_policy = input("Do you want to add a policy for this client? (yes/no): ")
        if add_policy == 'yes':
            print(f"Available policy types: {', '}")
            p_number = input("Enter Policy Number: ")
            p_type = input("Enter Policy Type: ")
            if p_type not in POLICY_TYPES:
                print(f"Invalid policy type! Please choose from {POLICY_TYPES}")
                continue
            try:
                p_sum_assured = int(input("Enter Sum Assured amount: "))
                p_premium = int(input("Enter Annual Premium amount: "))
            except ValueError:
                print("Invalid amount. Please enter numbers only.")
                continue

            policy_data = (p_number, p_type, p_sum_assured, p_premium)
            print("Policy added successfully!")
        else:
            break

    clients.append(new_client)
    next_client_id += 1

    print(f"\nClient '{name}' with ID {new_client['id']} added successfully!")

def view_clients():
    print("\n--- All Client Records ---")
    if not clients:
        print("No client records found.")
        return

    for client in clients:
        print("------------------")
        print(f"Client ID: {client['id']}")
        print(f"Name     : {client['name']}")
        print(f"DOB      : {client['dob']}")
        print(f"Contact  : {client['contact']}")

        if client['policies']:
            print("Policies :")
            for policy in client['policies']:
                p_num, p_type, p_sum, p_prem = policy
                print(f"  - No: {p_num}, Type: {p_type}, Sum Assured: ₹{p_sum}, Premium: ₹{p_prem}")
        else:
            print("Policies : No policies found for this client.")
    print("------------------")

def modify_client():
    print("\n--- Modify a Client ---")
    try:
        client_id_to_modify = int(input("Enter the ID of the client you want to modify: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    client = find_client_by_id(client_id_to_modify)
    if client is None:
        print(f"Error: Client with ID {client_id_to_modify} not found.")
        return

    print(f"Modifying client: {client['name']} (ID: {client['id']})")

    client['name'] = input(f"Enter new name (current: {client['name']}): ") or client['name']
    client['dob'] = input(f"Enter new DOB (current: {client['dob']}): ") or client['dob']
    client['contact'] = input(f"Enter new contact (current: {client['contact']}): ") or client['contact']

    print("\nClient details updated successfully!")

def delete_client():
    print("\n--- Delete a Client ---")
    try:
        client_id_to_delete = int(input("Enter the ID of the client you want to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    client = find_client_by_id(client_id_to_delete)
    if client is None:
        print(f"Error: Client with ID {client_id_to_delete} not found.")
        return

    confirm = input(f"Are you sure you want to delete {client['name']} (ID: {client['id']})? (yes/no): ")

    if confirm == 'yes':

        print("Client deleted successfully.")
    else:
        print("Deletion cancelled.")

def search_client():
    print("\n--- Search for a Client ---")
    print("Search by: \n1. Name \n2. Policy Type")

    choice = input("Enter your choice (1 or 2): ")
    found_clients = []
    if choice == '1':
        search_name = input("Enter the client name to search for: ")
        for client in clients:
            if search_name in client['name']:
                found_clients.append(client)

    elif choice == '2':
        search_policy = input(f"Enter policy type to search for ({', '}): ")
        for client in clients:
            for policy in client['policies']:
                if policy[1] == search_policy:
                    found_clients.append(client)
                    break
    else:
        print("Invalid choice.")
        return

    if found_clients:
        print("\n--- Search Results ---")
        for client in found_clients:
            print(f"ID: {client['id']}, Name: {client['name']}, Contact: {client['contact']}")
    else:
        print("\nNo clients found matching your criteria.")

def generate_reports():
    print("\n--- System Reports ---")

    total_clients = len(clients)
    total_policies = 0
    total_sum_assured = 0

    for client in clients:
        total_policies += len(client['policies'])
        for policy in client['policies']:
            total_sum_assured += policy[2]

    print(f"Total Number of Clients: {total_clients}")
    print(f"Total Number of Policies: {total_policies}")
    print(f"Total Sum Assured Across All Policies: ₹{total_sum_assured}")

def main_menu():
    while True:
        print("\n=============================")
        print("  Insurance Advisor System Menu")
        print("=============================")
        print("1. Add a new client")
        print("2. View all clients")
        print("3. Modify a client's details")
        print("4. Delete a client")
        print("5. Search for a client")
        print("6. Generate reports")
        print("7. Exit")
        print("=============================")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_client()
        elif choice == '2':
            view_clients()
        elif choice == '3':
            modify_client()
        elif choice == '4':
            delete_client()
        elif choice == '5':
            search_client()
        elif choice == '6':
            generate_reports()
        elif choice == '7':
            print("Thank you for using the Insurance Advisor System. Goodbye!")
            sys.exit()  #for program exit
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def login():
    print("--- Welcome to the Insurance Advisor System ---")
    for attempt in range(3):
        password = input("Please enter the password to continue: ")
        if password == SYSTEM_PASSWORD:
            print("Access Granted!")
            return True
        else:
            remaining_attempts = 2 - attempt
            if remaining_attempts > 0:
                print(f"Incorrect password. You have {remaining_attempts} attempt(s) left.")
            else:
                print("Too many incorrect attempts. The program will now exit.")
                return False
    return False

if __name__ == "__main__":
    if login():
        main_menu()
