
# Define some sample modules
def module1():
    print("This is module 1")

def module2():
    print("This is module 2")

def module3():
    print("This is module 3")

# Display a menu to the user
print("Select a module:")
print("1. Module 1")
print("2. Module 2")
print("3. Module 3")

# Get the user's selection
selection = int(input("Enter the number of the module you want to load: "))

# Load the selected module
if selection == 1:
    import module1
elif selection == 2:
    import module2
elif selection == 3:
    import module3
else:
    print("Invalid selection")