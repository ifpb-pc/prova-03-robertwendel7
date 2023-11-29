def q1(cidades):
    
    mais_de_100 = []
    
    for cidade, idade in cidades.items():
        if idade > 100:
            mais_de_100.append(cidade)
        
    return mais_de_100

    

def q2(lista1, lista2):
    
    soma_listas = lista1 + lista2
    total = 0
    nova_lista = []
    for valor in soma_listas:
        if valor > 0:
            total += valor
            nova_lista.append(valor)

    lista_ordenada = sorted(nova_lista)
    
    
    
    return total, lista_ordenada

    

def q3(valores):
    return [],[]

def q4(valores):
    return []

def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    main()


