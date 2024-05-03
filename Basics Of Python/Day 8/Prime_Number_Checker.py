n = int(input("Enter a number : "))
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"Yes {number} is a prime number.")
    else:
        print(f"No {number} is not prime number.")
prime_checker(number = n)