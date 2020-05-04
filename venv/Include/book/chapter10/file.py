pi_path="D:\\abc\\Pi.txt"

with open(pi_path) as file_object:
    for line in file_object:
        print(line.rstrip())

wheather_path="D:\\abc\\wheather.txt"
with open(wheather_path) as wheather_object:
    contents = wheather_object.read()
    for line in contents:
        print(line, end="")

with open(wheather_path) as wheather_object:
    contents = wheather_object.read()

print(contents)

print("-------------------------------------")

with open(wheather_path) as wheather_object:
    lines = wheather_object.readlines()

print(lines)
for line in lines:
    print(line.rstrip())

print("-------------------------------------")
with open(pi_path) as pi_obj:
    lines = pi_obj.readlines()

pi_string=''
for line in lines:
    pi_string += line.strip()

print(pi_string[:10] + "...")
print(len(pi_string))

# birthday = input("Please Input Your Birthday: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first 30 digits of pi!")
# else:
#     print("Your birthday not appears in the first 30 digits of pi!")

print("--------------------------------------")
write_file = "D:\\abc\\programming.txt"
with open(write_file, 'w') as pro_obj:
    pro_obj.write("I love Yangjinyun!\n")
    pro_obj.write("I love Programming!\n")
    pro_obj.write("I love China!\n")\

with open(write_file, 'a') as pro_obj:
    pro_obj.write("------------------------\n")
    pro_obj.write("hello Python!\n")

