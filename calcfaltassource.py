import time 
def menu():
    print('[1] Calcular com dias inteiros :')
    print('[2] Calcular com atrasos:')
    print('[0] Sair do Programa')

menu()
option = int(input('o que vc deseja fazer ?: '))

#loop que comanda o menu
while option != 0:
    #primeira opção do menu é executada, pede o numero de horas do modulo e o numero de dias faltados, calcula as faltas restantes.
    if option  == 1:
        HrTotal = float((input('quantas horas tem o modulo ?: ')))
        Falt = float((input('quantos dias vc faltou ? : ')))
        
        if HrTotal and Falt < 0 :
            print('Numero invalido, coloque valor positivo.')
            time.sleep(1)
            quit
        
        else:
                HorasPorFalta = float (HrTotal / 4)
                DiasPorFalta =  float (HorasPorFalta / 3)
                FaltFinal = float (DiasPorFalta - Falt)
                if DiasPorFalta < Falt:
                    
                    print('vc ja excedeu o limite de faltas.')
                    time.sleep(1)
                    quit
                else:
                    
                    print('Vc pode faltar {} dias ainda' .format(int(FaltFinal)))
                    time.sleep(5)
                    quit
    
    #opção 2 do menu, pede as horas, faltas e atrasos 
    elif option  == 2:
        
        HrTotal = float((input('quantas horas tem o modulo ?: ')))
        Falt = float((input('quantos dias vc faltou ? : ')))
        Atraso = float(input('quantas vezes você se atrasou ?: '))
        
        if HrTotal and Falt and Atraso < 0:
            
            print ('Numero invalido, Por favor use valores positivos')
            time.sleep(2)
            quit
        
        else:
            HorasPorFalta = HrTotal / 4
            DiasPorFalta = HorasPorFalta / 3
            FaltasFinal = float( DiasPorFalta - Falt - Atraso)
            
            if DiasPorFalta < Falt:
                
                print('Vc ja excedeu o limite de faltas')
                time.sleep(2)
                quit
            
            else :
                print ('vc pode faltar {} vezes ainda' .format(int(FaltasFinal)))
                time.sleep(2)
                quit
           

    #checa opção invalida 
    else:
        print('invalido.')
    menu()
    option = int(input('o que vc deseja fazer ?:'))
print('Obrigado por usar o Programa!')
time.sleep(2)