
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
    encrpt_word=''
    for letter in text:
        position=alphabet.index(letter)
        new_pos=position+shift
        encrpt_letter=alphabet[new_pos]
        encrpt_word+=encrpt_letter    
    print(encrpt_word)

   
encrypt(text,shift)
