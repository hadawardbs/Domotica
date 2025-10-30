#!/bin/bash

#Instalando pip e pip3
apt install python-pip
apt install python3-pip

#instalando espeak do proprio sistema
apt install espeak

#instalando mbrola
apt install mbrola-br1

#Instalando espeak do python
apt install python3-espeak || pip install espeak
apt install python-espeak || pip3 install espeak

#Instalando speech
pip install SpeechRecognition
pip3 install SpeechRecognition

#Instalando pyaudio
apt install python-pyaudio || pip install pyaudio
apt install python3-pyaudio || pip3 install pyaudio

#Instalando pygame
apt install python-pygame || pip install pygame
apt install python3-pygame || pip3 install pygame

