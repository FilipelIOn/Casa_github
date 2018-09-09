from Assentos import Assento

class controladorAssento():
    def __init__ (self,linha,coluna):
        self.__linha=linha
        self.__coluna=coluna
        self.__listaAssentos = {}
        self.__matrizAlpha = {}
        self.__listaCompradas = []
        self.__resumoVendas = 0
        self.__listaDevolve =[]
        self.__a=[]


    def getLinha(self):
        return self.__linha
    def getColuna(self):
        return self.__coluna



    def criarMatriz(self):
        a=0
       
        for i in range(self.__linha):
            for j in range(self.__coluna):
                self.__matrizAlpha[(i,j)]= a
                a+=1

    def criarAssentos(self):
        a=0
        for i in range(self.__linha):
            preco = 20-i
            for j in range(self.__coluna):
                novoAssento = Assento(a,preco)
                self.__listaAssentos[(i,j)]= novoAssento
                a+=1
        
    def imprimeMatriz(self):
        totalint = self.__linha * self.__coluna
        totalstr = str(totalint)
        tamanho = len(totalstr)
        
        for x in range(self.__linha):
            linha = ""
            for y in range(self.__coluna):
                linha += " "+ str(self.__matrizAlpha[(x,y)]).zfill(tamanho)
            print(linha)

    
    def compraAssento(self,compra):
        for i in compra:
            i = int(i)
            PL = i//self.__coluna
            PC = i%self.__coluna
            if self.__listaAssentos[(PL,PC)].getDisponivel() == True:
                self.__listaCompradas.append(i)
                self.__resumoVendas+=self.__listaAssentos[(PL,PC)].getPreco()
                print()
                print("Chair %d bought"%i)
                print()
                self.__listaAssentos[(PL,PC)].setDisponivel(False)
            else:
                print()
                print("Chair %d busy"%i)
    def getListaComprada(self):
        return self.__listaCompradas
    
    
    def xxSet(self):
        for i in self.__listaCompradas:
            i = int(i)
            PL = i//self.__coluna
            PC = i % self.__coluna
            self.__matrizAlpha[(PL,PC)] = "X"*len(str(self.__linha*self.__coluna))
                         
     
    def devolverAssento(self,devolve):
        for i in devolve:
            i = int(i)
            PL = i//self.__coluna
            PC = i%self.__coluna
            if self.__listaAssentos[(PL,PC)].getDisponivel() == False:
                self.__listaDevolve.append(i)
                self.__resumoVendas-=(self.__listaAssentos[(PL,PC)].getPreco()*0.9)
                print()
                print("Chair %d returned"%i)
                print()
                self.__listaAssentos[(PL,PC)].setDisponivel(True)
            else:
                print()
                print("The chair %s can't be returned"%i)


    def xxBack(self):
        for i in self.__listaDevolve:
            i = int(i)
            PL = i//self.__coluna
            PC = i % self.__coluna
            self.__matrizAlpha[(PL,PC)] = i

    def resumoVendas(self):
        qtdCompra = len(self.__listaCompradas)
        qtdDevolvidas =len(self.__listaDevolve)
        print()
        print("Room occupancy at the moment:%d"%(qtdCompra-qtdDevolvidas))
        print()
        print("Amount of tickets returned:%d"%qtdDevolvidas)
        print()
        print("Total value determined US$%.2f"%self.__resumoVendas)
        
    def arquivoSalva(self):
        arq = open("salvar.txt","w")
        
        arq.write(str(self.__linha))
        arq.write(":")
        arq.write(str(self.__coluna))
        arq.write(":")
        arq.write(str(self.__listaCompradas))
        arq.write(":")
        arq.write(str(self.__listaDevolve))
        arq.write(":")
        
        arq.write(str(self.__resumoVendas))
        arq.close()
        
        
    def arquivoBack(self):
        
        arq = open("salvar.txt")
        self.__a= arq.readline()
      
        arq.close()
 

    def getArquivo(self):
        return self.__a