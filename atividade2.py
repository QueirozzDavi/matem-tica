def bissetriz_interna(AB, AC, BC):
    """
    Calcula a divisão do lado BC pela bissetriz interna do triângulo.
    
    Parâmetros:
    - AB: Lado do triângulo.
    - AC: Lado do triângulo.
    - BC: Lado do triângulo (lado oposto à bissetriz).
    
    Retorna:
    - BD: A divisão do lado BC determinada pela bissetriz interna.
    - DC: A outra divisão de BC, onde BD + DC = BC.
    """
    BD = (AB * BC) / (AB + AC)
    DC = BC - BD
    return BD, DC

def bissetriz_externa(AB, AC, BC):
    """
    Calcula a divisão do lado BC pela bissetriz externa do triângulo.
    
    Parâmetros:
    - AB: Lado do triângulo.
    - AC: Lado do triângulo.
    - BC: Lado do triângulo (lado oposto à bissetriz).
    
    Retorna:
    - BD: A divisão do lado BC determinada pela bissetriz externa.
    - DC: A outra divisão de BC, onde BD - DC = BC.
    
    Lança:
    - ValueError: Se a condição AC <= AB não for satisfeita.
    """
    if AC <= AB:
        raise ValueError("Para a bissetriz externa, AC deve ser maior que AB.")
    
    BD = (AB * BC) / (AC - AB)
    DC = BD - BC
    return BD, DC

def main():
    """
    Controla a execução do programa.
    
    Solicita ao usuário valores para os lados do triângulo e exibe as divisões
    do lado BC pelas bissetrizes interna e externa.
    """
    try:
        # Solicita a entrada dos lados
        AB = float(input("Digite o valor de AB: "))
        AC = float(input("Digite o valor de AC: "))
        BC = float(input("Digite o valor de BC: "))
        
        # Calcula a bissetriz interna
        BD_interna, DC_interna = bissetriz_interna(AB, AC, BC)
        print(f"Bissetriz Interna -> BD: {BD_interna}, DC: {DC_interna}")
        
        # Calcula a bissetriz externa e trata a exceção caso a condição não seja atendida
        try:
            BD_externa, DC_externa = bissetriz_externa(AB, AC, BC)
            print(f"Bissetriz Externa -> BD: {BD_externa}, DC: {DC_externa}")
        except ValueError as e:
            print(e)
    
    except ValueError:
        print("Erro: por favor, insira valores numéricos válidos para os lados.")

# Permite que o script seja executado diretamente
if __name__ == "__main__":
    main()
