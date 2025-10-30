import os
import pygame
from subprocess import getstatusoutput

def escreve(nome, cont):
    with open(nome, 'w') as f:
        f.write(cont)

if not os.path.isfile('/sys/class/gpio/gpio21/direction'):
    escreve('/sys/class/gpio/export', '21')

while True:
    status, output = getstatusoutput('cat /sys/class/gpio/gpio21/value')
    if int(output) == 1:
        print('Uma atividade suspeita foi detectada!')
        pygame.init()
        pygame.mixer.music.load('danger.mp3')
        pygame.mixer.music.play()
