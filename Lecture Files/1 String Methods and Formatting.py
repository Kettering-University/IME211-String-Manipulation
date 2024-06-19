# String Methods and Formatting in Python

# ----------------------------------------------------
# region String Methods
# ----------------------------------------------------
# Python provides a variety of methods that can be used to manipulate strings effectively. These methods do not modify the original string but return new strings.

# Example: Common String Methods
sample_text = "  industrial engineering  "
upper_text = sample_text.upper()  # Converts all characters to uppercase
lower_text = sample_text.lower()  # Converts all characters to lowercase
stripped_text = sample_text.strip()  # Removes leading and trailing spaces
found_index = sample_text.find('engineer')  # Returns the start index of the substring
replaced_text = sample_text.replace('engineering', 'management')  # Replaces 'engineering' with 'management'

# TODO: Activity 3 - Applying String Methods
# First, create a string 'Python Programming' and convert it to uppercase.
# Next, find the position of 'Pro' in the string and replace 'Programming' with 'Development'.
# Your code here:


# endregion

# ----------------------------------------------------
# region String Formatting
# ----------------------------------------------------
# Python provides several ways to format strings, which is especially useful when you need to create strings dynamically.

# Example: Using str.format() and f-strings
base_price = 120
tax_rate = 0.05
total_price = base_price * (1 + tax_rate)
f_string = f"The total price with tax is: ${total_price:.2f}"  # Using f-string

# endregion

# ----------------------------------------------------
# region Working with Multiline Strings
# ----------------------------------------------------
# Multiline strings in Python are created using triple quotes, which can be either double quotes (""") or single quotes ('''). This is useful for creating strings that span multiple lines.

# Example: Creating and Using Multiline Strings
multi_line_string = """This is an example of a
multiline string that spans several
lines in the Python code."""
print(multi_line_string)

# TODO: Activity 5 - Working with Multiline Strings
# First, create a multiline string that represents a simple block of text explaining a basic concept of industrial engineering.
# Next, print this string.
# Your code here:


# endregion

# ----------------------------------------------------
# region Advanced String Operations
# ----------------------------------------------------
# Python strings offer a variety of advanced methods that can be used for complex manipulations.
# These include searching for substrings, replacing parts of strings, and splitting strings into lists.

# Example: Searching, Replacing, Splitting, and Joining
detailed_description = "The process involves analysis, design, and optimization."
# Split the string into words
words = detailed_description.split()
print(words)
print(words[1])
# Join words into a sentence with a specific separator
joined_sentence = ' | '.join(words)

# TODO: Activity 6 - Analyzing and Reformatting a String
# First, split the sentence into words
# Then, join them with a hyphen '-' as a separator.
# Finally, print just 'aunt' from the list of split words
# Your code here:
sentence = "Please~excuse~my~dear~aunt~Sally."


# endregion
