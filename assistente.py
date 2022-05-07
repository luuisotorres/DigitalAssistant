# Importando as biblioteca
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys

# Criando uma instância para reconhecer a fala
listener = sr.Recognizer()

# Criando instância que será usada como referência para a fala da assistente
engine = pyttsx3.init()

# Definindo a Língua Portuguesa como idioma das pesquisas na Wikipedia
wikipedia.set_lang("pt")

# Criando uma função que faça a assistente responder o usuário com voz
def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    

# Criando uma função que consiga reconhecer a fala e traduzi-la em comandos    
def user_commands():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', ' ')
                print(command)
    except:
        pass
    return command

# Criando função que informa comandos para serem executados pela assistente    
def run_alexa():
    command = user_commands()
    if 'toque' in command:
        song = command.replace('toque', ' ')
        print('Alexa: tocando ' + song + ' no Youtube')
        engine_talk('tocando' +song + ' no Youtube')
        pywhatkit.playonyt(song)
    elif 'que horas são' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Alexa: Agora são ' + time)
        engine_talk('Agora são' +time)
    elif 'pesquise' in command:
        search = command.replace('pesquise', ' ')
        info = wikipedia.summary(search, 2)
        print(info)
        engine_talk(info)
    elif 'qual é o seu nome' in command:
        print('Alexa: Pode me chamar de Alexa.')
        engine_talk('Pode me chamar de Alexa.')
    elif 'quem te criou' in command:
        print('Alexa: Eu fui criada por Luís Fernando.')
        engine_talk('Eu fui criada por Luís Fernando')
        
    elif 'fechar' in command:
        sys.exit()
    else:
        engine_talk("Eu não entendi. Pode repetir?")
        

while True: 
    run_alexa()