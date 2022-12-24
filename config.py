# i want to use a class for all the global variables
class Configs:
    def __init__(self, is_prod) -> None:
        self.init(is_prod)

    def init(self, is_prod):
        self.is_prod = is_prod
        if self.is_prod:
            self.client_id = 100
        else:
            self.client_id = 300
