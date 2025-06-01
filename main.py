import pandas as pd

# Baca file Excel yang benar namanya
df = pd.read_excel('sample-case.xlsx')
df = df.dropna()
# Simpan nilai lama dulu
df['Score Lama'] = df['Score']

# Cari nilai asli Nyimansata
nilai_awal_nyimansata = df.loc[df['Nama Mahasiswa'] == 'NYIMANSATA FOFANA', 'Score'].values[0]

# Nilai baru yang diinginkan
nilai_baru_nyimansata = 90

# Hitung selisih kenaikan
selisih = nilai_baru_nyimansata - nilai_awal_nyimansata

# Tambahkan selisih ke semua nilai dan batasi maksimum 100
df['Score Baru'] = df['Score Lama'] + selisih
df['Score Baru'] = df['Score Baru'].clip(upper=100)

# Klasifikasi nilai huruf berdasarkan Score Baru
bins = [0, 40, 55, 70, 85, 101]
labels = ['E', 'D', 'C', 'B', 'A']

df['Nilai'] = pd.cut(df['Score Baru'], bins=bins, labels=labels, right=False)

# Tampilkan hasil
print(df[['Nama Mahasiswa', 'Score Lama', 'Score Baru', 'Nilai']])
df.to_excel('sample-case-updated.xlsx', index=False)

