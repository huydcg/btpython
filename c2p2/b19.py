with open("d:\\VKU\\42\\Lập trình Python\\btpython\\c2p2\\b19.txt", "r", encoding="utf-8") as ftext:
    tu_dien_cac_tu = {}
    for dong in ftext:
        danh_sach_tu = dong.split()
        for tu in danh_sach_tu:
            tu_dien_cac_tu[tu] = tu_dien_cac_tu.get(tu, 0) + 1

print(tu_dien_cac_tu)

danh_sach = []
for khoa, gia_tri in tu_dien_cac_tu.items():
    newtup = (gia_tri, khoa)
    danh_sach.append(newtup)

print(danh_sach)

danh_sach = sorted(danh_sach, reverse=True)

for gia_tri, khoa in danh_sach[:10]:
    print(khoa, gia_tri)