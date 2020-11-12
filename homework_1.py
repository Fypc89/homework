# zadanie 1
a = 30
b = 50
c = "My nice text"
request_1 = int(input("type any number between 1-10: "))
request_2 = int(input("type any number between 11-20: "))
request_3 = input("type any 2 words: ")
print(f"here is your results: '{request_1}', '{request_2}', '{request_3}'")
print("-------->")

# zadanie 2
time_in_seconds = int(input("please enter time in seconds "))
hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = time_in_seconds % 3600 % 60
print(f"the time is: {hours}:{minutes}:{seconds}")
print("-------->")

# zadanie 3
n = int(input("type any number from 1-100: "))
n = str(n)
nn = n + n
nnn = n + n + n
result_1_3 = int(n)+int(nn)+int(nnn)
print(f"{n} + {nn} + {nnn} = ", result_1_3)
print("-------->")

# zadanie 4
user_n = int(input("Please enter your number: "))
high_n = 0
while user_n > high_n:
    new_n = user_n % 10
    if new_n > high_n:
        high_n = new_n
        user_n = user_n // 10
    else:
        user_n = user_n // 10
print(f"Highest digit is: {high_n}")
print("-------->")

# zadanie 5
rev = float(input("Revenue in USD: "))
exp = float(input("Expenses in USD: "))
if rev > exp:
    print("You are in profit! Congrats!")
    prof_to_rev = (rev - exp) / rev
    prof_to_rev = "%.2f" % prof_to_rev
    print(f"Your profit ratio is: {prof_to_rev}")
    staff = int(input("How many people work in your company? "))
    prof_per_1 = (rev - exp) / staff
    prof_per_1 = "%.2f" % prof_per_1
    print("Your profit per person is", prof_per_1, "USD")
else:
    print("You are in loss! bye bye")
print("-------->")

# zadanie 6
a = int(input("First day result in km: "))
b = int(input("Target in km: "))
count = 1
while a < b:
    a = a * 1.1
    count += 1
print("Number of days to reach target is:", count)
