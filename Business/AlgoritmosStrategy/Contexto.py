#Lucas Lopes do Couto- 217083106
class Contexto:
    strategy: Strategy  ## the strategy interface

    def setStrategy(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def executeStrategy(self) -> str:
        print(self.strategy.execute())