import random
from time import sleep
from utilitarios.cores import*
from time import sleep

def iniciar_conversa():
    return None

def propor_conversa(acao, objeto, _):
    if acao in ["propor", "contar"]:
        if objeto == "historia":
            sleep(3)
            historias = [
                       "Uma vez, uma coruja sábia ajudou uma tartaruga a atravessar a estrada.",
                       "Um dia ensolarado, um grupo de crianças brincou com balões coloridos no parque.",
                       "Numa noite estrelada, uma família de esquilos construiu uma casa em uma árvore.",
                       "Certa vez, um coelhinho descobriu um jardim secreto cheio de flores coloridas.",
                      "Numa manhã fresca, um passarinho ensinou seus filhotes a voar pela primeira vez."]
            historia_escolhida = random.choice(historias)
            print(GREEN + "-------------------------------------------------------------")
            print("História do Dia:")
            print(CYAN + historia_escolhida)
            print(GREEN + "Espero que tenha gostado da história :)")
            print("-------------------------------------------------------------" + RESET)


        elif objeto == "dica":
            dicas = [
            "Lembre-se de beber bastante água ao longo do dia para se manter hidratada.",
            "Faça caminhadas curtas diariamente para manter a saúde e o bem-estar.",
            "Uma boa noite de sono é essencial para recarregar as energias. Tente dormir bem todas as noites.",
            "Mantenha uma alimentação equilibrada, rica em frutas, vegetais e fibras."]
            dica_escolhida = random.choice(dicas)
            print(GREEN + "-------------------------------------------------------------")
            print("Dica do Dia:")
            print(CYAN + dica_escolhida)
            print(GREEN + "Espero que essa dica seja útil para você :)")
            print("-------------------------------------------------------------")

        elif objeto == "conversa":
            conversas = [
            "Conte-me sobre alguma memória especial que você tenha da sua infância.",
            "Você tem alguma história engraçada para compartilhar comigo?",
            "Gostaria de falar sobre algum hobby ou passatempo que você goste?",
            "Como foi seu dia hoje? Gostaria de compartilhar alguma experiência?"]
            conversa_escolhida = random.choice(conversas)
            print(GREEN + "-------------------------------------------------------------")
            print("A MAMA adora conversar com você :)")
            print(CYAN + conversa_escolhida)
            print(GREEN + "Espero que essa conversa seja agradável para você, como foi para mim :)")
            print("-------------------------------------------------------------")

             