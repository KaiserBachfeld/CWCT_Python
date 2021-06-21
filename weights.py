##############################################
#                                            #
# James Bachelder                            #
# CWCT - Python                              #
# M02 Programming Assignment 1               #
#                                            #
# Original Commit Date: 20 June 2021         #
# Purpose - Weight on Other Planets          #
#                                            #
##############################################

#You can calculate an individual's weight on another planet by multiplying their weight times the relative surface gravity of the other world.

#Weight on Other Planet = Weight on Earth x Multiple of Earth’s Gravity

#Design a Python program that asks a user for their name and weight. The program will greet the user by name and then calculate/display the user's weight on the other planets.
#Each item should be displayed on a line by itself.

print("Greetings")
name = input("What is your name? ")
print()
print("Hello", name)
weight = float(input("What is your weight? "))
print()
print("Your weight on the following solar bodies is as follows:")
print()
print("Your weight on the Sun  - ", (weight * 27.01))
print("Your weight on Mercury  - ", (weight * 0.38))
print("Your weight on Venus    - ", (weight * 0.91))
print("Your weight on Earth    - ", (weight * 1))
print("Your weight on the Moon - ", (weight * 0.166))
print("Your weight on Mars     - ", (weight * 0.38))
print("Your weight on Jupiter  - ", (weight * 2.34))
print("Your weight on Saturn   - ", (weight * 1.06))
print("Your weight on Uranus   - ", (weight * 0.92))
print("Your weight on Neptune  - ", (weight * 1.19))
print("Your weight on Pluto    - ", (weight * 0.06))
