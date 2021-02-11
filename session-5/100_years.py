#Write a program to ask users for their name and age and print to the user the year in which they'll be of 100 years of age

name = input("What is your name? ")
print("Hello", name)
age = int(input("What is your age? "))

print(f"{name}, you will be of 100 years of age in the year {2021+(100-age)}")
