'''
Created on 14 de fev de 2017

@author: Filipe
'''
from ControladorAssento import controladorAssento
import time

while True:

    try:

        linhas = int(input("What's number of line?"))
        if linhas > 20:
            print("Line can't be big than the number 20")
            continue
        colunas = int(input("What's number of columns?"))
        sala = controladorAssento(linhas,colunas)
        sala.criarMatriz()
        sala.criarAssentos()
        sala.imprimeMatriz()
        break


    except:
        print("Oops, that was no valid number. Try again...")
        continue

while True:
    cont = 0
    print(" ")
    print("*************Welcome to the menu of cinema*************")
    print(' ')
    print("Choose the operation that you wish:")
    print("1-Buy the Tickets")
    print("2-Return tickets")
    print("3-Sales summary")
    print("4-Get Out")

    try:
        digiteNumero =int (input("Enter your choice: "))
        if digiteNumero > 4:
            print()
            print("Choose between the four options")
    except:
        print()
        print("Oops, that was no valid number. Try again...")
        print()
        continue


    if digiteNumero == 1:
        while True:
            try:
                compraCadeira = input("Enter yours chairs:").split(",")
                sala.compraAssento(compraCadeira)
                sala.xxSet()
                sala.imprimeMatriz()
                if type(compraCadeira) is not int:
                    break
                if compraCadeira > (sala.getLinha*sala.getColuna):
                    print()
                    print("Typer number <%d"%(sala.getLinha*sala.getColuna))
                    continue
            except:
                print()
                print("Enter a valid number")

    if digiteNumero ==2:
        while True:
            try:
                if len(sala.getListaComprada()) == 0:
                    print("")
                    print("There are no chairs to return")
                    break
                devolveAssento = input("Enter yours chairs: ").split(",")
                sala.devolverAssento(devolveAssento)
                sala.xxBack()
                sala.imprimeMatriz()
                if type(devolveAssento) is not int:
                    break
                
                if devolverAssento > (sala.getLinha*sala.getColuna):
                    print("Typer number <%d"%(sala.getLinha*sala.getColuna))
                    continue
            except:
                print("Enter a valid number")

    if digiteNumero == 3:
        sala.resumoVendas()

    if digiteNumero == 4:
        print("______________Thank you for coming__________________")
        print("______________We are wait for you again___________________")
        time.sleep(3)
        break


    sala.arquivoSalva()
