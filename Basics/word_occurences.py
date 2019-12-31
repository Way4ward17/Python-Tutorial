s = "I am a python developer and i am alaso a Nigerian"

tokens = s.split(" ")
d = {}
for token in tokens:
    if token in d:
        d[token] += 1
    else:
        d[token] = 1

print(d)