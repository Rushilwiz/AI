file = open("rrNodeCity.txt", "r")
for word in file.readlines():
    print(word.strip().split(" ", 1))