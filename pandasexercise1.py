import pandas

df1=pandas.DataFrame([[10,20,30],[30,40,50]],columns=["sasi","raki","loki"])

print(df1)

print(".............................")

df1=pandas.DataFrame([[10,20,30],[30,40,50]],columns=["sasi","raki","loki"],index=["first","second"])

print(df1)

print(".............................")

df2=pandas.DataFrame([{"name":"rakesh","surname":"g"},{"name":"lokesh","surname":"g"}])

print(df2)

print("..............................")

print(df1.mean())

print("..............................")

print(df1.mean().mean())

print("...............................")

print(df1.sasi)

print("...........................")

print(df1.sasi.mean())

print("..........................")