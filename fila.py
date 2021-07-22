class Fila:
     def __init(self):
          self.fila=[]
     def enfilheira(self,F):
          self.fila.append(F)
     def desenfilheira(self):
         if not self.isVazia(): 
            self.fila.pop(0)
         else:
             print("fila vazia")
     def isVazia(self):
          if  len(self.fila)==0:
              return True
          else:
              return False
     def __str(self):
          return self.fila
     def repr(self):
         return str(self.fila)
