# TODO: Crie uma Tuncao: recomendar plano para receber o consumo medio mensal:
def recomendar_plano(consumo):

    if consumo <= 10:
        return "Plano Essencial Fibra - 5@Mbps"
    elif consumo > 10 and consumo < 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"


# TODO: Crie uma estrutura condicional para verificar o consumo médio mensal:
def solicitar_consumo():
    while True:
        try:
            consumo = float(input(f"Informe o consumo de dados mensal(em Gigabytes): "))
            if consumo >= 0:
                return consumo
            else:
                print("o consumo médio mensal deve ser um valor néo negativo.")
        except ValueError:
            print("Por favor, insira um valor numérico valido.")


planos = [
    (10, "Plano Essencial Fibra - 50Mbps"),
    (20, "Plano Prata Fibra - 100Mbps"),
    (float("inf"), "Plano Premium Fibra - 300Mbps"),
]

consumo = solicitar_consumo()

for limite, plano in planos:
    if consumo <= limite:
        plano_recomendado = plano
        break

print(plano_recomendado)
