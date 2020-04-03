import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from dotenv import load_dotenv
load_dotenv()
import time

update_id = None

def main():
    global update_id
    bot = telegram.Bot(os.geten('TELEGRAM_API'))
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    while True:
        try:
            echo(bot)
        except NetworkError:
            time.sleep(1)
        except Unauthorized:
            update_id += 1


def echo(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if update.message: 
            if update.message.text in {'/acende@Papocobot','/acende'}:
                time.sleep(5)
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text='Não solte rojão, proteja os cãezinhos'
                )
                time.sleep(0.3) 
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text='Comemorações com fogos de artifi­cio são traumáticas para os animais, cuja audição é mais apurada que a humana.'
                )
                time.sleep(0.3)
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text='Muitos da fauna silvestre morrem ou sofrem alterações do seu ciclo reprodutor.'
                )
                time.sleep(0.3)
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text='Os cães latem em desespero e enforcam-se nas correntes.'
                )
                time.sleep(0.3)
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text='Eles e os gatos tem taquicardia, salivação, tremores, medo de morrer, escondem-se em locais minúsculos, fogem para nunca mais serem encontrados, provocam acidentes nas vias publicas e são vi­timas de atropelamento.'
                )

if __name__ == '__main__':
    main()