#João Vitor Gregorini
#obs: o código transoforma automaticamente todas as letras em
#letras maiuscula
#O nome do arquivo txt deve ser digitado sem a extensão .txt
import sys
import re
#Funções
def erro():
    print("Erro na leitura do arquivo")
    print("Saindo....")
    sys.exit()

    #Código operações
def Uniao(A, B):
    result = []
    for a in range(0, len(A)):
        result.append(A[a])
    for u in range(0, len(B)):
        if B[u] not in result:
            result.append(B[u])
    return result

def Inter(A, B):
    aux = []
    result = []
    for a in range(0, len(A)):
        aux.append(A[a])
    for i in range(0, len(B)):
        if B[i] in aux:
            result.append(B[i])

    return result

def Difer(A, B):
    result = []
    for a in range(0, len(A)):
        if A[a] not in B:
            result.append(A[a])

    return result

def Pvetorial(A, B):
    result = []
    aux = ""
    for a in range(0, len(A)):
        result.append([])
        for b in range(0, len(B)):
            aux = str(A[a]) + str(B[b])
            result[a].append(aux)

    return result

#Abrir o arquivo
url = "txt/"
url += str(input("Digite o nome do arquivo txt: ")) + ".txt"
try:
    linha = open(url)
    linha = linha.readlines()
except:
    erro()
#Separar os dados
mat = []
for i in range(0, len(linha)):
    mat.append([])
    aux = linha[i].strip("\n")
    aux = aux.split(",")
    for j in range(0, len(aux)):
        mat[i].append(aux[j])

for l in range(0, len(mat)):
    for c in range(0, len(mat[l])):
        mat[l][c] = mat[l][c].strip()
        mat[l][c] = mat[l][c].upper()

#Reconhecer as operações
try:
    n = int(mat[0][0])
except:
    erro()

for o in range(1, n * 3, 3):
    print("---------------------------------------------------------------")
    op = mat[o][0]
    A, B = mat[o + 1], mat[o + 2]

    if op == "U":
        res = Uniao(A, B)
        A, B, res = str(A)[1:-1], str(B)[1:-1], str(res)[1:-1]
        A = re.sub("\'", "", A)
        B = re.sub("\'", "", B)
        res = re.sub("\'", "", res)
        print("União: conjunto 1 {", A, "}, conjunto 2 {", B,"}. Resultado: {", res, "}")

    elif op == "I":
        res = Inter(A, B)
        A, B, res = str(A)[1:-1], str(B)[1:-1], str(res)[1:-1]
        A = re.sub("\'", "", A)
        B = re.sub("\'", "", B)
        res = re.sub("\'", "", res)
        print("Intersecção: conjunto 1 {", A, "}, conjunto 2 {", B,"}. Resultado: {", res, "}")

    elif op == "D":
        res = Difer(A, B)
        A, B, res = str(A)[1:-1], str(B)[1:-1], str(res)[1:-1]
        A = re.sub("\'", "", A)
        B = re.sub("\'", "", B)
        res = re.sub("\'", "", res)

        print("Diferenciação: conjunto 1 {", A, "}, conjunto 2 {", B,"}. Resultado: {", res, "}")

    elif op == "C":
        res = Pvetorial(A, B)
        A, B, res = str(A)[1:-1], str(B)[1:-1], str(res)[1:-1]
        A = re.sub("\'", "", A)
        B = re.sub("\'", "", B)
        res = re.sub("\'", "", res)
        print("Produto Cartesiano: conjunto 1 {", A, "}, conjunto 2 {", B,"}.\nResultado: {", res, "}")

    else:
        erro()

    print()
