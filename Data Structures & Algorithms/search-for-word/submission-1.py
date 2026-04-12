class Solution:
   """
   BruteForce:
   Just check all sell what if the cell by the node's value is target

   """
   def exist(self, board: List[List[str]], word: str) -> bool:
       self.height, self.width = len(board), len(board[0])
       candidates = [[i, j] for i in range(self.height) for j in range(self.width)]
       self.visited = [[False] * self.width for _ in range(self.height)]

       def backtraking(target_i: int, candidates: List[List[int]]):
           if target_i == len(word):
               return True
               
           for i, j in candidates:
               if board[i][j] == word[target_i] and not self.visited[i][j]:
                   self.visited[i][j] = True
                   if backtraking(target_i + 1, self.get_neighbours(i, j)):
                       return True
                   self.visited[i][j] = False
           return False

       return backtraking(0, candidates)

   def get_neighbours(self, i: int, j: int) -> List[List[int]]:
       neighbours = []

       if j + 1 < self.width and not self.visited[i][j + 1]:
           neighbours.append([i, j + 1])
       
       if i + 1 < self.height and not self.visited[i + 1][j]:
           neighbours.append([i + 1, j])
       
       if j - 1 >= 0 and not self.visited[i][j - 1]:
           neighbours.append([i, j - 1])
       
       if i - 1 >= 0 and not self.visited[i - 1][j]:
           neighbours.append([i - 1, j])

       return neighbours