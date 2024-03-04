import modules.stock as stk
if __name__ == '__main__':
    def mnu():
        print("""
            
            Gention de inventario
                        
            1.Registro de productos
            2.Visualizar productos
            3.Actualizar stock
            4.Actualizar precios
            5.Informe de productos criticos
            6.Calculo de ganancia potencial
            7.Salir
            
            
            """)
        menu = input()
        match menu:
            case '1':
                stk.rgstPrdcs()
            case '2':
                stk.show()
            case '3':
                stk.updtStk()
            case '4':
                stk.updtVl()
            case '5':
                stk.shwCrt()
            case '6':
                stk.calcPtnc()
            case '7':
                exit()
            case _:
                print('El numero indicado no coincide')
                input()
                
    while True:
        mnu()

            