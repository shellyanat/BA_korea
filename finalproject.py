import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
from numerize import numerize
import plotly
import plotly.graph_objects as go
import plotly.express as px

#title
st.set_page_config(layout="wide")
st.title("Artis Korea sebagai Duta Merek Brand Lokal")


#data
df = pd.read_excel("ba_artis_korea.xlsx")

#data preparation
df2 = df.copy()
df2 = df.drop(['date','day','trend_brand'],axis=1)
df2 = df2.drop_duplicates(keep='first')
df2 = df2.reset_index(drop=True)

#metrics
st.metric("Total Number of The Brands Having Korean Artist as Their Brand Ambassador", df2['brand_artis'].nunique())

met2,met3 = st.columns(2)
with met2:
    st.metric("Number of Brand", df2['brand'].nunique())
with met3:
    st.metric("Number of Artist", df2['artis'].nunique())

with st.expander("Data Brand Ambassador Artis Korea di Indonesia"):
    st.dataframe(df2)
    st.caption("tgl_ba: hari diumumkannya artis sebagai brand ambassador")





#visualization

#percentage of brand category
df_kategori = df['kategori'].value_counts().rename_axis('kategori').reset_index(name='counts')
cmap = plt.get_cmap('pink')
colors = list(cmap(np.linspace(0.45, 0.85, len(df_kategori))))
fig_pie1, ax1 = plt.subplots()
ax1.pie(df_kategori['counts'], labels=df_kategori['kategori'],autopct='%.1f%%', startangle=90,colors=colors)
ax1.set_title('Brand Category', fontsize=18)
ax1.axis('equal')

#percentage of artist category
df_profesi = df['profesi'].value_counts().rename_axis('profesi').reset_index(name='counts')
cmap = plt.get_cmap('autumn')
colors = list(cmap(np.linspace(0.45, 0.85, len(df_profesi))))
fig_pie2, ax2 = plt.subplots()
ax2.pie(df_profesi['counts'], labels=df_profesi['profesi'], autopct='%.1f%%', startangle=90,colors=colors)
ax2.set_title('Artist Category', fontsize=18)
ax2.axis('equal')

#distribution of BA's announcement date
df3 = df2.copy()
list_YM = df3['tgl_ba'].dt.to_period('M')
df3['YM'] = list_YM
df3['YM'].value_counts()
df_tglba = df3['YM'].value_counts().rename_axis('year-month').reset_index(name='counts')
cmap = plt.get_cmap('winter')
colors = list(cmap(np.linspace(0.45, 0.85, len(df_tglba))))
fig_bar, ax3 = plt.subplots()
ax3=sns.barplot(x='year-month', y='counts',
               data=df_tglba[df_tglba['counts']>1], palette=colors)
ax3.set_title('Top Brand Ambassador Announcement Date by Month', fontsize=18)
ax3.axis('equal')


with st.container():
    chart1,chart2 = st.columns(2)
    with chart1:
        st.pyplot(fig_pie1)
    with chart2:
        st.pyplot(fig_pie2)

st.pyplot(fig_bar)



#selectbox
#by kategori
ktgr = df['kategori'].drop_duplicates()
with st.container():
    st.title("Dashboard")
    ktgr_choice = st.selectbox("Pilih kategori brand", ktgr)

#metric
met1, met2 = st.columns(2)
with met1:
    st.metric("Number of Brand", df[df["kategori"] == ktgr_choice]['brand'].nunique())
with met2:
    st.metric("Number of Artist", df[df["kategori"] == ktgr_choice]['artis'].nunique())




#extract color palette, the palette can be changed
list_BA = df[df["kategori"] == ktgr_choice].brand_artis.values.tolist()
list_BA = sorted(list(set(list_BA)))

pal = list(sns.color_palette(palette='viridis', n_colors=len(list_BA)).as_hex())



fig_hist = go.Figure()
for b,p in zip(list_BA, pal):
    fig_hist.add_trace(go.Scatter(x = df[df['brand_artis']==b]['day'],
                             y = df[df['brand_artis']==b]['trend_brand'],
                             name = b,
                             line_color = p, 
                             fill=None))   #tozeroy 


fig_hist.show()
