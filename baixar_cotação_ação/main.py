from IPython.display import display
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, datetime

lista_acoes = ['AAPL']

while True:
    acao_i = input('Digite o Ticker da Ação que você quer: ').upper()
    if acao_i in lista_acoes:
        print('Vamos pegar as cotações dessa ação agora.')
        break
    else:
        print('Você digitou uma ação que não está na lista, por favor, digite de novo.')

# Conseguindo as datas de 1, 3, 5 e 10 anos em forma de string.
atual_d = date.today().day
atual_m = date.today().month
atual_a = date.today().year
data_10 = f'{atual_a - 10}-{atual_m}-{atual_d}'
data_5 = f'{atual_a - 5}-{atual_m}-{atual_d}'
data_3 = f'{atual_a - 3}-{atual_m}-{atual_d}'
data_1 = f'{atual_a - 1}-{atual_m}-{atual_d}'

# Dando escolha para o usuário pegar o range de datas que quiser.
while True:
    print('Você pode escolher pegar cotações de: 1, 3, 5, e 10 anos. Se quiser um tempo personalisado, digite 200.')
    tempo = int(input('Digite o número de anos que você quer:'))
    if tempo == 1:
        print('Aqui estão as todas as cotações diárias em 1 ano.')
        acao_i_hist = yf.download(acao_i, data_1, date.today())
        display(acao_i_hist)
        break
    elif tempo == 3:
        print('Aqui estão as todas as cotações diárias em 3 anos.')
        acao_i_hist = yf.download(acao_i, data_3, date.today())
        display(acao_i_hist)
        break
    elif tempo == 5:
        print('Aqui estão as todas as cotações diárias em 5 anos.')
        acao_i_hist = yf.download(acao_i, data_5, date.today())
        display(acao_i_hist)
        break
    elif tempo == 10:
        print('Aqui estão as todas as cotações diárias em 10 anos.')
        acao_i_hist = yf.download(acao_i, data_10, date.today())
        display(acao_i_hist)
        break
    elif tempo == 200:
        print('Digite em seguida o dia, mês e ano da data inicial para pegar a cotação:')
        ini_dia = int(input('Dia: '))
        ini_mes = int(input('Mês: '))
        ini_ano = int(input('Ano: '))
        data_ini = f'{ini_ano}-{ini_mes}-{ini_dia}'
        print('Agora digite o dia, mês e ano da data final: ')
        fim_dia = int(input('Dia: ')) + 1 # Aparentemente, se eu colocar 16 no dia, ele vai mostrar o até o dia 15, por isso estou colocando +1, gambiarra.
        fim_mes = int(input('Mês: '))
        fim_ano = int(input('Ano: '))
        data_fim = f'{fim_ano}-{fim_mes}-{fim_dia}'
        acao_i_hist_perso = yf.download(acao_i, data_ini, data_fim)
        print('Aqui estão as todas as cotações diárias do tempo selecionado.')
        display(acao_i_hist_perso)
        break
    else:
        print('Você digitou um tempo que não está na lista, por favor digite novamente.')
