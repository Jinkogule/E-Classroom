from PedidoManager import *

#Daniel Fernandes Pereira - 217083085
class PagamentoHandle(db.Model):
   
    
    def VerificarPagamento(chavePedido):
        
        #Chamada para o a instituicao de pagamento
        print("Verificando Pagamento...")

        if(true):
            nextHandle(chavePedido)
        else:
            return print("O pedido nao esta disponivel")

        return 


    def nextHandle(chavePedido):

        PedidoManager.ConcluirPedido(chavePedido)
        
        return