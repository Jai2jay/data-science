a={"epic","warcraft","tangled"}
b={"tangled","frozen","DMC"}

aANDb= a.intersection(b)
aORb=a.union(b)
print(aANDb)
print(aORb)

aLONE=a.difference(b)
print(aLONE)

aSHOULD=b.difference(a)
print(aSHOULD)