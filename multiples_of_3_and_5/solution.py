def multiples_of_3_and_5(num):
    sum = 0
    for i in range(num):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    print(sum)

num =1000
print(multiples_of_3_and_5(num)) # 233168