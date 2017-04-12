class Pokemon:
    def __init__(self,specieIN, dexIN,catchrateIn):
        self.specie = specieIN
        self.dex = dexIN
        self.catchrate = catchrateIn
        self.probability = min((self.catchrate+1), 151) / 449.5

    def __str__ (self):
        s = self.specie
        return s
p = Pokemon("Pikachu", 5,55)
print(p)
print(p.probability)
