##############################################
#                                            #
# James Bachelder                            #
# CWCT - Python                              #
# M02 Programming Assignment 1               #
#                                            #
# Original Commit Date: 20 June 2021         #
# Purpose - Restaurant Bill                  #
#                                            #
##############################################

#Prompt the user for the amount of the meal (e.g. $32.95).
#Compute the tax on the restaurant bill. The tax should be 6.75 percent of the meal cost. 
#Prompt the user for the tip amount (Suggesting a value equal to 18 percent of the total).
#Display the meal cost, tax amount, tip amount, and total bill on the screen.

#Name your script restaurant.py and submit it as an attachment to the assignment.


meal = float(input("Amount of Meal: "))
tax = 6.75
tip = float(input("Please leave a tip (suggested amount is 18): "))

p_tax = ((tax/100)+1) #convert to percentages to add to the total
p_tip = ((tip/100)+1) 

total = ((meal * p_tax) * p_tip)

print("Meal Cost $", meal)
print("Tax Amount", tax, "%")
print("Tip Amount", tip, "%")
print("Total Bill $", round(total,2))