import pandas as pd

#Dataframe es la informacion basica para armar el excel
print("Init")
data = {
    "pieazas:" : ["pata","tablero","puerta","estante","panel lateral"],
    "centimentros": [40,120,60,30,180]
}

df = pd.DataFrame(data)

#Guardamos el df en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)
