import modules.sismo as ss
if __name__ == '__main__':
    def mnu():
        print("""
            
            Registro de sismos
            
            1.Registrar ciudad
            2.Registrar Sismo
            3.Buscar sismos por cuidad
            4.Informe de riesgo
            5.Salir 
            
            
            """)
        menu = input()
        match menu:
            case '1':
                ss.rgstCty()
            case '2':
                ss.rgstSsm()
            case '3':
                ss.srchSsm()
            case '4':
                ss.evalCty()
            case '5':
                exit()
            case _:
                print('El numero indicado no coincide')
                input()
    
    while True:
        mnu()

            