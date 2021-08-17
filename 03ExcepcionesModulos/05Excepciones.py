def suma(a,b):
    try:
        #print(x)
        resultado  = int(a) + int(b)
        return resultado
    except ValueError:
        print("No puedo convertir lo que me diste")
        return 0
    except:
        print("Algo salio muy mal")
        return 0
    finally:
        print("Finalmente")

print(suma(10,20))
print(suma(10, "a"))
print(suma(10, []))