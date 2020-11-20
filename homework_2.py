# zadanie 1
list = ["text", 1, 18.5, None]
print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(type(list[3]))
print("------------>")
print("------------>")

# zadanie 2
user_inp = input("Type your list HERE: ").split()
print("list:", user_inp)
even = user_inp[1::2]
uneven = user_inp[::2]
print("even positions:", even)
print("uneven positions:", uneven)
result = []
for i in range(len(even)):
    result.append(even[i])
    result.append(uneven[i])
if len(even) < len(uneven):
    result.append(uneven[-1])
    print(result, " - merging of even and uneven positions, last position untouched")
else:
    print(result, " - merging of even and uneven positions")
print("------------>")
print("------------>")

# zadanie 3
my_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
           6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
user_entry = int(input("Enter month number 1-12: "))
print("Your month is: ", my_dict.get(user_entry))
print("------------>")
print("------------>")

# zadanie 4
user_entry = input("Type your list here:").split()
count = 0
for el in user_entry:
    count +=1
    print(count, el[0:10])
print("------------>")
print("------------>")


# zadanie 5
my_list = [7, 5, 3, 3, 2]
u_number = int(input("Enter your number here:"))
my_list.insert(0, u_number)
for j in range(0, 6):
    for i in range(0, 5):
        if my_list[i] <= my_list[i + 1]:
            swap = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = swap
print(my_list)
print("------------>")
print("------------>")

# zadanie 6
dict1 = {}
name = input("name:")
price = input("price:")
qty = input("qty:")
unit = input("unit:")
dict1.update({"name": name, "price": price, "qty": qty, "unit": unit})
print(dict1)
dict2 = {}
name = input("name:")
price = input("price:")
qty = input("qty:")
unit = input("unit:")
dict2.update({"name": name, "price": price, "qty": qty, "unit": unit})
print(dict2)
dict3 = {}
name = input("name:")
price = input("price:")
qty = input("qty:")
unit = input("unit:")
dict3.update({"name": name, "price": price, "qty": qty, "unit": unit})
print(dict3)
print("name: ", [dict1.get("name"), dict2.get("name"), dict3.get("name")])
print("price: ", [dict1.get("price"), dict2.get("price"), dict3.get("price")])
print("qty: ", [dict1.get("qty"), dict2.get("qty"), dict3.get("qty")])
print("unit: ", [dict1.get("unit"), dict2.get("unit"), dict3.get("unit")])
