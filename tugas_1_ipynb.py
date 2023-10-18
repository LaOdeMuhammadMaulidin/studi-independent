# -*- coding: utf-8 -*-
"""Tugas 1 ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/194R8C4RGzbXpmLL8LJAuPuDMDNIurj-s
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Membuat dictionary
data = {
    'Divisi': ['IT', 'Sales', 'Marketing', 'Accounting'],
    'Jumlah Karyawan': [50, 25, 30, 20],
    'Rata-rata Gaji (juta Rupiah)': [8, 6, 7, 5]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Membuat grafik batang jumlah karyawan di setiap divisi
plt.figure(figsize=(5, 5))
plt.bar(df['Divisi'], df['Jumlah Karyawan'], color='red')
plt.xlabel('Divisi')
plt.ylabel('Jumlah Karyawan')
plt.title('Jumlah Karyawan di Setiap Divisi')
plt.show()

# Membuat grafik batang rata-rata gaji karyawan di setiap divisi
plt.figure(figsize=(5, 5))
plt.bar(df['Divisi'], df['Rata-rata Gaji (juta Rupiah)'], color='blue')
plt.xlabel('Divisi')
plt.ylabel('Rata-rata Gaji (juta Rupiah)')
plt.title('Rata-rata Gaji Karyawan di Setiap Divisi')
plt.show()