import random
import time
from os import system

class point():

	def __init__(self,n):
		self.x=random.randint(0,1)			
		if(self.x==0):
			self.y=random.randint(0,n-1)
		else:
			self.y=0
			self.x=random.randint(0,n-1)


class obstacle():

	def __init__(self,n):

		self.x=random.randint(0,n-1)			
		self.y=random.randint(0,n-1)			



class reward():

	def __init__(self,n):

		self.x=random.randint(0,n-1)
		self.y=random.randint(0,n-1)
		self.value=random.randint(1,9)
	

def initiate(n):

	a=[n][n]
	for i in range(n):
		for j in range(n):
			a[i][j].append(".")

	return a
def initiate_obs(grid):
	
	for i in grid.myObstacles:
		if(grid.grid[i.x][i.y]=="." and grid.grid[i.x][i.y]!="O" and grid.grid[i.x][i.y]!="E"):
			grid.grid[i.x][i.y]="#"


def initiate_rew(grid):
	
	for i in grid.myRewards:
		if(grid.grid[i.x][i.y]=="." and grid.grid[i.x][i.y]!="#" and grid.grid[i.x][i.y]!="O" and grid.grid[i.x][i.y]!="E"):
			grid.grid[i.x][i.y]=i.value


import copy
class grid():

	def __init__(self,n,player):

		self.grid=[["." for i in range(n)] for j in range(n)]
		self.n=n
		self.start=point(n)		
		self.goal=point(n)		
		self.myObstacles=[obstacle(n) for i in range(2*n)]		#obstacle class will provide the obstacles
		self.myRewards=[reward(n) for i in range((2*n)//3)]			#reward class will provide the rewards
		self.grid[self.start.x][self.start.y]="O"
		self.grid[self.goal.x][self.goal.y]="E"
		initiate_obs(self)
		initiate_rew(self)
		self.player=player
		





	def rotateClockwise(self):

		a=copy.deepcopy(self.grid)
		
		
		for i in range(self.n):
			for j in range(self.n):
				if(self.grid[i][j]!="O" and self.grid[i][j]!="E" and a[n-j-1][i]!="O" and a[n-1-j][i]!="E"):
					self.grid[i][j]=a[n-1-j][i]
					

		

	def rotateAnticlockwise(self):
		a=copy.deepcopy(self.grid)
		
		
		for i in range(self.n):
			for j in range(self.n):
				if(self.grid[i][j]!="O" and self.grid[i][j]!="E" and a[j][n-1-i]!="O" and a[j][n-1-i]!="E"):
					self.grid[i][j]=a[j][n-1-i]


	def showGrid(self):

		system('cls')

		print("\nEnergy:",self.player.energy)

		for i in range(self.n):
			for j in range(self.n):
				
				print(self.grid[i][j],end="    ")
				
			print("\n")
		time.sleep(0.5)



def update(player):
	global grid
	player.x=grid.start.x
	player.y=grid.start.y





class player():

	def __init__(self,n):
		self.x=0			
		self.y=0			
		self.energy=2*n		
		


	def makeMove(s):

		pass

	def updatestart(self):
		global grid
		self.x=grid.start.x
		self.y=grid.start.y






n=int(input("enter the size of grid:"))


player=player(n)
grid=grid(n,player)
player.updatestart()

grid.showGrid()

moves=str(input("enter your move:"))
moves=moves.lower()

def right(grid,player,num):
	energy=0
	end=0
	for i in range(num):
		if(player.y!=n-1 and grid.grid[player.x][player.y+1]=='#'):
			player.energy-=4*n
		elif(player.y!=n-1 and grid.grid[player.x][player.y+1]!='.' and grid.grid[player.x][player.y+1]!='#' and grid.grid[player.x][player.y+1]!='O' and grid.grid[player.x][player.y+1]!='E'):
			player.energy+=int(grid.grid[player.x][player.y+1])
		else:
			player.energy-=1
		if(player.y==n-1):
			grid.grid[player.x][player.y]='.'
			player.y=-1
		else:
			grid.grid[player.x][player.y]='.'

		
		if(player.energy<=0):
			energy=1
		if(grid.grid[player.x][player.y+1]=="E"):
			end=1
		grid.grid[player.x][player.y+1]="O"
		grid.showGrid()
		if(energy==1):
			print("player loses (low energy")
			break
		if(end==1):
			print("player wins")
			break
		
		player.y+=1
	return end
		

		


def left(grid,player,num):
	energy=0
	end=0
	for i in range(num):
		if(grid.grid[player.x][player.y-1]=='#'):
			player.energy-=4*n
		elif(grid.grid[player.x][player.y-1]!='.' and grid.grid[player.x][player.y-1]!='#' and grid.grid[player.x][player.y-1]!='O' and grid.grid[player.x][player.y-1]!='E'):
			player.energy+=int(grid.grid[player.x][player.y-1])
		else:
			player.energy-=1
		if(player.y==0):
			grid.grid[player.x][player.y]='.'
			player.y=n
		else:
			grid.grid[player.x][player.y]='.'
		
		if(player.energy<=0):
			energy=1
		if(grid.grid[player.x][player.y-1]=="E"):
			end=1
		grid.grid[player.x][player.y-1]="O"
		grid.showGrid()
		
		if(energy==1):
			print("player loses (low energy")
			break
		if(end==1):
			print("player wins")
			break
		
		player.y-=1
		return end
		

def up(grid,player,num):
	energy=0
	end=0
	for i in range(num):
		if(player.x!=n-1 and grid.grid[player.x-1][player.y]=='#'):
			player.energy-=4*n
		elif(player.x!=n-1 and grid.grid[player.x-1][player.y]!='.' and grid.grid[player.x-1][player.y]!='#' and grid.grid[player.x-1][player.y]!='O' and grid.grid[player.x-1][player.y]!='E'):
			player.energy+=int(grid.grid[player.x-1][player.y])
		else:
			player.energy-=1
		if(player.x==0):
			grid.grid[player.x][player.y]='.'
			player.x=n
		else:
			grid.grid[player.x][player.y]='.'
		
		if(player.energy<=0):
			energy=1
		if(grid.grid[player.x-1][player.y]=="E"):
			end=1
		grid.grid[player.x-1][player.y]="O"
		grid.showGrid()
		
		if(energy==1):
			print("player loses (low energy")
			break
		if(end==1):
			print("player wins")
			break
		
		player.x-=1
	return end



def down(grid,player,num):
	energy=0
	end=0
	for i in range(num):
		if(player.x!=n-1 and grid.grid[player.x+1][player.y]=='#'):
			player.energy-=4*n
		elif(player.x!=n-1 and grid.grid[player.x+1][player.y]!='.' and grid.grid[player.x+1][player.y]!='#' and grid.grid[player.x+1][player.y]!='O' and grid.grid[player.x+1][player.y]!='E'):
			player.energy+=int(grid.grid[player.x+1][player.y])
		else:
			player.energy-=1
		if(player.x==n-1):
			grid.grid[player.x][player.y]='.'
			player.x=-1
		else:
			grid.grid[player.x][player.y]='.'
		if(player.energy<=0):
			energy=1
		if(grid.grid[player.x+1][player.y]=="E"):
			end=1
		grid.grid[player.x+1][player.y]="O"
		grid.showGrid()
		
		if(energy==1):
			print("player loses (low energy")
			break
		if(end==1):
			print("player wins")
			break
		
		player.x+=1
	return end

		

def clock(grid,player,num):
	for i in range(num):
		grid.rotateClockwise()
		player.energy-=grid.n//3
		grid.showGrid()

	return 0

def anti(grid,player,num):
	for i in range(num):
		grid.rotateAnticlockwise()
		player.energy-=grid.n//3
		grid.showGrid()

	return 0

def move(moves,grid,player):

	z=0
	for i in range(0,len(moves),2):

		m=moves[i:i+1]
		num=int(moves[i+1:i+2])
		if(m=='l'):
			z=left(grid,player,num)
		elif(m=='r'):
			z=right(grid,player,num)
		elif(m=='u'):
			z=up(grid,player,num)
		elif(m=='d'):
			z=down(grid,player,num)
		elif(m=='c'):
			z=clock(grid,player,num)
		elif(m=='a'):
			z=anti(grid,player,num)

	if(player.energy>0 and z==0):
		ans=input("your health is remaining wanna try some more moves?(y/n):")
		if(ans=='y'):
			moves=str(input("enter your move:"))
			moves=moves.lower()
			move(moves,grid,player)

	

move(moves,grid,player)


	
