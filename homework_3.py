# zadanie 1:
def dev(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "can't devide on 0"
result = dev(float(input("number 1: ")), float(input("number 2: ")))
print(round(result, 2))
print("------------>")
print("------------>")

# zadanie 2:
def lst(name, surname, dob, city, email, phone):
    return (name, surname, dob, city, email, phone)

print(lst(input("имя: "), input("фамилия: "), input("год рождения: "),
          input("город проживания: "), input("email: "), input("телефон: ")))
print("------------>")
print("------------>")

# zadanie 3:
def my_func(el1, el2, el3):
    if el1 >= el3 and eld2 >= el3:
        print("the sum is:", el1 + el2)
    elif el1 >= el2 and el3 >= el2:
        print("the sum is:", el1 + el3)
    else:
        print("the sum is:", el2 + el3)
my_func(int(input("Number1: ")), int(input("Number2: ")), int(input("Number3: ")))
print("------------>")
print("------------>")
# zadanie 4.1
def my_func(x, y):
    res = x ** (y * -1)
    res = 1 / res
    print(res)
my_func(float(input("Positive number: ")), int(input("Negative number: ")))

# zadanie 4.2
def my_func(x, y):
    res = 1
    for n in range(y * -1):
        res = res * x
    return 1 / res

print(my_func(float(input("Positive number: ")), int(input("Negative number: "))))
print("------------>")
print("------------>")

# zadanie 5
def my_sum ():
    fin_sum = 0
    b = False
    while b == False:
        number = input('Input numbers or A to stop: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'A':
                b = True
                break
            else:
                res = res + int(number[el])
        fin_sum = fin_sum + res
        print(f'Current sum is {fin_sum}')
    print(f'Your final sum is {fin_sum}')

my_sum()
print("------------>")
print("------------>")

# zadanie 6
def int_func(words):
    result = ""
    for el in words:
        el = el[0].upper() + el[1:]
        result += el + " "
    return result


fin_res = input("type your words: ")
print(int_func(fin_res.split()))
print("------------>")
print("------------>")
