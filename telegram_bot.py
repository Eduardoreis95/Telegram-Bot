import telebot

CHAVE_API = "1958267141:AAE7r-----------------"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Ok. Para abrirmos o seu protocolo, infome os seguintes dados:
    Nome completo:
    Telefone:
    E-mail:
    Cidade:
    Motivo da abertura de protocolo:
    """
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.reply_to(mensagem, "Certo. Informe por gentielza o número de seu protocolo.")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    Para que possamos realizar o cancelamento do seu protocolo, informe:
    Numero do protocolo:
    Data de abertura:
    Motivo de cancelamento:
    """
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    bot.reply_to(mensagem, "Valeu! Dudu mandou outro abraço de volta!")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item)
    
    /opcao1 Abertura de protocolo
    /opcao2 Consulta protocolo
    /opcao3 Cancelamento de protocolo
    /opcao4 Mandar um abraço para o Dudu

Responder qualquer outra coisa não irá funcionar, clique em uma das opções. 
    """
    bot.reply_to(mensagem, texto)

bot.polling()