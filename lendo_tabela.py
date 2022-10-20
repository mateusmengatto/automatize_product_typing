import pandas as pd


itens_saldo_negativo = pd.read_excel(r'C:\Users\Renan\OneDrive\Área de Trabalho\automatize\falantes_emp2_20-10-2022.xlsx')
empresa1_saldo = pd.read_excel(r'C:\Users\Renan\OneDrive\Área de Trabalho\automatize\estoq_emp_20-10-22.xlsx')




# faltantes = []
# for i in range(len(tabela)):
#     consulta_saldo = empresa1_saldo.loc[empresa1_saldo['codigo_de_barras'] == 
#                                         tabela['codigo_de_barras'][i]]
#     saldo_necess_emp2 = int((tabela['estoque_disponivel'][i].split(','))[0])*(-1)
#     saldo_emp_1 = int((consulta_saldo['estoque_disponivel'].iat[0].split(','))[0])
  
#     if saldo_necess_emp2 <= saldo_emp_1:
#         print(tabela['codigo_fabricante'][i], saldo_necess_emp2, "---comporta---", consulta_saldo['codigo_fabricante'].iat[0], saldo_emp_1)
#     else:
#         faltantes.append(tabela['codigo_fabricante'][i])

# print('Os seguintes itens faltam no estoque da empresa 1:')        
# for i in faltantes:
#     print(i)
    