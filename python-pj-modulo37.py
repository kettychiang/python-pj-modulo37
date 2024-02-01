def map_number_to_char(num):
    if 0 <= num <= 25:
        # Map to uppercase alphabet
        return chr(ord('A') + num)
    elif 26 <= num <= 35:
        # Map to decimal digits
        return str(num - 26)
    elif num == 36:
        # Map 36 to underscore
        return "_"
    else:
        # Handle other cases (optional)
        return "?"

# List of numbers to be mapped
numbers = [350, 63, 353, 198, 114, 369, 346, 184, 202, 322, 94, 235, 114, 110, 185, 188, 225, 212, 366, 374, 261, 213]

# Map each number and concatenate the results
result = ''.join(map(lambda num: map_number_to_char(num % 37), numbers))

# Print the result
print(result)
