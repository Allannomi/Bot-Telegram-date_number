from data_random import data, aleatorio
from telegram.ext import Application, CommandHandler, MessageHandler ,ContextTypes, filters
from telegram import Update
from dotenv import load_dotenv
import os

"""
TOKEN TELEGRAM
"""
load_dotenv()
token = os.getenv("token")
if token is None:
    print("tivemos um erro na validação do token")
    exit()

async def command_date(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    date = data()
    """
    FAZER MANDAR UMA MENSAGEM DE TEXTO NO CHAT
    """
    await update.message.reply_text(date)

async def command_number(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    numero = aleatorio()
    await update.message.reply_text(str(numero))

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    """
    FAZENDO MENSAGEM DE COMEÇO, SEMPRE ANTES DE UM CARACTER USAR  \\
    """
    text_help = (
        "olá\\!, somos seu bot assistente\\.\n\n"
        "aqui estão os comando disponiveis:\n"
        "/date \\- mostra a data e hora atual\\.\n"
        "/number \\- mostra um numero aleatorio entre 1 e 100\\."
    )
    await update.message.reply_text(text_help, parse_mode="MarkdownV2")

async def desconhecido(update:Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    """
    {update.message.text}, ACESSA A MENSAGEM DE ETXTO
    """
    await update.message.reply_text(f"comando '{update.message.text}' não é reconhecido, tente /start e veja os comandos disponiveis")


def main():
    print("criando aplicação[+]...")
    """
    COMEÇANDO A APLICAÇÃO, CONTRUINDO COM BASE NO TOKEN
    """
    application = Application.builder().token(token).build()
    print("seu bot esta funcionando[+]")

    """
    FAZENDO MULTIPLOS COMANDOS
    """
    date_command = CommandHandler("date", command_date)
    application.add_handler(date_command)
    number_command = CommandHandler("number", command_number)
    application.add_handler(number_command)
    start_command = CommandHandler("start", start)
    application.add_handler(start_command)

    """
    SE FOR UM COMANDO QUALQUER, E NAO FOR NENHUM DOS ACIMA, ELE EXECUTA A FUNÇÃO DESCONHECIDO  
    """
    application.add_handler(MessageHandler(filters.COMMAND, desconhecido))

    """
    COMEÇAR A RODAR
    """
    application.run_polling()

if __name__ == "__main__":
    main()