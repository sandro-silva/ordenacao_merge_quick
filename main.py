import sys
import os
import time

from src.merge_sort import merge_sort
from src.quick_sort import quick_sort


def ler_arquivo(caminho):
    try:
        with open(caminho, 'r') as f:
            return list(map(int, f.read().split()))
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        sys.exit(1)
    except ValueError:
        print("Erro: o arquivo deve conter apenas números inteiros.")
        sys.exit(1)


def executar_algoritmo(algoritmo, arquivo):

    dados = ler_arquivo(arquivo)

    # Escolha do algoritmo
    if algoritmo == "merge":
        func = merge_sort
    elif algoritmo == "quick":
        func = quick_sort
    else:
        print("Erro: algoritmo inválido!")
        print("Use: merge ou quick")
        sys.exit(1)

    # Medição de tempo
    inicio = time.time()
    resultado = func(dados.copy())
    fim = time.time()

    print(f"\nArquivo: {arquivo}")
    print("Entrada:", dados)
    print("Saída:", resultado)
    print(f"Tempo: {fim - inicio:.6f}s")


def executar_todos(algoritmo, pasta="data"):
    print(f"\nExecutando '{algoritmo}' em todas as bases...\n")

    arquivos = sorted([
        f for f in os.listdir(pasta)
        if f.endswith(".in")
    ])

    for nome_arquivo in arquivos:
        caminho = os.path.join(pasta, nome_arquivo)
        executar_algoritmo(algoritmo, caminho)


if __name__ == "__main__":

    if len(sys.argv) == 1:
        algoritmo = "merge"  # padrão
        executar_todos(algoritmo)

    elif len(sys.argv) == 2:
        algoritmo = sys.argv[1].lower()
        executar_todos(algoritmo)

    elif len(sys.argv) == 3:
        algoritmo = sys.argv[1].lower()
        arquivo = sys.argv[2]
        executar_algoritmo(algoritmo, arquivo)

    else:
        print("Uso correto:")
        print("python main.py [merge|quick] [arquivo.in]")
        sys.exit(1)
