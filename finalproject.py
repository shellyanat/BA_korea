import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
from numerize import numerize
from chart_studio import plotly
plotly.sign_in(username='shellyanat', api_key='CHyax83b2yesSo6k1bUL')
import plotly.graph_objects as go
import plotly.express as px

#page setting
st.set_page_config(layout="wide")

st.markdown('''
<style>
/*center metric label*/
[data-testid="stMetricLabel"] > div:nth-child(1) {
    justify-content: center;
}

/*center metric value*/
[data-testid="stMetricValue"] > div:nth-child(1) {
    justify-content: center;
}
</style>
''', unsafe_allow_html=True)

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: rgba(28, 131, 225, 0.1);
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 2% 2% 2% 8%;
   border-radius: 5px;
   color: rgb(72,61,139);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: darkSlateBlue;
}
</style>
"""
, unsafe_allow_html=True)

st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: darkSlateBlue !important;
}
</style>
""",
    unsafe_allow_html=True,
)

#data
df = pd.read_excel("ba_artis_korea.xlsx")

#data preparation
df2 = df.copy()
df2 = df.drop(['date','day','trend_brand'],axis=1)
df2 = df2.drop_duplicates(keep='first')
df2 = df2.reset_index(drop=True)

#title
st.title("Artis Korea sebagai Duta Merek Brand Lokal")
st.caption("4th August, 2022")
st.markdown("---")
with st.container():
    prof_pic,prof,port = st.columns([1,5,4])
    with prof_pic:
        image = Image.open('SNA.png')
        st.image(image,width=100)
    with prof:
        st.write("Shellya Nur Atqiya ")
        st.write("Final Year Mathematics Student at Universitas Pendidikan Indonesia")
        st.write ("shellyaaa29@gmail.com | shellyanra08@gmail.com")
    with port:
        st.write("https://www.linkedin.com/in/shellyanra/")
        st.write("https://shellyanat.github.io/")
st.markdown("---")
st.write("")
with st.container():
    st.subheader('"Saat kita mengajak tokoh dunia seperti BTS dan Blackpink, setiap bulan bisa world wide trending topic." - CEO Tokopedia, Wiliam Tanuwidjaja.')
#title end

st.markdown("---")

#intro
st.subheader("HALLYU WAVE")
with st.expander("Sedikit Kilas Balik Hallyu Wave di Indonesia"):
    hw1,hw2= st.columns([5,3])
    with hw1:
        st.markdown('<div style="text-align: justify;">Hallyu Wave atau Demam Korea diawali dengan meledaknya kepopuleran drama korea yang ditayangkan di stasiun TV Indonesia seperti “Full House” dan “Boys Before Flowers”. Penyanyi Rain, yang juga salah satu aktor pada drama “Full House” menjadi penyanyi K-pop pertama yang berhasil menggelar konser di Indonesia pada 2005. Sejak 2011 hingga 2022 ini, berbagai artis Korea rutin berkunjung ke Indonesia untuk konser ataupun sekadar fanmeeting, walaupun sempat terhenti saat pandemi Covid-19 pada 2020-2021. Tak hanya itu, dilansir dari website resmi Twitter, Indonesia menjadi negara yang paling banyak membuat tweet mengenai  K-pop sekaligus menempati posisi pertama dengan jumlah fans K-pop terbesar pada 2021 lalu.</div>', unsafe_allow_html=True)
    with hw2:
        tw1 = Image.open('twitter1.jpg')
        st.image(tw1,width=400,caption='sumber: blog.twitter.com')
    #kpop popularity graph
    labels = 'Very Popular', 'Popular', 'Popular for a few people', 'Not really'
    sizes = np.array([295, 149, 47,9])
    colors = list(sns.color_palette(palette='deep', n_colors=len(sizes)))
    fig_pop, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels,autopct='%.1f%%', startangle=90,colors=colors)
    ax1.set_title('K-pop Popularity in Indonesia (2018)', fontsize=18)
    ax1.axis('equal')
    pop1, pop2 = st.columns([3,7])
    with pop1:
        st.pyplot(fig_pop)
    with pop2:
        st.markdown('<div style="text-align: justify;">Berdasarkan survei yang dilakukan oleh Lembaga Pertukaran Budaya Internasional Korea pada 2018, sebanyak 59% responden menyatakan bahwa K-pop sangatlah popular di Indonesia dan didukung dengan pernyataan 29.8% responden lain yang setuju bahwa K-pop cukup popular. Tak hanya itu, dilansir dari website resmi Twitter, Indonesia menjadi negara yang paling banyak membuat tweet mengenai  K-pop sekaligus menempati posisi pertama dengan jumlah fans K-pop terbesar pada 2021 lalu.</div>', unsafe_allow_html=True)
#intro end

st.markdown("---")

#body1
df_show = df2.copy()
df_show = df_show.drop(['packaging', 'bundle', 'photocard', 'fanmeet'], axis=1)

st.subheader("Fenomena Wajah Korea untuk Duta Merek Berbagai Brand di Indonesia")


a1,a2 = st.columns([7,3])
with a1:
    with st.expander("Data Brand Ambassador Artis Korea di Indonesia November 2018 - Juni 2022"):
        st.dataframe(df_show)
        st.caption("tgl_ba: hari diumumkannya artis sebagai brand ambassador")
with a2:
    @st.cache
    def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
         return df.to_csv(index=False).encode('utf-8')
    csv = convert_df(df)
    st.download_button(
        label="Download Dataset Lengkap",
        data=csv,
        file_name='ba_artis_korea.csv',
        mime='text/csv',
    )

#metrics information
fwk1, fwk2 = st.columns(2)
with fwk1:
    st.metric("Jumlah Brand Menggunakan Brand Ambassador Artis Korea", df2['brand_artis'].nunique())
with fwk2:
    st.write("Setidaknya sudah 30 kali artis korea menjadi brand ambassador berbagai  macam bisnis di Indonesia, mulai dari e-commerce hingga sprei.")
st.write("")
met2,met3,met4 = st.columns([5,2.5,2.5])
with met2:
    st.write("Pada periode November 2018 hingga Juni 2022 ini, ada 22 artis yang telah menandatangani kontrak sebagai duta merek untuk 24 brand.")
with met3:
    st.metric("Total Brand", df2['brand'].nunique())
with met4:
    st.metric("Total Artis", df2['artis'].nunique())

#visualization information

#percentage of brand category
df_kategori = df['kategori'].value_counts().rename_axis('kategori').reset_index(name='counts')
cmap = plt.get_cmap('pink')
colors = list(cmap(np.linspace(0.45, 0.85, len(df_kategori))))
fig_pie1, ax1 = plt.subplots(figsize=(3,2))
ax1.pie(df_kategori['counts'], labels=df_kategori['kategori'],autopct='%.1f%%', startangle=90,colors=colors)
ax1.set_title('Brand Category',fontsize=10)
ax1.axis('equal')

#top 5 brand
df_brand= df2['brand'].value_counts().rename_axis('brand').reset_index(name='counts')


with st.container():
    chart1,chart2,chart3 = st.columns([4,2,3])
    with chart1:
        st.pyplot(fig_pie1)
    with chart2:
        st.dataframe(df_brand.head())
    with chart3:
        st.markdown('<div style="text-align: justify;">Fenomena ini dipimpin oleh Tokopedia yang telah 3 kali menggunakan artis korea sebagai  bintang iklannya baik di TV maupun Youtube, diikuti oleh Shopee yang lebih sering mengundang artis korea untuk mengisi acaranya dibanding menjadikan artis sebagai brand ambassador resmi.</div>', unsafe_allow_html=True)

#date

#distribution of BA's announcement date
#by month
df3 = df2.copy()
list_YM = df3['tgl_ba'].dt.to_period('M')
df3['YM'] = list_YM
df3['YM'].value_counts()
df_tglba = df3['YM'].value_counts().rename_axis('year-month').reset_index(name='counts')
cmap = plt.get_cmap('winter')
colors = list(cmap(np.linspace(0.45, 0.85, len(df_tglba))))
fig_bar, ax3 = plt.subplots(figsize=(4, 3))
ax3=sns.barplot(x='year-month', y='counts',
               data=df_tglba[df_tglba['counts']>1], palette=colors)
ax3.set_title('Top Brand Ambassador Monthly Count', fontsize=18)
ax3.set_xticklabels(df_tglba[df_tglba['counts']>1]['year-month'],rotation=45)
ax3.axis('equal')


#by year
df4 = df2.copy()
list_Y = df4['tgl_ba'].dt.strftime('%Y')
df4['Y'] = list_Y
df_year = df4['Y'].value_counts().rename_axis('year').reset_index(name='counts')
df_year = df_year.sort_values(by=['counts'])
cmap = plt.get_cmap('winter')
colors = list(cmap(np.linspace(0.45, 0.85, len(df_year))))
fig_lc, ax_lc = plt.subplots(figsize=(4, 3))
ax_lc=sns.lineplot(x='year', y='counts', data=df_year)
ax_lc.set_title('Brand Ambassador Yearly Count', fontsize=19)

#show
ba1,ba2,ba3= st.columns([3,3,3])
with ba1:
    st.markdown('<div style="text-align: justify;">Grafik disamping menunjukkan bahwa setiap tahunnya fenomena artis korea sebagai duta merek brand Indonesia terus meningkat. Puncaknya pada bulan April 2022, ada 5 brand yang mengumumkan bintang baru sebagai duta merek mereka yaitu Bukalapak, Azarine Cosmetic, Mister Potato, Kintakun Sprei dan Avoskin.</div>', unsafe_allow_html=True)
with ba2:
    st.pyplot(fig_lc)
with ba3:
    st.pyplot(fig_bar)
#body1 end

st.markdown("---")

#dashboard
#body google trends
st.subheader("Menilik Grafik Google Trends dari Bisnis dengan Brand Ambassador Artis Korea")
with st.container():
    st.write("Grafik yang ditampilkan berikut bersumber dari google trends dengan rentang waktu 30 hari sebelum hingga 30 hari sesudah brand mengumumkan brand ambassadornya.")

#selectbox
#by kategori
ktgr = df['kategori'].drop_duplicates()
with st.container():
    st.write("Pilih Kategori Brand dan Kategori Artis")
    pil1, pil2,pil3, pil4,pil5= st.columns([2,1.5,1.5,4,1])
    with pil1:
        ktgr_choice = st.selectbox("Pilih kategori brand", ktgr)


#checkbox
#by profesi
with pil4:
    profesi_list = df['profesi'].unique()
    profesi = st.container()   
with pil5:
    st.write("")
    st.write("")
    all = st.checkbox("Select all", value=True)
if all:
    selected_options = profesi.multiselect("Pilih satu atau lebih kategori artis:",
        profesi_list, profesi_list)
else:
    selected_options =  profesi.multiselect("Pilih satu atau lebih kategori artis:",
        profesi_list)
data = df[df["kategori"] == ktgr_choice].loc[df["profesi"].isin(selected_options)]


#metric option for graph show

with pil2:
    st.metric("Total Brand", data['brand'].nunique())
with pil3:
    st.metric("Total Artis", data['artis'].nunique())

#graphic
list_BA = data.brand_artis.values.tolist()
list_BA = sorted(list(set(list_BA)))
pal = list(sns.color_palette(palette='deep', n_colors=len(list_BA)).as_hex())

fig_hist = go.Figure()
for b,p in zip(list_BA, pal):
    fig_hist.add_trace(go.Scatter(x = df[df['brand_artis']==b]['day'],
                             y = df[df['brand_artis']==b]['trend_brand'],
                             name = b,
                             line_color = p, 
                             fill=None))   
fig_hist.update_layout(title="Grafik Brand di Google Trend Sebelum dan Sesudah Menggunakan BA Artis Korea")

st.plotly_chart(fig_hist,use_container_width=True)

#histogram end

#growth from d-30 to d-day
df10=df2.copy()

#new column to get trend value from d-day
df11 = pd.DataFrame()
df11['day0'] = np.where(df['day']==0, df['trend_brand'], 1000)
df11=df11.drop(df11[(df11.day0 == 1000)].index).reset_index(drop=True)

#new colum to get trend value from d-30
df12 = pd.DataFrame()
df12['day_min30'] = np.where(df['day']==-30, df['trend_brand'], 1000)
df12=df12.drop(df12[(df12.day_min30 == 1000)].index).reset_index(drop=True)

#join all the dataframe
df_new = pd.concat([df10,df12,df11],axis=1)

#count growth
df_new['growth']=(df_new['day0'] - df_new['day_min30'])/ df_new['day_min30']
df_new.replace([np.inf, -np.inf], 100, inplace=True) #replace inf value with 100
df_new.replace(np.nan, 0, inplace=True) #replace NaN value with 0
df_gs = df_new.copy()
df_gs = df_gs.drop(df_gs.iloc[:, 1:-1],axis = 1)
df_gs = df_gs.sort_values(['growth'],ascending=False).reset_index(drop=True)

#show growth
st.subheader("Melihat Nilai Growth Google Trends dari Bisnis dengan Brand Ambassador Artis Korea")
st.write("Nilai growth berikut menunjukkan berapa kali lipat besarnya nilai ketenaran suatu merek pada hari diumumkannya artis korea sebagai brand ambassador dibandingkan dengan 30 hari sebelum pengumuman.")
growth1, growth2, growth3,growth4 = st.columns([2.3,4,2.3,1.4])
with growth1:
    st.write(df_gs.head())
with growth2:
    st.markdown('<div style="text-align: justify;">Tabel di sebelah kiri menunjukkan 5 pertumbuhan tertinggi. Nilai growth 100 menunjukkan bahwa nilai trend brand tersebut pada h-30 hari pengumuman adalah 0 dan meningkat menjadi 100 di hari-h pengumuman. Tabel di sebelah kanan menunjukkan 5 brand dengan nilai growth terendah, tabel selengkapnya dapat dilihat di bawah ini.</div>', unsafe_allow_html=True)
    st.write("")
    st.write("")
    with st.expander("Tabel Nilai Growth Google Trends"):
        st.write(df_gs)
with growth3:
    st.write(df_gs.tail())
with growth4:
    with st.expander("Informasi ruangguru_treasure"):
        st.markdown('<div style="text-align: justify;">Alasan mengapa nilai trend Ruangguru rendah di hari Treasure resmi menjadi brand ambassador mereka adalah karena penggemar Treasure telah menduga hal ini akan terjadi berkat teaser yang diberikan Ruangguru beberapa hari sebelumnya. Selain itu, trend Ruangguru meningkat menjadi 100 pada tanggal 7 September atau 4 hari setelah pengumuman, akibat dari diadakannya fanmeeting yang disiarkan beberapa stasiun TV Indonesia. Oleh karena itu, kurang tepat jika dikatakan Ruangguru tidak mengalami peningkatan popularitas selama menggandeng Treasure. Nilai growth khusus Ruangguru section berikutnya akan mengacu pada nilai trend pada hari fanmeeting Treasure x Ruangguru, yaitu 100.</div>', unsafe_allow_html=True)

#growth ends


#correlation map

st.subheader("Korelasi Nilai Growth Google Trends dengan Variabel Lainnya")

df_new1= df_new.copy()

#growth value correction
df_new1['day0'] = np.where(df_new1['brand_artis']=='ruangguru_treasure', np.nan, df_new1['day0'])
df_new1.replace(np.nan, 100, inplace=True)


df_new1['growth']=(df_new1['day0'] - df_new1['day_min30'])/ df_new1['day_min30']
df_new1.replace([np.inf, -np.inf], 100, inplace=True) #replace inf value with 100
df_new1.replace(np.nan, 0, inplace=True) #replace NaN value with 0

df_new2 = df_new1.copy()
df_new2 = df_new2.drop(['tgl_ba','brand_artis','brand','artis','day_min30','day0'],axis=1)
df_new3 = pd.get_dummies(df_new2)

#df corr 
df_corr = df_new3.corr()
df_corr = pd.concat([df_corr],axis=1)

corr1, corr2 = st.columns(2)
with corr1:
    st.write("Korelasi nilai growth dengan variabel lain seperti strategi marketing, kategori brand dan kategori artis.")
    st.markdown('<div style="text-align: justify;">Strategi marketing brand yang telah dilakukan selama November 2018 - Juni 2022 di antaranya memberikan photocard, menggunakan wajah artis untuk packaging produk, menyediakan bundling produk khusus artis tersebut dan mengadakan fanmeeting online ataupun offline.</div>', unsafe_allow_html=True)
with corr2:
    with st.expander("Tabel Korelasi Seluruh Variabel"):
        st.write(df_corr)


#variable choice
st.write("Lihat korelasi beberapa variabel tertentu dengan bantuan heatmap:")
chc1,chc2 = st.columns([7,1])
with chc1:
    korelasi_list = list(df_new3)
    korelasi = st.container()   
with chc2:
    st.write("")
    st.write("")
    all = st.checkbox("All", value=True)
if all:
    selected_options = korelasi.multiselect("Pilih satu atau lebih variabel:",
        korelasi_list, korelasi_list)
else:
    selected_options =  korelasi.multiselect("Pilih satu atau lebih variabel:",
        korelasi_list)
data = df_new3.loc[:,df_new3.columns.isin(selected_options)]

df_new4 = data.corr()
fig = go.Figure(data=go.Heatmap(
                   z=df_new4,
                   x=df_new4.columns,
                   y=df_new4.columns,
                   hoverongaps = False))
fig.update_layout(title="Peta Nilai Korelasi Faktor-Faktor yang Mempengaruhi Pertumbuhan Nilai pada Google Trend")

st.plotly_chart(fig, use_container_width=True)

#show corr
#plotly.offline.plot(fig)

with st.expander("Interpretasi Nilai Korelasi:"):
    st.write("Beberapa insight yang didapatkan dari hasil heatmap korelasi antar variabel adalah:")
    st.markdown('<div style="text-align: justify;">1. Dua variabel yang memiliki nilai korelasi paling tinggi adalah bundle dan kategori_Beauty. Hal ini menunjukkan bahwa untuk hampir seluruh brand kecantikan dapat dipastikan akan menyediakan bundle produk hasil kolaborasi dengan brand ambassador-nya. Begitupun brand yang menyediakan bundle produk, dapat dipastikan brand tersebut berfokus pada industri kecantikan.</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">2. Faktor tertinggi yang mempengaruhi nilai growth suatu brand adalah kategori_F&B. Dengan nilai korelasi lebih dari 0.5, dapat dikatakan bahwa sebagian besar brand yang memiliki nilai growth tinggi berasal dari industri food and beverages.</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">3. Profesi dengan nilai growth tertinggi adalah Idol. Artinya brand ambassador dengan profesi idol lebih menjamin peningkatan brand awareness suatu brand dibanding profesi artis lainnya.</div>', unsafe_allow_html=True)
 
 #corr end
 #dashboard end
st.markdown("---")

#conclusion
st.subheader("Kesimpulan")
st.markdown('<div style="text-align: justify;">Hasil analisis di atas dapat menjadi pertimbangan untuk perusahaan yang ingin menggunakan artis korea sebagai brand ambassadornya. Hal penting yang perlu diperhatikan antara lain:</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">1. Menerapkan strategi marketing yang sekiranya berhasil dilakukan oleh brand-brand sebelumnya seperti packaging atau photocard sebagai langkah awal.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">2. Setiap tahunnya brand dengan duta merek artis korea terus bertambah, alangkah baiknya jika perusahaan menyiapkan inovasi baru sebagai plan cadangan jika strategi lama kurang efektif meningkatkan brand awareness.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">3. Menggunakan brand ambassador yang berprofesi sebagai idol untuk meminimalisir kerugian. Berdasarkan hasil analisis data, artis dengan profesi idol paling banyak digunakan oleh brand-brand sebelumnya sebagai duta merek. Meskipun paling banyak digunakan, artis dengan profesi idol juga terbukti meningkatkan brand awareness dari brand yang dibintanginya dibanding artis dengan profesi lain.</div>', unsafe_allow_html=True)

#notes
st.subheader("Catatan")
st.markdown('<div style="text-align: justify;">1. Penulis sudah berusaha seteliti dan semaksimal mungkin dalam pengerjaan analisis ini. Akan tetapi, penulis membuat dataset sendiri berdasarkan data dari berita dan google trends sehingga memungkinkan adanya kesalahan pada data maupun hasil analisis data.</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">2. Masih banyak variabel lain seperti tingkat kepopuleran artis di Indonesia, frekuensi kemunculan iklan baik di media sosial dan di televisi, serta rentang waktu grafik google trend yang dapat mempengaruhi hasil korelasi antar variabel dan hasil analisis data.</div>', unsafe_allow_html=True)
