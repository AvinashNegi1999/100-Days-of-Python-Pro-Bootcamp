#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        
# Read the list of names from the invited_names.txt file
# Using raw string (r"") so backslashes in the path are treated literally
with open(r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 024\Mail Merge Project Start\Input\Names\invited_names.txt") as invited_names:
    names_list = invited_names.readlines()  # Reads all lines into a list

# Read the letter template from starting_letter.txt
with open(r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 024\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    contents = file.read()  # Reads the entire file as a single string

# Loop through each name from the names list
for name in names_list:
    name = name.strip()  # Removes newline characters (\n) from the name
    new = contents.replace("[name]", name)  # Replace placeholder with actual name

    # Save the personalized letter in the "ReadyToSend" folder
    # f-string is used to dynamically include the person's name in the filename
    with open(
        fr"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 024\Mail Merge Project Start\Output\ReadyToSend\letter_for_{name}.txt",
        mode="w"  # "w" mode creates a new file or overwrites an existing one
    ) as final_file:
        final_file.write(new)  # Write the personalized letter to the file
