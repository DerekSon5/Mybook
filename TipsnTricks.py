## Exercice 9.3
import random
number = random.randint(1,51)
print(number)
number = random.randint(1,51)
print(number)
number = random.randint(1,51)
print(number)

numb = input ("Type a number: ")

try:
    result = int(numb) + 1
except:
    print("Not valid number")
    quit()

print("The result is " + str(result))
