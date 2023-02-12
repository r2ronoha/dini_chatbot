from time import sleep

print("hello i am jokey.How are you?")
age = input("How old are you?")
age = int(age)
if 1 <= age <= 3:
    print("What stays in the corner but can travel the world?")
    for i in range(10):
        print(".")
        sleep(1)
    print("A stamp")

elif 4 <= age <= 6:
    print("What begins with T has Tea in the middle and ends with T?")
    for i in range(10):
        print(".")
        sleep(1)
    print("Teapot")

elif 7 <= age <= 9:
    print("There are four doors first has a serial killer, \
        \nsecond poisonous gas, \
        \nthird a drop to an endless void, \
        \nfourth crocodiles in the ocean \
        \nwhich one is the safest? ")
    for i in range(10):
        print(".")
        sleep(1)
    print("Crocodiles don't live in the ocean.")
