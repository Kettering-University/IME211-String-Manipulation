# Integrated Example: Client Communication Processing

# ----------------------------------------------------
# region Setup and Data Initialization
# ----------------------------------------------------
# In this integrated example, you will begin by preparing a personalized greeting for a client, using string formatting to process and present basic client data.

# Given client data: name, the month of the last order, and the amount spent.
client_name = "John Doe"
last_order_month = "April"
amount_spent = 450.75

# Your code here:
# Display a greeting that includes the client's name, last order month, and the formatted amount spent.


# endregion

# ----------------------------------------------------
# region Processing Multiline Client Message
# ----------------------------------------------------
# A client has sent a message that needs to be cleaned up for processing. The message includes unnecessary whitespace, varied capitalization, and confidential information that should be removed before processing.

# Given sample client message:
client_message = """
   Hello,

   There's an issue with the new software update installed last week on our systems. 
   We have noticed a significant slowdown in data processing speeds, which is impacting our daily operations.
   Can you please look into this matter urgently?

   Sincerely,
   John Doe
"""

# Your code here:
# Convert the message to lower case, trim leading/trailing white spaces,
# and remove everything after 'sincerely' for confidentiality.


# endregion

# ----------------------------------------------------
# region Appending Internal Case ID
# ----------------------------------------------------
# After processing the client message for public use, we need to append an internal case ID to the message for internal tracking and reference.

# Given internal case ID:
internal_case_id = "CASE123456"

# Your code here:
# Append the internal case ID to the end of the cleaned message.
final_client_message =

print("Final Client Message with Case ID:")
print(final_client_message)

# endregion
