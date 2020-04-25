current_num = 1
while current_num <= 4:
    print(current_num, end="\t")
    current_num += 1

# little game
prompt = "\nTell me something, and I will repeat it to you: "
prompt = "\nEnter 'quit' to end the program. "
message = ''
active = True
while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active = False