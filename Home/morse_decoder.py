#!/usr/bin/env checkio --domain=py run morse-decoder

# Your task is to decrypt the secret message using theMorse code.
# The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
# If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
# 
# 
# 
# Input:The secret message.
# 
# Output:The decrypted text.
# 
# Precondition:
# 0<len(message)<100
# The message will consists of numbers and English letters only.
# 
# 
# END_DESC

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    #replace this for solution
    c = code.split('  ')
    s = ''
    for i in range(len(c)):
        t = c[i].split()
        for y in range(len(t)):
            for k,v in MORSE.items():    #k for k,v in d.items() if v == value
             if k == t[y]:
                if i == 0 and y ==0:
                    s = s + str(v).upper()
                    continue
                s= s +  str(v)
        if i < len(c)-1: 
            s = s +' '
            
    
   


    return s

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder("... --- -- .   - . -..- -"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")