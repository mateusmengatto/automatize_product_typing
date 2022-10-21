import pandas as pd 

df = pd.read_excel(r'C:\Users\Renan\OneDrive\Área de Trabalho\automatize\VERIFICANDO_COD_BARRA.xlsx', header=0,
                            converters={'codigo_fabricante':str, 'codigo_de_barras':str, 'codigo_de_pesquisa_1':str, 'codigo_de_pesquisa_2':str, 'codigo_de_pesquisa_3':str, 'codigo_de_pesquisa_4':str, 'codigo_de_pesquisa_5':str, 'codigo_de_pesquisa_6':str})

double = []

for i in range(len(df)):
    if df['codigo_de_barras'][i] == df['codigo_de_pesquisa_1'][i] or df['codigo_de_barras'][i] == df['codigo_de_pesquisa_2'][i] or df['codigo_de_barras'][i] == df['codigo_de_pesquisa_3'][i] or df['codigo_de_barras'][i] == df['codigo_de_pesquisa_4'][i] or df['codigo_de_barras'][i] == df['codigo_de_pesquisa_5'][i] or df['codigo_de_barras'][i] == df['codigo_de_pesquisa_6'][i]:
        double.append(df['codigo_fabricante'][i])
    else:
        pass

df_to_ex = pd.DataFrame(double)
df_to_ex.to_excel('codbarra_com_cod_pesq.xlsx', index = False)
