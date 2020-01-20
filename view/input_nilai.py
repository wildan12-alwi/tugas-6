# menginput data

def input_data():
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = int(input ("Nilai Tugas : "))
    uas = int(input("Nilai UAS : "))
    uts = int(input("Nilai UTS : "))
    a = tugas * 30 / 100
    b = uas * 35 / 100
    c = uts * 35 /100
    akhir = a + b + c


    return {'nim':nim,
            'nama':nama,
            'tugas':tugas,
            'uas':uas,
            'uts':uts,
            'akhir':akhir
            }