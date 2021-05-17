'''A basic base64 encoder/decoder built with python'''

import codecs


print("Welcome to basically64, a simple Base64 encoder/decoder. \n")


user_continue = True  # Set a variable for a while loop

while user_continue != False:
    user_choice = input("Please type '1' to encode, or '2' to decode text. ")  # Get user input
    if user_choice == "1":
        text_to_encode = input("Paste your text to encode. \n").encode()  # Get text and store as bytes
        encoded_text = codecs.encode(text_to_encode, "base64").strip()  # Encode the text and then strip the \n
        print(encoded_text)
        print("")
        stop_program = input("Would you like to run the program again? 'Y/N' ").lower()  # Check if user wants to run again
        if stop_program == "y":
            continue
        else:
            break
    elif user_choice == "2":
        text_to_decode = input("Paste the text you would like to decode \n").encode()
        decoded_text = codecs.decode(text_to_decode, "base64").strip()
        print(decoded_text)
        stop_program = input("Would you like to run the program again? 'Y/N' ").lower()
        if stop_program == "n":  # I'm not sure if this is the right way to kill the program, both methods seem to work
            user_continue = False
    else:
        print("Sorry, I didn't unerstand that.")  # Print if users enters anything besides 1 or 2
print("Thanks, bye!")


