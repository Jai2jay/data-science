import pandas as p
data = {'name':['alice','bob','cat','dog','kuttan','ger'],'score':[3,5,6,80,4,7]} 
d=p.DataFrame(data)
print(d)

print(d.head(2))
print(d.tail())

k=p.DataFrame(data)
d.info()
print(d.describe())
