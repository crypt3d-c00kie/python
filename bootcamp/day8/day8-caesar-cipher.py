#day8
#caesar cipher


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :\n")
# text = input("Type your message :\n").lower()
# shift = int(input("Type the shift number : "))

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)    
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The encoded text ::  {cipher_text}")

# encrypt(text,shift)

import string

alphabets = string.ascii_lowercase + string.ascii_lowercase
text = list(input("Text :: ".lower()))
choice = input("Enter encode to ENCRYPT, decode to DECRYPT, exit to EXIT :: ".lower())
shift_number = int(input("Shift (1 to 25) :: "))

end = False

while not end:
    #search through the text
    if choice == "encode":
        for i in range(len(text)):
            #get position of each character within sentence
            if text[i] == ' ':
                text[i] = ' '
            else:
                new_letter = alphabets.index(text[i]) + shift_number
                text[i] = alphabets[new_letter]
            #converting list back to string
        print(" ".join(map(str,text)))
        end = True
    elif choice == "decode":
        for i in range(len(text)):
            if text[i] == ' ':
                text[i] = ' '
            else:
                new_letter = alphabets.index(text[i]) - shift_number
                text[i] = alphabets[new_letter]
        print(" ".join(map(str,text)))
        end = True
    else:
        print("Invalid entry, try again!")