def find_largest_prime(num):
    factor  = 2
    factors =[]

    while num > 1:
        if num % factor == 0:
            factors.append(factor)
            num /= factor
        elif factor ==2:
            factor += 1
        else: factor +=2
    return max(factors)

def main():
    num =  600851475143
    print(find_largest_prime(num))

main() # 6857