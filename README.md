# Asymmetric Cryptography: Diffie-Hellman Key Exchange

Repositori ini berisi implementasi mandiri (*from scratch*) dari algoritma **Diffie-Hellman Key Exchange** menggunakan Python. Proyek ini mendemonstrasikan bagaimana dua pihak dapat menyepakati sebuah kunci rahasia (Shared Secret) melalui saluran komunikasi yang tidak aman tanpa pernah mengirimkan kunci itu sendiri.

## Tentang Algoritma
**Diffie-Hellman (DH)** dikembangkan oleh Whitfield Diffie dan Martin Hellman pada tahun 1976. Ini adalah salah satu protokol pertukaran kunci pertama dan paling berpengaruh di dunia kriptografi.

### Kegunaan di Dunia Nyata:
- **HTTPS (TLS/SSL):** Mengamankan komunikasi antara browser dan server.
- **SSH:** Mengamankan akses remote ke server.
- **VPN:** Membangun tunnel komunikasi yang aman.

## Alur Kerja Program
Program ini mensimulasikan interaksi antara dua pihak (misalnya **Yara** dan **Bima**) dengan langkah-langkah berikut:

1.  **Parameter Publik:** Menyepakati bilangan prima ($p$) dan generator ($g$) yang tidak rahasia.
2.  **Private Key:** Yara dan Bima masing-masing menghasilkan angka acak rahasia.
3.  **Public Key:** Menghitung nilai publik menggunakan rumus $g^x \pmod{p}$.
4.  **Exchange:** Kedua pihak bertukar nilai publik tersebut.
5.  **Shared Secret:** Melalui keajaiban matematika, keduanya menghitung nilai akhir yang identik untuk digunakan sebagai kunci enkripsi simetris.



## Instalasi & Penggunaan

### Prasyarat
- Python 3.x terinstal.

### Cara Menjalankan
1. Clone repositori:
   ```bash
   git clone [https://github.com/farras-ara/Diffie-HellmanKeyExchange.py.git](https://github.com/farras-ara/Diffie-HellmanKeyExchange.py.git)