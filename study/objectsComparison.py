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