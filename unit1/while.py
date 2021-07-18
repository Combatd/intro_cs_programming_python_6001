# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

i = 2
while i <= 10:
    print(i)
    i += 2
print("Goodbye!")

# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print("Hello!")
i = 10
while i > 0:
    print(i)
    i -= 2

# fibonacci sequence in while loop
i = 0
end = 5

while end > 0:
    i += end
    end -= 1
print(i)