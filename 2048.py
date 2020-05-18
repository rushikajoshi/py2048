import random
import os
import numpy
import argparse
from time import sleep
def new_tile(game):
	for x in range(len(game)*len(game)):
		a=random.randint(0,len(game)-1)
		b=random.randint(0,len(game)-1)
		if(game[a][b]==0):
			game[a][b]=2
			break
	return game
def reverse(game):
	return[ele for ele in reversed(game)]
def game_transpose(game):
	transpose=[]
	for i in range(len(game)):
		new_row=[]
		for j in range(len(game)):
			new_row.append(game[j][i])
		transpose.append(new_row)
		i=0
	return transpose
def tile_move(game,flag=0):
	for j in range(len(game)):
			for g in range(len(game)-1):
				if(game[g][j]==game[g+1][j] or game[g+1][j]==0 or game[g][j]==0):
					flag=1
					break
			if(flag==1):
				for i in range(len(game)):
					for k in range(len(game)-1):
						if(game[i][j]==game[k+1][j] and game[i][j]!=0 and k+1!=i):
							game[i][j]=2*game[i][j]
							game[k+1][j]=0
							break
						if(game[k+1][j]!=0 and game[k][j]==0):
							game[k][j]=game[k+1][j]
							game[k+1][j]=0
						if(game[k+1][j]!=0 and game[k][j]!=0 and game[k+1][j]!=game[k][j]):
							k=k+1
				flag=0
	return game
def play_move(move,game):
	if(move=='w'):
		tile_move(game)
	elif(move=='s'):
		reverse_game=reverse(game)
		tile_move(reverse_game)
	elif(move=='a'):
		transpose=game_transpose(game)
		transpose_move=tile_move(transpose)
		game=game_transpose(transpose_move)
	elif(move=='d'):
		inverted_game=[]
		for row in game:
			inverted_row=reverse(row)
			inverted_game.append(inverted_row)
		transpose=game_transpose(inverted_game)
		transpose_move=tile_move(transpose)
		detranspose=game_transpose(transpose_move)
		game=[]
		for detransposed_row in detranspose:
			row=reverse(detransposed_row)
			game.append(row)
	else:
		print("INVALID MOVE! ")
		sleep(1)
	
	return game
def win_check(game,End_number):
	for i in range(len(game)):
		for j in range(len(game)):
			if(game[i][j]==End_number):
				print("YOU WIN!")
				return False
	return True
def gameover_check(game,flag=0):
	for i in range(len(game)):
		for j in range(len(game)-1):
			if(game[i][j]!=0 or game[i][j]!=game[i][j+1] or game[j][i]!=game[j+1][i]):
				flag=1
		if(flag==1):
			break
	if(flag==0):
		print("GAME OVER!")
		return False
	else:
		return True
#driver code
parser=argparse.ArgumentParser()
parser.add_argument("--n", default=4, help="size of the game board")
parser.add_argument("--w", default=2048, help="target number")
args=parser.parse_args()
game_size=int(args.n)
End_number=int(args.w)
game=numpy.zeros([game_size, game_size], dtype=int)
new_tile(game)
for i in range(game_size):
	for j in range(game_size):
		print(game[i][j],end="   ")
	print()
	print()
play=True
while play==True:
	move=input()
	game=play_move(move,game)
	if(move=='a' or move=='d' or move=='s' or move=='w'):
		new_tile(game)
	os.system("cls")
	p1=win_check(game,End_number)
	if p1:
		play=gameover_check(game)
	else:
		play=False
	for i in range(len(game)):
		for j in range(len(game)):
			print(game[i][j],end="   ")
		print()
		print()
