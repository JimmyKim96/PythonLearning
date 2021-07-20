#coding-utf8
#this file is samples for .lower .upper .swapcase .zfill


infoa = 'MtFk You SoB!'
infob = 'nmsl1024Times'

l_infoa = infoa.lower()
l_infob = infob.casefold()

print(l_infoa, l_infob)

U_infoa = infoa.upper()
U_infob = infob.upper()

print(U_infoa,U_infob)

swap_infoa = infoa.swapcase()
swap_infob = infob.swapcase()

print(swap_infoa,swap_infob)

Asample = infoa.zfill(25)

print(Asample)