from pyparsing import WordStart
from caesar_cipher.corpus_loader import word_list, name_list






def encrypt(plain_txt, key):
   
  
  text = ''

  for char in plain_txt:
    if not char.isalpha():
      text += char
    elif char.isupper():
      text += chr((ord(char) + key - 65) % 26 + 65)
    else:
      text += chr((ord(char) + key - 97) % 26 + 97)
  
  return text

 
def decrypt(plain_txt, key):
    return encrypt(plain_txt, -key)
   

# def crack(text):
#     key = 0
#     percent = 0
#     for letters in text:
#       real_word = 0
#       key+=1
#       message = decrypt(text, key)
#       output_message = message.split(' ')


def crack(plain_txt):

    for i in range(26):
        total = 0
        test_text = encrypt(plain_txt, i)
        output_list = test_text.split()
        for letters in output_list:
            if letters in name_list or letters.lower() in word_list:
                total += 1
        
        if (total / len(output_list)) > 1/2:
            return ' '.join(output_list)

    return ''



    
