import csv
flag = True
from random import randint
diente = 0
while flag == True:
    with open("Zonas.csv","r",encoding="latin-1") as file:
        heading = next(file)
        file_reader = csv.reader(file)
        print ("Las zonas donde puedes registrar sismos son: \n")
        temp = []
        temp2 = []
        for a in file_reader:
            if a[1] not in temp:
                temp.append(a[1])
            temp2.append(a)
        for a in temp:
            print (f"Zona {a}")
        if diente == 0:
            opt1 = input("\n¿ Deseas continuar ? 1(si) / 2(no): ")
            diente += 1
        if diente == 2:
            flag = False
            break
        opt = input("\nElige una zona\nCual zona escoges: ")
        print ("\nDe la zona escogida están: \n")
        opt = opt.lower()
        temp3= []
        for a in temp2:
            a[1]=a[1].lower()
            if a[1] == opt:
                print(a[0])
                temp3.append(a[0])
                temp3.append(str(randint(1,9)))
                temp3.append(str(randint(1,9)))
                temp3.append(str(randint(1,9)))
        print ("")
        contador = 0
        temp4= 0
        for check in temp3:
            if check[0] in ["0","1","2","3","4","5","6","7","8","9"] and contador<4:
                if float(check)>temp4:
                    temp4=float(check)
                contador+=1
            else:
                print (f"El mayor sismo de {check} fué de: ",end="")
            if contador == 3:
                print (temp4)
                temp4 = 0
                contador = 0
        opt1 = input("\n¿ Deseas continuar ? 1(si) / 2(no): ")
        if opt1 == "2":
            flag = False
            break
        temp4 = 0
        contador = 0




