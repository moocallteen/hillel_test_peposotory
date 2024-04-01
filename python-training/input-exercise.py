userOutput = "Your result:"

num1 = int(input("Your first number:"))

num2 = int(input("Your second number:"))

print(userOutput, num1 + num2)
print(userOutput, num1 - num2)
print(userOutput, num1 * num2)
print(userOutput, num1 / num2)
print(userOutput, pow(num1, num2))
print(userOutput, round(num1 / num2))

num11 = int(input("Your another first number:"))
num11 += 1 # num11 + 1

num21 = int(input("Your another second number:"))

print(userOutput, num11 + num21)
print(userOutput, num11 - num21)
print(userOutput, num11 * num21)
print(userOutput, num11 / num21)
print(userOutput, pow(num11, num21))
print(userOutput, round(num11 / num21))