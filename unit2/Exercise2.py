# infinite loop (never breaks the first while loop)

# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while guess <= x:
#     if abs(guess**2 -x) >= epsilon:
#         guess += step

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))

# 4.999999....

# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while abs(guess**2-x) >= epsilon:
#     if guess <= x:
#         guess += step
#     else:
#         break

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))

# prints out failed (never higher than the epsilion)
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))