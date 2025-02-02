import time
import sys

def tampilkan_lirik_dengan_animasi():
    # Lirik lagu
    lirik = [
    
        "CANTIKNYAAAAA ISTRIIIKUUUUUUUUU",
        "hfsfksdjgjksdglkgsk",
        "LOPYUUUU MEWIII SAGHJFKAJHKFHAKHFLKAS",
       
    ]

    print("Lirik Lagu (dengan animasi):\n")
    
    # Tampilkan lirik satu baris pada satu waktu
    for baris in lirik:
        for char in baris:
            sys.stdout.write(char)  # Cetak karakter satu per satu
            sys.stdout.flush()      # Segera tampilkan output
            time.sleep(0.12)        # Penundaan animasi per karakter
        print()  # Pindah ke baris berikutnya
        time.sleep(1)  # Penundaan antar baris

# Jalankan program
tampilkan_lirik_dengan_animasi()