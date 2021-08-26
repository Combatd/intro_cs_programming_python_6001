# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

s = 'azcbobobegghakl'
substrings = [s[i: j] 
    for i in range(len(s))
    for j in range(i + 1, len(s) + 1)
]
countOfBob = substrings.count('bob')

print("Number of times bob occurs is: " + str(countOfBob))