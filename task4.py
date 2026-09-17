import random

otp = random.randint(1000, 9999)

print("Your OTP is:", otp)

user_otp = int(input("Enter OTP: "))

if user_otp == otp:
    print("OTP Verified Successfully")
else:
    print("Invalid OTP")

name = input("enter your name: ")
print("Hello", name, "would you like to proceed with the transaction? (yes/no)")
if input().capitalize() == "Yes":
   print("transaction processing....")
else:
   print("transaction cancelled")

print("what would you like to check?", name, "if you want to check your balance or transaction history? (balance/history)")
if input().capitalize()=="Balance":
    print("your balance is Rs. 100000")
else:
    print("please visit bank for your transaction history")
