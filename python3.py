import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Veri yükleme
df = pd.read_csv("yzt2 ilk.py/yzt3.py/movies_initial.csv")

# Sütun düzenleme
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')

# imdbVotes: virgülleri kaldır → sayı yap
df['imdbVotes'] = df['imdbVotes'].astype(str).str.replace(",", "", regex=False)
df['imdbVotes'] = pd.to_numeric(df['imdbVotes'], errors='coerce')

# Sadece gerekli kolonlarda eksik olanları sil
df = df.dropna(subset=['rating', 'imdbVotes'])

# Tür kolonunu parçala
all_genres = df['genre'].dropna().str.split(',').explode().str.strip()

# -----------------------------------------------------
# KISA ÖZET ÇIKTI

print("\n--- IMDb Veri Seti Özet ---")
print("\nEn Popüler 5 Tür:")
print(all_genres.value_counts().head(5))

print("\n(Detaylı tablolar kaldırıldı — sadece özet gösteriliyor.)")

# -----------------------------------------------------
# GRAFİKLER

plt.hist(df['rating'], bins=20)
plt.title("Puan Dağılımı")
plt.xlabel("Puan")
plt.ylabel("Film Sayısı")
plt.show()

plt.scatter(df['imdbVotes'], df['rating'], alpha=0.5)
plt.xscale('log')
plt.xlabel("Oy Sayısı (log)")
plt.ylabel("Puan")
plt.title("Oy Sayısı vs Puan")
plt.show()

top_genres = all_genres.value_counts().head(10)
plt.bar(top_genres.index, top_genres.values)
plt.xticks(rotation=45)
plt.title("En Sık Görülen Türler")
plt.show()

print("\nAnaliz tamamlandı.")