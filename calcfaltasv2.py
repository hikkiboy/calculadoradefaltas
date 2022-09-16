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
            FaltasMax = HorasPorFalta / 3
            DiasPorFalta = HorasPorFalta / 3
            ConverteDias =  (Atraso / 3)
            FaltasFinal = float( FaltasMax - Falt - ConverteDias)
            SobraHoras = float ( Atraso % 3 )
            SobraAulas = int (Atraso / 3)
            SobraHoraemDia = int ( SobraHoras / 3 ) 

            if isinstance ( ConverteDias, float):
                AulasMax =  int (SobraHoraemDia + FaltasFinal)
                Sobrasparte1 = int (FaltasMax - AulasMax)
                if DiasPorFalta < Falt:
                    print('Vc ja excedeu o limite de faltas')
                    time.sleep(2)
                    quit
                else:
                    print('você pode faltar {} dias e atrasar {} horas' .format(AulasMax, SobraHoras))
                    time.sleep(3)
            else:
                quit
           

    #checa opção invalida 
    else:
        print('invalido.')
    menu()
    option = int(input('o que vc deseja fazer ?:'))
print('Obrigado por usar o Programa!')
time.sleep(2)
