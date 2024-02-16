import csv

# Define the CSV file containing usernames and passwords
csv_file = 'CSV Key.csv'

# Function to prompt user for login credentials
def get_login_credentials():
    username = input("Username: ")
    password = input("Password: ")
    return (username, password)

# Check if provided username and password are present in the same row of the CSV file
def authenticate(username, password, csv_file):
    found_in_same_row = False
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if username == row[0] and password == row[1]:
                found_in_same_row = True
                break
# Add Import Libraries Here after successful login
    if found_in_same_row:
        print("O7 sir")
    else:
        print("Intruder! Your attempt has been logged")

# Get user input for login credentials
username, password = get_login_credentials()

# Authenticate the user
authenticate(username, password, csv_file)
