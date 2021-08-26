s = 'aeiou'
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for vowel in vowels:
    for letter in s:
        if letter == vowel:
            count += 1
print("Number of vowels: " + str(count))