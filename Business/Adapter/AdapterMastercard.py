from models import *
from app import *

#Lucas Pimenta Santana Murta - 218083122
from ServicoAutorizaCartaoInterface import *

class AdapterMastercard(Target, Adaptee):

    def __init__(self, obj, adapted_methods):
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		return getattr(self.obj, attr)