# speech_robot
Speech Based Robot

For Speech Recognition Install as follows

Firstly install pyAudio
sudo apt-get install python-pyaudio

Now Install flac
sudo apt-get install flac

now install Speech Recognition Library
sudo pip install SpeechRecognition

Example is here

```
import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index = 2, sample_rate = 48000) as source:
        audio = r.record(source, duration = 3)
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    try:
        print("You said: " + r.recognize_google(audio))
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
