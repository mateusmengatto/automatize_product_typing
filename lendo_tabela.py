import pandas as pd


itens_saldo_negativo = pd.read_excel(r'arquivos_estoque\faltemp2.xlsx', header=0, converters={'codigo_fabricante':str, 'codigo_de_barras':str})
empresa1_saldo = pd.read_excel(r'arquivos_estoque\estoemp1.xlsx', header=0, converters={'codigo_fabricante':str, 'codigo_de_barras':str})





    