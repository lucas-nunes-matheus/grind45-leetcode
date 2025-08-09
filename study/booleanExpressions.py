'''
Aqui vamos elevar o nível de estudos, sendo assim:

'''

if False and Nada:
    print("Isso nunca será exibido.")
else:
    print("""O Python avalia as condições da esquerda para direita, no
            chamado 'short-circuit evaluation', sendo assim, a cláusula
            "if False and (...):" sempre será False!
            """)

if True or QueroVerVocêPegarEssa:
    print("""O mesmo acontece para as cláusulas "if True or (...)"
            que sempre retornará True!
            """)