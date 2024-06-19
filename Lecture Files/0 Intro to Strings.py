# Introduction to Strings in Python

# ----------------------------------------------------
# region Introduction to Strings
# ----------------------------------------------------
# Strings in Python are used to store textual data and are one of the most commonly used data types.
# They are created by enclosing characters in single quotes (' ') or double quotes (" ").

# Example: Creating Strings
string1 = 'Hello, Industrial Engineering!'
string2 = "Python programming is powerful."

# Immutability of Strings
# Strings are immutable, which means once a string is created, the characters within it cannot be changed.

# endregion

# ----------------------------------------------------
# region Accessing Characters in Strings
# ----------------------------------------------------
# Individual characters in a string can be accessed using indexing, with indices starting at 0 for the first character.

# Example: Indexing and Slicing
greeting = "Hello, World!"
first_letter = greeting[0]  # Accesses the first character 'H'
slice_of_greeting = greeting[7:12]  # Slices the string to get 'World'

# TODO: Activity 1 - Slicing Strings
# First, access the last character of the greeting.
# Next, slice the greeting to only include "Hello".
# Your code here:


# endregion

# ----------------------------------------------------
# region Basic String Operations
# ----------------------------------------------------
# Strings can be concatenated (added together) and repeated using operators.

# Example: Concatenation and Repetition
part1 = "Data"
part2 = "Analysis"
full_phrase = part1 + " " + part2  # Concatenates 'Data' and 'Analysis'
repeated_phrase = (part1 + " ") * 3  # Repeats 'Data ' three times

# TODO: Activity 2 - Combining and Repeating Strings
# First, create two strings: 'Industrial' and 'Engineering', and concatenate them with a space between.
# Next, repeat the word 'Hello' 5 times with spaces in between each repetition.
# Your code here:


# endregion
