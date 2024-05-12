import re 
import numpy as np

class sudoku:
    
    def __init__(self) -> None:
        
        self.game = []
        self.compteur = 0 
        
        
    def checknumber(self,lignes,indice):
        ParsedList = []
        compteur1 = 0
        compteur2 = 0
        while(compteur1 < len(lignes) and lignes[indice][compteur1] != "," ):
            while(lignes[indice][compteur2] != ","):
                compteur2 += 1
                print(lignes[indice][compteur1:compteur2])
                ParsedList.append(int(lignes[indice][compteur1:compteur2]))
                compteur1 = compteur2 + 1
                compteur2 = compteur1
                if compteur1 > len(lignes[indice]) - 1:
                    break
        return ParsedList
        
    def read_data(self,text):
        fichier = open(text, "r",encoding="utf8")
        lines = fichier.readlines()
        lines = [lines[i] for i in range(len(lines)) if lines[i] != "\n"]
        lines = [ re.sub("\n", "", lines[i]) for i in range(len(lines))]
        print(lines)
        self.game = [self.checknumber(lines,i)  for i in range(len(lines))]
        print("list: ", self.game)
        self.game = np.array(self.game)
        print("array: ", self.game)
        
        
    def check_solution(self,x,y,n):
        x_sudoku_square = (x//3) * 3
        y_sudoku_square = (y//3) * 3
        check = True 
        for i in range(0,9):
            if self.game[x,i] == n:
                check = False
        for j in range(0,9):
            if check == False:
                break
            if self.game[j,y] == n:
                check = False
        for i in range(0,3):
            for j in range(0,3):
                if check == False:
                    break
                if self.game[x_sudoku_square + i, y_sudoku_square + j] == n:
                    check = False
        return check 
    
    
    def AC3_solve(self):
        self.compteur += 1
        for i in range(0,9):
            for j in range(0,9):
                if self.game[i,j] == 0:
                    for n in range(1,10):
                        if self.check_solution(i,j,n) == True:
                            self.game[i,j] = n
                            self.AC3_solve()
                            self.game[i,j] = 0
                    return
        print(self.game)
                

    
                                                        
                    
        
    
    

