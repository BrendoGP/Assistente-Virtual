# imports
import pyaudio, wave , os

#variáveis
format = pyaudio.paInt16
channels = 2
rate = 44100
chunk = 1024
record_seconds = 6

# função para gravar áudio
def gravar_audio(temp_dir = ".", seconds = record_seconds):
    audio = pyaudio.PyAudio()

    #iniciando gravação 
    print("Fale algo para que a MAMA possa ajudar...")
    stream = audio.open(f = format, c = channels, r = rate , input = True, frames_per_buffer = chunk)
    frames = []

    for _ in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        if data:
            frames.append(data)

    # parando secording
    stream.stop_stream()
    stream.close()
    stream.terminate()

    # salvando arquivo de audio temporariamente 
    arquivo_temporario = temp_dir + "/speech.wav"
    if os.path.isfile(arquivo_temporario):
        os.remove(arquivo_temporario)

    print(f"arquivo de áudio sendo gerado: {arquivo_temporario}")
    with wave.open(arquivo_temporario, "wb") as wave_file: 
        wave_file.setnchannels(channels)
        wave_file.setsampwidth(audio.get_sample_size(format))
        wave_file.setframerate(rate)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

    return os.path.isfile(arquivo_temporario), arquivo_temporario