import modules.consume as cns
if __name__ == '__main__':
    def mnu():
        print("""
            
            Registro de consumo electrico
            
            1.Registrar dependencia
            2.Registrar consumo
            3.Ver CO2 producido
            4.Dependencia que mas CO2 produce
            5.Salir 
            
            
            """)
        menu = input()
        match menu:
            case '1':
                cns.rgstDpncy()
            case '2':
                Cnsm(cns.show())
            case '3':
                cns.lkCO2()
            case '4':
                cns.hghstCnsm()
            case '5':
                exit()
            case _:
                print('El numero indicado no coincide')
                input()
                
    def Cnsm(i):
        print("""
            
            Registro consumo por dependencia
            
            1.Consumo base
            2.Consumo por vehiculo
            3.Consumo por dispositivo
            4.Regresar
            
            
            """)
        menu = input()
        match menu:
            case '1':
                print('si')
                cns.rgstCnsm(1,i)
            case '2':
                cns.rgstCnsm(2,i)
            case '3':
                cns.rgstCnsm(3,i)
            case '4':
                mnu()
            case _:
                print('El numero indicado no coincide')
                input()
        
    while True:
        mnu()

            