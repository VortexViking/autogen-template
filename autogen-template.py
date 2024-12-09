# Variables

#feel free to modify this code according to your needs

#input

name = input("Enter name: ")

date = input("Enter today's date (MM/DD/YYYY): ")

ending = input("Enter ending")

#Without Variables

# print(f"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim aeque 
#       doleamus animo, cum corpore dolemus, fieri tamen permagna accessio potest, si aliquod aeternum et infinitum impendere 
#       malum nobis opinemur. Quod idem licet transferre in voluptatem, ut.")


#WITH Variables

print(f"Hello {name}! Today is {date}. The day will end in {ending} days. Here's a snippet of text for you to enjoy: \n 
      Lorem ipsum dolor sit amet, consectetur adipiscing")

#Optional Input Validation
# from datetime import datetime

# def is_valid_name(name):
#     # Check if the name contains only alphabetic characters and spaces
#     return name.replace(" ", "").isalpha()

# def is_valid_date(date_str):
#     # Check if the date is in the format MM/DD/YYYY
#     try:
#         datetime.strptime(date_str, "%m/%d/%Y")
#         return True
#     except ValueError:
#         return False

# # Input
# name = input("Enter name: ")
# while not is_valid_name(name):
#     print("Invalid name. Please enter a valid name.")
#     name = input("Enter name: ")

# date = input("Enter today's date (MM/DD/YYYY): ")
# while not is_valid_date(date):
#     print("Invalid date format. Please enter the date in MM/DD/YYYY format.")
#     date = input("Enter today's date (MM/DD/YYYY): ")

# ending = input("Enter ending: ")

# # Without Variables
# print("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim aeque "
#       "doleamus animo, cum corpore dolemus, fieri tamen permagna accessio potest, si aliquod aeternum et infinitum impendere "
#       "malum nobis opinemur. Quod idem licet transferre in voluptatem, ut.")

# # With Variables
# print(f"Hello {name}! Today is {date}. The day will end in {ending} days. Here's a snippet of text for you to enjoy: \n Lorem ipsum dolor sit amet, consectetur adipiscing")