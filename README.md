# Automatização de Entrada de Dados (Produtos) no Sistema SS Plus para confecção de notafiscal
Problemática, devido a divergencias entre estoque, e ou gereção de notafiscal em um sistema que não permitia a importação de dados, esta automação foi criada.
Este script automatiza o processo de entrada de dados em um sistema chamado "SS Plus" e lida com itens com saldo negativo.


#Como funciona.

1.Função de Digitação de Itens e Processamento: A parte principal do script começa aqui. Ele espera por 3 segundos antes de começar a execução.

2Loop Principal: Itera sobre a tabela de itens com saldo negativo (presumivelmente obtida de algum lugar, não fornecida no script) e executa algumas operações para cada item.

3.Consulta de Saldo: Para cada item na tabela, consulta o saldo do item em uma empresa chamada "empresa1" usando a função loc do pandas.

4.Cálculo da Quantidade Necessária: Calcula a quantidade necessária do item para cobrir o saldo negativo na empresa2. A quantidade é calculada com base na embalagem mínima.

5.Verificação de Condições: Verifica se a quantidade necessária está disponível na empresa1 e se o preço do item não é zero.

6.Entrada de Dados no Sistema SS Plus: Se as condições forem atendidas, o script simula a entrada de dados no sistema "SS Plus" usando o pyautogui. 
Ele escreve o código de barras do item, a quantidade necessária e pressiona as teclas 'enter' conforme necessário para realizar a entrada.

7.Registra Itens Faltantes: Se as condições não forem atendidas, o item é registrado como faltante em uma string de texto.

8.Escrita de Itens Faltantes em Arquivo: Após o loop, o script escreve a string de itens faltantes em um arquivo de texto chamado "faltantes.txt".

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- numpy
- pyautogui
- pandas

## Como Usar

1. Execute o script em um ambiente Python compatível.
2. Aguarde a execução completa do script.
3. Verifique o arquivo "faltantes.txt" para itens que não puderam ser processados.


## Licença

Este projeto está licenciado sob a Licença GNU General Public License. Consulte o arquivo LICENSE para obter mais detalhes.

#Autor

Contato Se você tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato através do email: mateusmengatto@gmail.com
