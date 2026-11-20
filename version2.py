# Version 2: Added String Formatting

# 1. Get inputs and remove accidental extra spaces at the start/end
first_name = input("Enter First Name: ").strip()
last_name = input("Enter Last Name: ").strip()
section = input("Enter Section: ").strip()
favorite_subject = input("Enter Favorite Subject: ").strip()

# 2. Combine and format strings
full_name = f"{first_name} {last_name}".title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()
char_count = len(full_name)

# 3. Display final formatted output
print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Favorite Subject:", formatted_subject)
print("Character Count:", char_count)
