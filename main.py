# Crie uma função chamada media que receberá três números como argumentos. Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

def media (nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3


nota1_input = float(input("Digite a nota1"))
nota2_input = float(input("Digite a nota2"))
nota3_input = float(input("Digite a nota3"))

print(f"{media(nota1_input, nota2_input, nota3_input):.1f}")