# import required module
import simpleaudio as sa
import keyboard
import librosa
import soundfile as sf
import threading
import time

key_name = input("Name of sound file (with the extension) :")

if "mp3" in key_name:
    x,_ = librosa.load(key_name, sr=16000)
    key_name = key_name[0:-3]+"wav"
    sf.write(key_name, x, 16000)


def play_key_sound():
    # define an object to play
    wave_object = sa.WaveObject.from_wave_file(key_name)
    print('playing sound using simpleaudio')
    
    # define an object to control the play
    play_object = wave_object.play()
    play_object.wait_done()


last = ""
while True:
    first = keyboard.read_key()
    if first and first != last:
        threading.Thread(target=play_key_sound,args=()).start()
        last = keyboard.read_key()
        time.sleep(0.01)
