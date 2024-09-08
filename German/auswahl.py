from fall1 import *
from fall2 import *

def degrees_to_gon(deg):
    return deg * 10 / 9

def radians_to_gon(rad):
    return degrees_to_gon(degrees(rad))

#Fall suche
def berechnung(a, b, c, alpha, beta, gamma, einheit):
    if a > 0 and b > 0 and c > 0:
        return fall_1(a, b, c)
    elif a > 0 and b > 0 and alpha > 0:
        return fall_2(a, b, alpha)
    elif a > 0 and b > 0 and beta > 0:
        return fall_3(a, b, beta)
    elif a > 0 and c > 0 and alpha > 0:
        return fall_4(a, c, alpha)
    elif a > 0 and c > 0 and gamma > 0:
        return fall_5(a, c, gamma)
    elif b > 0 and c > 0 and beta > 0:
        return fall_6(b, c, beta)
    elif b > 0 and c > 0 and gamma > 0:
        return fall_7(b, c, gamma)
    elif a > 0 and b > 0 and gamma > 0:
        return fall_8(a, b, gamma)
    elif a > 0 and c > 0 and beta > 0:
        return fall_9(a, c, beta)
    elif b > 0 and c > 0 and alpha > 0:
        return fall_10(b, c, alpha)
    elif a > 0 and alpha > 0 and beta > 0:
        return fall_11(a, alpha, beta)
    elif a > 0 and alpha > 0 and gamma > 0:
        return fall_12(a, alpha, gamma)
    elif a > 0 and beta > 0 and gamma > 0:
        return fall_13(a, beta, gamma)
    elif b > 0 and alpha > 0 and beta > 0:
        return fall_14(b, alpha, beta)
    elif b > 0 and alpha > 0 and gamma > 0:
        return fall_15(b, alpha, gamma)
    elif b > 0 and beta > 0 and gamma > 0:
        return fall_16(b, beta, gamma)
    elif c > 0 and alpha > 0 and beta > 0:
        return fall_17(c, alpha, beta)
    elif c > 0 and alpha > 0 and gamma > 0:
        return fall_18(c, alpha, gamma)
    elif c > 0 and beta > 0 and gamma > 0:
        return fall_19(c, beta, gamma)
    else:
        raise ValueError("Kein gueltiger Fall gefanden.")

def neue_berechnung():
    # Einheit auswählen
    print("Waehle die Einheit\nfuer die Winkel:")
    print("1: Grad (°)")
    print("2: Gon")
    einheit = int(input("Auswahl: "))

    if einheit == 1:
        einheit_text = "Grad"
    elif einheit == 2:
        einheit_text = "Gon"
    else:
        raise ValueError("Waehle 1 oder 2.")

    # Benutzer zur Eingabe
    print("Gebe die bekannten\nGroessen ein:")
    a = input("Seite a: ")
    b = input("Seite b: ")
    c = input("Seite c: ")
    alpha = input("alpha: ")
    beta = input("beta: ")
    gamma = input("gamma: ")

    # Umwandlung der Eingaben in Float, wenn vorhanden und nicht 0
    a = float(a) if a and float(a) != 0 else 0
    b = float(b) if b and float(b) != 0 else 0
    c = float(c) if c and float(c) != 0 else 0
    alpha = float(alpha) if alpha and float(alpha) != 0 else 0
    beta = float(beta) if beta and float(beta) != 0 else 0
    gamma = float(gamma) if gamma and float(gamma) != 0 else 0

    # Umwandlung von Gon in Grad
    if einheit == 2:
        alpha = alpha * 9 / 10
        beta = beta * 9 / 10
        gamma = gamma * 9 / 10

    # Berechnung
    result = berechnung(a, b, c, alpha, beta, gamma, einheit)

    # Ergebnis anzeigen
    if isinstance(result, tuple):
        a, b, c, alpha, beta, gamma, area = result
        alpha_gon = degrees_to_gon(alpha)
        beta_gon = degrees_to_gon(beta)
        gamma_gon = degrees_to_gon(gamma)
        
        print("Seite a:{:.4f}".format(a))
        print("Seite b:{:.4f}".format(b))
        print("Seite c:{:.4f}".format(c))
        print("a: {:.4f} {:.4f}".format(alpha, alpha_gon))
        print("b: {:.4f} {:.4f}".format(beta, beta_gon))
        print("g: {:.4f} {:.4f}".format(gamma, gamma_gon))
        
        flaeche_anzeigen = input("Flaecheninhalt?")
        if flaeche_anzeigen == '1':
            print("Flaeche: {:.4f}".format(area))
    else:
        print(result)

#Schleife der Berechnung
while True:
    neue_berechnung()
    weiter = input("Weiter rechnen? (ja=1/nein=0): ")
    if weiter != '1':
        break
