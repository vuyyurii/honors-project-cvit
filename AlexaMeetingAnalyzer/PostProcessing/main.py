import os
import time
from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import argparse
import cv2
import speech_recognition as sr
import shutil 
import speech_to_text as st
import sqlite3


audio_path = '../audio1.flac'
images_dir = '../images/'


def meeting_analyzer(name, vu):

	if os.path.isdir('../meetings'):
		a = [name for name in os.listdir('../meetings/')]
	else:
		os.mkdir('../meetings')
		a = []
	rew = name
	rew = rew.replace(" ", "")
	cur = '../meetings/' + rew
	#m = -1
	#if len(a) == 0:
	#	cur = '../meetings/meeting-1'
	#	m = 0
	#else:
	#	for name in a:
	#		temp = name.split('-')
	#		n = int(temp[1])
	#		if(n > m):
	#			m = n
	#	cur = '../meetings/meeting-' + str(m+1)
	
	#name = 'meeting-' + str(m+1)
	if os.path.isdir(cur):
		temm = cur
		tem = name
		iii = 1
		while(os.path.isdir(temm) == True):
			temm = cur
			tem = name			
			temm = temm + '_' + str(iii)
			tem = tem + '_' + str(iii)
			iii = iii + 1
		name = tem
		cur = temm
	name = name
	os.mkdir(cur)
	f = open(cur + '/transcript.txt',"w+")
	#vu = time.ctime(os.path.getctime(audio_path))
	f.write(vu)
	f.write("\n")
	f.close()
	tim = vu
	sri = st.speech_to_text(audio_path, cur)
	if sri == '':
		sri = "No text detected"
	transcript = sri
	shutil.move(audio_path, cur + '/')	
	curr = cur + '/recognized_words'
	fkk = cur + '/images_boxes'
	os.mkdir(curr)
	os.mkdir(fkk)

	#temp = m + 1
	if os.path.isdir('../images'):
		b = [name for name in os.listdir('../images/')]
	else:
		b = []
	if len(b) == 0:
		print("No Screenshots were taken")
		wods = "{'NoImage':'No words'}"
	else:
		words = {}
		zz = 1
		for exp in b:
			currr = curr + '/' + str(zz) +'.txt'
			f = open(currr, "w+")
			vu = time.ctime(os.path.getctime("../images/" + exp))
			f.write(vu)
			f.write("\n")
			f.close()
			os.system('python text_recognition.py --east frozen_east_text_detection.pb --image ../images/' + exp + ' --padding 0.05 --path ' + currr + ' --imname ' + exp + ' --oupath ' + fkk)
			zz = zz + 1
			print('python text_recognition.py --east frozen_east_text_detection.pb --image ../images/' + exp + ' --padding 0.05 --path ' + currr + ' --imname ' + exp + ' --oupath ' + fkk)
			f = open(currr)
			words[exp] = [line.rstrip('\n') for line in f]
			f.close()
	
		wods = str(words)
		shutil.move(images_dir, cur + '/')
	a = (name, tim, sri, wods)
	conn = sqlite3.connect('../../second/db.sqlite3')
	print("Opened database successfully")
	conn.execute("INSERT INTO meetings_meeting (name,tim,transcript,words) \
      VALUES (?, ?, ?, ?)", a);	conn.commit()
	print("Records created successfully")
	conn.close()



#meeting_analyzer()
