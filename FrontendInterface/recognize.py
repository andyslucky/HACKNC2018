import speech_recognition as recognition

print(recognition.__version__)

recognizer = recognition.Recognizer();

harvard = recognition.AudioFile("harvard.wav");

with harvard as source:

    audio1 = recognizer.record(source, duration=4)
    audio2 = recognizer.record(source, duration=4)

    recognizer.recognize_sphinx(audio1)

    recognizer.recognize_sphinx(audio2)





