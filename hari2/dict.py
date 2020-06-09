def ninja_intro(ninja_dictionary):
    for key,val in ninja_dictionary.items():
    print("I am {} and I am a {} belt.".format(key, val))

ninja_belts = {}

while True
    ninja_name = input("Ninja name : ")
    ninja_belt = input("Ninja belt : ")
    ninja_belts[ninja_name] = ninja_belt

    another = input("Add another? y/n ")
    if another == 'y':
        continue
    else:
        break

print(ninja_belts)
ninja_intro(ninja_belts)