import numpy as np
import tkinter as tk
import random 

class Solution:
    def __init__(self, n =8, want_all_answers = False):
        self.n = n
        self.array = np.zeros((n,n))
        self.want_all_answers = want_all_answers
        self.solutions = []
        self.solution() # by default, give me all answers

    def is_safe(self,row, col): # function for checking if a house is valid
        for k in range(len(self.array)):
            if self.array[row][k] == 1 :
                return False
        for k in range(len(self.array)):
            if self.array[k][col] == 1 :
                return False
        i,j = row, col
        while i >= 0 and j >= 0 :
            if self.array[i][j] == 1:
                return False
            i -= 1
            j -= 1
        i,j = row, col
        while i<len(self.array) and j <len(self.array):
            if self.array[i][j] == 1:
                return False
            i+= 1
            j-= 1
        i,j = row, col
        while i<len(self.array) and j >=0 :
            if self.array[i][j] == 1:
                return False
            i+=1
            j-= 1
        i,j = row, col
        while i >= 0 and j < len(self.array):
            if self.array[i][j]==1:
                return False
            i-= 1
            j+=1
        return True
    
    def solution(self):
        def backtrack(row = 0):
            if row == self.n :
                self.solutions.append(self.array.copy())
                return
            for col in range(self.n):
                if self.is_safe(row, col):
                    self.array[row][col] = 1
                    backtrack(row+1)
                    self.array[row][col] = 0
            return
        backtrack()
        return self.solutions
    
    def print_all_solutions(self): # if the user want to see every answer
        counter = 1
        for i in self.solutions:
            print(f"--------------> solution : {counter} <--------------")
            print(i)
            counter += 1

    def make_chess_board(self):
        if len(self.solutions) == 0 :
            return 
        window = tk.Tk() # creating tkinter application
        window.title("Chess Board")
        window.geometry(f"{self.n*80}x{self.n*80}") # adjust the app with the size of n 
        randnum = random.randint(0, len(self.solutions)-1)
        board = self.solutions[randnum]
        for i in range(self.n): # coloring and filling chess cells
            for j in range(self.n):
                text = "♕" if board[i][j] == 1 else ""
                cell = tk.Label(text=text, font="Areal 35 bold")
                cell.place(x=i*80, y=j*80,height=80, width=80 )
                if ((i%8) % 2 == 0 and j%2 != 0) or ((i%8) % 2 != 0 and j%2 == 0) :
                    cell.config(bg="dark green")
                elif ((i%8) % 2 != 0 and j%2 != 0) or ((i%8) % 2 == 0 and j%2 == 0) :
                    cell.config(bg="white")
        window.mainloop()
    
if __name__ == "__main__":
    solution = Solution() # n_deafault = 8, wants_all_answers_default = False
    if solution.want_all_answers: # u can set it True if want all answers
        solution.print_all_solutions() # note that computation may take time 
    solution.make_chess_board() # showing one of the random solutions