#Lucas Pimenta Santana Murta - 218083122
class ServicoMastercard(object):
	def __init__(self, numero, data):
		self.numero = numero
        self.data = data

	def atualiza(self, numero, data):
		return