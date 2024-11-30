mata_kuliah = {
    "SI101": {"nama": "Algoritma Pemrograman", "sks": 4},
    "SI102": {"nama": "Logika Engineering", "sks": 4},
    "SI103": {"nama": "Statistika", "sks": 4},
    "SI104": {"nama": "PTIK", "sks": 3},
    "SI105": {"nama": "Keterampilan Interpersonal", "sks": 3},
    "SI106": {"nama": "Manajemen Organisasi", "sks": 3},
    "SI107": {"nama": "Pancasila", "sks": 2}
}

maksimal_sks = 20
pilihan_mahasiswa = {}
data_mahasiswa = {}

def tampilkan_mata_kuliah():
    print("==== Daftar Mata Kuliah: ====")
    print(f"{"Kode"} | {"Nama"} | {"SKS"}")
    print("==============================")
    for kode, info in mata_kuliah.items():
        print(f"{kode} | {info["nama"]} | {info["sks"]}")
print()

def hitung_total_sks(daftar_pilihan):
    total_sks = 0 
    for kode in daftar_pilihan: 
        if kode in mata_kuliah: 
            total_sks += mata_kuliah[kode]["sks"]
    return total_sks
print()

def pilih_mata_kuliah(nim):

    daftar_pilihan = pilihan_mahasiswa[nim]
    print(f"=== Memilih Mata Kuliah untuk Mahasiswa: {data_mahasiswa[nim]} ===")

    while True:
        tampilkan_mata_kuliah()
        kode = input("Masukkan kode mata kuliah yang ingin dipilih (atau ketik 'selesai' untuk menyimpan): ")
        if kode == "selesai":
            break
        if kode not in mata_kuliah:
            print("Kode mata kuliah tidak valid. Silakan coba lagi")
            print()
            continue
        if kode in daftar_pilihan:
            print("mata kuliah ini sudah dipilih")
            print()
            continue

        daftar_pilihan.append(kode)
        total_sks = hitung_total_sks(daftar_pilihan)

        if total_sks > maksimal_sks:
            print(f"Total SKS ({total_sks}) melebihi batas maksimum ({maksimal_sks}) mata kuliah tidak ditambahkan")
            daftar_pilihan.remove(kode)
            print()
        else:
            print(f"Mata kuliah {kode} berhasil ditambahkan Total SKS saat ini: {total_sks}")
            print()

    pilihan_mahasiswa[nim] = daftar_pilihan
    print(f"pilihan mata kuliah untuk {data_mahasiswa[nim]} berhasil disimpan.")
print()

def tampilkan_pilihan_mahasiswa(nim):
    print()
    daftar_pilihan = pilihan_mahasiswa[nim]
    if not daftar_pilihan:
        print("Anda belum memilih mata kuliah.")
        return

    print(f"==== pilihan Mata Kuliah yang sudah di simpan {data_mahasiswa[nim]}: ====")
    total_sks = hitung_total_sks(daftar_pilihan)
    print(f"Total SKS: {total_sks}")
    for kode in daftar_pilihan:
        info = mata_kuliah[kode]
        print(f"- {info['nama']} ({info['sks']} SKS)")
    print("=====================================")
    print()

    print("====== GANTI PILIHAN ======")
    print("A. Hapus Mata Kuliah")
    print("B. Update mata kuliah")
    print("C. Kembali ke Menu Utama")
    print("===========================")

    pilihan = input("Pilih opsi (A/B/C): ")
    print()
    if pilihan == "A":
        hapus_pilihan(nim)
    elif pilihan == "B":
        gantipilihan(nim)
    elif pilihan == "C":
        return
    else:
        print("Pilihan tidak valid.")
print()

def hapus_pilihan(nim):
    daftar_pilihan = pilihan_mahasiswa[nim]
    if not daftar_pilihan:
        print("Anda belum memilih mata kuliah.")
        return

    # Menampilkan daftar mata kuliah yang dipilih
    print ("=== HAPUS PILIHAN ===")
    print("Daftar mata kuliah yang telah Anda pilih:")
    nomor = 1
    for kode in daftar_pilihan:
        nama = mata_kuliah[kode]["nama"]
        sks = mata_kuliah[kode]["sks"]
        print(f"{nomor}. {nama} ({sks} SKS)")
        nomor += 1
    print("=====================")

    # Meminta input dari pengguna
    print("Masukkan nomor mata kuliah yang ingin Anda hapus:")
    input_nomor = input("> ")

    indeks = int(input_nomor) - 1  # Konversi input menjadi indeks daftar
    if 0 <= indeks < len(daftar_pilihan):  
        kode_dihapus = daftar_pilihan[indeks]

        print(f"Anda akan menghapus mata kuliah :")
        print(f"{mata_kuliah[kode_dihapus]['nama']} ({mata_kuliah[kode_dihapus]['sks']} SKS)")
        konfirmasi = input("Ketik (ya) untuk menghapus: ")

        if konfirmasi == "ya":
            daftar_pilihan.pop(indeks) 
            print(f"Mata kuliah {mata_kuliah[kode_dihapus]['nama']} berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("Nomor tidak valid. Harap masukkan nomor yang sesuai dengan daftar.")
print()

def gantipilihan(nim):
    daftar_pilihan = pilihan_mahasiswa[nim]
    if not daftar_pilihan:
        print("anda belum memilih mata kuliah.")
        return

    # Menampilkan mata kuliah yang sudah dipilih
    print("=== GANTI MATA KULIAH ===")
    print("daftar mata kuliah yang telah Anda pilih:")
    nomor = 1
    for kode in daftar_pilihan:
        nama = mata_kuliah[kode]["nama"]
        sks = mata_kuliah[kode]["sks"]
        print(f"{nomor}. {nama} ({sks} SKS)")
        nomor += 1
    print("=========================")

    print("Masukkan nomor mata kuliah yang ingin diganti:")
    input_nomor = input("> ")

    if not input_nomor.isdigit():
        print("Masukan tidak valid. Harap masukkan angka.")
        return

    indeks = int(input_nomor) - 1
    if 0 <= indeks < len(daftar_pilihan):
        kode_lama = daftar_pilihan[indeks]
        print(f"Mata kuliah yang akan diganti: {mata_kuliah[kode_lama]['nama']} ({mata_kuliah[kode_lama]['sks']} SKS)")
        print()
        tampilkan_mata_kuliah()

        # Meminta input kode mata kuliah baru
        kode_baru = input("pilih mata kuliah baru: ")

        if kode_baru in mata_kuliah:
            if kode_baru not in daftar_pilihan:
                daftar_pilihan[indeks] = kode_baru
                total_sks = hitung_total_sks(daftar_pilihan)
                if total_sks > maksimal_sks:
                    print(f"Total SKS ({total_sks}) melebihi batas maksimum ({maksimal_sks}).")
                    daftar_pilihan[indeks] = kode_lama  # Kembali ke mata kuliah lama
                else:
                    print(f"Mata kuliah {mata_kuliah[kode_baru]['nama']} berhasil ditambahkan.")
            else:
                print("Mata kuliah ini sudah Anda pilih sebelumnya, tidak bisa untuk mengganti")
        else:
            print("Kode mata kuliah tidak valid.")
    else:
        print("Nomor tidak valid. Harap masukkan nomor yang sesuai.")
print()

def tampilkan_semua_pilihan_mahasiswa():
    """Menampilkan pilihan mata kuliah semua mahasiswa yang telah memilih."""
    if not pilihan_mahasiswa:
        print("Belum ada mahasiswa yang memilih mata kuliah.")
        return 

    print("==== Pilihan Mata Kuliah Semua Mahasiswa ====")
    for nim, daftar_pilihan in pilihan_mahasiswa.items():
        # Mengecek apakah NIM ada dalam data_mahasiswa
        if nim in data_mahasiswa:
            nama = data_mahasiswa[nim]
        else:
            nama = "tidak Diketahui" 

        print(f"NIM: {nim} | Nama: {nama}")
        
        if not daftar_pilihan:
            print("- Belum memilih mata kuliah.")
        else:
            total_sks = hitung_total_sks(daftar_pilihan)
            print(f"Total SKS: {total_sks}")
            for kode in daftar_pilihan:
                info = mata_kuliah[kode]
                print(f"- {info['nama']} ({info['sks']} SKS)")
            print(">====")
            print()
    print("=============================================")
print()

def input_nim():
    # memastikan nim tidak duplikat
    while True:
        nim = int(input("masukkan NIM mahasiswa: "))
        if nim in data_mahasiswa:
            print("NIM sudah terdaftar. Silakan masukkan NIM lain")
            print()
        else:
            return nim
print()

while True:
    print("=== PROGRAM PEMILIHAN MATA KULIAH ===")
    nim = input_nim()
    nama = input("masukkan nama mahasiswa: ")
    if nim == "keluar" or nama == "keluar":
        print("Sistem dihentikan.")
        print()
        break
    print()

    if nim not in pilihan_mahasiswa:
        data_mahasiswa[nim] = nama
        pilihan_mahasiswa[nim] = []
        print(f"Selamat datang {nama} silahkan pilih mata kuliah anda.")

    while True: 
        print("=== Menu Utama ===")
        print("A. Tampilkan Mata Kuliah")
        print("B. Pilih Mata Kuliah")
        print("C. Tampilkan Pilihan Saya")
        print("D. Tampilkan Pilihan Semua Mahasiswa")
        print("E. Ganti Mahasiswa")
        print("F. Keluar")
        print("=================")
        pilihan = input("Pilih menu: ")
        print()

        if pilihan == "A":
            tampilkan_mata_kuliah()
            print()
        elif pilihan == "B":
            pilih_mata_kuliah(nim)
            print()
        elif pilihan == "C":
            tampilkan_pilihan_mahasiswa(nim)
            print()
        elif pilihan == "D":
            tampilkan_semua_pilihan_mahasiswa()
            print()
        elif pilihan == "E":
            print("Berpindah ke mahasiswa lain")
            print()
            break
        elif pilihan == "F":
            print("Terima kasih telah menggunakan program ini!!!!")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi")