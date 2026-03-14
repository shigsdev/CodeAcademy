"""

Casual Coded Correspondence: The Project In this project, you will be working to code and decode various messages
between you and your fictional cryptography enthusiast pen pal Vishal. You and Vishal have been exchanging letters
for quite some time now and have started to provide a puzzle in each one of your letters. Here is his most recent
letter:

 Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a  Caesar
 Cipher. Here's how it works: You take your message, something like "hello" and then you shift all of the letters by
 a certain offset. For example, if I chose an offset of 3 and a message of "hello", I would code my message by
 shifting each letter 3 places to the left (with respect to the alphabet). So "h" becomes "e", "e" becomes, "b",
 "l" becomes "i", and "o" becomes "l". Then I have my coded message,"ebiil"! Now I can send you my message and the
 offset and you can decode it. The best thing is that Julius Caesar himself used this cipher, that's why it's called
 the Caesar Cipher! Isn't that so cool! Okay, now I'm going to send you a longer coded message that you have to
 decode yourself!

    xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa
    myjx jxu iqcu evviuj!

This message has an offset of 10. Can you decode it?
"""

'''

Step 1: Decode Vishal's Message In the cell below, use your Python skills to decode Vishal's message and print the 
result. Hint: you can account for shifts that go past the end of the alphabet using the modulus operator, 
but I'll let you figure out how! 

'''
print("\n####################### Step 1: Decode Vishal's Message **********************************************\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"


def decode(string, offset):
    newstring = ""

    for letters in range(len(string) - 1):
        if string[letters].lower() in alphabet:
            newletter = ""
            newposition = alphabet.find(string[letters]) + offset
            if newposition > len(alphabet) - 1:
                newposition = newposition - len(alphabet)
            newletter = alphabet[newposition]
            newstring += newletter
        else:
            newstring += string[letters]

    return newstring


print(decode(
    "    xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!",
    10))

'''
Provided Solution: 

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""
for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        translated_message += letter
print(translated_message)
'''

print("\n####################### Step 2: Send Vishal a Coded Message**********************************************\n")


def encode(string, offset):
    newstring = ""
    for letters in string:
        if letters.lower() in alphabet:
            # newletter = ""
            # newposition = alphabet[alphabet.find(letters) - offset]
            # if newposition > len(alphabet) - 1:
            #    newposition = newposition - len(alphabet)
            newstring += alphabet[alphabet.find(letters) - offset]
        else:
            newstring += letters

    return newstring


if encode(
        "    hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back "
        "with the same offset",
        10) == "    xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj":
    print("Correct")
print(encode(
    "    hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back "
    "with the same offset",
    10))

print("\n###################Step 4 - Cesar Cipher with No Keyword**********************************************\n")


def decode_brute_force(string):
    possibles = []
    for offsets in range(1,len(alphabet)):
        possibles.append("Offset " + str(offsets) + decode(string, offsets))
    return possibles


brute_forced = decode_brute_force(
    "        vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")

for options in brute_forced:
    print(options, "\n")

'''  
solution provided 
coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# The easiest way to break this code is to simply brute force though all of the possible shifts.
# We'll only need to try 25 different shifts, so it's not computationally expensive. Then we can 
# look through all of the outputs and look for the one that in english, and we've decoded our message!
for i in range(1,26):
    print("offset: " + str(i))
    print("\t " + decoder(coded_message, i) + "\n")
    
'''


print("\n###################Step 5 - The Vingere Cipher**********************************************\n")


def decode_vigenere(coded_message, keyword):
    keyword_counter = 0
    decoded_message = ""
    for letter in coded_message:
        if not letter in alphabet:
            decoded_message += letter
        else:
            offset_keyword = alphabet.find(keyword[keyword_counter])
            decoded_letter = alphabet[alphabet.find(letter) - offset_keyword]
            decoded_message += decoded_letter
            if keyword_counter < (len(keyword) - 1):
                keyword_counter += 1
            else:
                keyword_counter = 0
    return decoded_message


print(decode_vigenere("     dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!",
                      "friends"))

'''  
def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))

'''
def encode_vigenere(coded_message, keyword):
    keyword_counter = 0
    encoded_message = ""
    for letter in coded_message:
        if not letter in alphabet:
            encoded_message += letter
        else:
            encoded_letter = alphabet[(alphabet.find(letter) + alphabet.find(keyword[keyword_counter])) % (len(alphabet))]
            encoded_message += encoded_letter
            if keyword_counter < (len(keyword) - 1):
                keyword_counter += 1
            else:
                keyword_counter = 0
    return encoded_message


print("     you were able to decode this? nice work! you are becoming quite the expert at crytography! encoded with friends = ", encode_vigenere("     you were able to decode this? nice work! you are becoming quite the expert at crytography!",
                      "friends"))

''' 
Solution Provided: 

def vigenere_coder(message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(vigenere_coder(message_for_v,keyword))
print(vigenere_decoder(vigenere_coder(message_for_v, keyword), keyword))

'''