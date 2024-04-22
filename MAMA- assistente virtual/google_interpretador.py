# imports
import speech_recognition as sr

# variaveis
language = "pt-BR"

# função para interpretar o audio
def interpretar_audio():
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as fonte_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_audio)
        print("fale alguma coisa para a MAMA...")
        fala = reconhecedor.listen(fonte_audio, timeout=3)
        try:
            texto = reconhecedor.recognize_google(fala, language)
            print("você falou:", texto)

        except sr.UnknownValueError:
            print("a MAMA não conseguiu entender o que você disse :(")

if __name__ == "__main__":
    interpretar_audio()