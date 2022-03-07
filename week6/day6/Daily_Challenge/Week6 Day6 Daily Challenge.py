#test text = how are you?
#test cipher = ipx bsf zpv@
def caesar_cipher():
  space = " "
  shift = 1
  while True:
    start = input("would you like to encrypt (type:enc) or decrypt (type:dec)?")
    if start == "enc":
      text = input("enter text:")
      cypher_text = ""
      for letter in text:
        if letter == space:
          cypher_text += space
        else:
          cypher_text += chr(ord(letter) + shift)
      print(f"encrypted text: {cypher_text}")
      break
    elif start == "dec":
      cypher_text = input("enter cipher:")
      text = ""
      for letter in cypher_text:
        if letter == space:
          text += space
        else:
          text += chr(ord(letter) - shift)
      print(f"decrypted text: {text}")
      break
    else:
      print("type again")
      continue

caesar_cipher()







