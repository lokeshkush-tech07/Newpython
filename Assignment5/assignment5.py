word = "codes"
line = 1
with open("sample.txt", "r") as f:
    while True:
        data =  f.readline()
        if word in data:
           print(f"{word}, founded in line {line}")
           break
        else:
           pass
        line +=1
    