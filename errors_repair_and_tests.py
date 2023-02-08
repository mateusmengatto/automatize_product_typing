import pyautogui
from lendo_tabela import itens_saldo_negativo as tabela
from lendo_tabela import empresa1_saldo


#FUNÇÃO DIGITAÇÃO
pyautogui.sleep(3)
faltantes = ''
for i in range(len(tabela)):
    consulta_saldo = empresa1_saldo.loc[(empresa1_saldo['codigo_de_barras']) == 
                                        (tabela['codigo_de_barras'][i])]
    saldo_necess_emp2 = int((tabela['estoque_disponivel'][i].split(','))[0])*(-1)
    saldo_emp_1 = int((consulta_saldo['estoque_disponivel'].iat[0].split(','))[0])
  
    if saldo_necess_emp2 <= saldo_emp_1:
        #print(tabela['codigo_de_barras'][i], tabela['codigo_de_barras'][i], (str((tabela['estoque_disponivel'][i]))[1:]))    
        pass
    else:
        print(tabela['codigo_de_barras'][i], tabela['codigo_fabricante'][i], (str((tabela['estoque_disponivel'][i]))[1:])," sem saldo")  
        

