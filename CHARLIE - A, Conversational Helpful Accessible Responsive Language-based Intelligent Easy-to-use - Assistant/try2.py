import random
f = open("jokes.txt",'r',encoding="utf8")

data = f.readlines()
print(data)
joke = random.choice(data)
print(joke)

f.close()