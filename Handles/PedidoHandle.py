from PagamentoHandle import *

#Daniel Fernandes Pereira - 217083085
class PedidoHandle(db.Model):
   

    def VerificarDisponibilidade(chavePedido):
        
        #Chamada para a model de produtos
        print("Verificando disponibilidade do Pedido")

        if(true):
            nextPagamentoHandle(chavePedido)
        else:
            return print("O pedido nao esta disponivel")

        return 


    def nextPagamentoHandle(chavePedido):

        PagamentoHandle.VerificarPagamento(chavePedido)
        
        return