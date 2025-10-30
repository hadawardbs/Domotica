#========================================#
#	       BIBLIOTECAS		 #
#========================================#
import speech_recognition as sr
from datetime import datetime
from random import choice
from sys import exit
import subprocess
import webbrowser
import pygame
import os
from time import sleep

#========================================#
#		  FUNÇÕES		 #
#========================================#
def ler_arquivo(nomedoarquivo): #função para ler um arquivo
	arq = open(nomedoarquivo, 'r')
	txt_lido = arq.read()
	arq.close()
	return txt_lido

def escrever_arquivo(nomedoarquivo, conteudo): #função para escrever em um arquivo
	arq = open(nomedoarquivo, 'a')
	arq.write(conteudo)
	arq.close

def limpar(): #função para limpar a tela do terminal
	os.system('clear')

def sair(): #função para sair do programa
	sintese_voz('"Encerrando processos... Até logo!"')
	exit(0)

def captura_voz(): #função para capturar a voz/comando do usuário
	print('\nOuvindo...')
	#Habilita o microfone para ouvir o usuário
	r = sr.Recognizer()

	with sr.Microphone() as s:
		#Chama a função de redução de ruído disponível na speech_recognition
		r.adjust_for_ambient_noise(s)

		#Armazena a informação de audio na variável
		audio = r.listen(s)

		try:
			#Passa o áudio para o reconhecedor de padrões do speech_recognition
			fala = r.recognize_google(audio, language = 'pt-br') #speech
			print('\n>>> {}'.format(fala))
			return fala
		except:
			#caso não entenda o que foi dito
			fala = 'none'
			print('\n>>> {}'.format(fala))
			return fala

def irreconhecido(): #função para quando o speech_recognition não entender o que foi dito
	sintese_voz('"Não entendi, tente ir a um lugar com menos barulho e inteferência e repita por favor!"')

def sintese_voz(frase): #função para sintetizar a voz do assistente
	print('\nAssistente: {}'.format(frase))
	os.system('espeak -v mb-br1 -s 120 {}'.format(frase))

def reconhecimento(): #função para reconhecer quem é o usuário tentando usar o assistente
	while True:
		users = ler_arquivo('usuários.txt').split()
		login = captura_voz().strip().lower().capitalize().split()[0]
		if login in users:
			sintese_voz('"Acesso confirmado. Seja Bem Vindo {}"'.format(login))
			break
		elif login in ['sair', 'cancelar', 'sair do programa']:
			sair()
		elif login == 'None':
			irreconhecido()
		else:
			sintese_voz('"Acesso Negado! Tente novamente."')

def cumprimento(): #função que seleciona um cumprimento aleatório
	cumprimentos = ['Oi', 'Olá', 'Saudações', 'Como vai', 'Iae']
	cumprimento = choice(cumprimentos)
	return cumprimento

def manual_escrito(): #função para exibir manual(geral) escrito
	manual = ler_arquivo('manual_escrito.txt')
	limpar()
	print(manual)

def manual_voz(): #função para exibir manual(geral) por voz
	manual = ler_arquivo('manual_voz.txt')
	limpar()
	sintese_voz('"{}"'.format(manual))

def tempo(): #função que exibi a data e a hora atual do sistema
	data_hora = datetime.now()
	data_formatada = data_hora.strftime('%d/%m/%Y')
	hora_formatada = data_hora.strftime('%H:%M')
	#----------------------------
	ano = data_hora.year
	mes = data_hora.month
	dia = data_hora.day
	hora = data_hora.hour
	minuto = data_hora.minute
	#----------------------------
	meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
	#----------------------------
	limpar()
	print('=-=' * 20)
	print('''{:^60}'''.format('Data & Hora'))
	print('=-=' * 20)
	print('''\nData: {}
Hora: {}'''.format(data_formatada, hora_formatada))
	print('=-=' * 20)
	sintese_voz('"Hoje é dia {}, de {}, do ano de {}. E agora são {} horas e {} minutos."'.format(dia, meses[mes - 1], ano, hora, minuto))

def playlist(): #função que exibi a playlist de músicas
	sintese_voz('"Bem Vindo a PlayList de Músicas, sinta-se a vontade!"')
	playlist = ler_arquivo('playlist.txt')
	limpar()
	print(playlist)

def manual_casa_simples_escrito(): #função para exibir manual(casa_simples) escrito
	manual = ler_arquivo('manual_casa_simples_escrito.txt')
	limpar()
	print(manual)

def manual_casa_simples_voz(): #função para exibir manual(casa_simples) por voz
	manual = ler_arquivo('manual_casa_simples_voz.txt')
	limpar()
	sintese_voz('"{}"'.format(manual))

def manual_casa_completo_escrito(): #função para exibir manual(casa_completo) escrito
	manual = ler_arquivo('manual_casa_completo_escrito.txt')
	limpar()
	print(manual)

def manual_casa_completo_voz(): #função para exibir manual(casa_completo) por voz
	manual = ler_arquivo('manual_casa_completo_voz.txt')
	limpar()
	sintese_voz('"{}"'.format(manual))

def menu_casa(): #função que executa o menu_casa
	#pi = '10.2.201.3'
	sintese_voz('"Você está no menu casa. Deseja usar o modo de operação simples ou completo ?"')
	while True:
		modo_op = captura_voz().lower() #captura o modo de operação(simples ou completo)
		if modo_op in ['simples', 'modo simples', 'menu simples', 'modo de operação simples', 'operação simples']:
			menu_casa_simples()
			break
		elif modo_op in ['completo', 'completa', 'modo completo', 'menu completo', 'modo de operação completo', 'operação completa']:
			menu_casa_completo()
			break
		elif modo_op in ['relembrar', 'me relembre', 'onde estou']:
			sintese_voz('"Você está no menu casa. Escolha qual modo de operação deseja usar."')
		elif modo_op in 'sair cancelar voltar retornar':#sai do menu_casa
			sintese_voz('"Saindo do menu casa!"')
			break
		elif modo_op == 'none':
			irreconhecido()
		else:
			sintese_voz('"Este modo de operação não existe. Tente novamente."')

def menu_casa_simples(): #executa o modo de operação simples da casa
	sintese_voz('"Modo de operação simples confirmado! Escolha o objeto que deseja controlar."')
	while True:
		obj_op_simples = captura_voz().lower() #objetos que deseja controlar
		if obj_op_simples in ['manual', 'exibir manual', 'mostrar manual']: #objeto manual
			sintese_voz('"Deseja acesso ao manual escrito ou por voz ?"')
			while True:
				manual_casa_simples = captura_voz().lower()
				if manual_casa_simples in ['manual escrito', 'escrito']:
					manual_casa_simples_escrito()
					break
				elif manual_casa_simples in ['manual por voz', 'manual de voz', 'manual voz', 'voz', 'por voz']:
					manual_casa_simples_voz()
					break
				elif manual_casa_simples in 'sair cancelar retornar': #cancelar manual
					break
				elif manual_casa_simples == 'none':
					irreconhecido()
				else:
					sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
		elif obj_op_simples in ['iluminação', 'lâmpada', 'lâmpadas', 'luzes', 'controlar lâmpada', 'controlar lâmpadas']: #objeto lâmpada
			sintese_voz('"Você está controlando a iluminação da casa. Escolha um cômodo para controlar."')
			while True:
				comodo = captura_voz().lower() #cômodos que deseja controlar
				if comodo in ['quarto', 'controlar quarto', 'cômodo quarto']: #cômodo quarto
					sintese_voz('"Você está controlando as lâmpadas do quarto. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para se controlar uma lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio25/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_quarto_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio25/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_quarto_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio25/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada do quarto está acesa!"')
							else:
								sintese_voz('"A lâmpada do quarto está apagada!"')
						elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo quarto, controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do cômodo quarto
							sintese_voz('"Saindo do cômodo quarto!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif comodo in ['sala', 'controlar sala', 'cômodo sala']: #cômodo sala
					sintese_voz('"Você está controlando as lâmpadas da sala. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para se controlar uma lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio23/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_sala_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio23/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_sala_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio23/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada da sala está acesa!"')
							else:
								sintese_voz('"A lâmpada da sala está apagada!"')
						elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo quarto, controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do cômodo sala
							sintese_voz('"Saindo do cômodo sala!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif comodo in ['cozinha', 'controlar cozinha', 'cômodo cozinha']: #cômodo cozinha
					sintese_voz('"Você está controlando as lâmpadas da cozinha. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para se controlar uma lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio16/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_cozinha_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio16/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_cozinha_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio16/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada da cozinha está acesa!"')
							else:
								sintese_voz('"A lâmpada da cozinha está apagada!"')
						elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo quarto, controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do cômodo cozinha
							sintese_voz('"Saindo do cômodo cozinha!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif comodo in ['jardim', 'controlar jardim', 'cômodo jardim']: #cômodo jardim
					sintese_voz('"Você está controlando as lâmpadas do jardim. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para se controlar uma lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio24/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_jardim_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio24/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_jardim_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio24/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada do jardim está acesa!"')
							else:
								sintese_voz('"A lâmpada do jardim está apagada!"')
						elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo quarto, controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do cômodo jardim
							sintese_voz('"Saindo do cômodo jardim!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif comodo in ['garagem', 'controlar garagem', 'cômodo garagem']: #cômodo garagem
					sintese_voz('"Você está controlando as lâmpadas da garagem. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para se controlar uma lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio18/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_garagem_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio18/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_garagem_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio18/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada da garagem está acesa!"')
							else:
								sintese_voz('"A lâmpada do jardim está apagada!"')
						elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo quarto, controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do cômodo garagem
							sintese_voz('"Saindo do cômodo garagem!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif comodo in ['banheiro', 'controlar banheiro', 'cômodo banheiro']: #cômodo banheiro
					sintese_voz('"Você está controlando as lâmpadas do banheiro. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para se controlar uma lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio20/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_banheiro_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio20/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_banheiro_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio20/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada do banheiro está acesa!"')
							else:
								sintese_voz('"A lâmpada do jardim está apagada!"')
						elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo quarto, controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do cômodo banheiro
							sintese_voz('"Saindo do cômodo banheiro!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está controlando a iluminação da casa. Escolha o cômodo que deseja controlar."')
				elif comodo in 'sair voltar retornar': #sair do objeto iluminação
					sintese_voz('"Saindo do menu iluminação!"')
					break
				elif comodo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Este cômodo não foi reconhecido. Tente novamente."')
		elif obj_op_simples in ['clima', 'ventilação', 'ventilador', 'controlar ventilação', 'controlar ventilador']: #objeto ventilador
			sintese_voz('"Você está controlando a ventilação da casa! Somente o cômodo quarto possui um ventilador. O que deseja fazer ?"')
			while True:
				pi = '10.2.201.3'
				ventilação = captura_voz()
				if ventilação in ['ligar', 'ligar ventilador', 'ligar ventilação', 'ativar', 'ativar ventilador', 'ativar ventilação']:
					status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio12/value", shell = True)
					if int(status) == 0:
						sintese_voz('"O ventilador já está ligado!"')
					else:
						os.system('ssh pi@{} ventilador_quarto_on'.format(pi))
						sintese_voz('"Ventilador ligado!"')
				elif ventilação in ['desligar', 'desligar ventilador', 'desligar ventilação', 'desativar', 'desativar ventilador', 'desativar ventilação']:
					status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio12/value", shell = True)
					if int(status) == 1:
						sintese_voz('"O ventilador já está desligado!"')
					else:
						os.system('ssh pi@{} ventilador_quarto_off'.format(pi))
						sintese_voz('"Ventilador desligado!"')
				elif ventilação in ['status', 'exibir status', 'relatório', 'exibir relatório', 'situação', 'exibir situação']:
					status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio12/value", shell = True)
					if int(status) == 0:
						sintese_voz('"O ventilador do quarto está ligado!"')
					else:
						sintese_voz('"O ventilador do quarto está desligado!"')
				elif ventilação in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está controlando a ventilação do quarto. O que deseja fazer ?"')
				elif ventilação in 'sair voltar retornar': #Sair do objeto ventilação
					sintese_voz('"Saindo do menu ventilação!"')
					break
				elif ventilação == 'none':
					irreconhecido()
				else:
					sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
		elif obj_op_simples in ['tempo', 'hora', 'data', 'exibir data', 'exibir hora']: #objeto relógio
			tempo()
		elif obj_op_simples in ['relembrar', 'me relembre', 'onde estou']:
			sintese_voz('"Você está no menu casa, usando o modo de operação simples. Escolha o objeto que deseja controlar."')
		elif obj_op_simples in 'sair fechar voltar retornar': #sair do menu_casa
			sintese_voz('"Saindo do menu casa"')
			break
		elif obj_op_simples == 'none':
			irreconhecido()
		else:
			sintese_voz('"Este objeto não foi reconhecido. Tente novamente."')
					

def menu_casa_completo(): #executa o modo de operação completo da casa
	sintese_voz('"Modo de operação completo confirmado! Escolha o cômodo que deseja controlar."')
	while True:
		cmd_op_completo = captura_voz().lower() #cômodo que deseja controlar
		if cmd_op_completo in ['manual', 'exibir manual']:
			sintese_voz('"Deseja acesso ao manual escrito ou por voz ?"')
			while True:
				manual_casa_completo = captura_voz().lower()
				if manual_casa_completo in ['manual escrito', 'escrito']:
					manual_casa_completo_escrito()
					break
				elif manual_casa_completo in ['manual por voz', 'manual de voz', 'manual voz', 'voz', 'por voz']:
					manual_casa_completo_voz()
					break
				elif manual_casa_completo in 'sair cancelar retornar': #cancela manual
					break
				elif manual_casa_completo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Esta opção não foi reconhecida, tente novamente."')
		elif cmd_op_completo in ['quarto', 'controlar quarto', 'cômodo quarto']: #cômodo quarto
			sintese_voz('"Cômodo quarto selecionado. Escolha o objeto que deseja controlar."')
			while True:
				obj_op_completo = captura_voz().lower() #objeto que deseja controlar
				if obj_op_completo in ['iluminação', 'lâmpada', 'lâmpadas', 'controlar lâmpadas', 'controlar lâmpada', 'luzes']: #objeto lâmpada
					sintese_voz('"Você está controlando as lâmpadas do quarto. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para controlar lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio25/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_quarto_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio25/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_quarto_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio25/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada do quarto está acesa!"')
							else:
								sintese_voz('"A lâmpada do quarto está apagada!"')
						elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo quarto controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do objeto iluminação
							sintese_voz('"Saindo do menu iluminação!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_completo in ['clima', 'ventilação', 'ventilador', 'controlar ventilação', 'controlar ventilador']: #objeto ventilador
					sintese_voz('"Você está controlando a ventilação do quarto. O que deseja fazer ?"')
					while True:
						ventilação = captura_voz()
						if ventilação in ['ligar', 'ligar ventilador', 'ligar ventilação', 'ativar', 'ativar ventilador', 'ativar ventilação']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio12/value", shell = True)
							if int(status) == 0:
								sintese_voz('"O ventilador já está ligado!"')
							else:
								os.system('ssh pi@{} ventilador_quarto_on'.format(pi))
								sintese_voz('"Ventilador ligado!"')
						elif ventilação in ['desligar', 'desligar ventilador', 'desligar ventilação', 'desativar', 'desativar ventilador', 'desativar ventilação']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio12/value", shell = True)
							if int(status) == 1:
								sintese_voz('"O ventilador já está desligado!"')
							else:
								os.system('ssh pi@{} ventilador_quarto_off'.format(pi))
								sintese_voz('"Ventilador desligado!"')
						elif ventilação in ['status', 'exibir status', 'relatório', 'exibir relatório', 'situação', 'exibir situação']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio12/value", shell = True)
							if int(status) == 0:
								sintese_voz('"O ventilador do quarto está ligado!"')
							else:
								sintese_voz('"O ventilador do quarto está desligado!"')
						elif ventilação in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está controlando a ventilação do quarto. O que deseja fazer ?"')
						elif ventilação in 'sair voltar retornar': #Saindo do objeto ventilação
							sintese_voz('"Saindo do menu ventilação!"')
							break
						elif ventilação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_completo in ['tempo', 'data', 'hora', 'exibir data', 'exibir hora']: #objeto relógio
					tempo()
				elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está no cômodo quarto. Escolha o objeto que deseja controlar."')
				elif obj_op_completo in 'sair voltar retornar': #sair do cômodo quarto
					sintese_voz('"Saindo do cômodo quarto!"')
					break
				elif obj_op_completo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Este objeto não foi reconhecido. Tente novamente."')
		elif cmd_op_completo in ['sala', 'controlar sala', 'cômodo sala']: #cômodo sala
			sintese_voz('"Cômodo sala selecionado. Escolha o objeto que deseja controlar."')
			while True:
				obj_op_completo = captura_voz().lower() #objeto que deseja controlar
				if obj_op_completo in ['iluminação', 'lâmpada', 'lâmpadas', 'controlar lâmpada', 'controlar lâmpadas', 'luzes']: #objeto lâmpada
					sintese_voz('"Você está controlando as lâmpadas da sala. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para controlar lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio23/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_sala_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio23/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_sala_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio23/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada da sala está acesa!"')
							else:
								sintese_voz('"A lâmpada da sala está apagada!"')
						elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo sala controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do objeto iluminação
							sintese_voz('"Saindo do menu iluminação!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_completo in ['ventilador', 'clima', 'ventilação', 'controlar ventilação', 'controlar ventilador']: #objeto ventilador
					sintese_voz('"O cômodo sala não possui um ventilador!"')
				elif obj_op_completo in ['tempo', 'data', 'hora', 'exibir data', 'exibir hora']: #objeto relógio
					tempo()
				elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está no cômodo sala. Escolha o objeto que deseja controlar."')
				elif obj_op_completo in 'sair voltar retornar': #sair do cômodo sala
					sintese_voz('"Saindo do cômodo sala!"')
					break
				elif obj_op_completo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Este objeto não foi reconhecido. Tente novamente."')
		elif cmd_op_completo in ['cozinha', 'controlar cozinha', 'cômodo cozinha']: #cômodo cozinha
			sintese_voz('"Cômodo cozinha selecionado. Escolha o objeto que deseja controlar."')
			while True:
				obj_op_completo = captura_voz().lower() #objeto que deseja controlar
				if obj_op_completo in ['iluminação', 'lâmpada', 'lâmpadas', 'luzes', 'controlar lâmpadas', 'controlar lâmpada']: #objeto lâmpada
					sintese_voz('"Você está controlando as lâmpadas da cozinha. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para controlar lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio16/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_cozinha_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio16/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_cozinha_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio16/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada da cozinha está acesa!"')
							else:
								sintese_voz('"A lâmpada da cozinha está apagada!"')
						elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo cozinha controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do objeto iluminação
							sintese_voz('"Saindo do menu iluminação!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_completo in ['ventilador', 'clima', 'ventilação', 'controlar ventilação', 'controlar ventilador']: #objeto ventilador
					sintese_voz('"O cômodo cozinha não possui um ventilador!"')
				elif obj_op_completo in ['tempo', 'data', 'hora', 'exibir data', 'exibir hora']: #objeto relógio
					tempo()
				elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está no cômodo cozinha. Escolha o objeto que deseja controlar."')
				elif obj_op_completo in 'sair voltar retornar': #sair do cômodo cozinha
					sintese_voz('"Saindo do cômodo cozinha!"')
					break
				elif obj_op_completo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Este objeto não foi reconhecido. Tente novamente."')
		elif cmd_op_completo in ['jardim', 'controlar jardim', 'cômodo jardim']: #cômodo jardim
			sintese_voz('"Cômodo jardim selecionado. Escolha o objeto que deseja controlar."')
			while True:
				obj_op_completo = captura_voz().lower() #objeto que deseja controlar
				if obj_op_completo in ['iluminação', 'lâmpada', 'lâmpadas', 'luzes', 'controlar lâmpadas', 'controlar lâmpada']: #objeto lâmpada
					sintese_voz('"Você está controlando as lâmpadas do jardim. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para controlar lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio24/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_jardim_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio24/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_jardim_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio24/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada do jardim está acesa!"')
							else:
								sintese_voz('"A lâmpada do jardim está apagada!"')
						elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo jardim controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do objeto iluminação
							sintese_voz('"Saindo do menu iluminação!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_completo in ['ventilador', 'clima', 'ventilação', 'controlar ventilação', 'controlar ventilador']: #objeto ventilador
					sintese_voz('"O cômodo jardim não possui um ventilador!"')
				elif obj_op_completo in ['tempo', 'data', 'hora', 'exibir data', 'exibir hora']: #objeto relógio
					tempo()
				elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está no cômodo jardim. Escolha o objeto que deseja controlar."')
				elif obj_op_completo in 'sair voltar retornar': #sair do cômodo jardim
					sintese_voz('"Saindo do cômodo jardim!"')
					break
				elif obj_op_completo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Este objeto não foi reconhecido. Tente novamente."')
		elif cmd_op_completo in ['garagem', 'controlar garagem', 'cômodo garagem']: #cômodo garagem
			sintese_voz('"Cômodo garagem selecionado. Escolha o objeto que deseja controlar."')
			while True:
				obj_op_completo = captura_voz().lower() #objeto que deseja controlar
				if obj_op_completo in ['iluminação', 'lâmpada', 'lâmpadas', 'luzes', 'controlar lâmpadas', 'controlar lâmpada']: #objeto lâmpada
					sintese_voz('"Você está controlando as lâmpadas da garagem. O que deseja fazer ?"')
					while True:
						pi = '10.2.35.204'
						iluminação = captura_voz().lower() #opções para controlar lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio18/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_garagem_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio18/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_garagem_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio18/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada da garagem está acesa!"')
							else:
								sintese_voz('"A lâmpada da garagem está apagada!"')
						elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo garagem controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do objeto iluminação
							sintese_voz('"Saindo do menu iluminação!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_completo in ['ventilador', 'clima', 'ventilação', 'controlar ventilação', 'controlar ventilador']: #objeto ventilador
					sintese_voz('"O cômodo garagem não possui um ventilador!"')
				elif obj_op_completo in ['tempo', 'data', 'hora', 'exibir data', 'exibir hora']: #objeto relógio
					tempo()
				elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está no cômodo garagem. Escolha o objeto que deseja controlar."')
				elif obj_op_completo in 'sair voltar retornar': #sair do cômodo garagem
					sintese_voz('"Saindo do cômodo garagem!"')
					break
				elif obj_op_completo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Este objeto não foi reconhecido. Tente novamente."')
		elif cmd_op_completo in ['banheiro', 'controlar banheiro', 'cômodo banheiro']: #cômodo banheiro
			sintese_voz('"Cômodo banheiro selecionado. Escolha o objeto que deseja controlar."')
			while True:
				obj_op_completo = captura_voz().lower() #objeto que deseja controlar
				if obj_op_completo in ['iluminação', 'lâmpada', 'lâmpadas', 'luzes', 'controlar lâmpadas', 'controlar lâmpada']: #objeto lâmpada
					sintese_voz('"Você está controlando as lâmpadas do banheiro. O que deseja fazer ?"')
					while True:
						pi = '10.2.201.3'
						iluminação = captura_voz().lower() #opções para controlar lâmpada
						if iluminação in ['acender', 'acender lâmpada', 'ligar', 'ligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio20/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada já está acesa!"')
							else:
								os.system('ssh pi@{} lampada_banheiro_on'.format(pi))
								sintese_voz('"Lâmpada acesa!"')
						elif iluminação in ['apagar', 'apagar lampada', 'desligar', 'desligar lâmpada']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio20/value", shell = True)
							if int(status) == 1:
								sintese_voz('"A lâmpada já está apagada!"')
							else:
								os.system('ssh pi@{} lampada_banheiro_off'.format(pi))
								sintese_voz('"Lâmpada apagada!"')
						elif iluminação in ['relatório', 'exibir relatório', 'situação', 'exibir situação', 'status', 'exibir status']:
							status = subprocess.check_output("ssh pi@10.2.35.204 cat /sys/class/gpio/gpio20/value", shell = True)
							if int(status) == 0:
								sintese_voz('"A lâmpada do banheiro está acesa!"')
							else:
								sintese_voz('"A lâmpada do banheiro está apagada!"')
						elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
							sintese_voz('"Você está no cômodo banheiro controlando a iluminação. O que deseja fazer ?"')
						elif iluminação in 'sair voltar retornar': #sair do objeto iluminação
							sintese_voz('"Saindo do menu iluminação!"')
							break
						elif iluminação == 'none':
							irreconhecido()
						else:
							sintese_voz('"Esta opção não foi reconhecida. Tente novamente."')
				elif obj_op_completo in ['ventilador', 'clima', 'ventilação', 'controlar ventilação', 'controlar ventilador']: #objeto ventilador
					sintese_voz('"O cômodo banheiro não possui um ventilador!"')
				elif obj_op_completo in ['tempo', 'data', 'hora', 'exibir data', 'exibir hora']: #objeto relógio
					tempo()
				elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
					sintese_voz('"Você está no cômodo banheiro. Escolha o objeto que deseja controlar."')
				elif obj_op_completo in 'sair voltar retornar': #sair do cômodo banheiro
					sintese_voz('"Saindo do cômodo banheiro!"')
					break
				elif obj_op_completo == 'none':
					irreconhecido()
				else:
					sintese_voz('"Este objeto não foi reconhecido. Tente novamente."')
		elif cmd_op_completo in ['tempo', 'hora', 'data', 'exibir data', 'exibir hora']: #objeto relógio
			tempo()
		elif obj_op_completo in ['relembrar', 'me relembre', 'onde estou']:
			sintese_voz('"Você está no menu casa, usando o modo de operação completo. Escolha o cômodo que deseja controlar."')
		elif cmd_op_completo in 'sair voltar retornar': #sair do menu_casa
			sintese_voz('"Saindo do menu casa!"')
			break
		elif cmd_op_completo == 'none':
			irreconhecido()
		else:
			sintese_voz('"Este comando não foi reconhecido. Tente novamente."')

#========================================#
#		   MENU			 #
#========================================#
sintese_voz('"{}, sou seu assistente. Me diga quem esta falando ?"'.format(cumprimento()))
reconhecimento() #faz o reconhecimento de quem está tentando usar o assistente
sintese_voz('"Para executar algum comando é só me chamar, estarei descansando!"')
while True:
	start = captura_voz().lower()
	if start in 'assistente': #inicia o assistente
		limpar()
		sintese_voz('"Olá, como posso ajudar ?"')
		while True: #MENU PRINCIPAL
			comando = captura_voz().lower() #captura os comandos principais
			if comando in 'manual':
				sintese_voz('"Deseja acesso ao manual escrito ou por voz ?"')
				while True:
					manual_op = captura_voz()
					if manual_op in ['escrito', 'impresso', 'manual escrito']:
						manual_escrito()
						break
					elif manual_op in ['voz', 'fala', 'falado', 'por voz', 'manual por voz']:
						manual_voz()
						break
					elif manual_op == 'none':
						irreconhecido()
					else:
						sintese_voz('"Esta opção não existe. Tente novamente"')
			elif comando in ['tempo', 'hora', 'data', 'exibir data', 'exibir hora']:
				tempo()
			elif comando in ['playlist', 'músicas', 'lista de músicas', 'exibir playlist']:
				playlist()
			#====================================================== SESSÃO MULTIMIDIA ===========================================================#
			elif comando in ['tocar música 1', 'tocar músisa um', 'executar música 1', 'executar música um']:
				pygame.init()
				pygame.mixer.music.load('playlist/byob.mp3')
				pygame.mixer.music.play()
			elif comando in ['tocar música 2', 'tocar música dois', 'executar música 2', 'executar música dois']:
				pygame.init()
				pygame.mixer.music.load('playlist/anotherbites.mp3')
				pygame.mixer.music.play()
			elif comando in ['tocar música 3', 'tocar músisa três', 'executar música 3', 'executar música três']:
				pygame.init()
				pygame.mixer.music.load('playlist/anotherbrick.mp3')
				pygame.mixer.music.play()
			elif comando in ['tocar música 4', 'tocar músisa quatro', 'executar música 4', 'executar música quatro']:
				pygame.init()
				pygame.mixer.music.load('playlist/sweetdreams.mp3')
				pygame.mixer.music.play()
			elif comando in ['tocar música aleatória', 'música aleatória', 'tocar música', 'executar música', 'executar música aleatória']:
				lista_musicas = ['anotherbites', 'anotherbrick', 'sweetdreams', 'byob']
				pygame.init()
				musica_aleatoria = choice(lista_musicas)
				pygame.mixer.music.stop()
				pygame.mixer.music.load('playlist/{}.mp3'.format(musica_aleatoria))
				pygame.mixer.music.play()
			elif comando == 'parar música':
				pygame.mixer.music.stop()
			#====================================================================================================================================#
			elif comando in ['internet', 'menu internet']: #Menu para acessar sites e realizar novas buscas
				sintese_voz('"Bem Vindo ao menu Internet. O que deseja buscar ?"')
				while True:
					browser = captura_voz().lower()
					if browser in ['google', 'abrir google']:
						sintese_voz('"Abrindo Google"')
						webbrowser.open_new('https://www.google.com.br')
					elif browser in ['youtube', 'abrir youtube']:
						sintese_voz('"Abrindo YouTube"')
						webbrowser.open_new('https://www.youtube.com.br')
					elif browser in ['facebook', 'abrir facebook']:
						sintese_voz('"Abrindo Facebook"')
						webbrowser.open_new('https://www.facebook.com')
					elif browser in 'sair voltar retornar': #Sair do menu Internet
						sintese_voz('Saindo do menu internet!')
						break
					elif browser == 'none':
						irreconhecido()
					else: #Busca qualquer coisa que o usuário diga
						sintese_voz('"Buscando resultados para {}"'.format(browser))
						webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q={}'.format(browser))
			elif comando in ['casa', 'menu casa', 'controlar casa']: #ABRIR MENU CASA
				menu_casa()
			elif comando in ['acender todas as lâmpadas']:
				pi = '10.2.201.3'
				os.system('ssh pi@{} lampada_garagem_on'.format(pi))
				os.system('ssh pi@{} lampada_sala_on'.format(pi))
				os.system('ssh pi@{} lampada_jardim_on'.format(pi))
				os.system('ssh pi@{} lampada_quarto_on'.format(pi))
				os.system('ssh pi@{} lampada_banheiro_on'.format(pi))
				os.system('ssh pi@{} lampada_cozinha_on'.format(pi))
			elif comando in ['apagar todas as lâmpadas']:
				pi = '10.2.201.3'
				os.system('ssh pi@{} lampada_garagem_off'.format(pi))
				os.system('ssh pi@{} lampada_sala_off'.format(pi))
				os.system('ssh pi@{} lampada_jardim_off'.format(pi))
				os.system('ssh pi@{} lampada_quarto_off'.format(pi))
				os.system('ssh pi@{} lampada_banheiro_off'.format(pi))
				os.system('ssh pi@{} lampada_cozinha_off'.format(pi))
			elif comando in ['teste', 'demonstrar', 'demonstração']:
				pi = '10.2.201.3'
				os.system('ssh pi@{} lampada_garagem_on'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_sala_on'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_jardim_on'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_quarto_on'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_banheiro_on'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_cozinha_on'.format(pi))
				sleep(1)
				os.system('ssh pi@{} ventilador_quarto_on'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_garagem_off'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_sala_off'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_jardim_off'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_quarto_off'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_banheiro_off'.format(pi))
				sleep(1)
				os.system('ssh pi@{} lampada_cozinha_off'.format(pi))
				sleep(1)
				os.system('ssh pi@{} ventilador_quarto_off'.format(pi))
				sleep(1)
			elif comando in ['relembrar', 'me relembre', 'onde estou']:
				sintese_voz('"Você está no menu principal. Escolha o que deseja fazer."')
			elif comando in 'sair fechar encerrar finalizar': #encerrar programa
				sair()
			elif comando == 'none':
				irreconhecido()
			else:
				sintese_voz('"Este comando não foi reconhecido. Tente novamente."')
	if start in 'sair fechar encerrar finalizar': #encerrar programa
		sair()

