# Produto parte 1 - nome do arquivo: produto.py

class Produto:

    def __init__(self, codigo, nome, preco, quantidade):
        # Atributos privados
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
        
    # --- Propriedades (Getters e Setters) ---

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter 
    def codigo(self, cod):

        if isinstance(cod, int) and cod >= 0:
            self.__codigo = cod
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):

        if isinstance(novo_preco, (float, int)) and novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: O preÃƒÂ§o deve ser um valor positivo.")


    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, nova_quantidade):

        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Erro: A quantidade deve ser um nÃƒÂºmero inteiro nÃƒÂ£o negativo.")
        

    # --- MÃƒÂ©todos de NegÃƒÂ³cio ---

    def vender(self, quantidade):
        # ValidaÃƒÂ§ÃƒÂ£o mais robusta na venda
        if not isinstance(quantidade, int) or quantidade <= 0:
            print('Erro: A quantidade de venda deve ser um nÃƒÂºmero inteiro positivo.')
            return
            
        if self.__quantidade >= quantidade:
            self.__quantidade -= quantidade
            print(f'Venda de {quantidade} unidades de {self.nome} registrada. Estoque atual: {self.__quantidade}')
        else:
            print(f'ERRO: Quantidade ({quantidade}) superior ao estoque atual ({self.__quantidade}).')



    def valor_total_estoque(self): 
        try:

            return self.__preco * self.__quantidade
             
        except Exception as e:
            # Este bloco serÃƒÂ¡ acionado se houver um erro de conversÃƒÂ£o (o que nÃƒÂ£o deve acontecer se os setters funcionarem)
            print('ERRO ao calcular valor total:', e)
            return 0.0




#  # Produto parte 1 - nome do arquivo: produto.py

# class Produto:

#     def __init__(self, codigo, nome, preco, quantidade):
#         # Atributos privados
#         self.__codigo = codigo
#         self.__nome = nome
#         self.__preco = preco
#         self.__quantidade = quantidade
        
#     # --- Propriedades (Getters e Setters) ---

#     @property
#     def codigo(self):
#         return self.__codigo
    
#     @codigo.setter 
#     def codigo(self, cod):

#         if isinstance(cod, int) and cod >= 0:
#             self.__codigo = cod
        

#     @property
#     def nome(self):
#         return self.__nome
    
#     @nome.setter
#     def nome(self, novo_nome):
#         self.__nome = novo_nome


#     @property
#     def preco(self):
#         return self.__preco
    
#     @preco.setter
#     def preco(self, novo_preco):

#         if isinstance(novo_preco, (float, int)) and novo_preco >= 0:
#             self.__preco = novo_preco
#         else:
#             print("Erro: O preço deve ser um valor positivo.")


#     @property
#     def quantidade(self):
#         return self.__quantidade
    
#     @quantidade.setter
#     def quantidade(self, nova_quantidade):

#         if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
#             self.__quantidade = nova_quantidade
#         else:
#             print("Erro: A quantidade deve ser um número inteiro não negativo.")
        

#     # --- Métodos de Negócio ---

#     def vender(self, quantidade):
#         # Validação mais robusta na venda
#         if not isinstance(quantidade, int) or quantidade <= 0:
#             print('Erro: A quantidade de venda deve ser um número inteiro positivo.')
#             return
            
#         if self.__quantidade >= quantidade:
#             self.__quantidade -= quantidade
#             print(f'Venda de {quantidade} unidades de {self.nome} registrada. Estoque atual: {self.__quantidade}')
#         else:
#             print(f'ERRO: Quantidade ({quantidade}) superior ao estoque atual ({self.__quantidade}).')



#     def valor_total_estoque(self): 
#         try:

#             return self.__preco * self.__quantidade
             
#         except Exception as e:
#             # Este bloco será acionado se houver um erro de conversão (o que não deve acontecer se os setters funcionarem)
#             print('ERRO ao calcular valor total:', e)
#             return 0.0