import math
import sympy as sp


def bisection(fonksiyon,fonksiyon2, iterasyon_sayisi):
   


    sonuc=2-fonksiyon(2)+fonksiyon2(2)


  

    for iterasyon in range(iterasyon_sayisi):
         print(fonksiyon(sonuc))
         print(fonksiyon2(sonuc))
         sonuc= sonuc - fonksiyon(sonuc)/fonksiyon2(sonuc)
         print(sonuc)
    return sonuc

def fonksiyon(x):
    f_x = 4 * sp.exp(-0.5 * x) - x
    return f_x

def trvFonksiyon(x_val):
     x = sp.symbols('x')
     f_x=fonksiyon(x)

     df_dx = sp.diff(f_x, x)
     trv_deger = df_dx.evalf(subs={x: x_val})
     return trv_deger
 
 
 




iterasyon_sayisi = 4

kok = bisection(fonksiyon,trvFonksiyon,iterasyon_sayisi)
print(f"Kök: {kok}")

