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

def caesar_cipher(text, shift):
    """Function to Caesar-cipher a given sentence/string with a right shift of 5, preserving the case"""
    
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text


plain_text = input("Please enter a sentence: ")
shift = 5
encrypted_text = caesar_cipher(plain_text, shift)
print(f"The encrypted sentence is: {encrypted_text}")
