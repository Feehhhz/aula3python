carro = {"Marca": "Ford",
          "Modelo": "Ka",
          "Ano": 2020,
          "Cor": "Cinza"
}
if "cor" in carro:
    carro["cor"] = "Preto"
else:
    del carro["ano"]

print(carro)