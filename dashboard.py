import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Atur konfigurasi halaman
st.set_page_config(page_title="Dashboard Penjualan", layout="wide")

# Judul halaman
st.title("📊 Dashboard Analisis Data Penjualan")
st.markdown("---")

# Load data
df = pd.read_csv("data_bersih.csv")

# Tampilkan data
with st.expander("🔍 Lihat 5 Data Teratas"):
    st.dataframe(df.head())

# Statistik Deskriptif
with st.expander("📈 Statistik Deskriptif"):
    st.write(df.describe())

st.markdown("## 📊 Visualisasi Data")
st.markdown("---")

# Buat layout 2 kolom
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧾 Metode Pembayaran")
    payment_counts = df['Payment Method'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%',
            startangle=90, colors=sns.color_palette('pastel'))
    ax1.axis('equal')
    st.pyplot(fig1)

with col2:
    st.subheader("🌍 Revenue per Region")
    revenue_per_region = df.groupby('Region')['Total Revenue'].sum()
    fig2, ax2 = plt.subplots()
    ax2.pie(revenue_per_region, labels=revenue_per_region.index, autopct='%1.1f%%',
            startangle=140, colors=plt.cm.Pastel1.colors)
    ax2.axis('equal')
    st.pyplot(fig2)

st.markdown("---")

with col1:
    st.subheader("💰 Revenue per Kategori Produk")
    revenue_per_category = df.groupby('Product Category')['Total Revenue'].sum().sort_values(ascending=False)
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    revenue_per_category.plot(kind='bar', color='coral', ax=ax3)
    ax3.set_xlabel('Kategori Produk')
    ax3.set_ylabel('Total Revenue')
    st.pyplot(fig3)

with col2:
    st.subheader("🏷️ Rata-rata Harga Produk per Kategori")
    avg_price = df.groupby('Product Category')['Unit Price'].mean().sort_values(ascending=False)
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(x=avg_price.values, y=avg_price.index, palette='viridis', ax=ax4)
    ax4.set_xlabel('Rata-rata Harga')
    ax4.set_ylabel('Kategori Produk')
    st.pyplot(fig4)

# Footer
st.markdown("---")
st.caption("© 2025 - Dashboard ini dibuat oleh Tim Analisis Data menggunakan Streamlit")

