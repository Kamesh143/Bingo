import random 
import os
os.system('clear')
print("Let's play Bingo😍️")

player1 = [[],[],[],[],[]]
player2 = [[],[],[],[],[]]
Done = []
p1Name = input("Enter player1 name : ")
p2Name = input("Enter player2 name : ")
os.system('clear')

def checkWin(player):
	count = 0
	# Column check
	for i in range(5):
		flag = 0
		for j in range(5):
			if player[j][i] not in Done:
				flag = 1
				break
		if flag == 0:
			count += 1
			
	# Row check
	for i in range(5):
		flag = 0
		for j in range(5):
			if player[i][j] not in Done:
				flag = 1
				break
		if flag == 0:
			count += 1
			
	# Cross right-check
	flag = 0
	for i in range(5):
		if player[i][i] not in Done:
			flag = 1
			break
	if flag == 0:
		count += 1
	
	# Cross left-check
	for i in range(5):
		if player[4-i][i] not in Done:
			flag = 1
			break
	if flag == 0:
		count += 1
	
	if count >= 5:
		return True
	else: 
		return False
		
	
def play():
	for i in range(5):
		# print(len(player1[i]))
		while len(player1[i]) != 5:
			x = random.randint(1,25)
			if x not in sum(player1,[]):
				player1[i].append(x)
		while len(player2[i]) != 5:
			x = random.randint(1,25)
			if x not in sum(player2,[]):
				player2[i].append(x)
		
	# print(player1)
	# print(player2)

	flag = 0
	while True:
		if flag == 0:
			for i in player1:
				for j in i:
					if j in Done:
						print(str(j)+"\u0336",end="\t")
					else:
						print(j,end="\t")
				print()
			p1 = int(input(f"Enter you choice {p1Name} : "))
			if p1 not in Done : Done.append(p1)
			flag = 1
			if checkWin(player1):
				print(p1Name,"Won")
				break
			if checkWin(player2):
				print(p2Name,"Won")
				break
			os.system('clear')
			input(f"Turn to {p2Name} ...")
		else:
			for i in player2:
				for j in i:
					if j in Done:
						print(str(j)+"\u0336",end="\t")
					else:
						print(j,end="\t")
				print()
			p2 = int(input(f"Enter you choice {p2Name} : "))
			if p2 not in Done : Done.append(p2)
			flag = 0
			if checkWin(player2):
				print(p2Name,"Won")
				break
			if checkWin(player1):
				print(p1Name,"Won")
				break
			os.system('clear')			
			input(f"Turn to {p1Name} ...")	
play()

