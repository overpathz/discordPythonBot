class DSUser:
    def __init__(self, name):
        self.name = name
        self.lockdown = 10

    def minusTime(self):
        self.lockdown -= 1

    def get_name(self):
        return str(self.name)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'
