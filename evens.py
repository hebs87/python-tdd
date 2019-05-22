'''Define function after the tests have been written'''

def is_even(number):
    '''Helper function
    Checks if the number of evens is even or odd
    Returns True if even, or False if odd'''
    return number % 2 == 0

def even_number_of_evens(numbers):
    '''
    Returns the number of even numbers contained in a list of numbers.
    `numbers` should be a list containing numbers
    
    Returns either True or False based on a number of criteria.
        - if `numbers` is empty, return `False`
        - if the number of even numbers is odd, return `False`
        - if the number of even numbers is 0, return `False`
        - if the number of even numbers is even, return `True`
    '''
    
    # Check to see if the list is empty
    '''refactor code
    if numbers ==[]:
        return False
    else:'''
    # Set a `number_of_evens` variable that will be incremented each time an even number is found
    #evens = 0
    # Iterate of over each item and if it's an even number, increment the `evens` variable
    #for num in numbers:
        # Use modulo operator to see if the number is fully divisible by 2 - if it is, it is an even number
    ''' Refactored code with helper function
    if num % 2 == 0:'''
        #if is_even(num):
            #evens += 1
        
    #if evens == 0:
        #return False
    #else:
        # Returns true if the number of evens is even
    '''Refactored code with helper function
    return evens % 2 == 0'''
        #return is_even(evens)
    
    '''Final step of REFACTORING - using Pythonic method'''
    evens = sum([1 for num in numbers if is_even(num)])
    return False if evens == 0 else is_even(evens)
    
'''Challenge to write a function that returns true if the list contains an even number of even numbers
Tests written before defining the function'''
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2,3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert  even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed")