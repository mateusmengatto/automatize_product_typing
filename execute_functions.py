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
  
    if saldo_necess_emp2 <= saldo_emp_1:
        pyautogui.write(str(tabela['codigo_de_barras'][i]))
        pyautogui.press('enter')  
        pyautogui.sleep(0.5)
        pyautogui.write(str((tabela['estoque_disponivel'][i]))[1:])
        pyautogui.sleep(0.3)
        pyautogui.press('enter')
        pyautogui.press('enter')        
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.sleep(0.2)
    else:
        faltantes = faltantes + f"{tabela['codigo_fabricante'][i]} ; {tabela['estoque_disponivel'][i]} \n"

print('Os seguintes itens faltam no estoque da empresa 1:')
print(' ')    
print('**********')
print( 'Item  -------------- Quantidade')
print(faltantes)    
print('**********')
 #GERAR LISTA COM QUANTIDADES
    



####abrir ssplus###
# pyautogui.click(x=1478, y=886, clicks=1, button='left')
# pyautogui.press('winleft')
# pyautogui.write('ssplus')
# pyautogui.press('enter')
# #print(pyautogui.KEYBOARD_KEYS)1,000



""" 
#Backup
pyautogui.sleep(3)
faltantes = ''
for i in range(len(tabela)):
    consulta_saldo = empresa1_saldo.loc[(empresa1_saldo['codigo_de_barras']) == 
                                        (tabela['codigo_de_barras'][i])]
    saldo_necess_emp2 = int((tabela['estoque_disponivel'][i].split(','))[0])*(-1)
    saldo_emp_1 = int((consulta_saldo['estoque_disponivel'].iat[0].split(','))[0])
  
    if saldo_necess_emp2 <= saldo_emp_1:
        pyautogui.sleep()
        pyautogui.write(str(tabela['codigo_de_barras'][i]))
        pyautogui.sleep(0.5)
        pyautogui.press('enter')  
        pyautogui.sleep(1.5)
        pyautogui.write(str((tabela['estoque_disponivel'][i]))[1:])
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(0.5)
        pyautogui.press('enter')        
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.sleep(2)
    else:
        faltantes = faltantes + f"{tabela['codigo_fabricante'][i]} --- {tabela['estoque_disponivel'][i]} \n"

print('Os seguintes itens faltam no estoque da empresa 1:')
print(faltantes)   """