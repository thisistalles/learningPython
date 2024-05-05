class CarroBrinquedo:
    def __init__(self, marca, modelo, cor, tipo):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.tipo = tipo

    def show_information(self):
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Cor: ', self.cor)
        print('Tipo: ', self.tipo)
        

print('\n')
MarioMobile = CarroBrinquedo('Shint', 'H1-1', 'Vermelho', 'Brinquedo manual')
MarioMobile.show_information()
print('\n')
RedRacer = CarroBrinquedo('FastCars', 'ThunderBolt', 'Red', 'Eletrico')
RedRacer.show_information()
print('\n')
BlueSpeedster = CarroBrinquedo('SpeedyWheels', 'BlueLightning', 'Blue', 'Eletrico')
BlueSpeedster.show_information()
print('\n')
DarkBlueThunder = CarroBrinquedo('ElectricRides', 'Supra', 'DarkBlue', 'Controle/Eletrico')