import speech_recognition as sr
import robot
robot.init()
while True:
    r = sr.Recognizer()
    print 'say something'
    with sr.Microphone(device_index = 2, sample_rate = 48000) as source:
        audio = r.record(source, duration = 2)
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    try:
        a = r.recognize_google(audio)
        print a
        if a == 'forward':
            robot.fwd()
        if a =='stop':
            robot.stp()
        print("You said: " + r.recognize_google(audio))
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
