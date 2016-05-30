token = '150389785:AAHEsIWkHQhBwvUOpismRvMQCDWkpTSeCCI'
import telebot

greeting = "Bonjour, mon ami. "
help_message = '''
HOT NEWS - first task is already here. use /task to get it
my Boss mr.Feldman is waiting for You here today(30-th of May) at 20:00. He will try to answer your questions about this course. An will declare program for first module
about me: I am bot and my mission is to serve people, help you to grow in python.
'''
task='''
this task it the same for each course participants
See example of code by link https://repl.it/CW9p
Your task is to modify this code, to show information about you. what is your name
do you have an ambitious dream, how many time you spent with python
After you modify this code - save your version by pressing button save
keep url to your version. later I will ask this link as your first task
if any question-please use this chat
best regards, Serg Feldman
'''
eating_time=False

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message.text)

    if "/help" in message.text:
        bot.send_message( message.chat.id,greeting + help_message)
    elif "/task" in message.text:
        bot.send_message( message.chat.id,greeting + task)
    elif "/bon_appetit" in message.text:
        if eating_time:
            bot.send_message(message.chat.id, "Merci, mon ami")
        else:
            bot.send_message(message.chat.id, "Pardon, mon ami. I am not hungry now")
    elif message.text == "/beer":
        pass
    else:
        bot.send_message(message.chat.id, "Pardon, mon ami. I don't understand You")


if __name__ == '__main__':
    bot.polling(none_stop=True)
