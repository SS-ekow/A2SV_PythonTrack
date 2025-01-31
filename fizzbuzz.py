def fizzbuzz(nums):

    for num in nums:
        if num %3 ==0 and num %5==0:
            print("FizzBuzz")

        elif num %3 ==0:
            print("Fizz")

        elif num %5 == 0:
            print("Buzz")

        else:
            print("None")


    
x = [1,2,3,4,5,6,7,8,9,10,15, 12, 30]

fizzbuzz(x)



