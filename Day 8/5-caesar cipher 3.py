alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift):
    if(direction=="encode"):
      second_text = ""
      for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        second_text += alphabet[new_position]
      print(f"The encoded text is {second_text}")
    else:
      second_text = ""
      for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        second_text += alphabet[new_position]
      print(f"The decoded text is {second_text}")

caesar(text,shift)