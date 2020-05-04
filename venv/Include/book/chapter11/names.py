from use_unittest import get_format_name

print("Enter 'q' at any time you want to quit. ")
while True:
    first = input("\nPlease Give Me Your First-Name: ")
    last = input("\nPlease Give Me Your Last-Name: ")
    if first == 'q' or last == 'q':
        break
    full_name = get_format_name(first, last)
    print("Your Full-Name is: {}".format(full_name))