import pandas as pd

df = pd.read_excel('sample-case.xlsx')
df = df.dropna()
print(df)

df['Score Lama'] = df['Score']

nilai_awal_nyimansata = df.loc[df['Nama Mahasiswa'] == 'NYIMANSATA FOFANA', 'Score'].values[0] 
nilai_baru_nyimansata = 90

selisih = nilai_baru_nyimansata - nilai_awal_nyimansata

df['Score Baru'] = df['Score Lama'] + selisih
df['Score Baru'] = df['Score Baru'].clip(upper=100)

bins = [0,40,55,70,85,101]
labels = ['E','D','C','B','A']

df['Nilai'] = pd.cut(df['Score Baru'], bins=bins, labels=labels, right=False)

print(df[['Nama Mahasiswa', 'Score Lama', 'Score Baru', 'Nilai']])
df.to_excel('sample-case-terbaru.xlsx', index=False)
