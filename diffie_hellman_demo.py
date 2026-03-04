import random
import time

def generate_step_by_step_dh():
    print("----------------------------------------------------")
    print("   SIMULASI DIFFIE-HELLMAN KEY EXCHANGE (DHKE)     ")
    print("-------------------------------------------------\n")
    p = 997 
    g = 7
    
    print(f"[STEP 1] Parameter Publik Disepakati:")
    print(f"  - Bilangan Prima (p): {p}")
    print(f"  - Generator (g)     : {g}")
    print("  (Parameter ini boleh diketahui oleh siapapun/Eavesdropper)\n")
    time.sleep(1.5)

    Yara_private = random.randint(100, 900)
    Bima_private = random.randint(100, 900)
    
    print(f"[STEP 2] Pembuatan Private Key (RAHASIA):")
    print(f"  - Private Key Yara (a): {Yara_private}")
    print(f"  - Private Key Bima (b): {Bima_private}")
    print("  (Angka ini TIDAK PERNAH dikirim melalui jaringan)\n")
    time.sleep(1.5)

    Yara_public = pow(g, Yara_private, p)
    Bima_public = pow(g, Bima_private, p)
    
    print(f"[STEP 3] Penghitungan Public Key:")
    print(f"  - Public Key Yara (A = g^a mod p): {Yara_public}")
    print(f"  - Public Key Bima (B = g^b mod p): {Bima_public}\n")
    time.sleep(1.5)

    print(f"[STEP 4] Simulasi Pertukaran Kunci")
    print(f"  -> Yara mengirim {Yara_public} ke Bima")
    print(f"  <- Bima mengirim {Bima_public} ke Yara\n")
    time.sleep(2)

    Yara_shared_secret = pow(Bima_public, Yara_private, p)
    Bima_shared_secret = pow(Yara_public, Bima_private, p)
    
    print(f"[STEP 5] Penghitungan Shared Secret:")
    print(f"  - Yara menghitung (B^a mod p): {Bima_public}^{Yara_private} mod {p} = {Yara_shared_secret}")
    print(f"  - Bima menghitung (A^b mod p): {Yara_public}^{Bima_private} mod {p} = {Bima_shared_secret}\n")
    time.sleep(1.5)

    print("---------------------------------------------------------")
    if Yara_shared_secret == Bima_shared_secret:
        print(f" HASIL: BERHASIL!")
        print(f" Kunci Simetris yang disepakati: {Yara_shared_secret}")
        print(" Kunci ini sekarang bisa digunakan untuk enkripsi AES/ChaCha20.")
    else:
        print(" HASIL: GAGAL! Terjadi kesalahan perhitungan")
    print("---------------------------------------------------------\n")

if __name__ == "__main__":
    generate_step_by_step_dh()