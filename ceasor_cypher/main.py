alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  text.strip(' ')
  encrypted_text = []
  for item in text:
      if item in alphabet:
          indx = alphabet.index(item) + shift
          if indx < 26:
              encrypted_text.append(alphabet[indx])
          else:
              encrypted_text.append(alphabet[(indx - 26)])
      else:
          encrypted_text.append(item)
  encrypted_text = ''.join(encrypted_text)
  return encrypted_text


def decrypt(text, shift):
  text.strip(' ')
  decrypted_text = []
  for item in text:
      if item in alphabet:
          indx = alphabet.index(item) - shift
          if indx >= 0:
              decrypted_text.append(alphabet[indx])
          else:
              decrypted_text.append(alphabet[(indx + 26)])
      else:
          decrypted_text.append(item)
  decrypted_text = ''.join(decrypted_text)
  return decrypted_text

def caesar(text,shift,direction):
  if direction == 'encode':
    result = encrypt(text, shift)
  elif direction == 'decode':
    result = decrypt(text, shift)
  else:
    print("Wrong input")

  print(f"Here's the {direction}d result: {result}")
 
from art import logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text,shift,direction)