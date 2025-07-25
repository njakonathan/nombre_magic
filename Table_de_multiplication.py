print("BIENVENUE SUR NOTRE PROGRAMME DE TABLE DE MULTIPLICATION")

n = int(input("Table de multiplication de : "))
m = int(input("à : "))

if n > m:
    print("Nous ne pouvons pas réaliser cette multiplication !")
else:
    while n <= m:
        
        i = 1
        while i <= 12:
            print(f"{n} x {i} = {n * i}")
            i += 1
        n += 1  
        print("-----------")
