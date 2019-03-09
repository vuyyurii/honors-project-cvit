pip install --upgrade imutils


To install tesseract :-
====================

For UBUNTU - 18.04 :-
==================
sudo apt install tesseract-ocr


For OLDER VERSION :-
=================
sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt install tesseract-ocr



Using PIP :-
=========
pip install pillow
pip install pytesseract
pip install imutils


To Run :-
======

python3 main.py


Directory Structure :-
===================

AlexaMeetingAnalyzer
|
|-----------------images (contains images taken during meeting)
|-----------------audio.flac (recording of the meeting)
|-----------------PostProcessing (contains code for speech conversion and text recognition)
|-----------------meetings(contains results of the postprocessing)