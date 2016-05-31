import telebot
from jokes import give_a_joke
token = '150389785:AAHEsIWkHQhBwvUOpismRvMQCDWkpTSeCCI'

greeting = "Bonjour, mon ami. "
help_message = '''
task is already here. use /task to get it
about me: I am monsieur Edu Botez and my mission is to serve people, help you to grow in python.
'''
task = '''
the task it the same for each course participants
you need to register on https://www.codecademy.com, start here course "Python"
and make all exercises in "Unit 1: Python Syntax". there is a brief theory in unit tasks
but if it is not enough for you - see book “A Byte of Python” by  Swaroop Chitlur in original
or translated version.
if any question-please use phorum on codecademy.com or this chat
best regards, Serg Feldman
'''
program = '''
Course program. Unit 1
Short introduction in python
Python Syntax. Writing hello world program
Comments, how to care about program reader
Numbers – Integer and Float, how to calculate using python
Strings – how to process words
Console Output – how to interact with users
Conditionals & Control Flow – how programs make their decisions
Functions – how to write  reusable and testable pieces of programs

main manual for this unit - “A Byte of Python” by  Swaroop Chitlur https://www.gitbook.com/book/swaroopch/byte-of-python/
there is a russian translation http://wombat.org.ua/AByteOfPython/
'''

faq = '''
What will be discussed on offline meetings?
 we try to overcome your technical problems, reeview some advanced topics
Could you please send the detail  description of the course in Email? Where can I find out more about the course, schedule, tasks and so on? And what is the programm of our studing?
You can request EduBot for this info
I am  Ukraininan,  but now  live in Belgium, and have  only  online possibility to learn Python. Is it possible to do this with your course, without offline meetings?
Yes, it is possible
Reason of life?
42
Who will be teaching us?
You teach yourself, our instructors help and motivate you
How long this course is going to be held in the summer?
We expect that unit 1 will be 2 weeks
Will this course pay more attention in creating web-applications or the simple python learning is included to the course too?
We start course from very beginning
What is the main purpose of this course? What is your aim?
To make your brain work hard
where and when will be meetups?
Main activity takes place in online. We plan to organize off-line meetups as bonus
Could you tell me please how often offline meetings will be organized and can I see the program?
It depends on you
Is it mostly theoretical or practically oriented?
Practical
Why is this course free?
You are welcome to give us donations
What is company smartCRM?
We develop new-age CRM. It's all I can say now because of NDA
'''

eating_time = False
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message.text)
    # bot.send_message(message.chat.id, "Z-z-z-z. Pardon, mon ami. I am sleeping now")
    # if "/réveille-toi s'il te plait" in message.text:
    #     bot.send_message(message.chat.id, greeting + " I am glad to hear you. Have a good day")

    if "/help" in message.text or "/aider" in message.text:
        bot.send_message(message.chat.id, greeting + help_message)
    elif "/task" in message.text or "/la_tâche" in message.text:
        bot.send_message(message.chat.id, greeting + task)
    elif "/faq" in message.text:
        bot.send_message(message.chat.id, greeting + faq)
    elif "/program" in message.text:
        bot.send_message(message.chat.id, greeting + program)
    elif "/plaisanter" in message.text:
        bot.send_message(message.chat.id, give_a_joke())
    elif "/where_is_mr_feldman" in message.text:
        bot.send_message(message.chat.id, greeting + " mon patron monsieur Feldmant is very busy now")
    elif "/bon_appetit" in message.text:
        if eating_time:
            bot.send_message(message.chat.id, "Merci, mon ami")
        else:
            bot.send_message(message.chat.id, "Pardon, mon ami. I am not hungry now")
    else:
        if message.text[0] == "/":
            bot.send_message(message.chat.id, "Pardon, mon ami. I don't understand You")


if __name__ == '__main__':
    bot.polling(none_stop=True)


# task = '''
# la task it the same for each course participants
# See example of code by link https://repl.it/CW9p
# Your task is to modify this code, to show information about you. what is your name
# do you have an ambitious dream, how many time you spent with python
# After you modify this code - save your version by pressing button save
# keep url to your version. later I will ask this link as your first task
# if any question-please use this chat
# best regards, Serg Feldman
# '''