import random
import string
l = string.ascii_letters + string.digits + string.punctuation
while True:
    pass_len = int(input("\nEnter the length of the password: "))
    print("\nYour password is: ",end = "")
    for i in range(pass_len):
        print(random.choice(l),end = "")
    print()
    print("\nDo you want to generate another password?")
    choice = input("Enter Yes or No: ").strip().lower()
    if choice == "no":
        print("Thank you for using the Random Password Generator")
        break   

