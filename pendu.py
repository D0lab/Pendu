from random import randint
from PIL import Image,ImageFont,ImageDraw
import platform
import os
import sys
import time
import webbrowser

#CODE PAR DORIAN LABASTE EN MAI 2022
#MIS A JOUR LE 10/12/2024 pour remplacer le getSize en getbox






def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
		

		
pendu_gagne = resource_path('img/pendu_gagne.png')
pendu_perdu = resource_path('img/pendu_perdu.png')


def gagneimg(): #AFFICHAGE image fin gagne
	img = Image.open(pendu_gagne)
	str1="\"" + str(motfinal)+"\""
	font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",50)
	left, top, right, bottom = font.getbbox(str1)
	w = right - left
	h = bottom - top
	draw = ImageDraw.Draw(img)
	draw.text(((512-w)/2,(625-h)/2),str1,font=font,fill="white")
	img.show()
	time.sleep(1)
	img.close()
	
def perduimg(): #AFFICHAGE image fin perdu
	img = Image.open(pendu_perdu)
	str1="\"" + str(motfinal)+"\""
	font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",50)
	left, top, right, bottom = font.getbbox(str1)
	w = right - left
	h = bottom - top
	draw = ImageDraw.Draw(img)
	draw = ImageDraw.Draw(img)
	draw.text(((512-w)/2,(625-h)/2),str1,font=font,fill="white")
	img.show()
	time.sleep(1)
	img.close()
	

fin = 0
essais = 6
compteurgagne = 0
compteurperdu = 0





def Clean(): #Nettoie la console (selon la plateforme)
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    

while True:	
	
	dicofr = resource_path("data/dico_fr.csv")
	dicoen = resource_path("data/dico_en.csv")
	dicoes = resource_path("data/dico_es.csv")
	dicoit = resource_path("data/dico_it.csv")
	dicode = resource_path("data/dico_de.csv")
			
			
	def credit():
		Clean()
		print("==============")
		print("Ce jeu a été codé par Dorian LABASTE")
		print("Surtout n'écrivez pas le code \"IDDQD\" durant le jeu, vous aurez la réponse sinon ! ;) ")
		print("==============")
		
	ok1 = 0
	
	

	while ok1 == 0:
		
		print("1 = Français")
		print("2 = Anglais")
		print("3 = Espagnol")
		print("4 = Italien")
		print("5 = Allemand")
		print("")
		langue = str(input("Quelle langue choisissez-vous pour le mot mystère ? : "))
		
			
		if langue == "1" or langue == "2" or langue == "3" or langue == "4" or langue == "5":
			ok1 +=1
			
		if langue == "credit" or langue == "CREDIT":
			credit()
			
		else:
			Clean()
			print("Vous devez entrer un des chiffres disponible ci-dessous !")
			print("")

	if langue == "1":
		lg = dicofr
	if langue == "2":
		lg = dicoen
	if langue == "3":
		lg = dicoes
	if langue == "4":
		lg = dicoit
	if langue == "5":
		lg = dicode
		
		
	file = open(lg, "r")
	lines = file.readlines()
	file.close()

	mot = lines[randint(0,len(lines)-1)] #Mot à trouver
	motfinal = mot[:-2]
	
	def sautligne(): #Permet de sauter 2 lignes, ça fait plus propre
		print('')
		print('')
		
		
			
	def pendu():
		
		if essais==0:
			print(" ==========Y= ")
			print(" ||/       |  ")
			print(" ||        0  ")
			print(" ||       /|\ ") 
			print(" ||       /|  ")                   
			print("/||           ")
			print("==============")
			
		if essais==1:
			print(" ==========Y= ")
			print(" ||/       |  ")
			print(" ||        0  ")
			print(" ||           ") 
			print(" ||           ")                  
			print("/||           ")
			print("==============")
			
		if essais==2:
			print(" ==========Y= ")
			print(" ||/       |  ")
			print(" ||           ")
			print(" ||           ") 
			print(" ||           ")                  
			print("/||           ")
			print("==============")
			
		if essais==3:
			print(" ============ ")
			print(" ||/          ")
			print(" ||           ")
			print(" ||           ") 
			print(" ||           ")                  
			print("/||           ")
			print("==============")
			
		if essais==4: 
			print("              ")
			print(" ||           ")
			print(" ||           ")
			print(" ||           ") 
			print(" ||           ")                  
			print("/||           ")
			print("==============")
			
		if essais==5:
			print("              ")
			print("              ")
			print("              ")
			print("              ") 
			print("              ")                  
			print("              ")
			print("==============")
			
		if essais==6:
			print("              ")
			print("              ")
			print("              ")
			print("              ") 
			print("              ")                  
			print("              ")
			print("              ")
			


	def afficher(): 
		Clean()	

		global langue
		
		if langue == "1":
			print("VOTRE MOT MYSTERE EST EN FRANCAIS !")
		if langue == "2":
			print("VOTRE MOT MYSTERE EST EN ANGLAIS !")
		if langue == "3":
			print("VOTRE MOT MYSTERE EST EN ESPAGNOL !")
		if langue == "4":
			print("VOTRE MOT MYSTERE EST EN ITALIEN !")
		if langue == "5":
			print("VOTRE MOT MYSTERE EST EN ALLEMAND !")

		print("Vous avez gagné",compteurgagne,"fois et perdu",compteurperdu,"fois !")
		print("Il vous reste",essais,"faute(s) possible(s)") #Nombre d'essais restants
		
		print("")
		if langue == "3":
			print("pour le caractère \"ñ\" vous devez entrer \"ny\" !")
		print("")
		historique()
		sautligne()
		for x in range(len(affichage)): #(+1) affiche sur la même ligne la ligne du pendu
			print(affichage[x], '',end = "")
		sautligne()
		pendu()
			
		
	def historique():
		print("Les lettres déjà entrées sont : ")
		for m in range(len(hstrq)): #(+1) affiche sur la même ligne la ligne du pendu
			print(hstrq[m], ' , ',end = "")	


	prerempli = ["-"," ","'"] #Liste de caractères à pré-remplir dans la ligne du pendu



	hstrq = [] #liste pour lettres déjà entrées
	
	

	def lettre():
			
		global essais #(+3) Mise en place des variables
		global hstrq
		cmpt = 0 #var pour vérifier si la lettre est présente
		cmpt3 = 0
		
		
		sautligne()
		afficher()
		possible=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		
		
		ok2 = 0
		checklettre = 0
		while ok2 == 0:
			l = str(input("Quelle lettre voulez-vous entrer ? : "))
			for i in range(len(possible)):
				if l == possible[i]:
					checklettre = 1
				
			if len(l) == 1 and checklettre == 1:
				ok2 +=1
				
			elif langue == "3" and l == "ny":
				l = "ñ"
				ok2 +=1
				
			elif l == "IDDQD" or l == "iddqd":
				webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
				Clean()
				afficher()
				
			else:
				Clean()
				afficher()
				print("Ce caractère n'est pas autorisé, veuillez entrer une lettre !")
		
		
		   
		
		
		
		Clean()
		
			
		for u in range(len(hstrq)):
			if l == hstrq[u]:
				Clean()
				afficher()
				cmpt3 = 1
				print("Vous avez déjà entré cette lettre !")
			
		
		if cmpt3 == 0:
		
			hstrq.append(l)	

			for i in range(len(motfinal)):
				if l == motfinal[i]:
					
					ind = i
					affichage[ind] = l
					cmpt += 1
				
			
			if cmpt == 0:
				Clean()
				afficher()
				essais -= 1
			
		
			
			
		

	affichage = [] #(+4) Permet d'afficher la toute premiere ligne du pendu)
	affichage.append(motfinal[0])
	for w in range(len(motfinal)-1):
		affichage.append("_")
		
	for p in range(len(motfinal)):
		for t in range(len(prerempli)):
			if motfinal[p] == prerempli[t]:
				ind = p
				affichage[ind] = prerempli[t]
	for g in range(len(motfinal)):
		if motfinal[0] == motfinal[g]:
				ind2 = g
				affichage[ind2] = motfinal[0]
				
	afficher()


	while fin == 0 :		
		
		if essais == 0:
			
			fin = 1
			Clean()
			print("Dommage c'est perdu ! Le mot était \"",motfinal,"\"")
			compteurperdu += 1
			perduimg()
			essais = 0
			pendu()
		else : 
			
			cmpt = 0
			
		
			for i in range(len(affichage)):
				if affichage[i] == "_":
					cmpt += 1
			if cmpt > 0:
				jeu = 1
				lettre()
			else: 
				fin = 2
				print("Bravo ! Le mot était bien \"",motfinal,"\"")
				print("Avec",6-essais,"faute(s)")
				compteurgagne += 1
				gagneimg()
				pendu()
				
				

	
		
	while True:
		answer = input('Voulez-vous rejouer ? (o/n): ')
		
		if answer == 'o':
			Clean()
			print('Rejouons !')
			essais = 6
			fin = 0
			break
			
		if answer == 'n':
			quit()
			break
			
		else:
			Clean()
			print("Vous devez répondre o pour oui ou n pour n !")
			
			
			

	
	
