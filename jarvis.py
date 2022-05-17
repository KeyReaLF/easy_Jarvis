import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3 as p
import random

author = "Jarvis"
text = "Приветствую вас Сэр! Чем могу быть полезен? Если вы используете Jarvis в первый раз, то советую громко и чётко сказать в микрофон - командный лист."
    
print("Jarvis: "+ text)  # Первое сообщение      

def command():  # Микрофон
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('Распознаю голос Сэр')  # Ожидание команды
        rec.pause_threshold = 1   # Задержка 
        rec.adjust_for_ambient_noise(source, duration=1)  # Удаление фонового шума
        audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio, language="ru-RU").lower()  # Распознание текста
        print('Вы:  ' + text[0].upper() + text[1:])  # Вывод сказанного текста на экран
    except sr.UnknownValueError:  # Если не распознался тест из аудио
        text = 'Не понимаю. Повторите.' # Начинает заново слушать
        print('Jarvis: ' + text)
        text = command()
    return text

command_list = ['Приветствие - привет, здравствуй',   
                'Повторение фразы сказанной пользователем - произнеси, скажи, повтори (текст)',   
                'Вопрос о правильности выполнения кода - проверка работы, проверка на работоспособность',   
                'Вопрос к ассистенту, как я его зовут - твоё имя, как тебя зовут, имя',   
                'Просьба открыть YouTube - открой ютуб, открой youtube',   
                'Просьба открыть Вконтакте - открой вк, открой вконтакте, открой vk',   
                'Просьба сгенерировать случайное число от ... до ... - случайное число от ... до ...',   
                'Рассказать анекдот - анекдот',   
                'Вызов списка команд - командный лист',   
                'Завершение работы ассистента - завершение работы, завершить работу, отбой']

def makeSomething(text):  # Тут Команды
    if 'открой ютуб' in text or 'открой youtube' in text:
        print('Jarvis: Открываю Youtube')
        webbrowser.open('https://www.youtube.com/')
    elif 'привет' in text or 'здравствуй' in text:
        print('Jarvis: Приветсвую Сэр')
    elif 'произнеси' in text or 'скажи' in text or 'повтори' in text:  #Повторение фразы пользователя
        print('Jarvis: ' + text[10].upper() + text[11:])
    elif 'открой вк' in text or 'открой вконтакте' in text or 'открой vk' in text:
        print('Jarvis: Открываю Вконтакте')
        webbrowser.open('https://vk.com')
    elif 'проверка работы' in text or 'проверка на работоспособность' in text:
        print('Jarvis: Все системы и функции в порядке и хорошо функционируют Сэр.')
    elif 'твоё имя' in text or 'как тебя зовут' in text or 'имя' in text: #Спрашиваем имя Джарвиса
        print('Jarvis: Меня зовут Jarvis. Я первая версия Искуственного Интелекта, разрабатываемая Кириллом для решения простых задач.')
    elif 'случайное число' in text:
        ot=text.find('от')
        do=text.find('до')
        f_num=int(text[ot+3:do-1])
        l_num=int(text[do+3:])
        r=str(random.randint(f_num, l_num))
        print('Jarvis: ' + r)
    elif 'завершить работу' in text or 'отбой' in text or 'завершение работы' in text:
        print('Jarvis: Прощайте Сэр :(')
        sys.exit()
    elif 'анекдот' in text:
        print('Jarvis: Зачем нужно плохое ПО? Без него у многих программистов не будет работы.')
    elif 'секрет' in text or 'Секрет' in text:
        print('Jarvis: Мой создатель просит вас поставить зачёт и пустить в 3 этап аттестации с ништяками.')
    elif 'командный лист' in text:
        print('Jarvis: Вот список команд доступных в первой версии Jarvis:', command_list)
while True:
    makeSomething(command())