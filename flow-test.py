#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def even_numbers():
    x = 0
    while x < 50:
        x+=1
        if x%2!=0:
            continue
        print(x)
even_numbers() 
#Write a function that takes a list of integers as input and prints the sum of all
# the even numbers in the list
def even_nums_sum(nums):
    sum = 0
    for n in nums:
        if n%2==0:
            sum+=n
            print(sum)
nums = [12,45,6,9,16,20,43,67]
even_nums_sum(nums)

#Write a function that takes any two integers as input, and prints the sum of all the numbers
# between the two integers (inclusive) that are divisible by 3.
def divisible_by_three(num1,num2):
    sum = 0
    for i in range (num1,num2):
        if i %3==0:
            sum+=i
            print(sum)
divisible_by_three()
#Write a function that takes an integer argument and prints "Prime" if the number is prime,
# and "Not prime" if the number is not prime.
def check_prime(number):
    condition = False
    if number == 1:
        print("${number} is not a prime number")
    elif number > 1:
        for i in range(2,number):
            if number%i==0:
                condition = True
    if condition:
        print("Is not a prime number")
    else:
        print("Is a prime number")