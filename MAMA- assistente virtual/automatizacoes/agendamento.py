import random
from datetime import datetime, timedelta
from time import sleep
from utilitarios.cores import*

def iniciar_consulta():
    return None

def marcar_consulta(acao, objeto, _):
    if acao in [ "agendar", "marcar" ] and objeto in["consulta", "exame", "medico"]:
        if random.random() < 0.2:  # 20% de chance de não haver disponibilidade
            sleep(3)
            print(YELLOW + "-------------------------------------------------------------")
            print("Desculpe, no momento não há disponibilidade para agendar uma consulta.")
            print("Por favor, tente novamente mais tarde.")
            print("MAMA enviará um lembrete assim que houver horários disponíveis.")
            print("-------------------------------------------------------------" + RESET)
        else:
         consultas = ["Consulta médica geral", "Consulta com especialista", "Exame de rotina", "Consulta de acompanhamento"]
         horarios = ["8:00", "9:00", "10:00", "14:00", "15:00", "16:00"]  # Horários de trabalho padrão
         data_atual = datetime.now()
         data_consulta = data_atual + timedelta(days=random.randint(1, 30))  # Consulta marcada dentro dos próximos 30 dias
         horario_consulta = random.choice(horarios)
         consulta_escolhida = random.choice(consultas)
         sleep(4)
         print(GREEN + "-------------------------------------------------------------")
         print(f"Consulta marcada com sucesso !!!")
         print("-------------------------------------------------------------")
         print(f"data:{data_consulta.strftime('%d/%m/%Y')}")
         print(f"horário:{horario_consulta}")
         print(f"tipo de exame:{consulta_escolhida}")
         print("O lembrete foi adicionado. MAMA enviará um aviso próximo à data da consulta.")
         print("-------------------------------------------------------------" + RESET)
        