from model.daftar_nilai import data

def cetak (data = {}):
    print("===================================================================")
    print("| NO |    NIM    |      NAMA      | TUGAS |  UAS  |  UTS  | AKHIR |")
    print("===================================================================")
    if len(data) <= 0:
        print ("===========================BELUM ADA DATA==========================")
    else:
        no = 1
        for x in data.values():
            print("| {0:2} | {1:9} | {2:14} | {3:5} | {4:5} | {5:5} | {6:5.2f} |".format
                (no,x['nim'],x['nama'],x['tugas'],
                x['uas'],x['uts'],float(x['akhir'])))
            no += 1
        print("===================================================================")

def search():
    print("Mencari Daftar Nilai : ")
    print("=======================")
    nama = input("Masukan nama untuk mencari daftar nilai : ")
    if nama in data.keys():
        print("Nama {0}, dengan NIM : {1}\n"
              "Nilai Tugas: {2}, UTS: {3}, dan UAS: {4}\n"
              "dan nilai akhir {5}".format(nama, data[nama]['nim'],
                                           data[nama]['tugas'], data[nama]['uts'],
                                           data[nama]['uas'], data[nama]['akhir']))
    else:
        print("'{}' Tidak ditemukan".format(nama))