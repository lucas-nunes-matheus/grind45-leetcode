# Notas

### Divisão
Notação: a / b = c, typeof(c) -> float

O resultado do quociente ('c') sempre será um float.

### Floor division (divisão inteira)
Notação: a // b = c, typeof(c) -> int

O resultado sempre será um inteiro, menor ou igual ao resultado do quociente da divisão comum.

### Booleanos
Valores: True or False
Actually: (1) or (0) 

True and False -> True
True or False -> False
True + True -> 2
1 > False -> True

### Comparadores
Igualdade de valor: == (ou Diferença: !=)
--> Compara se o valor de duas variáveis são iguais

Igualdade de referência: is (ou Diferença: is not)
--> Compara se duas variáveis são (ou referenciam) o mesmo objeto

Ex.:
```python
# Atribuição de uma lista
a = [1, 2, 3]
# 'b' referencia a mesma lista que 'a'
b = a

# a == b -> True
# a is b -> True

# Nova atribuição para 'b'
b = [1, 2, 3]

# a == b -> True, mesmo valor de 'a'
# a is b -> False, referencia um objeto diferente de 'a'
```