import streamlit as st
import eda
import prediction

# Membuat sidebar dengan opsi menu
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediction'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.image('https://cdn2.iconfinder.com/data/icons/biometrics-11/64/1_1._face_scan_identification_biometric_access_recognition-512.png')

# Memilih halaman berdasarkan opsi yang dipilih
if page == 'Home Page':
    # Tampilan Home Page
    st.image('https://t3.ftcdn.net/jpg/00/73/19/46/360_F_73194646_tRMWbpxyDFdaGFa0h3G8Pga7DCAOjUXS.jpg')
    st.markdown("<h1 style='text-align: center;'>Welcome to Home Page<br>Grade Challenge 7</h1>", unsafe_allow_html=True)
    st.markdown("========================================================================================")
    st.write('')
    st.markdown("<p style='text-align: left;'>Name : Muhammad Insani</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>Batch : HCK-010</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left;'>Objective : This program was created to predict gender, ethnicity and age</p>", unsafe_allow_html=True)
    st.write('')
    st.caption('Please select another menu in the Select Box on the left side of your screen to get started.!')
    st.write('')
    st.write('')



    # Menampilkan Deskripsi dataset
    with st.expander("Dataset Description"):
        st.caption('''
                   
                   CSV dataset of face images labeled by age, gender, and ethnicity. 
                   This dataset includes 27305 rows and 5 columns
                   
                   
                    | Column Name | Description                                                                |
                    |------------|---------------------------------------------                             |
                    | age        | Age of the subject on the face photo                                              |
                    | ethnicity  | Race/ethnicity of photo subject (0=White, 1=Black, 2=Asian, 3=Indian, 4=Others)|
                    | gender     | Gender of the photo subject (0=Male, 1=Female)                             |
                    | img_name   | Unique file name for each image                                         |
                    | pixels     | Matrix of image pixel values (0-255)                                        |

                   
                   
                   ''')
 
    with st.expander("Conclusion On Model Performance"):
        st.caption('''
                   
                   Dari segi waktu pelatihan, model transfer learning cenderung membutuhkan waktu lebih lama, tetapi dapat memberikan peningkatan kinerja yang signifikan. Insight yang bisa diambil untuk keperluan bisnis:

                   Gender Classification:

                   Model transfer learning lebih unggul dalam mengklasifikasikan gender dengan akurasi yang lebih tinggi.
                   Dalam bisnis yang berkaitan dengan segmentasi pasar berdasarkan gender, penggunaan model transfer learning dapat memberikan hasil yang lebih dapat diandalkan.

                   Ethnicity Classification:

                   Model transfer learning memiliki performa yang lebih baik secara keseluruhan dalam mengklasifikasikan kategori etnis.
                   Pemilihan model transfer learning dapat memberikan informasi etnis yang lebih akurat dalam aplikasi seperti penelitian demografis atau pengembangan produk yang disesuaikan dengan keberagaman etnis.

                   Age Classification:

                   Model transfer learning juga menunjukkan peningkatan kinerja dalam mengklasifikasikan kategori usia.
                   Untuk bisnis yang memerlukan penargetan berdasarkan kelompok usia, menggunakan model transfer learning dapat meningkatkan akurasi prediksi.
                                    
                   
                   ''')
        
    with st.expander("Conclusion on Business Progress"):
        st.caption('''
                   
                   Penerapan model transfer learning untuk mengklasifikasikan gender, etnis, dan usia membawa dampak positif pada kemajuan bisnis. Dengan kemampuan yang lebih baik dalam mengidentifikasi karakteristik demografis pelanggan, bisnis dapat melakukan segmentasi pasar yang lebih akurat, memungkinkan strategi pemasaran yang lebih terfokus dan penawaran produk yang lebih personal. Personalisasi ini tidak hanya dapat meningkatkan retensi pelanggan tetapi juga mengoptimalkan pengalaman pengguna secara keseluruhan, menciptakan lingkungan online yang lebih sesuai dengan preferensi individu.
                   Selain itu, hasil yang lebih akurat dari model klasifikasi dapat digunakan untuk analisis demografis mendalam, memberikan wawasan yang berharga tentang perilaku konsumen dan tren pembelian. Dengan dasar informasi ini, bisnis dapat membuat keputusan strategis yang lebih terinformasi, membuka peluang untuk inovasi produk yang lebih efektif dan pengembangan strategi pemasaran yang lebih canggih. Keseluruhan, penggunaan model transfer learning tidak hanya memperkuat daya saing bisnis tetapi juga meningkatkan efisiensi operasional dan relevansi bisnis dalam memenuhi kebutuhan pelanggan secara lebih presisi.
                                    
                   
                   ''')
        
elif page == 'Exploration Data Analysis':
    # Menjalankan fungsi untuk EDA
    eda.run()
else:
    # Menjalankan fungsi untuk Model Prediction
    prediction.run()
