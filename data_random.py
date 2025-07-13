import datetime
import random

def data():
    agora = datetime.datetime.now()
    data_agora = agora.strftime("%d/%m/%Y às %H:%M:%S")
    """
    SEMPRE TEM QUE SER RETURN
    O BOT DO TELEGRAM NÃO USA PRINT, TEM QUE RETORNAR A INFORMAÇÃO, NAO PRINTAR
    """
    return data_agora

def aleatorio():
    numero = random.randint(1,100)
    return numero
