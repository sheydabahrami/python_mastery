# 08 For Loops

# They are used to reapet a task
# In this example we are trying to send a message to a use at least 3 time

for number in range(3):  # the range goes from 0, 1, 2
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):  # range goes from 1, 2, 3
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):  # range goes from 1, 3, 5, 7, 9
    print("Attempt", number, number * ".")



# 09 For..Else

# Lesson how to break a for loop

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# 10 Nested Loops
# Loops inside other loops

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")



# 11 Iterables

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)


# 12 While Loops

number = 100
while number > 0:
    print(number)
    number = number // 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)



# 13 Infinte Loops

while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break



# 11 Exercice

# Display the even number ( 2 4 6 8) followed by this message "We have 4 even numbers"
# 2
# 4
# 6
# 8
# We have 4 even numbers

# My anwser
for number_even in range(1, 10):
    if number_even % 2 == 0:
        print(number_even)
    elif number_even > 8:
        print("We have 4 even numbers")
        break

# Mosh anwser
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count = count + 1
        print(number)
print(f"we have {count} even number")


# In my anwser I did not count the numbers