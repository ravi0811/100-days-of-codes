PLACEHOLDER= "[name]"

with open(r"file_location..........","r") as names_file:
    names= names_file.readlines()

with open(r"file_location..........","r") as letter_file:
    letter_content=letter_file.read()
    for name in names:
        stripped_name= name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)

        with open(f"file_location..........","w") as completed_letter:
            completed_letter.write(new_letter)
