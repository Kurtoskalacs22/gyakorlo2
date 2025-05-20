nev = input("Kérem adja meg Anna mire gyűjti a pénzt: ")
szam = int(input("Kérem adja meg hány kutyát sétáltat: "))

ora = (szam * 20)//60
perc =(szam * 20)%60
bevetel = 700*szam
if bevetel >= 5000:
   print(f"Anna {szam} kutyát sétáltatott {ora}:{perc} alatt, ezért {bevetel} Ft-ot kapott. Ez elég a {nev} árához.")
else:
    print(f"Anna {szam} kutyát sétáltatott {ora}:{perc} alatt, ezért {bevetel} Ft-ot kapott. Ez nem elég a {nev} árához.")