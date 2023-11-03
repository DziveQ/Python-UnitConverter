def landing():
    print('1: KM/Mil')
    print('2: CM/Feet')
    print('3: KG/Pounds')
    valg = int(input('Velg:'))
    match valg:
        case 1:
            kmMil()
        case 2:
            cmFeet()
        case 3:
            kgPound()


def kmMil():
    valg = int(input('Vil du regne KM til Mil (Velg 1) eller Mil til KM (Velg 2): '))
    match valg:
        case 1:
            km = float(input('Skriv lengde i KM: '))
            mil = round(km*0.62137119,2)
            print(km,'Km er lik',mil,'Mil')

        case 2:
            mil = float(input('Skriv lenge i Mil: '))
            km = round(mil*1.60934,2)
            print(mil,'Mil er lik',km,'Km')

def cmFeet():
    valg = int(input('Vil du regne CM til Feet (Velg 1) eller Feet til CM (Velg 2): '))
    match valg():
        case 1:
            cm = float(input('Skriv lengde i CM: '))
            feet = round(cm*0.0328084,2)
            print(cm,'CM er lik',feet,'Feet')

        case 2:
            feet = float(input('Skriv lengde i Feet: '))
            cm = round(feet*30.48, 2)
            print(feet,'Feet er lik ',cm,'CM')

def kgPound():
    valg = int(input('Vil du regne Kilogram til Pounds (Velg 1) eller Pounds til Kilogram (Velg 2): '))
    match valg:
        case 1:
            kg = float(input('Skriv vekt i Kilogram: '))
            pound = round(kg*2.20462, 2)
            print(kg,' KG er lik', pound,'LBS')

        case 2:
            pound = float(input('Skriv lengde i Feet: '))
            kg = round(pound*0.453592,2)
            print(pound,'LBS er like',kg,'KG')

landing()