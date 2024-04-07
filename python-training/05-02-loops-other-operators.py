# for i in range(11):

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

for i in range(1, 111):
    # if i == 5:
    #     break
    if i % 2 == 0 or i % 3 == 0: # except all numbers that divide by 2 and 3
        continue
    print(i)