# Import library yang digunakan
import streamlit as st
from PIL import Image

# Fungsi untuk menjalankan aplikasi
def run():
    
    # Tampilan judul halaman
    st.markdown("<h1 style='text-align: center;'>Welcome to Explaration Data Analysis</h1>", unsafe_allow_html=True)
    st.markdown("========================================================================================")
    st.markdown("")
    
    # Membagi layar menjadi dua kolom
    col1, col2 = st.columns(2)

    col1.markdown("<h4 style='text-align: left;'>1. Age Distribution</h4>", unsafe_allow_html=True)
    image = Image.open('newplot.png')
    col1.image(image, caption='figure 1')

    with col1.expander('Explanation'):
        st.caption('Berdasarkan visualisasi distribusi umur pada dataset sangat bervariasi, dengan rentang umur mulai dari 1 tahun hingga 116 tahun. Umur 26 tahun menjadi umur yang paling umum muncul dengan jumlah data sebanyak 2.197, diikuti oleh umur 1 tahun dengan 1.123 data, dan umur 28 tahun dengan 918 data. Perlu diperhatikan bahwa ada variasi yang signifikan dalam jumlah data untuk setiap umur, dan perlu dilakukan strategi pengelompokan umur yang cermat agar model dapat mengatasi variasi tersebut dengan baik.')

    col2.markdown("<h4 style='text-align: left;'>2. Age Category Distribution</h4>", unsafe_allow_html=True)
    image = Image.open('newplot2.png')
    col2.image(image, caption='figure 2')

    with col2.expander('Explanation'):
        st.caption('Berdasarkan visualisasi distribusi label kategori umur pada dataset, kategori Adults mendominasi dengan jumlah data sebanyak 16.815, menjadi kelompok terbesar di antara kategori umur lainnya. Disusul oleh kategori Elderly dengan 2.395 data, Childrens dengan 1.808 data, Baby dengan 1.605 data, dan Teens dengan 1.082 data. Dengan demikian, fokus pada kelompok Adults menjadi krusial dalam pengembangan model, namun tetap perlu memperhitungkan representasi yang cukup dari kelompok umur lainnya agar model dapat memberikan prediksi yang lebih seimbang untuk semua kategori umur.')
        
    col1.markdown("<h4 style='text-align: left;'>3. Ethnicity Distribution</h4>", unsafe_allow_html=True)
    image = Image.open('newplot3.png')
    col1.image(image, caption='figure 3')

    with col1.expander('Explanation'):
        st.caption('Berdasarkan visualisasi, dapat dilihat bahwa distribusi target ethnicity dalam dataset sangat tidak seimbang. Label white mendominasi dengan jumlah data sebanyak 10.078, lebih dari dua kali lipat dari label black yang merupakan label kedua terbanyak dengan jumlah 4.526 data. Sementara itu, label Asian memiliki 3.434 data, Indian 3.975 data, dan Others 1.692 data. Ketidakseimbangan ini perlu diperhatikan dalam pengembangan model, karena dapat mempengaruhi kinerja dan generalisasi model terhadap kelompok etnis yang kurang representatif. Strategi untuk mengatasi ketidakseimbangan ini mungkin melibatkan teknik oversampling atau undersampling pada kelompok etnis yang kurang representatif.')

    col2.markdown("<h4 style='text-align: left;'>4. Gender Distribution</h4>", unsafe_allow_html=True)
    image = Image.open('newplot4.png')
    col2.image(image, caption='figure 4')

    with col2.expander('Explanation'):
        st.caption('Berdasarkan visualisasi yang terlihat, dapat diambil kesimpulan bahwa distribusi label antara male dan female cenderung seimbang, dengan jumlah male sekitar 12.391 dan female sekitar 11.314. Hal ini menunjukkan proporsi yang relatif seragam antara kedua kategori, menciptakan keseimbangan dalam representasi jenis kelamin dalam dataset tersebut.')

    col1.markdown("<h4 style='text-align: left;'>5. Distribution Shape size</h4>", unsafe_allow_html=True)
    image = Image.open('output.png')
    col1.image(image, caption='figure 5')

    with col1.expander('Explanation'):
        st.caption('Berdasarkan pengamatan visual dari representasi data piksel, dapat disimpulkan bahwa panjang array piksel secara keseluruhan menunjukkan konsistensi yang signifikan, yakni seluruhnya memiliki nilai 2304. Hal ini mencerminkan dimensi gambar secara keseluruhan, setara dengan ukuran 48x48 piksel. Temuan ini menggambarkan konsistensi yang dapat diandalkan dalam struktur dan ukuran data piksel pada seluruh dataset, memberikan pandangan yang stabil terhadap setiap komponen gambar yang diamati dalam analisis.')

    col2.markdown("<h4 style='text-align: left;'>6. Overview of Photo Characteristics</h4>", unsafe_allow_html=True)
    image = Image.open('output2.png')
    col2.image(image, caption='figure 6')

    with col2.expander('Explanation'):
        st.caption('Berdasarkan gambaran karakteristik foto yang akan digunakan sebagai fitur dalam pelatihan model, dapat disimpulkan bahwa fitur tersebut akan mencakup variasi karakter wajah, seperti penggunaan atau tidaknya kacamata, terlihat atau tidaknya rambut, ekspresi wajah yang terlihat sedang memandang kamera, dan foto yang menampilkan wajah secara keseluruhan dari dagu hingga kening. Selain itu, fitur akan menggunakan representasi warna dalam satu dimensi (grayscale)')

