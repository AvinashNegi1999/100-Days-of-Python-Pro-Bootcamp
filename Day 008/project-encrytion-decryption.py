from art import logo
print(logo)

# Caesar Cipher program to encrypt and decrypt a message

# List of lowercase alphabets used for shifting.
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define the Caesar cipher function
def caesar_cipher(original_text, shift_amount, mode):
    output_text = ""  # To store the final result

    # Loop through each letter in the input text
    for letter in original_text:
        # Check if the letter is in the alphabet list
        if letter in alphabets:
            # Find the current index of the letter
            position = alphabets.index(letter)

            # Calculate the shifted index based on encode or decode mode
            if mode == "encode":
                shifted_position = (position + shift_amount) % 26
            elif mode == "decode":
                shifted_position = (position - shift_amount) % 26

            # Append the shifted letter to the result
            output_text += alphabets[shifted_position]
        else:
            # If character is not a letter, keep it unchanged (like space, punctuation)
            output_text += letter

    # Print the final encoded or decoded result
    print(f"Here is your {mode}d result: {output_text}")


# Run the program in a loop until the user chooses to stop
while True:
    # Ask the user whether they want to encode or decode the message
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()

    # Ask the user for the input text
    text = input("Enter your word here: ").lower()

    # Ask how many shifts the user wants to apply
    shift = int(input("How many shifts do you want in the word: "))

    # Call the Caesar cipher function
    caesar_cipher(text, shift, direction)

    # Ask the user if they want to run it again
    restart = input("Do you want to go again? Type 'yes' or 'no': ").lower()
    if restart != 'yes':
        print("Goodbye!")
        break
