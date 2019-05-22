x = 2
y = 1

'''assert keyword declares an assertion
We say that if the condition returns true, code runs as normal
If condition runs false, we throw an error and the code execution stops
assert, followed by condition, followed by message if condition returns false
Put in placeholders and use .format() to pass variable values into placeholders
The error message shows as 'AssertionError' in interpreter'''
assert x < y, "{0} should be less than {1}".format(x, y)

print(x + y)