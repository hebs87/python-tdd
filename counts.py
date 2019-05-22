'''Function designed to count the number of uppercase characters in a message
Starts with a count
Increments the count each time an uppercase character is identified
Returns the total count'''
def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
    #Alternative way of writing the function
    #return sum([1 for c in message if c.isupper()])

'''Automated test using assertions'''
#Assertion with empty string to ensure count is 0
assert count_upper_case("") == 0, "Empty string"
#Assertion with one uppercase to ensure count is 1
assert count_upper_case("A") == 1, "One upper case"
#Assert to check for multiple uppercase chars
assert count_upper_case("Aa Aa Aa Aa") == 4, "Four upper case"
#Assertion with one lowercase to ensure count is 0 and function isn't just counting all string chars
assert count_upper_case("a") == 0, "One lower case"
#Assertion with just special chars, which we would expect to be 0
assert count_upper_case("£$%^&") == 0, "Special characters"
#Addition assert to check for uppercase if passed with special, lowercase and numbers chars
assert count_upper_case("A£a;1") == 1, "One upper case with special chars"

#Finally, a print statement to confirm that all test passed
print("All the tests passed")

'''Manual test
print(count_upper_case("Hello World"))'''