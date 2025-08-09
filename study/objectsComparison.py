# class ClassC:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# obj3 = ClassC(10, 20)
# obj4 = ClassC(10, 20)

# print(obj3 == obj4) # False

class ClassC:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Agora vamos testar novamente
obj3 = ClassC(10, 20)
obj4 = ClassC(10, 20)

print(obj3 == obj4) # True

# Detalhe: alterar o método __eq__ para mudar o comportamento do python \
# ao usar '==' só funciona para comparação de objetos da mesma classe

# =========
# Anotações
# =========

'''
None em Python é um Objeto

Só existe um único objeto None em Python, sendo assim, todas as variáveis 
com o valor None apontam (fazem referência) para o mesmo objeto  

Embora a comparação com None possa ser feita com os operadores "==" e "is",
a PEP recomenda que seja usado o comparador "is" para verificar a identidade

Sendo assim, comparar objetos com None exige cuidado, considerando:
if ObjetoSendoComparado.valor is None:
    return True

Pode possivelmente retornar um 'AttributeError', pois se o 
'ObjetoSendoComparado' apontar para None, o objeto None não possuirá o
atributo '.valor', portanto, erro de atributo

O mais correto é comparar o objeto com None, sendo assim:
if ObjetoSendoComparado is None:
    return True
'''