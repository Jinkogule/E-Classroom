#Lucas Lopes do Couto- 217083106
from abc import ABC, abstractmethod

## Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass