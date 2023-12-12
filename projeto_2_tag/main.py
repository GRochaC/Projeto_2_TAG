from funcoes.ler_entrada import ler_entrada
import time
from funcoes.gale_shapley import gale_shapley
from funcoes.imprimir_saida import imprimir_saida

inicio = time.time()

print("Lendo a entrada...")
time.sleep(2)
print()
entrada = ler_entrada("entradaProj2Tag.txt")
projetos, alunos = entrada[0], entrada[1]

print("Computando...")
time.sleep(2)
print()
retorno = gale_shapley(projetos, alunos)

imprimir_saida(retorno[0], retorno[1])
print('"saidaProj2Tag.txt" gerado com sucesso.')

with open("saidaProj2Tag.txt", 'r') as saida:
    for linha in saida:
        print(linha, end = '')

fim = time.time()
print(f"\nPrograma finalizado em {fim-inicio:.2f} segundos.")