import unittest
from assistente_mama import *
from google_interpretador import *
from testes.diretorio_audio import*
from utilitarios.cores import *

# testando o nome do assistente
class TesteNomeAssistente(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_reconhecer_nome(self):
        comando = processar_audio_do_comando(CHAMANDO_MAMA)
        comando = comando.split()
        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()
            print(f"nome chamado: {nome_assistente}")
        self.assertIn("mama", nome_assistente)

    def testar_nao_reconhecer_outro_nome(self):
        comando = processar_audio_do_comando(CHAMANDO_PATRICIA)
        comando = comando.split()
        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()
            print(f"nome chamado: {nome_assistente}")

        self.assertNotIn("mama", nome_assistente)

#testar agendamento
class TesteAgendamento(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_agendar_consulta(self):
        comando = processar_audio_do_comando(AGENDAR_CONSULTA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)

    def testar_agendar_exame(self):
        comando = processar_audio_do_comando(AGENDAR_EXAME)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)

    def testar_agendar_medico(self):
        comando = processar_audio_do_comando(AGENDAR_MEDICO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_marcar_consulta(self):
        comando = processar_audio_do_comando(MARCAR_CONSULTA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_marcar_medico(self):
        comando = processar_audio_do_comando(MARCAR_MEDICO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_marcar_exame(self):
        comando = processar_audio_do_comando(MARCAR_EXAME)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

#testar lembrete
class TesteLembrete(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_agendar_lembrete(self):
        comando = processar_audio_do_comando(AGENDAR_LEMBRETE)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)

        self.assertTrue(valido)

    def testar_agendar_remedio(self):
        comando = processar_audio_do_comando(AGENDAR_REMEDIO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_agendar_medicamento(self):
        comando = processar_audio_do_comando(AGENDAR_MEDICAMENTO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_marcar_lembrete(self):
        comando = processar_audio_do_comando(MARCAR_LEMBRETE)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_marcar_remedio(self):
        comando = processar_audio_do_comando(MARCAR_REMEDIO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_marcar_medicamento(self):
        comando = processar_audio_do_comando(MARCAR_MEDICAMENTO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_lembrar_lembrete(self):
        comando = processar_audio_do_comando(LEMBRAR_LEMBRETE)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_lembrar_remedio(self):
        comando = processar_audio_do_comando(LEMBRAR_REMEDIO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_lembrar_medicamento(self):
        comando = processar_audio_do_comando(LEMBRAR_MEDICAMENTO)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

#testar lembrete
class TesteConversa(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_contar_conversa(self):
        comando = processar_audio_do_comando(CONTAR_CONVERSA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_contar_dica(self):
        comando = processar_audio_do_comando(CONTAR_DICA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_contar_historia(self):
        comando = processar_audio_do_comando(CONTAR_HISTORIA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_propor_conversa(self):
        comando = processar_audio_do_comando(PROPOR_CONVERSA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_propor_dica(self):
        comando = processar_audio_do_comando(PROPOR_DICA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_propor_historia(self):
        comando = processar_audio_do_comando(PROPOR_HISTORIA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

#testar emergencia
class TesteEmergencia(unittest.TestCase):

    def setUp(self):
        iniciar()

    def testar_chamar_emergencia(self):
        comando = processar_audio_do_comando(CHAMAR_EMERGENCIA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)

    def testar_solicitar_emergencia(self):
        comando = processar_audio_do_comando(SOLICITAR_EMERGENCIA)
        print(f"Testando comando: {comando}")
        acao, objeto = tokenizar_comando(comando)
        valido = validar_comando(acao, objeto)
        self.assertTrue(valido)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()
    print(YELLOW + "------------------------------------------------------")
    print("               !!! iniciando testes !!!")
    print("------------------------------------------------------" + RESET)
    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteAgendamento))
    testes.addTest(carregador.loadTestsFromTestCase(TesteLembrete))
    testes.addTest(carregador.loadTestsFromTestCase(TesteConversa))
    testes.addTest(carregador.loadTestsFromTestCase(TesteEmergencia))
    executor = unittest.TextTestRunner()
    executor.run(testes)

# Autor: Brendo Gomes Prates
# Projeto: Assistente virtual MAMA para cuidado de idosos