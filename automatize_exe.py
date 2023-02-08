from numpy import str0
import pyautogui
import pandas as pd
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
    preco_zero = int((consulta_saldo['preco'].iat[0].split(','))[0])
  
    if saldo_necess_emp2 <= saldo_emp_1 and preco_zero != 0:
        pyautogui.write(str(tabela['codigo_de_barras'][i]))
        pyautogui.press('enter')  
        pyautogui.sleep(0.8)
        pyautogui.write(str((tabela['estoque_disponivel'][i]))[1:])
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.press('enter')        
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.sleep(0.3)
        pyautogui.press('enter')

    else:
        faltantes = faltantes + f"{tabela['codigo_fabricante'][i]} ; {tabela['estoque_disponivel'][i]} \n"
        #criar saida de tabela para facilitar 
        
print('Os seguintes itens faltam no estoque da empresa 1:')
print(' ')    
print('**********')
print( 'Item  -------------- Quantidade')
print(faltantes)    
print('**********')
 #GERAR LISTA COM QUANTIDADES
    