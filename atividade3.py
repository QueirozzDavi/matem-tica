from itertools import product

# Funções para as condições lógicas
def cond1(P, Q):
    return not P or Q  # P -> Q

def cond2(P, Q, R):
    return not (P or Q) or R  # (P ∨ Q) -> R

def cond3(P, M, R):
    return not P or (not M or R)  # ¬P -> (M -> R)

# Gera a tabela verdade
def gerar_tabela():
    print(f"{'P':<5}{'Q':<5}{'M':<5}{'R':<5}{'C1':<5}{'C2':<5}{'C3':<5}{'Resultado'}")
    for P, Q, M, R in product([True, False], repeat=4):
        # Avaliação das condições
        c1 = cond1(P, Q)
        c2 = cond2(P, Q, R)
        c3 = cond3(P, M, R)
        resultado = c1 and c2 and c3
        print(f"{P:<5}{Q:<5}{M:<5}{R:<5}{c1:<5}{c2:<5}{c3:<5}{resultado}")

# Executa a função para imprimir a tabela verdade
gerar_tabela()
