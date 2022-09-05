# keysmash
 Encode text into keysmash-like text.

## How it works

 The encode function takes in a string and a row of keys. This row can be one of the included English layout rows, or a custom string.
 Then every character in the string is given a random pair in the key row (making the keysmash), their difference is calculated, and that difference is turned into a character in the alphabet (making the code). The keysmash and code are returned.
 
 Decoding works similarly. The function takes in the encoded string and the code to decode it. The index of each of the code's characters in the alphabet is calculated, and if it exceeds the difference between 25 and the index of the corresponding encoded string's character, then a negative index is used (index minus 26). Then those indices are added to the characters of the encoded string, effectively cancelling out the difference between the original letters and the keysmash ones.

 The encoder doesn't preserve case. This is intended behaviour.

 As far as I can tell, this works similarly to a one-time pad substitution cipher.
