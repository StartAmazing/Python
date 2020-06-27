# # use elif judge
# while True:
#     replay = input("Enter Your Age: ")
#     if replay == 'stop': break
#     elif not replay.isdigit(): print("bad" * 10)
#     else: print(int(replay) ** 2)
# print("Game Over!")


# use try-catch
while True:
    replay = input("Enter Your Age: ")
    if replay == 'stop': break
    try:
        age = int(replay)
    except:
        print("bad" * 8)
    else:
        print(age ** 3)
print("Bye")