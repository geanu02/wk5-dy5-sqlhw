# Objective: Write a Python function called count_vowels that takes a single string argument and returns the total count of vowels (a, e, i, o, u) in the input string.
# Function signature: def count_vowels(s: str) -> int:
# Examples:
# count_vowels(“hello”) should return 2
# count_vowels(“world”) should return 1
# count_vowels(“Python”) should return 1
# count_vowels(“aeiou”) should return 5
# count_vowels(“”) should return 0
# Constraints:
# The input string will only contain lowercase and uppercase English letters (a-z, A-Z).
# The function should be case-insensitive, i.e., it should count both lowercase and uppercase vowels.

def count_vowels(_input):
    vow_count = 0
    for letter in _input:
        if letter.lower() in 'aeiou':
            vow_count += 1
    return vow_count

print(count_vowels('as'))