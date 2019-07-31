def tower_builder(x):
    z=''
    for item in range(0,6):
        for item1 in range(0,10-item*2):
            z+='   '
        for item2 in range(1,item*2+1):
            z+=' * '
        for item3 in range(0,item*2):
            z+=' * '
        z+='\n'
    print(z)
tower_builder(23)

