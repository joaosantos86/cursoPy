
# // PROBLEMA: AVISO SOBRE TEMPERATURA
# // Faça um script que peça para o usuário informar o valor de uma temperatura em graus Celsius:
# // - Caso a temperatura esteja abaixo de 100 graus Celsius, o programa deverá apresentar a mensagem "Está muito baixa!";
# // - Caso a temperatura esteja até 200 graus Celsius (inclusive), deverá apresentar a mensagem "Está baixa!";
# // - Se estiver acima de 200 graus Celsius e inferior a 500 graus Celsius, deverá apresentar a mensagem "Está normal!";
# // - Contudo, caso esteja acima de 500 graus Celsius, deverá apresentar a mensagem "Está muito alta!";

# // ENTRADA

temperatura = int(input("Informe a temperatura: "))

if temperatura < 100:
    print("Está muito baixa!")
elif temperatura <= 200:
    print("Está baixa!")
elif temperatura < 500:
    print("Está normal!")
else:  # temperatura >= 500
    print("Está muito alta!")





# //PROCESSAMENTO


# //SAÍDA