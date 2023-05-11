#Ukol A.1
import pandas

titanic = pandas.read_csv ("titanic.csv")
#print(titanic.head (10))

titanic_pivot = pandas.pivot_table (data= titanic, values="Survived", index= "Sex", columns= "Pclass", aggfunc= len, fill_value=0)
print (titanic_pivot)

#Ukol A.2

firstClass = titanic [titanic["Pclass"]==1]
print (firstClass.head())
print (firstClass.dtypes)

firstClass ["Age_Groups"]= pandas.cut (firstClass["Age"], [0,12,19,65, float("inf")], labels= ["kids","teen", "adult", "senior"])
print (firstClass)


#Ukol B.1

import pandas

london_bicycles = pandas.read_csv ("london_merged.csv")
print (london_bicycles.head())

#print (london_bicycles.dtypes)

london_bicycles ["timestamp"]= pandas.to_datetime(london_bicycles["timestamp"])
london_bicycles["year"]= london_bicycles["timestamp"].dt.year
print (london_bicycles.dtypes)


london_pivot = pandas.pivot_table( data=london_bicycles, index="weather_code", columns= "year", values= "cnt", aggfunc= len, fill_value=0, margins=True)

#Ukol B.2
london_pivot = london_pivot.div (london_pivot.iloc[-1,:], axis=1)
print (london_pivot)







