import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
df = pd.read_csv('hour.csv')

# Title of dashboard
st.title("Bike Renting Dashboard")

#Pertanyaan Bisnis 1: Berapa banyaknya sepeda yang dipinjam pada hari kerja dan hari libur?
st.header("Jumlah Sepeda yang Dipinjam pada Hari Kerja dan Hari Libur")
df['workingday'] = df['workingday'].map({1: 'Hari Kerja', 0: 'Hari Libur'})
df_hari = df.groupby('workingday')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='workingday', y='cnt', data=df_hari, palette='Blues', ax=ax)
ax.set_title('Jumlah Sepeda yang Dipinjam pada Hari Kerja dan Hari Libur')
ax.set_xlabel('Hari')
ax.set_ylabel('Jumlah Sepeda')
st.pyplot(fig)

# Pertanyaan Bisnis 2: Berapa presentase sepeda yang pininjam berdasarkan musim?
st.header("Jumlah Sepeda yang Dipinjam pada Musim Panas dan Musim Dingin")
df['season'] = df['season'].map({1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'})
df_musim = df.groupby('season')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 6))
sns.set_color_codes("pastel")
plt.pie(df_musim['cnt'], labels=df_musim['season'], autopct='%1.1f%%', ax=ax)
ax.set_title('Jumlah Sepeda yang Dipinjam pada Musim Panas dan Musim Dingin')
st.pyplot(fig)