def media (nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3


nota1_input = float(input("Digite a nota1"))
nota2_input = float(input("Digite a nota2"))
nota3_input = float(input("Digite a nota3"))


print(f"{media(nota1_input, nota2_input, nota3_input):.1f}")
