# Program ATM Sederhana
# By The BujangZ(Danangz-Noellendy-Irfanzz)😎🥶 

# Variabel global untuk menyimpan saldo
saldo = 1000000  # Saldo awal

# Fungsi untuk mengecek saldo
def cek_saldo():
    print(f"Saldo Anda saat ini adalah: {saldo}")

# Fungsi untuk deposit
def deposit(jumlah):
    global saldo
    saldo += jumlah
    print(f"Deposit sejumlah {jumlah} berhasil. Saldo Anda saat ini adalah: {saldo}")

# Fungsi untuk penarikan
def tarik(jumlah):
    global saldo
    if jumlah > saldo:
        print("Saldo tidak mencukupi untuk penarikan!")
    else:
        saldo -= jumlah
        print(f"Penarikan sejumlah {jumlah} berhasil. Saldo Anda saat ini adalah: {saldo}")

# Fungsi rekursif untuk menampilkan menu dan menerima input
def tampilkan_menu():
    print("\nSelamat Datang di ATM Sederhana")
    print("1. Cek Saldo")
    print("2. Deposit")
    print("3. Tarik")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == '1':
        cek_saldo()
    elif pilihan == '2':
        jumlah = float(input("Masukkan jumlah deposit: "))
        deposit(jumlah)
    elif pilihan == '3':
        jumlah = float(input("Masukkan jumlah penarikan: "))
        tarik(jumlah)
    elif pilihan == '4':
        print("Terima kasih telah menggunakan ATM Sederhana. Selamat tinggal!")
        return
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    
    # Rekursi untuk menampilkan menu lagi
    tampilkan_menu()

# Fungsi utama untuk menjalankan program ATM
def main():
    tampilkan_menu()

# Memanggil fungsi utama
if __name__ == "__main__":
    main()
