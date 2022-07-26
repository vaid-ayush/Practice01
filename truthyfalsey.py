def check_even(data):
    if data:
        for value in data:
            if value%2==0:
                print("Even number",value)
numbers=[1,2,3,4,5,6,7,8,9]            
check_even(numbers)                