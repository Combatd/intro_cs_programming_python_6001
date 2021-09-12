inputString = 'azcbobobegghakl'

prevChar = ""
currentString = ""
longestString = ""

for char in inputString: # iterate through each character
    if prevChar <= char: # each character has a "number" value relative to alphabet
        currentString += char # add it to the string if it is after the previous char alphabetically
        if len(currentString) > len(longestString): # check if it is longer than the previous longest string
            longestString = currentString # set the new longest String
    else:
        currentString = char # just set it to the char if the string is empty right now
    prevChar = char # track the previousChar before next iteration
print('Longest substring in alphabetical order is: ' + longestString )