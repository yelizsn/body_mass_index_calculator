kisi=input('Adınız:')
kullanici_boy  = float(input('Metre cinsinden boyunuz kaç:'))
kullanici_kilo = float(input('Kilogram cinsinden kilonuz nedir:'))

vki = round (kullanici_kilo / kullanici_boy ** 2)
if (vki > 0) and (vki < 18.4):
   print(kisi+' '+f"Vücut kitle indeksin: {vki}, zayıfsınız")
elif (vki > 18.4) and (vki <= 24.9):
   print(kisi+' '+f"Vücut kitle indeksin: {vki}, kilonuz normal")
elif (vki > 24.9) and (vki <=29.9):
   print(kisi+' '+f"Vücut kitle indeksin: {vki}, kilonuz biraz fazla")
elif (vki > 29.9) and (vki <=34.9):
   print(kisi+' '+f"Vücut kitle indeksin: {vki}, 1. derece obezsiniz")
elif (vki > 34.9) and (vki <=39.9):
   print(kisi+' '+f"Vücut kitle indeksin: {vki}, 2. derece obezsiniz")
else:
   print(kisi+' '+f"Vücut kitle indeksin: {vki}, 3. derece obezsiniz.")