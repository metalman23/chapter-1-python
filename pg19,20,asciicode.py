charachter = "K"
ascii =ord(charachter)
print (type(ascii))
print ("the decimal value for the letter K is: ",ascii)
output = chr(ascii)
print (type(output))
print ("the charachter represented by decimal value", ascii, " is: ",output)
print ("\n")

charachter = "C"
key = 3
ascii = ord(charachter)
encryptedLetter = chr(ascii + key)
print ("the encrypted letter is: ", encryptedLetter)
