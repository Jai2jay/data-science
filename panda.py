import pandas as p
data = {'name':['alice','bob','cat','dog','kuttan','ger'],'score':[3,5,6,80,4,None],} 
d=p.DataFrame(data,index=['a','b','c','d','e','f'])
print(d)

print(d.head(2))
print(d.tail())

k=p.DataFrame(data)
d.info()
print(d.describe())

print(d.columns)
print(d.shape)
(5,3)


print(d.loc['a'])
print(d.loc['b','name'])

print(d.iloc[0])

print(d.iloc[2,1])


print(d.isnull())
print(d.dropna())

print(d.fillna(0))

d['Age'].fillna(df['Age'].mean(),inplace=True)


