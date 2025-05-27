"""Create a Python function that takes a string as input and returns the reverse of that string. For example, if the input is "hello, " the function should return "olleh."""

def reverse_string(input_string):
    return "".join(reversed(input_string))

print(reverse_string("hello"))        