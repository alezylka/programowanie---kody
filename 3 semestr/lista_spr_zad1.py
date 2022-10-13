
import pandas as pd
import numpy

kolumna_a = []
kolumna_b = []

for x in range(15):
    a = round((numpy.random.uniform(low=1, high=10)), None)
    kolumna_a.append(a)
    b = round((numpy.random.uniform(low=1, high=10)), None)
    kolumna_b.append(b)


kolumny = {'a': kolumna_a, 'b': kolumna_b}

df = pd.DataFrame(kolumny)
df.drop_duplicates(subset ="a",\
                     keep = False, inplace = True)

df["a+b"] = df['a'] + df['b'] 
df["a*b"] = df['a'] * df['b'] 

print(df)
# & (df["a*b"]>30)
zad_3 = df[(df["a+b"]<15)]
zad_3_2 = zad_3[(zad_3['a*b']>30)]
if zad_3_2.empty:
    print("Dataframe jest pusty.")
else:
    print(zad_3_2)