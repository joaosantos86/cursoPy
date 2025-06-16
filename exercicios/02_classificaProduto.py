
    # /*
    # PROBLEMA: CLASSIFICAÇÃO DE PRODUTO
    # Faça um script que peça para o usuário informar o código de um determinado produto e mostre a sua classificação, considerando os seguintes dados de entrada e a sua mensagem correspondente:
    # - Código 1: Alimento não-perecível
    # - Código 2, 3 ou 4: Alimento perecível
    # - Código 5 ou 6: Vestuário
    # - Código 7: Higiene Pessoal
    # - Código 8 até 15: Limpeza e Utensílios Domésticos
    # - Código 16 até 20: Outros
    # - Qualquer outro código: Código inválido
    # */


# ENTRADA
codigo = int(input("Informe o código do produto: "))

# PROCESSAMENTO E SAÍDA
if codigo == 1:
    print("Alimento não-perecível")
elif codigo == 2 or codigo == 3 or codigo == 4:
    print("Alimento perecível")
elif codigo == 5 or codigo == 6:
    print("Vestuário")
elif codigo == 7:
    print("Higiene Pessoal")
elif 8 <= codigo <= 15:
    print("Limpeza e Utensílios Domésticos")
elif 16 <= codigo <= 20:
    print("Outros")
else:
    print("Código inválido")


