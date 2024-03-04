import module.tabletennis as tt
if __name__ == '__main__':
    def mnu():
        print("""
            
            Registro de Torneo de tenis de mesa
            
            1.Registrar jugador
            2.Registrar partido
            3.mostrar estado categoria
            4.mostrar participante
            5.Ganador por categoria
            6.Salir 
            7.print
            
            
            """)
        menu = input()
        match menu:
            case '1':
                tt.rgstPlyr()
            case '2':
                tt.rgstMtch()
            case '3':
                tt.shwCtgry()
            case '4':
                tt.shwPrtcpnt()
            case '5':
                tt.wnnr()
            case '6':
                exit()
            case '7':
                print(tt.scores)
            case _:
                print('El numero indicado no coincide')
                input()
    while True:
        mnu() 