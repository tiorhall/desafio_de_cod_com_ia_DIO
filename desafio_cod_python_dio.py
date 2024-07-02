import re

def analyze_sentiment():
    # Entrada do usuário
    comentario = input("Digite seu comentário: ")

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    # Verificação do sentimento com base nas contagens de palavras
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    elif count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    elif count_neutro > count_positivo and count_neutro > count_negativo:
        return "Neutro"
    else:
        return "Misto"  # Caso tenha uma combinação de sentimentos

# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)
