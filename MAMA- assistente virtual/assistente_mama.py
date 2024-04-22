# Autor: Brendo Gomes Prates
# Projeto: Assistente virtual MAMA para cuidado de idosos

# imports
import re
import unicodedata
import json
import speech_recognition as sr
from nltk import word_tokenize, corpus
from threading import Thread
from utilitarios.cores import *
from automatizacoes.lembrete import *
from automatizacoes.agendamento import *
from automatizacoes.emergencia import *
from automatizacoes.companhia_e_conversas import *

# Constantes 
IDIOMA_CORPUS = "portuguese"
IDIOMA_DE_FALA = "pt_BR"
CAMINHO_DE_CONFIGURACAO = "C:/Users/brend/OneDrive/Área de Trabalho/MAMA- assistente virtual/config.json"
ATUADORES = [
# atuadores
     {
        "nome": "consulta",
        "iniciar": iniciar_consulta,
        "parametro_de_atuacao": None,
        "atuar": marcar_consulta,
    }, 
    {
        "nome": "lembrete",
        "iniciar": iniciar_lembrete,
        "parametro_de_atuacao": None,
        "atuar": agendar_lembrete,
    },
     {
        "nome": "emergencia",
        "iniciar": iniciar_emergencia,
        "parametro_de_atuacao": None,
        "atuar": solicitar_emergencia,
    },
    {
        "nome": "conversas",
        "iniciar": iniciar_conversa,
        "parametro_de_atuacao": None,
        "atuar": propor_conversa,
    }
]

#funções
def iniciar():
    global reconhecedor
    global palavras_de_parada
    global nome_do_assistente
    global acoes

    reconhecedor = sr.Recognizer()
    palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))

    with open(CAMINHO_DE_CONFIGURACAO, "r") as arquivo_de_configuracao:
        configuracao = json.load(arquivo_de_configuracao)
        nome_do_assistente = configuracao["nome"]
        acoes = configuracao["acoes"]
        arquivo_de_configuracao.close()

    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["iniciar"]()
        atuador["parametro_de_atuacao"] = parametro_de_atuacao

def escutar_comando():
    global reconhecedor
    comando = None

    with sr.Microphone() as fonte_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_audio)

        print(BLUE + "Fale algo para a MAMA..." + RESET)
        fala = reconhecedor.listen(fonte_audio, timeout = 5, phrase_time_limit = 5)
        try:
            comando = reconhecedor.recognize_google(fala, language = IDIOMA_DE_FALA)
        except sr.UnknownValueError:
            pass

    return comando

def processar_audio_do_comando(audio_do_comando):
    global reconhecedor
    comando = None

    with sr.AudioFile(audio_do_comando) as fonte_audio:
        fala = reconhecedor.listen(fonte_audio)
        try:
            comando = reconhecedor.recognize_google(fala, language = IDIOMA_DE_FALA)
        except sr.UnknownValueError:
            pass

    return comando

def eliminar_palavras_de_parada(tokens):
    global palavras_de_parada

    tokens_filtrados = []
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)
                
    return tokens_filtrados

def tokenizar_comando(comando):
    global nome_do_assistente
    acao = None
    objeto = None
    tokens = word_tokenize(limpar_texto(comando), IDIOMA_CORPUS)
    
    if tokens:
        tokens = eliminar_palavras_de_parada(tokens)
        if len(tokens) >= 3:
            if nome_do_assistente == tokens[0].lower():
                acao = tokens[1].lower()
                objeto = tokens[2].lower()
           
    return acao, objeto

def validar_comando(ac, obj):
    global acoes
    valido = False
    if ac and obj:
        for acaoCadastrada in acoes:
            if ac == acaoCadastrada["nome"]:
                if obj in acaoCadastrada["objetos"]:

                    valido = True
                break
    
    return valido


def executar_comando(acao, objeto):
    print(BLUE + "Executando a ação:"+ RESET, acao,BLUE + " para " + RESET, objeto)
    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["parametro_de_atuacao"]

        processo_paralelo = Thread(target= atuador["atuar"], args=[acao, objeto, parametro_de_atuacao])
        processo_paralelo.start()

def limpar_texto(texto):
    # Remove caracteres especiais, exceto letras, espaços e acentos
    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-zA-Z\s]', '', texto_sem_acentos)


# main

if __name__ == "__main__":

    print(BOLD + "" + ROXO + "" + BG_WHITE +
          "Olá eu sou a MAMA a assistende virtual de auxílio de cuidados ao idoso em que posso ajudar :)" + RESET)
    iniciar()
    continuar = True
    while continuar:
        try:
            comando = escutar_comando()
            # print(f"processando o comando: {comando}")
            if comando:
                acao, objeto = tokenizar_comando(comando)
                valido = validar_comando(acao, objeto)
                if valido:
                    executar_comando(acao, objeto)
                else:
                    print(RED + "Não entendi o comando. Repita, por favor!" + RESET)
        except KeyboardInterrupt:
            print(RED + "Erro detectado tente reiniciar !!!" + RESET)
            continuar = False