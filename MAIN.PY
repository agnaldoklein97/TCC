import speech_recognition as sr
import pyttsx3
from config import *
from random import choice

reproducao = pyttsx3.init()

def sai_som(reposta):
    reproducao.say(reposta)
    reproducao.runAndWait()

def assistente():
    print("Oi, qual  é o nome da sua empresa")
    sai_som("Oi, qual  é o nome da sua empresa")
    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()

        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    user_name = rec.recognize_google(audio, language="pt")
                    user_name = verifica_nome(user_name)
                    name_list()
                    apresentacao = "{}".format(verifica_nome_exist(user_name))
                    print(apresentacao)
                    sai_som(apresentacao)
        
                    brute_user_name = user_name
                    user_name = user_name.split(" ")
                    user_name = user_name[0]
                    break
                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)
            break


    print("="* len(apresentacao))
    print("Ouvindo...")

    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()

        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)

            while True:
                try:
                    audio = rec.listen(s)
                    entrada = rec.recognize_google(audio, language="pt")
                    print("{}: {}".format(user_name, entrada))

                    reposta = conversas[entrada]

                    print("Assistente: {}".format(reposta))
                    sai_som("{}".format(reposta))

                except sr.UnknownValueError:
                    sai_som(resposta_erro_aleatoria)


if __name__ == '__main__':
    intro()
    sai_som("Iniciando")
    assistente()
