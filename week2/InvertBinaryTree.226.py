# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Basicamente, pensamos que a troca pode ser realizada em algumas etapas simples:
1. Acessamos um nodo
2. Verificamos o nodo que ele aponta à direita
3. Guardamos a referência desse nodo (direita)
4. A antiga referência para direita aponta para a esquerda 
5. A antiga referência para esquerda aponta para a direita (A partir da ref. guardada)
6. Aplicamos a todos os nodos
7. Retornamos o root
'''

'''
Contudo, para aplicarmos esse 'swap' nodo a nodo, iremos utilizar o DFS, em que basicamente:
1. Acessamos um nodo e realizamos uma operação
2. Enquanto existir, acessamos o nodo referenciado à esquerda (volta para o passo 1)
3. Enquanto existir, acessamos o nodo referenciado à direita (volta para o passo 1)
4. Retornamos a árvore (o root)
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left, root.right = root.rigth, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



        