for num in range(1,101):
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBUZZ")
    elif num % 5 ==0:
        print('buzz')
    elif num % 3== 0 :
        print('FIZZ') 
    else:
        print(num)
   