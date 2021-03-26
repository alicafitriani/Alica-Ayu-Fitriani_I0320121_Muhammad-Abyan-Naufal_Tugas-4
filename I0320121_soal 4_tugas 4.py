import time
runtime = time.time()

# Syarat mendaftar kursus online
usia = int(input("Berapa usia kamu? Masukkan usia:"))
hasil_ujian = input("Apakah anda sudah lulus ujian kualifikasi (Y/T)?")

if (usia >= 21) and (hasil_ujian == "Y") :
    print("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar kursus")

print("\nWaktu runtime adalah",time.time() - runtime, "detik")