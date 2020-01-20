from view.input_nilai import input_data
data = {}

def tambah_data():
    d = input_data()
    data[d['nama']]=d

def ubah_data():
    nama = input("Masukan nama untuk mengubah data: ")
    if nama in data.keys():
        print("Masukan Data yang diubah :")
        ubah = input("(Semua), (Nama), (NIM), "
                     "(Tugas), (UTS), (UAS) : ")
        if ubah.lower() == "semua":
            print("_______________________")
            print("Ubah Data {}".format(nama))
            print("-----------------------")
            data[nama]['nim'] = input("Ubah NIM : ")
            data[nama]['tugas'] = int(input("Ubah Nilai Tugas: "))
            data[nama]['uas'] = int(input("Ubah Nilai UAS : "))
            data[nama]['uts'] = int(input("Ubah Nilai UTS : "))
        elif ubah.lower() == "nim":
            data[nama]['nim'] = input("Ubah Nim : ")
        elif ubah.lower() == "tugas":
            data[nama]['tugas'] = int(input("Ubah Nilai Tugas : "))
        elif ubah.lower() == "uts":
            data[nama]['uts'] = int(input("Ubah Nilai UTS : "))
        elif ubah.lower() == "uas":
            data[nama]['uas'] = int(input("Ubah Nilai UAS : "))

    else:
        print("'{}' Tidak Ditemukan".format(nama))
    print(data)
def hapus_data():
    nama = input("Masukan nama untuk menghapus data : ")
    if nama in data.keys():
        del data[nama]
        print("Data '{}' dihapus".format(nama))
        return True
    else:
        print("'{}' Tidak Ditemukan".format(nama))
        return False
def cari_data():
    print("Mencari Daftar Nilai : ")
    print("=======================")
    nama = input("Masukan nama untuk mencari daftar nilai : ")
    if nama in data.keys():
        print("Nama {0}, dengan NIM : {1}\n"
              "Nilai Tugas: {2}, UTS: {3}, dan UAS: {4}\n"
              "dan nilai akhir {5}".format(nama, d['nim'],
                                           d['tugas'], d['uts'],
                                           d['uas'], d['akhir']))