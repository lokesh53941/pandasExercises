import pandas
df2=pandas.read_csv("C:\Lokesh\Repositories\pandas\pandasExercises\supermarkets.csv")
print(df2)
print(".......................................................................")
#setting index ID
df3=df2.set_index("ID")
print(df3)
print("........................................................................")
#replacing index
df4=df2.set_index("Name",drop=False)
print(df4)
print(".........................................................................")
#deleting columns
df5= df2.drop(df2.columns[0:3],1)
print(df5)
print("..........................................................................")
#deleting rows
df6=df2.drop(df2.index[0:3],0)
print(df6)
print("...........................................................")
#adding new columns
df2["continent"]=df2.shape[0]*["north america"]
print(df2)
print(".............................................................")
#reversong column to row
df2_t=df2.T
print(df2_t)
print("..................................................................")
#to convert columns to rows
df2_t[6]=[7,"my address","my city","my state","my country","my shop",34,"my continent"]
print(df2_t)
print("..............................................................")
df2=df2_t.T
print(df2)
print("..................................................................")
#to modefy the table
df2_t[0]=[7,"my address","my city","my state","my country","my shop",34,"my continent"]
print(df2_t)
print("..............................................................")
df2=df2_t.T
print(df2)

