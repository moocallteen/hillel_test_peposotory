# for i in range(6): # 6 numbers in row 0-5
#     print(i)

# for i in range(1, 7, 2): # numbers in row,  1 - first number,  7 - last number not included, 2 - step
#     print(i)

# word = "Hello World!"
# for i in word:
#     print(i)

# word = "Hello World!"
# for i in word:
#     print(i * 3)

# word = "Hello World!"
# for i in word:
#     if i == "!":
#         print("Yes")

count = 0
word = "Hello World!"
for i in word:
    if i == "l":
        count += 1

print("Count:", count)