def classificar_consumo():
    print("💧 Sistema de Classificação de Consumo de Água 💧\n")
    
    # Solicita o tipo de imóvel e padroniza o texto para letras minúsculas
    tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
    
    # Valida se a entrada do consumo é um número válido
    try:
        consumo = float(input("Digite o consumo mensal de água (em m³): "))
    except ValueError:
        print("Erro: Por favor, insira um número decimal válido (ex: 15.5).")
        return

    # Lógica de classificação baseada nas regras de negócio
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
        
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
        
    elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
        
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

# Executa o programa
if __name__ == "__main__":
    classificar_consumo()