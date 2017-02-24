import re

s= "My name is David Mwangi Mathenge. I am a computer scientist, not yet an accomplished one but the sky is the limit"

print(re.search("name", s))

print(re.search("name", s).start())

print(re.search("name", s).end())

start = re.search("name", s).start()

end = re.search("name", s).end()

print(s[start:end])