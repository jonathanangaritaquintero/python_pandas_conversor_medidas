import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


# leer archivo exccel

df = pd.read_excel("muebles_medidas.xlsx")

# anadir una columna al dataframe con el calculo de cms a pulgadas

df["pulgadas"] = df["centimentros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

print("conversion completada y guardada")
