from numpy import str0
import pyautogui
import pandas as pd
from lendo_tabela import itens_saldo_negativo as tabela
from lendo_tabela import empresa1_saldo


#FUNÇÃO DIGITAÇÃO DE ITENS E PROCESSAMENTO DENTRO DO SISTEMA SS PLUS

pyautogui.sleep(3)
faltantes = 'Código Fabricante; Código de Barras; Estoque negativo; Substituto; \n'
for i in range(len(tabela)):
    consulta_saldo = empresa1_saldo.loc[(empresa1_saldo['codigo_de_barras']) == 
                                        (tabela['codigo_de_barras'][i])]
    saldo_necess_emp2 = int((tabela['estoque_disponivel'][i].split(','))[0])*(-1)
    emb_minima = int((tabela['gramatembalagvenda'][i].split(','))[0])
    if saldo_necess_emp2 % emb_minima == 0:
        qnt_nota = saldo_necess_emp2
    else:
        qnt_nota = ((abs(saldo_necess_emp2)//emb_minima)+1)*emb_minima    

    saldo_emp_1 = int((consulta_saldo['estoque_disponivel'].iat[0].split(','))[0])
    preco_zero = int((consulta_saldo['preco'].iat[0].split(','))[0])
  
    if qnt_nota <= saldo_emp_1 and preco_zero != 0:
        pyautogui.write(str(tabela['codigo_de_barras'][i]))
        pyautogui.press('enter')  
        pyautogui.sleep(0.8)
        pyautogui.write(str(qnt_nota))
        pyautogui.sleep(0.5)
        pyautogui.press('enter')
        pyautogui.press('enter')        
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.sleep(0.3)
        pyautogui.press('enter')

    else:
        faltantes = faltantes + f"{tabela['codigo_fabricante'][i]}; {tabela['codigo_de_barras'][i]} ; {tabela['estoque_disponivel'][i]};\n"
        #criar saida de tabela para facilitar 
        
#write string to file
text_file = open("faltantes.txt", "w")
text_file.write(faltantes)
text_file.close()        


    
