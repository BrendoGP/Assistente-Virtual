import random
from datetime import timedelta
from time import sleep
from utilitarios.cores import *

def iniciar_lembrete():
    return None

def agendar_lembrete(acao, objeto, _):
    if acao in ["agendar", "marcar", "lembrar"] and objeto in ["medicamento", "remedio", "lembrete"]:
        medicamentos = ["Paracetamol", "Ibuprofeno", "Dipirona", "Omeprazol", "Insulina"] # Medicamentos da idosa
        horarios = ["8:00", "12:00", "16:00", "20:00"]  # Horários padrão para lembretes de medicamentos
        horario_lembrete = random.choice(horarios)
        medicamento_escolhido = random.choice(medicamentos)
        
        sleep(4)
        print(GREEN + "-------------------------------------------------------------")
        print("Lembrete de medicamento adicionado com sucesso !!!")
        print("-------------------------------------------------------------")
        print(f"Horário: {horario_lembrete}")
        print(f"Medicamento: {medicamento_escolhido}")
        print("-------------------------------------------------------------"+ RESET)

        if random.random() < 0.8:  # 80% de chance de um lembrete específico
            sleep(random.randint(6,16))
            print(YELLOW + "-------------------------------------------------------------")
            print("!!!!!!!!!!!!!!!!!!!! Lembrete !!!!!!!!!!!!!!!!!!!!")
            print(f"Agora são:{horario_lembrete}. É hora de tomar seu medicamento:"+ BOLD +
                   "" + BG_WHITE + f"{medicamento_escolhido}" + RESET)
            print(YELLOW + "-------------------------------------------------------------" + RESET)
