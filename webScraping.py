from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://thinkjubilee.com/cara-memperbaiki-cahaya-foto-digital-dengan-mudah/")
# driver.find_element(By.ID, "post-9126").text
# digunakan untuk menyeleksi teks

# jika ingin diambil teks nya maka harus ditambahkan variabel
# karena teks tersebut akan disimpan divariabel nya dan nanti tinggal di panggil.
# contohnya seperti berikut
teks = driver.find_element(By.ID, "post-9216").text

print(teks)

# Output :
# APRIL 7, 2022
# HOME / LOUNGE / CARA MEMPERBAIKI CAHAYA FOTO DIGITAL DENGAN MUDAH
# Cara Memperbaiki Cahaya Foto Digital dengan Mudah
# By adminApril 7, 2022Categories: Lounge, readTags: mengedit foto
# Cara memperbaiki cahaya foto digital bagaimana? Salah satu software unggulan NIK adalah Viveza 2. Secara khusus, software yang satu 
# ini berfungsi untuk mengoreksi foto yang berkaitan dengan warna dan cahaya. Jika dibandingkan dengan Color Efex Pro 4, Viveza 2 ini 
# mungkin memiliki tujuan yang tampak sama mengingat di dalam Color Efex Pro 4, kita pun menjumpai filter-filter untuk mengoreksi warna dan cahaya pada foto. Tapi jika ditelusuri lebih lanjut, Viveza 2 memang secara spesifik mengatasi masalah cahaya dan foto sehingga kontrol-kontrol yang disediakan di dalamnya benar-benar terfokus untuk mengatasi kedua masalah tersebut. Sementara itu, Color Efex Pro 4 berorientasi pada pembuatan efek-efek khusus yang menarik.
# Menjalankan dan Mengenal Interface Viveza 2
# Tugas pertama Anda adalah menginstall Viveza 2 ini ke dalam komputer agar dapat dikenali oleh Adobe Photoshop. Setelah itu, Anda bisa menggunakan Viveza 2 ini sebagai plugin Adobe Photoshop. Awali instalasi dengan mengklik-ganda file Viveza2-pl-ver2.007all.exe yang sudah diunduh dari situs NIK Software. Install aplikasi ini sesuai dengan langkah-langkah yang terlihat di dalam layar monitor.   
# Setelah itu, Anda bisa mengikuti langkah-langkah di bawah ini untuk menjalankan Viveza 2 lewat Adobe Photoshop:
# Luncurkan Adobe Photoshop terlebih dulu dan bukalah sebuah foto untuk diedit menggunakan Viveza 2.0.
# CREDIT FOTO:
# http://www.flickr.com/photos/31085717@N00/7930645178/lightbox/
# Pastikan Anda melihat panel NIK Software dimana Viveza 2 menjadi salah satu pilihan yang ada di situ bersama dengan Dfine dan Color 
# Efex Pro 4.
# Pilihlah menu Filter > NIK Software > Viveza 2.
# Editlah cahaya dan warna pada foto itu memakai kontrol-kontrol yang sudah disediakan di dalam jendela Viveza 2.
# Mengenal Interface Viveza 2
# Viveza 2 memiliki interface yang lebih sederhana untuk cara memperbaiki cahaya foto digital dibandingkan Color Efex Pro 4. Kontrol-kontrol yang ada di bagian kanan berfungsi untuk membantu Anda mengatur cahaya dan warna pada foto sampai pada titik kecemerlangan yang tinggi.
# Untuk membantu Anda mengoperasikan Viveza 2, ada baiknya kita kenali terlebih dulu interface plugin Photoshop yang satu ini terlebih dahulu:
# Filter Controls: di bagian ini, Anda bisa menambahkan control point untuk mengoreksi cahaya dan warna pada bagian kecil area yang ada di sebuah objek foto. Selain berfungsi untuk menambahkan control point baru, di dalam Filter Controls ini juga terdapat tombol-tombol untuk mengelola control point-control point yang sudah diletakkan di dalam foto, seperti menyatukan point-point itu lewat fitur 
# Group dan Ungroup.
# Kontrol untuk Adjustment: di bagian ini, Anda bisa mengatur cahaya dan warna foto dengan memanfaatkan slider-slider yang sudah disediakan di dalam panel tersebut. Secara umum, jika Anda memanfaatkan slider-slider yang ada di dalam panel ini, maka hasil koreksi yang akan terlihat untuk keseluruhan foto.
# Levels and Curves: apabila Anda ingin bernostalgia dengan Photoshop yang memanfaatkan Levels serta Curves untuk mengoreksi warna dan cahaya foto, maka manfaatkanlah panel tersebut dengan menggulung panel sebelah kanan ke arah bawah. Selanjutnya, Anda bisa mengoreksi foto memakai grafik Levels dan Curves.
# Selain bagian-bagian di atas, Anda juga akan menemukan bagian lain yang juga terdapat di Dfine maupun Color Efex Pro. Bacalah bab-bab awal buku ini sebagai referensinya.
# Mengoreksi Cahaya dan Warna Foto Menggunakan Adjustments
# Kontrol-kontrol yang masuk dalam kelompok Adjustments untuk cara memperbaiki cahaya foto digital dengan cara mengoreksi foto secara 
# menyeluruh berdasarkan slider-slider yang ada di dalam panel tersebut. Sebelum kita menggunakan Adjustments, perhatikan terlebih dulu kalau panel ini dilengkapi dengan dua buah ikon, yaitu:
# Collapse All Sliders. Berfungsi untuk menampilkan slider-slider utama saja di dalam panel tersebut, yaitu slider Brightness, Contrast, Saturation, dan Structure.
# Expand All Sliders. Berfungsi untuk menampilkan slider-slider yang lebih lengkap sehingga dengan demikian, pengaturan cahaya dan warna pada foto akan menjadi jauh lebih lengkap. Anda akan melihat panel Red, Green, Blue, dan sebagainya.
# Menggunakan Brightness
# Brightness berfungsi untuk mengontrol penambahan atau pengurangan cahaya pada foto secara keseluruhan. Geser ke sebelah kanan untuk 
# mendapatkan cahaya yang semakin meningkat, atau geser ke sebelah kiri untuk menggelapkan foto.
# CREDIT FOTO:
# http://www.flickr.com/photos/moriza/75374694/lightbox/
# Menggunakan Contrast
# Biasanya, contrast digunakan setelah Anda memakai Brightness untuk mengurangi cahaya pada foto. Efek samping pengurangan cahaya adalah munculnya kekusaman pada warna yang mengakibatkan foto tampak jenuh dan tumpul. Untuk mengatasi hal tersebut, Anda bisa meningkatkan kontras warna agar warna menjadi sedikit gelap dan tajam sekaligus.
# Contrast sendiri adalah perbedaan warna yang tajam antara warna yang terang dan gelap sehingga secara keseluruhan, foto itu menjadi 
# meningkat detail warnanya. Geser slider Contrast ke kanan untuk mendapatkan kontras yang semakin meningkat.
# CREDIT FOTO:
# http://www.flickr.com/photos/31085717@N00/7501836508/lightbox/
# Menggunakan Saturation
# Setelah contrast ditingkatkan, biasanya warna menjadi sangat tajam sehingga terlihat kurang realistik. Nah di sinilah Saturation mengambil peranan. Saturation berfungsi untuk mengatur tajam kusamnya warna. Jika warna terlalu tajam akibat penggunaan contrast yang berlebihan, maka ketajaman itu bisa diturunkan untuk menghasilkan warna objek yang lebih “tidak mengkilat”.
# Apabila Anda menggeser slider Saturation ke ujung paling kiri, maka foto akan kehilangan warnanya sehingga menjadi hitam-putih.     
# CREDIT FOTO:
# http://www.flickr.com/photos/31085717@N00/7890334194/lightbox/
# Shadow Adjustments
# Slider Shadow Adjustments berfungsi untuk cara memperbaiki cahaya foto digital dengan mengontrol cahaya pada bagian-bagian foto yang gelap. Dengan demikian, jika Anda menggunakan slider ini untuk pengontrolan cahaya, maka bagian yang terang pada foto tidak terlalu berpengaruh. Shadow Adjustments digunakan sebagai keseimbangan antara bagian yang terang dan gelap pada sebuah foto sehingga tidak 
# mengalami over atau under exposure di bagian-bagian tertentu.
# CREDIT FOTO:
# http://www.flickr.com/photos/uggboy/6383783943/lightbox/
# Apabila slider ini digeser ke arah kanan, maka bayangan pada objek akan mendapatkan cahaya tambahan sehingga menjadi seolah-olah tampak terang.
# Menggunakan Warmth
# Warmth digunakan untuk membuat foto tampak lebih hangat atau dingin. Jika slider ini digeser ke arah kanan, maka foto akan menjadi lebih hangat dengan penambahan warna kecoklatan. Sedangkan apabila slider ini digeser ke arah kiri, maka foto menjadi lebih dingin dengan penambahan intensitas warna biru.
# CREDIT FOTO:
# http://www.flickr.com/photos/kodomut/7121358869/lightbox/
# Penggunaan slider ini ideal dipakai untuk menekankan efek kesorean atau pagi dini hari pada sebuah foto.
# jub.id
# Load More
# Follow on Instagram
# Menggunakan Red, Green, dan Blue
# Slider Red, Green, dan Blue dipakai untuk mengontrol keseimbangan antara warna merah, hijau, dan biru. Anda bisa memanfaatkan slider ini untuk mendapatkan nuansa warna baru yang lebih menarik atau mengontrol keseimbangan warna pada foto, misalnya akibat adanya white balance yang tidak pas, sehingga warna-warna menjadi lebih natural.
# Secara default, posisi kontrol pada tiap-tiap slider berada di tengah. Pergeseran ke kanan atau ke kiri pada kontrol slider tersebut menghasilkan warna yang berbeda. Berikut perbedaan-perbedaan warna yang terjadi apabila seluruh slider Red, Green, dan Blue berada 
# di posisi tengah dan kita menggeser kontrol slider pada salah satu warna saja.
# Slider Red: jika digeser ke arah kiri akan menghasilkan nuansa warna kehijauan. Sedangkan apabila digeser ke arah kanan akan membuat warna menjadi sedikit kemerahan.
# Slider Green: jika digeser ke arah kiri akan menghasilkan nuansa warna magenta. Sedangkan jika digeser ke arah kanan, akan membuat warna menjadi lebih sedikit kehijauan.
# Slider Blue: jika digeser ke arah kiri, akan membuat warna pada foto menjadi agak kekuningan. Sedangkan apabila digeser ke arah kanan, akan membuat warna menjadi kebiruan.
# Menggunakan Hue
# Slider ini digunakan untuk mencari variasi warna pada foto dengan cara menggesernya ke kanan atau ke kiri. Apabila Anda memutuskan untuk memanfaatkan slider ini, maka seluruh warna pada foto akan berubah nuansanya.
# Menggunakan Control Point untuk Mengoreksi Cahaya dan Warna Secara Lokal pada Foto
# Untuk mengoreksi warna dan cahaya, Anda bisa menggunakan dua metode. Pertama, seluruh warna dan cahaya foto dikoreksi secara menyeluruh. Kedua, Anda pilih salah satu area lokal pada foto, misalnya wajah, rambut, atau apapun itu, dan mengoreksi hanya pada area lokal itu saja.
# Untuk menggunakan Control Point, Anda bisa memanfaatkan langkah-langkah sebagai berikut:
# Bukalah terlebih dulu foto yang akan diedit menggunakan Control Point.
# CREDIT FOTO:
# http://www.flickr.com/photos/fox_7357/7629496132/lightbox/
# Pilihlah ikon Add Control Point  yang ada di panel sebelah kanan.
# Klik di dalam area foto yang ingin dikoreksi cahaya dan warnanya. Nanti akan muncul titik lengkap dengan slider-slider yang bisa digunakan untuk memanipulasi cahaya dan warna di sekitar area objek tersebut.
# Geser slider-slider itu sesuai kebutuhan. Huruf-huruf yang ada di tiap-tiap slider berfungsi untuk mengatur tiap-tiap elemen, seperti Br untuk mewakili Brightness dan Co untuk mewakili Contrast, dan seterusnya.
# Jika perlu, Anda bisa membuat control point baru dengan memilih ikon Add Control Point  kembali dan mengarahkan kursor mouse di atas control point tersebut. Klik kalau sudah.
# Lakukan langkah-langkah di atas untuk membuat control point-control point lainnya sesuai kebutuhan.
# Dengan menggunakan control point, Anda bisa mengontrol atau mengoreksi bagian kecil pada sebuah objek. Area lain yang berada di luar jangkauan control point tidak akan terkena editing yang kita lakukan tersebut.
# Mengatur Luas Sempitnya Area Jangkauan Control Point
# Jika control point bisa digunakan untuk mengedit area tertentu pada sebuah objek, maka pertanyaannya seberapa luas jangkauan masing-masing control point itu? Luas sempitnya area jangkauan control point ditentukan oleh lingkaran yang akan muncul saat Anda mengklik 
# titik control point tersebut. Lihatlah gambar di bawah ini untuk melihat keberadaan lingkaran control point itu:
# Lingkaran itu menunjukkan area yang akan ikut dikoreksi kalau kita menggeser slider-slider yang ada di dalam setiap control point. Nah, untuk mengatur ukuran lingkaran itu (mengatur luas sempitnya area yang ingin diedit), cukup gunakan slider pertama (paling atas) yang ada di dalam control point tersebut. Jika digeser ke arah kanan, maka ukuran lingkaran akan semakin membesar, begitu pun sebaliknya.
# Menyatukan Seluruh Control Point Menggunakan Group
# Adakalanya, dua buah control point dibuat untuk mengoreksi area yang berdekatan dengan setting yang mirip. Sebagai contoh, Anda ingin mengedit foto wajah dimana pipi kiri dan kanan tampak gelap. Untuk mengoreksinya, gunakan dua buah control point yang memiliki setting sama. Nah, agar Anda tidak repot, Anda bisa menyatukan dua control point itu dalam satu group sehingga setting yang diterapkan 
# untuk satu control point akan langsung berefek pula pada control point lainnya sehingga mendapatkan setting yang sama.
# Berikut langkah-langkahnya:
# Buatlah dua control point—atau lebih—di tempat yang ingin dikoreksi dengan menggunakan setting yang sama.
# CREDIT FOTO:
# http://www.flickr.com/photos/vinothchandar/5602765430/lightbox/
# Setelah itu, klik-drag membentuk area seleksi berbentuk segi empat untuk menyeleksi control point-control point itu.
# Satukan dengan memilih ikon Group .
# Geser slider-slider itu sesuai kebutuhan. Apabila satu buah slider digeser, maka slider control point yang lain akan ikut tergeser mengikuti gerakan yang kita buat. Dengan demikian, dua titik—atau lebih—control point itu akan berjalan seiringan.
# Jika Anda ingin melepas “ikatan” group pada control point-control point tersebut, tekanlah ikon Ungroup .
# Dengan cara seperti ini, Anda bisa bekerja secara lebih efisien dibanding apabila mengontrol satu control point demi satu control point.
# Mengoreksi Warna dan Cahaya pada Foto Menggunakan Levels dan Curves
# Selain dengan memanfaatkan slider-slider seperti yang sudah dijelaskan di atas, Anda bisa pula mengoreksi warna dan cahaya pada foto menggunakan Levels dan Curves. Ketika Anda mengoreksi warna dan cahaya menggunakan Levels dan Curves, seluruh area foto akan mengalami efek koreksi.
# Berbeda dengan Photoshop yang memisahkan Levels dan Curves dalam dua jendela yang berbeda, Viveza 2 menyatukan dua fitur itu dalam satu panel. Dengan demikian, Anda bisa bekerja dengan Levels dan Curves sekaligus.
# Sedikit Memahami Histogram
# Jika Anda bekerja dengan Levels dan Curves, maka akan sangat sering menemukan histogram. Entah bekerja dengan Photoshop, Viveza 2, atau software lainnya yang berkaitan dengan photo editing, maka histogram merupakan fitur yang selalu ditemukan saat cara memperbaiki cahaya foto digital.
# Histogram pada dasarnya adalah grafik untuk melihat sebaran warna dan cahaya. Cara membacanya adalah: dari kiri ke kanan. Lihat grafik Histogram pada Photoshop di bawah ini (untuk mengaktifkannya, klik menu Window > Histogram):
# Cara membaca histogram di atas adalah sebagai berikut:
# Bagilah grafik di atas menjadi dua bagian.
# Bagian paling tengah disebut dengan istilah Midtones. Bagian tengah-ke kiri adalah Shadows. Sedangkan bagian tengah-ke kanan adalah 
# Highlight.
# Grafik yang berada di area Shadows menunjukkan seberapa kuat area yang gelap atau under exposure. Pada contoh gambar di atas, ditunjukkan grafik yang stabil (rata) sehingga dapat terlihat bahwa foto yang ada di kanvas tidak mengalami under exposure.
# Grafik yang berada di area Highlight menunjukkan seberapa kuat area yang terang atau over exposure. Pada contoh gambar di atas, terdapat indikasi terlalu banyak cahaya di bagian pojok kanan pada grafik histogram. Ini menunjukkan kalau di dalam foto ada bagian-bagian yang over exposure.
# Dengan membaca histogram, maka kita bisa melihat apakah foto yang kita miliki itu mengalami under exposure atau over exposure parah 
# atau tidak. Kata “parah” ditunjukkan dengan munculnya grafik yang mencuat tinggi ke atas.
# 12 Jurus Edit Foto Digital dengan Photoshop CC 2018
# Rp66.800,00
# 101 Tip dan Trik Photoshop CC 2018
# Rp44.800,00
# 40 Kasus Seleksi Photoshop
# Rp70.800,00
# Menggunakan Levels dan Curves untuk Mengoreksi Warna dan Cahaya
# Levels selalu dilengkapi dengan tiga buah anak panah kecil menghadap ke atas yang ada di bawah grafik histogram. Tiga buah anak panah itu mewakili:
# Anak panah sebelah kiri: mengatur shadow pada foto. Apabila shadow ini digeser ke arah kanan, maka foto akan menjadi lebih gelap.   
# Anak panah sebelah kanan: mengatur highlight pada foto. Apabila highlight ini digeser ke arah kiri, maka foto akan menjadi lebih terang.
# Anak panah tengah: mengatur Midtones pada foto. Biasanya, Midtones dipakai untuk menjaga agar foto tidak terlalu over atau under exposure jika shadow dan highlight mengalami pergeseran. Midtones juga dipakai untuk meningkatkan kontras warna pada foto.
# Kalau ingin menggunakan Curves, Anda harus memanfaatkan garis kurva yang disediakan di dalam panel tersebut. Cara pakainya, klik dulu di salah satu tempat pada garis itu sehingga muncul titik. Nah, titik itu bisa digeser ke atas serta ke bawah dan ke kanan dan ke 
# kiri untuk mendapatkan cahaya dan warna yang ideal. Curves itu memiliki hubungan langsung dengan grafik histogram yang ada di bawahnya. Apabila Anda membuat grafik dimana bagian kanan menonjol ke atas dan bagian bawah terpuruk ke bawah (biasa disebut kurva S), maka bagian terang pada foto (highlight) menjadi lebih terang lagi sementara bagian gelap pada foto (shadow) menjadi lebih gelap.      
# Memanfaatkan Brush untuk Mengoreksi Warna dan Cahaya Secara Selektif
# Sama seperti software NIK lainnya, Viveza 2 pun dilengkapi dengan fitur Brush untuk membantu Anda melakukan cara memperbaiki cahaya 
# foto digital dengan koreksi warna dan cahaya secara selektif memakai Brush Tool Photoshop.
# Berikut langkah-langkah memanfaatkan Brush untuk mengoreksi warna dan cahaya secara selektif:
# Editlah sebuah foto menggunakan Viveza 2 terlebih dulu.
# CREDIT FOTO:
# http://www.flickr.com/photos/martinaphotography/6991019825/lightbox/
# Tekan tombol Brush yang ada di bagian kanan bawah pada jendela Viveza 2 tersebut. Setelah itu, Anda akan melihat munculnya layer baru hasil duplikasi dari Layer Background. Lengkap dengan layer mask di dalam layer tersebut.
# Sekarang, dengan menggunakan Brush Tool, sapukan area yang ingin dikoreksi. Bagian yang tidak terkena sapuan brush yang Anda gerakkan akan tetap menjadi bagian foto yang tidak teredit.
# Tekan tombol Apply di dalam panel NIK Software.
# Dengan demikian, ada dua metode untuk mengoreksi foto secara selektif. Pertama adalah dengan menggunakan Control Point sedangkan kedua, lewat metode Brush seperti di atas.