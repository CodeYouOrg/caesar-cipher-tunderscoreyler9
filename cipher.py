# add your code here

# def caesar_cipher(s):
#     """Function to Caesar-cipher a given sentence/string with a right shift of 5"""
#     encrypted_text = []
    
#     for char in s:
#         if char.isalpha():
#             shift = 5
#             if char.isupper():
#                 ascii_offset = 65
#             else:
#                 ascii_offset = 97
                
#             encrypted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
#             encrypted_text.append(encrypted_char)
#         else:
#             encrypted_text.append(char)
    
#     return ''.join(encrypted_text)


# sentence = input("Please enter a sentence: ")
# encrypted_sentence = caesar_cipher(sentence)
# print(f"The encrypted sentence is: {encrypted_sentence}")

# def caesar_cipher(text, shift):
#     """Function to Caesar-cipher a given sentence/string with a right shift of 5, preserving the case"""
    
#     encrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             shift_amount = shift % 26
#             new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
#             encrypted_text += new_char
#         else:
#             encrypted_text += char
#     return encrypted_text


# plain_text = input("Please enter a sentence: ")
# shift = 5
# encrypted_text = caesar_cipher(plain_text, shift)
# print(f"The encrypted sentence is: {encrypted_text}")

#for char in phrase:
    # if char in alphabet:
    #     index = alphabet.find(char)
    #     index = (index + shift) % 26
    #     char = alphabet[index]
    # encrypted_phrase += char

def cipher(text):
    """Alternate version for caesar_cipher with a right shift of 5"""
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_phrase = ''
    shift = 5
    
    for char in text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            index = alphabet.find(char.lower())
            shifted_index = (index + shift) % 26
            new_char = alphabet[shifted_index]
            if is_upper:
                new_char = new_char.upper()
            encrypted_phrase += new_char
        else:
            encrypted_phrase += char  # Append the character as is if it's not in the alphabet
    
    return encrypted_phrase

def take_input():
    """Function to take input from the user"""
    return input("Please enter a sentence: ")

def main():
    word = take_input()
    encrypted_word = cipher(word)
    print("Your newly encrypted phrase is:", encrypted_word)

if __name__ == "__main__":
    main()