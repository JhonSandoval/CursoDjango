#Importar Libreria

import pandas as pd

#Leer archivo 
df = pd.read_excel("C:\MOCA1105A1.xlsx")
#Limpia carectes vacio
df = df.dropna()
#convierte el archivo a txt
df.to_csv("Control_Acuerdo_A_06COBY_11052023.txt", sep='\t', index=False)

#combina todo en una funciona de salida

def convert_excel_to_txt(input_file, output_file):
    df = pd.read_excel(input_file)
    df = df.dropna()
    df.to_csv(output_file, sep='\t', index=False)

