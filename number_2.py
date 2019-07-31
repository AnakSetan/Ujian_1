def expandedForm(num):
    num = int (input('Angka :'))
    satuan = round(num*1)
    puluhan= round(satuan*10)
    ratusan = round (puluhan*10)
    ribuan = round (ratusan*10)
    print ('Angka : '+str(satuan)+'+'+str(puluhan)+'+'+str(ratusan)+'+'+str(ribuan))
expandedForm(11)


