'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

'''


def create_phone_number(n):
    if len(n) > 10:
        raise Exception("Invalid Number")

    if len(n) == 10:
        area_code = n[:3]
        prefix = n[3:6]
        suffix = n[6:]

        return f'({area_code[0]}{area_code[1]}{area_code[2]}) {prefix[0]}{prefix[1]}{prefix[2]}-{suffix[0]}{suffix[1]}{suffix[2]}{suffix[3]}'



res = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(res)
