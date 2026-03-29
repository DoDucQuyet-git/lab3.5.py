# Bai 4
n = int(input("Nhap so: "))

ket_qua = []

if n % 2 == 0:
    ket_qua.append("2")

if n % 3 == 0:
    ket_qua.append("3")

if ket_qua:
    print("Chia het cho:", ", ".join(ket_qua))
else:
    print("Khong chia het cho 2 hoac 3")
