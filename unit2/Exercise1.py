# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

iteration = 0
while iteration < 5:
    count = 0 # count will always reset to 0 at beginning of every iteration
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 