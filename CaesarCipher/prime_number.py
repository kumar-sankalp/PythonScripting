'''
def prime_checker(number):
    if (number > 1) and (number <=100):
        if number not in (2,3,5,7,11,13):
            if number % 2==0 or number % 3==0 or number % 5==0 or  number % 7==0 or  number % 11==0 or number % 13==0:
                print("Not prime")    
            else:
                print("Its Prime!")
        else:
            print('its prime')        
    else:
        print("enter number b/w 1 to 100 Please!")                        

'''

def prime_checker(number):
    is_prime= True
    for i in range(2,number):
        print(i)
        print(number%i)
        if number % i ==0:
            is_prime=False
    if is_prime:
        print('The Number is prime')
    else: 
        print('Its not a prime')


n = int(input("enter number"))
prime_checker(number=n)
