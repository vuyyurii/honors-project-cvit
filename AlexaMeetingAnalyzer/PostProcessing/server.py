#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import pyaudio
import wave
import cv2
import json
import time
import threading 
import _thread
import os
import main





class S(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.count_video = 1
        self.count_audio = 1
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers()
        print("Received data:"+ post_data.decode('utf-8'))
        # process(self,post_data,self.count_video,self.count_audio)
        post_data= json.loads(post_data)
        message = {}
        if(post_data['audio']=='START'):
            if((post_data['time'])!='?'):
                # t1 = threading.Thread(target=audio_process, args=(self, self.count_audio))
                _thread.start_new_thread(self.audio_process, (post_data['name'],int(post_data['time'])))
            elif((post_data['time'])=='?'):
                message={'audio':0,'video':-1}           
            
            
        if(post_data['video']=='TAKE'):
            self.video_process()
            
        self.wfile.write(bytes(json.dumps(message), 'utf-8'))
        self.send_response(200)

    def audio_process(self, name, tim):
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = tim
        WAVE_OUTPUT_FILENAME = "../audio" + str(self.count_audio) + '.flac'
        ff = open(WAVE_OUTPUT_FILENAME,"w+")
        ff.close()
        vu = time.ctime(os.path.getctime(WAVE_OUTPUT_FILENAME))
        audio = pyaudio.PyAudio()

        # start Recording
        self.audio = False
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

        print("recording...")
        frames = []
        
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        self.audio = True
        print("finished recording")  
        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        main.meeting_analyzer(name, vu)
        #os.mkdir('../images')

    def video_process(self):
        cap = cv2.VideoCapture(1)
        print(self.count_video)
        ret,frame = cap.read()
        mmm = -1
        if os.path.isdir('../images'):
            a = [name for name in os.listdir('../images/')]
            for name in a:
                ttt = name.split('-')
                n = int(ttt[1].split('.')[0])
                if n > mmm:
                    mmm = n
            print("==")
            print(mmm+1)
            cv2.imwrite("../images/capture-%d.jpg" %(mmm+1) , frame)
            self.count_video += 1
        else:
            print("no images dir")
            os.mkdir('../images')
            cv2.imwrite("../images/capture-1.jpg", frame)
            self.count_video += 1
        #cv2.waitKey(0) 
        cap.release()

def run(server_class=HTTPServer, handler_class=S, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print( "Starting httpd...")
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
