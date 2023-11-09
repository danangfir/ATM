# Program ATM Sederhana
# By The BujangZ(Danangz-Noellendy-Irfanzz)😎🥶 
# Inisialisasi saldo awal
saldo = 1000000

# Fungsi untuk mengecek saldo
def cek_saldo():
    print(f"Saldo Anda saat ini adalah Rp{saldo}")

# Fungsi untuk deposit
def deposit(uang):
    global saldo
    saldo += uang
    print(f"Berhasil deposit Rp{uang}. Saldo Anda saat ini adalah Rp{saldo}")

# Fungsi untuk penarikan
def tarik(uang):
    global saldo
    if uang > saldo:
        print("Maaf, saldo Anda tidak cukup untuk melakukan penarikan.")
    else:
        saldo -= uang
        print(f"Berhasil menarik Rp{uang}. Saldo Anda saat ini adalah Rp{saldo}")

# Fungsi utama
def main():
    while True:
        print("\nSelamat datang di ATM Python")
        print("1. Cek Saldo")
        print("2. Deposit")
        print("3. Tarik Uang")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            cek_saldo()
        elif pilihan == '2':
            jumlah_uang = int(input("Masukkan jumlah uang untuk deposit: Rp"))
            deposit(jumlah_uang)
        elif pilihan == '3':
            jumlah_uang = int(input("Masukkan jumlah uang untuk penarikan: Rp"))
            tarik(jumlah_uang)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan ATM Python. Selamat tinggal!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memanggil fungsi utama
if __name__ == "__main__":
    main()
