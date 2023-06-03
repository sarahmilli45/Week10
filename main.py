print("Welcome!")

# Get company name
company_name = input("\nPlease enter your company name: ")
# Get number of feet of cable
feet_of_cable = input("Please enter the feet of cable: ")
feet_of_cable = float(feet_of_cable)
# Multiply feet by .87 for cost
cost_of_cable = feet_of_cable * .87

message = f"{company_name.title()}, your total cost is: $" + str(cost_of_cable)
print(message)
print("Thank you for your order!")
print("Come back soon!")