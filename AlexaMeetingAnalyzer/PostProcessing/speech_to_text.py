#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr 
import os, os.path

def speech_to_text(file, cur):

	AUDIO_FILE = file
	# use the audio file as the audio source 
	f = open(cur+'/transcript.txt',"a")
	
	r = sr.Recognizer()

	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)
	try:
		srii = r.recognize_google(audio)
		print("The audio file contains: " + srii) 
		f.write(srii)
		f.close()
		return srii
	except sr.UnknownValueError: 
		print("Google Speech Recognition could not understand audio")
		srii = "Google Speech Recognition could not understand audio"
		return srii
	except sr.RequestError as e: 
		print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
