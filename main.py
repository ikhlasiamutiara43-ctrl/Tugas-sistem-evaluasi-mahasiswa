# Sistem Evaluasi Mahasiswa

# 1. Input data mahasiswa
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
kehadiran = float(input("Masukkan persentase kehadiran (%): "))

# 2. Hitung nilai akhir (operator aritmatika)
nilai_akhir = (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)

# 3. Tentukan status kelulusan
# Syarat lulus: nilai akhir >= 75 DAN kehadiran >= 80%
if nilai_akhir >= 75 and kehadiran >= 80:
    # 4. Cek predikat: nilai >= 85, kehadiran >= 90%, dan nilai akhir genap
    if nilai_akhir >= 85 and kehadiran >= 90 and int(nilai_akhir) % 2 == 0:
        status = "LULUS DENGAN PREDIKAT"
    else:
        # 6. Lulus tetapi tidak memenuhi predikat
        status = "LULUS"
else:
    # 5. Tidak memenuhi syarat kelulusan
    status = "BELUM LULUS"

# Tampilkan hasil
print("\nHASIL EVALUASI")
print(f"Nilai Akhir : {nilai_akhir:.2f}")
print(f"Kehadiran   : {kehadiran:.0f}%")
print(f"Status      : {status}")
