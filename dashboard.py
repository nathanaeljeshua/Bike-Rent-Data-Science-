import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

day_df = pd.read_csv("day.csv")
year_rental= pd.read_csv('year_sum.csv')
month_rental_1=pd.read_csv('monthly_1.csv')
month_rental_2=pd.read_csv('monthly_2.csv')
hourly_mean_sum=pd.read_csv('hourly_rentals_mean_sum.csv')
workingday_rentals=pd.read_csv('workingday_rentals.csv')

colors=['#6d7a71','#ba806a', '#cdd9c5']
color_1='#6d7a71'
color_2='#ba806a'
st.header('Penyewaan Sepeda 🚲')

#Visualisasi 1
st.subheader('Total Penyewaan')

col1, col2 = st.columns(2)
with col1:
    total_sewa = year_rental[year_rental['yr'] == 0]['cnt'].sum()
    st.metric("Total Penyewaan Tahun 2021", value=total_sewa)

with col2:
    total_sewa_1 = year_rental[year_rental['yr'] == 1]['cnt'].sum()
    st.metric("Total Penyewaan Tahun 2022", value=total_sewa_1)

fig, ax = plt.subplots(figsize=(10, 10))

# Gunakan seaborn untuk membuat barplot
sns.barplot(x='tahun', y='cnt', data=year_rental, ax=ax, errorbar=None, palette=colors)
plt.xlabel('Tahun')
plt.ylabel('Total')

# Menampilkan plot di Streamlit
st.pyplot(fig)

#Visualisasi 2
st.subheader("Tren Penyewaan Dalam 2 Tahun")
fig, ax = plt.subplots(figsize=(15, 6))

#Gunakan Seaborn
sns.lineplot(x='bulan', y='cnt',data=month_rental_1, marker='o', label='Tahun 2012',color=color_1)
sns.lineplot(x='bulan', y='cnt',data=month_rental_2, marker='o', label='Tahun 2011',color=color_2)
plt.xlabel('Bulan')
plt.ylabel('Rata-Rata Penyewaan')
# Menampilkan plot di Streamlit
st.pyplot(fig)

#Visualisasi 3
st.subheader('Puncak Jam Penyewaan')
col1,=st.columns(1)
with col1:
    rata_sewa_17=hourly_mean_sum.loc[hourly_mean_sum['Hour'] == 17, 'Mean']
    rata_sewa_17=round(rata_sewa_17)
    st.metric("Rata-Rata Penyewaan di Jam ke-17", value=rata_sewa_17)
fig, ax = plt.subplots(figsize=(15, 6))
sns.lineplot(x='Hour', y='Mean',data=hourly_mean_sum, marker='o', color=color_1)
plt.xlabel('Jam')
plt.ylabel('Rata-Rata Penyewaan')

# Menampilkan plot di Streamlit
st.pyplot(fig)

#Visualisasi 4
st.subheader('Total Penyewaan saat Hari Kerja dan Libur')

col4, col5 = st.columns(2)
with col4:
    holiday_rentals = workingday_rentals[workingday_rentals['workingday'] == 0]['cnt'].sum()
    st.metric("Total Penyewaan Hari Libur", value=holiday_rentals)

with col5:
    work_rentals = workingday_rentals[workingday_rentals['workingday'] == 1]['cnt'].sum()
    st.metric("Total Penyewaan Hari Kerja", value=work_rentals)

fig, ax = plt.subplots(figsize=(10, 10))

# Gunakan seaborn untuk membuat barplot
sns.barplot(x='jenis_hari', y='cnt', data=workingday_rentals, ax=ax, errorbar=None, palette=colors)
plt.xlabel('Jenis Hari')
plt.ylabel('Total Penyewaan')

# Menampilkan plot di Streamlit
st.pyplot(fig)

#Visualisasi 5
st.subheader('Total Penyewaan di Tiap Kondisi Cuaca')
col6,=st.columns(1)
with col6:
    rata_sewa_cuaca_1=day_df.loc[day_df['weathersit'] == 1, 'cnt']
    rata_sewa_cuaca_1 = rata_sewa_cuaca_1.sum()
    st.metric("Total Penyewaan di Kondisi Cuaca 1", value=rata_sewa_cuaca_1)
fig, ax = plt.subplots(figsize=(10, 10))
sns.barplot(x='weathersit', y='cnt', data=day_df, estimator='sum', errorbar=None, palette=colors)
plt.xlabel('Cuaca')
plt.ylabel('Total')
# Menampilkan plot di Streamlit
st.pyplot(fig)
col7,=st.columns(1)
with col7:
    st.text("Cuaca 1: Clear, Few clouds, Partly cloudy")
    st.text("Cuaca 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
    st.text("Cuaca 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")
    st.text("Cuaca 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")

