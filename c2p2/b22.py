def Tao_In_DS():
    ds=list()
    for i in range(1,21):
        ds.append(i**2)
    print(ds[:5]+ds[len(ds)-5:])
Tao_In_DS()
