'''
Aluno: Filipe de Freitas Lima
IP 2018.1
'''


from string import ascii_letters, digits
from pagina import * 

def filtraEmails(texto):
    ''' Recebe uma variavel string e retorna os emails válidos em uma lista
    '''
    global lista_de_emails
    lista_de_emails = []
    for pos, caract in enumerate(texto):
        if caract in caracter_inicial:
            if caract == "@":
                if (texto[pos - 1] in caracteres_aceitos) and (texto[pos + 1] in caracteres_aceitos) :
                    add_email_lista(texto, pos)
            else:
                posica = arroba_meio(texto, pos, 4)
                if posica != None:
                    add_email_lista(texto, posica)
    return lista_de_emails

def add_email_lista(texto, posicao):
    '''Recebe um email e adiciona-o na lista de emails
    '''
    email = validacao_email((agrupador(texto, posicao)))
    if email != None:
        return lista_de_emails.append(email)

def agrupador(string, posicao):
    ''' Recebe uma string e a sua posição para concatenar os emails
    '''
    global final
    comeco = email_fim_comeco(string, posicao)
    final = email_fim_comeco(string, posicao, False)
    return comeco[::-1] + "@" + final

def arroba_meio(string, posicao, n = 0):
    '''Função para descobrir o meio nas alternativas para arroba'''
    arroba = string[posicao: posicao + n]
    if (arroba == "[at]") or (arroba == "(at)"):
        return int(posicao)

def email_fim_comeco(lista, posicao, reverso = True):
    ''' Verifica se qual o começo e o final do email
    '''
    parte = ""
    while True:
        if reverso == True:
            posicao -= 1
            if lista[posicao] in caracteres_aceitos:
                parte += lista[posicao]
            else:
                break
        else:
            posicao += 1
            if lista[posicao + 3] in caracteres_aceitos:
                parte += lista[posicao + 3]
            else:
                break
    return parte

def validacao_email(email):
    ''' Essa função verifica se o email tem mais do que um @ e se tem pelo menos um ponto na parte direita do @.
    '''
    if len(email) > 1:
        if "." in final:
            return email

# Variaveis

caracter_inicial = "@[("
shp = "_-."
caracteres_aceitos = digits + ascii_letters + shp
strPagina += "\nFinal"

# Chamando função abaixo daqui

print(filtraEmails(strPagina))