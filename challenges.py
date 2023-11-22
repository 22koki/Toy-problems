# Challenge 1: Converting 12-hour time to 24-hour time

def convert_to_24_hour(hour, minute, period):
    # If it's "am" and hour is 12, set hour to 0. If it's "pm" and hour is not 12, add 12 to the hour.
    if period == "am" and hour == 12:
        hour = 0
    elif period == "pm" and hour != 12:
        hour += 12
    # Return a formatted string with 24-hour time.
    return f"{hour:02d}{minute:02d}"

# Example usage:
result = convert_to_24_hour(8, 30, "am")
print(result)  # Output: "0830"

result = convert_to_24_hour(8, 30, "pm")
print(result)  # Output: "2030"


# Challenge 2: Two numbers are positive

def two_positive(a, b, c):
    # Count the number of positive numbers in the input.
    positive_count = sum(num > 0 for num in [a, b, c])
    # Return True if exactly two of the three numbers are positive.
    return positive_count == 2

# Example usage:
result = two_positive(2, 4, -3)
print(result)  # Output: True

result = two_positive(-4, 6, 0)
print(result)  # Output: False


# Challenge 3: Consonant value

def consonant_value(s):
    vowels = "aeiou"
    # Split the string into substrings using vowels as separators.
    substrings = s.split("[" + vowels + "]+")
    # Calculate the value of each substring and find the maximum value.
    values = [sum(ord(ch) - ord('a') + 1 for ch in substring) for substring in substrings]
    return max(values)

# Example usage:
result = consonant_value("zodiacs")
print(result)  # Output: 26

result = consonant_value("strength")
print(result)  # Output: 57
