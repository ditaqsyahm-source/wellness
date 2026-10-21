# -*- coding: utf-8 -*-
import os
import json

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
REPO_PATH = os.path.dirname(DIR_PATH)
CURRICULUM_PATH = os.path.join(REPO_PATH, "curriculum")

# 26 Curated Topics for Pillar 1: Sirkadian & Tidur Nyenyak (Senin)
P1_TOPICS = [
    ("Ritme Sirkadian Fajar: Foton Cahaya Membangunkan Jam Master Otak",
     "Bangun tidur masih lemas dan kepala berat? Jangan salahkan jam tidurmu, tapi sinyal foton matamu!",
     "Mata manusia memiliki sel ganglion fotosensitif yang khusus membaca spektrum biru matahari fajar.",
     "Paparan sinar alami sepuluh menit di luar ruangan mengunci jam sirkadian dan memicu lonjakan kortisol alami untuk energi stabil.",
     "Melangkahlah ke luar rumah atau teras sepuluh menit pertama setelah bangun pagi tanpa kacamata hitam.",
     "Matahari fajar adalah tombol start alami bagi seluruh organ tubuhmu. Mulai besok pagi, ingat rahasia ini:",
     "💬 Berapa menit setelah bangun biasanya kamu baru kena sinar matahari langsung? Tulis di bawah! 👇",
     "Dr. Satchin Panda", "The Circadian Code", "Sel ganglion retina ipRGCs mengirim sinyal langsung ke inti suprachiasmatic (SCN)."),
    ("Physiological Sigh: Trik Napas 30 Detik Penurun Detak Jantung",
     "Jantungmu berdebar kencang karena panik mendadak? Lakukan trik napas dua detik ini sekarang juga!",
     "Saat cemas, kantung udara kecil di paru-parumu (alveoli) mengempis dan memicu penumpukan gas karbon dioksida di darah.",
     "Dua tarikan napas cepat lewat hidung diikuti satu hembusan panjang lewat mulut membuka kembali alveoli dan menurunkan nadi seketika.",
     "Tarik napas dalam, tarik sedikit lagi di ujung napas, lalu hembuskan perlahan lewat mulut. Ulangi tiga kali.",
     "Ketenangan sistem sarafmu ada di ujung tarikan napasmu sendiri. Saat kepanikan mulai melanda, ingat trik ini:",
     "💬 Coba tes dua kali tarik napas lalu hembuskan panjang sekarang. Terasa ada beban yang lepas di dada nggak? 👇",
     "Dr. Andrew Huberman", "Stanford Medicine Studies", "Aktivasi alveoli paru-paru memicu barorefleks jantung menurunkan denyut nadi."),
    ("Suhu Kamar 19 Derajat: Kunci Rahasia Masuk Fase Deep Sleep",
     "Sering bolak-balik gelisah dan susah terlelap malam hari? Suhu kamarmu mungkin terlalu hangat!",
     "Otak membutuhkan penurunan suhu inti tubuh sebesar satu derajat celsius untuk memicu gelombang tidur lambat.",
     "Ruangan yang terlalu hangat menghambat pelepasan panas dari telapak tangan dan kaki, menahan otak dalam fase tidur dangkal.",
     "Atur pendingin ruangan di suhu sembilan belas derajat celsius, atau buka ventilasi udara segar agar kamarmu sejuk alami.",
     "Kesejukan udara kamar adalah undangan paling ramah bagi jiwamu untuk beristirahat. Malam ini sebelum tidur, ingat ini:",
     "💬 Kamarmu kalau tidur lebih suka dingin berselimut tebal atau hangat berangin sepoi-sepoi? Tulis di bawah! 👇",
     "Dr. Matthew Walker", "Why We Sleep", "Vasodilatasi kapiler ekstremitas membuang panas tubuh inti ke lingkungan sejuk."),
    ("Mouth Taping: Trik Bernapas Lewat Hidung untuk Tidur Lelap",
     "Bangun tidur dengan tenggorokan kering dan kepala pening? Kamu mungkin tidur dengan mulut terbuka!",
     "Bernapas lewat mulut saat tidur menurunkan kadar oksigen darah hingga dua puluh persen dan memicu dengkuran kasar.",
     "Napas hidung memproduksi gas nitric oxide yang melebarkan pembuluh darah dan menyaring udara masuk secara steril.",
     "Gunakan plester medis berpori mikro secara vertikal di bibir sebelum tidur untuk melatih pernapasan hidung sepanjang malam.",
     "Hidung diciptakan untuk bernapas, mulut diciptakan untuk makan. Malam ini sebelum memejamkan mata, ingat prinsip ini:",
     "💬 Siapa yang kalau bangun tidur tenggorokannya kering banget karena tidur mangap? Berani coba mouth tape? 👇",
     "James Nestor", "Breath: The Lost Art", "Produksi Nitric Oxide (NO) di rongga sinus hidung memaksimalkan saturasi oksigen alveolar."),
    ("Kegelapan Mutlak 100%: Tutup Titik LED di Kamar Tidurmu",
     "Titik lampu LED kecil di colokan atau AC kamarmu itu diam-diam merusak struktur tidur lelapmu!",
     "Kelopak mata manusia sangat tipis dan tetap mampu menyerap foton cahaya buatan bahkan saat terpejam rapat.",
     "Paparan cahaya serendah lima lux di kamar tidur menekan pelepasan hormon melatonin dan meningkatkan resistensi insulin di pagi harinya.",
     "Tutup lampu indikator perangkat elektronik dengan stiker hitam, dan pasang tirai blackout agar kamarmu benar-benar gelap gulita.",
     "Kegelapan pekat adalah sinyal purba bagi tubuhmu untuk meregenerasi sel yang rusak. Sebelum memadamkan lampu malam ini, ingat ini:",
     "💬 Kamarmu kalau tidur gelap gulita tanpa cahaya sama sekali, atau masih ada lampu colokan/HP yang kedap-kedip? 👇",
     "Northwestern Medicine", "PNAS Cardiometabolic Study", "Paparan foton malam hari menekan sintesis melatonin kelenjar pineal."),
    ("Power Nap 20 Menit: Reset Adenosin Tanpa Rasa Pusing",
     "Tidur siang bukannya segar malah bikin kepala pusing dan linglung? Kamu salah mengatur durasinya!",
     "Tidur siang lebih dari tiga puluh menit membuat otakmu masuk ke fase gelombang lambat yang sulit dibangunkan secara mendadak.",
     "Tidur siang taktis tepat dua puluh menit membersihkan akumulasi adenosin di otak tanpa memicu rasa kantuk lanjutan (sleep inertia).",
     "Pasang alarm tepat dua puluh lima menit, rebahkan tubuh di tempat tenang, dan pejamkan mata santai setelah jam makan siang.",
     "Dua puluh menit jeda di tengah hari adalah hak ragamu untuk memperbarui energi. Sebelum melanjutkan pekerjaan siang ini, ingat ini:",
     "💬 Kamu tim yang kalau tidur siang sebentar langsung segar, atau malah bablas sampai magrib terus pusing? 👇",
     "NASA Fatigue Countermeasures", "Alertness Studies", "Penurunan konsentrasi adenosin kognitif pasca 20 menit fase Non-REM ringan."),
]

# 26 Curated Topics for Pillar 2: Meredam Kortisol & Overthinking (Selasa)
P2_TOPICS = [
    ("Berdengung 60 Detik: Trik Menggetarkan Saraf Vagus untuk Tenang",
     "Pikiranmu sedang berputar tanpa henti dan dada terasa sesak? Lakukan getaran suara sederhana ini selama satu menit!",
     "Saraf vagus adalah saraf kranial terpanjang yang melintasi pita suara hingga ke organ jantung dan pencernaan.",
     "Getaran suara berdengung (humming) secara fisik menstimulasi reseptor mekanik di tenggorokan, memicu pelepasan asetilkolin penenang nadi.",
     "Tutup bibirmu rapat, tarik napas dalam lewat hidung, lalu hembuskan perlahan sambil mendengungkan suara rendah selama enam puluh detik.",
     "Suaramu sendiri adalah saklar alami untuk mematikan mode panik di tubuhmu. Saat pikiranmu mulai terlalu berisik, ingat trik ini:",
     "💬 Coba sekarang: tarik napas, lalu dengungkan 'hmmm' panjang di tenggorokan. Terasa ada getaran damai di dada? 👇",
     "Dr. Stephen Porges", "The Polyvagal Theory", "Stimulasi mekanik laring mengaktifkan cabang motorik nervus vagus ke nodus sinoatrial."),
    ("Celupkan Wajah ke Air Dingin: Hentikan Serangan Panik Seketika",
     "Serangan cemas mendadak membuat napasmu memburu? Celupkan wajahmu ke dalam mangkuk air es selama sepuluh detik!",
     "Suhu dingin ekstrem pada area mata dan hidung mengaktifkan refleks biologis mamalia purba (Mammalian Dive Reflex).",
     "Refleks ini secara otomatis memperlambat detak jantung sebesar dua puluh lima persen dan mengalihkan aliran darah ke organ vital.",
     "Isi mangkuk dengan air dingin dan es batu, tahan napas, lalu benamkan wajahmu selama sepuluh hingga lima belas detik.",
     "Tubuhmu memiliki mekanisme penyelamat otomatis yang siap meredakan kepanikanmu. Saat kecemasan memuncak, ingat trik ini:",
     "💬 Pernah coba basuh muka pakai air es pas lagi stres berat? Sensasi dinginnya langsung bikin sadar kan? 👇",
     "Dr. Peter Levine", "Somatic Experiencing", "Aktivasi saraf trigeminal memicu perlambatan detak jantung instan via sistem parasimpatis."),
    ("Pijat Daun Telinga: Titik Relaksasi Saraf Cepat",
     "Pijat lembut lekukan kecil di belakang daun telingamu selama tiga puluh detik! Ini sensasi rileks yang langsung terasa.",
     "Daun telinga luar memiliki cabang saraf auricularis dari saraf vagus yang berada sangat dekat dengan permukaan kulit.",
     "Stimulasi pijatan melingkar lembut di lekukan telinga mengirimkan sinyal penenang ke batang otak untuk mengendurkan otot bahu.",
     "Gunakan ibu jari dan telunjukmu. Buat gerakan memutar perlahan di daun telinga sambil mengambil tiga tarikan napas panjang.",
     "Titik saklar ketenangan tubuhmu ada di dekat telingamu sendiri tanpa butuh obat penenang. Saat kepalamu mulai tegang, ingat titik ini:",
     "💬 Coba pegang dan pijat daun telingamu sekarang. Terasa ada aliran hangat yang bikin rileks nggak? 👇",
     "Frontiers in Neuroscience", "Auricular Vagus Stimulation", "Stimulasi cabang auricularis nervus vagus memodulasi nukleus traktus solitarius."),
    ("Panoramic Vision: Menghentikan Mode Panik Lewat Pandangan Mata",
     "Luaskan sudut pandang matamu ke arah samping sekarang juga! Ini cara tercepat mematikan respon panik di otakmu.",
     "Saat cemas, pandangan matamu terkunci sempit pada satu titik fokus, meniru respon hewani saat sedang terancam bahaya.",
     "Mengaktifkan pandangan melebar (panoramic vision) memberi tahu sirkuit otak bahwa tidak ada ancaman predator di sekitarmu.",
     "Tatap satu titik di depanmu, lalu tanpa menoleh, sadari benda-benda di sudut paling kiri dan paling kanan pandanganmu.",
     "Cara matamu memandang ruangan menentukan cara sistem sarafmu merespons tekanan. Saat pikiranmu mulai menyempit dan tegang, ingat ini:",
     "💬 Coba luaskan pandanganmu sekarang tanpa menoleh kepala. Kamu bisa melihat kedua sudut ruangan sekaligus? 👇",
     "Dr. Andrew Huberman", "Visual System & Autonomic State", "Peralihan dari focal vision ke panoramic vision mendepresiasi aktivasi simpatis amigdala."),
    ("Rahang Mengunci & Bahu Naik: Sinyal Tersembunyi Kortisol Menumpuk",
     "Sadar nggak kalau saat ini rahangmu sedang mengatup kencang dan bahumu terangkat tegang ke arah telinga?",
     "Kortisol kronis membuat otot masseter di rahang dan otot trapezius di leher berada dalam status siaga perang tanpa henti.",
     "Ketegangan otot tanpa henti ini mengirim sinyal balik ke otak bahwa tubuh masih dalam kondisi bahaya, memicu overthinking berkepanjangan.",
     "Buka sedikit bibirmu, biarkan lidahmu menempel rileks di langit-langit mulut, dan jatuhkan bahumu ke bawah dengan sadar.",
     "Fisikmu yang mengendur akan menuntun pikiranmu untuk ikut melepaskan bebannya. Di tengah kesibukan harimu, ingat pesan ini:",
     "💬 Coba cek rahangmu sekarang: gigimu lagi saling menggigit rapat nggak? Lepaskan dan rasakan bedanya! 👇",
     "Dr. Gabor Mate", "When the Body Says No", "Biofeedback kontraksi tonik masseter dan trapezius mempertahankan hiperarousal amigdala."),
    ("Jalan Kaki Tanpa Earphone: Terapi Keheningan yang Dirindukan Otak",
     "Kapan terakhir kali kamu berjalan kaki sendirian tanpa menyumpal telingamu dengan musik atau podcast?",
     "Otak manusia modern mengalami kelebihan stimulasi sensorik audio yang terus-menerus memaksa korteks prefrontal bekerja aktif.",
     "Berjalan dalam keheningan selama lima belas menit memungkinkan Default Mode Network di otak menata kembali ingatan dan meredam kecemasan.",
     "Tinggalkan earphone di saku, berjalanlah dengan santai di sekitar taman atau komplek, dan dengarkan suara langkah kakimu sendiri.",
     "Keheningan bukanlah kekosongan, melainkan ruang tempat jiwamu berbicara jujur. Sore ini saat melangkah pulang, ingat ini:",
     "💬 Kuat nggak jalan kaki 15 menit tanpa dengerin lagu atau video sama sekali? Ceritakan tantanganmu di bawah! 👇",
     "University of Michigan", "Nature Immersion & Cognitive Rest", "Pemberhentian stimulasi auditori eksternal memfasilitasi dekompresi Default Mode Network."),
]

# 26 Curated Topics for Pillar 3: Usus Sehat & Emosi Bersih (Rabu)
P3_TOPICS = [
    ("Sering Cemas Tanpa Sebab? Periksa Ususmu, Bukan Kepalamu!",
     "Sering merasa cemas dan gelisah tiba-tiba padahal tidak ada masalah besar? Sumber masalahnya ada di perutmu!",
     "Sembilan puluh persen hormon serotonin pengendali rasa bahagia diproduksi oleh bakteri baik di dinding usus, bukan di otak.",
     "Saat mikrobioma ususmu meradang akibat makanan olahan, sinyal inflamasi dikirim lewat saraf vagus langsung ke pusat cemas otak.",
     "Mulailah menambahkan satu sendok makanan fermentasi alami seperti tempe mentah atau kimchi ke piring makan siangmu.",
     "Merawat isi perutmu adalah langkah awal paling nyata untuk menenangkan pikiranmu. Sebelum memilih makanan hari ini, ingat ini:",
     "💬 Pernah ngerasa kalau habis makan makanan berminyak/manis suasana hatimu jadi gampang bad mood? 👇",
     "Dr. Emeran Mayer", "The Mind-Gut Connection", "Produksi 90% serotonin perifer oleh sel enterochromaffin usus via mikrobiota seimbang."),
    ("Stop Minuman Diet Zero Sugar: Racun Rahasia Bagi Bakteri Ususmu",
     "Merasa aman minum soda diet karena label nol kalori? Pemanis buatan itu diam-diam merusak keseimbangan mentalmu!",
     "Pemanis buatan seperti sukralosa dan aspartam mengubah komposisi bakteri baik di usus besar menjadi bakteri pemicu radang.",
     "Kondisi disbiosis usus ini menurunkan sensitivitas insulin dan memicu fluktuasi suasana hati serta kecemasan tanpa sebab yang jelas.",
     "Ganti minuman manis buatan dengan air dingin beraroma irisan lemon segar, daun mint, atau seduhan teh hijau tanpa gula.",
     "Apa yang terasa manis di lidah belum tentu membawa kedamaian bagi sel-sel tubuhmu. Sebelum membeli minuman kaleng siang ini, ingat ini:",
     "💬 Kamu masih sering minum minuman berlabel 'Zero Sugar' atau 'Diet'? Yuk jujur di kolom komentar! 👇",
     "Nature Medicine", "Artificial Sweeteners & Gut Dysbiosis", "Perubahan taksonomi filum Bacteroidetes dan Firmicutes akibat senyawa pemanis sintetis."),
    ("Kaldu Tulang (Bone Broth): Obat Alami Lambung dan Dinding Usus",
     "Perut sering kembung, perih, atau begah setelah makan? Lapisan pelindung ususmu mungkin sedang mengalami luka mikro!",
     "Dinding usus manusia hanya setebal satu lapis sel epitel yang mudah merenggang akibat stres kronis dan pola makan buruk.",
     "Asam amino glutamin, prolin, dan kolagen dalam kaldu tulang bekerja merapatkan kembali celah antar sel epitel usus yang bocor.",
     "Nikmati secangkir kaldu tulang hangat dengan sejumput garam mineral di pagi hari sebelum menyantap makanan padat.",
     "Menyembuhkan tubuh dimulai dari memperbaiki fondasi pencernaanmu yang paling dalam. Sebelum sarapan besok pagi, ingat rahasia ini:",
     "💬 Pernah coba minum bone broth hangat pas perut lagi begah atau perih? Rasanya nyaman banget di lambung! 👇",
     "Dr. David Perlmutter", "Brain Maker", "Integritas tight junction epitel usus direstorasi oleh peptida asam amino glutamin dan kolagen."),
    ("Makan Sambil Menatap Layar HP: Mengapa Perutmu Selalu Buncit dan Begah",
     "Makan siang sambil scrolling TikTok atau nonton YouTube? Pantas saja perutmu terasa kembung dan begah seharian!",
     "Mata yang terpaku pada layar gawai memicu respon stres visual mikro yang mematikan fase sefalik pencernaan di lambung.",
     "Enzim pencernaan dan asam lambung gagal disekresi secara optimal, membuat makanan membusuk dan memproduksi gas berlebih di usus.",
     "Jauhkan ponselmu saat piring makanan tersaji di depanmu. Kunyah setiap suapan dua puluh kali dengan kesadaran penuh.",
     "Makan dengan tenang adalah bentuk penghormatan tertinggi bagi ragamu yang lelah. Saat menyantap makan siangmu hari ini, ingat ini:",
     "💬 Jujur, siapa di sini yang nggak bisa makan kalau layarnya nggak nyala nonton video? Ngaku di bawah! 👇",
     "Harvard Health Publishing", "Mindful Eating & Cephalic Digestion", "Hambatan sekresi asam klorida (HCl) lambung akibat distraksi visual simpatis saat makan."),
]

# 26 Curated Topics for Pillar 4: Biohacking Lembut & Slow Living (Kamis)
P4_TOPICS = [
    ("Grounding Kaki Telanjang: Penyembuhan Alami Dari Permukaan Bumi",
     "Kapan terakhir kali telapak kakimu menyentuh tanah basah atau rumput berembun tanpa alas sepatu?",
     "Permukaan bumi menyimpan muatan negatif alami yang kaya akan elektron bebas penyembuh peradangan sel.",
     "Sepatu bersol karet modern mengisolasi tubuh manusia dari kontak listrik bumi, membiarkan radikal bebas menumpuk di jaringan sel.",
     "Lepaskan sandalmu, melangkahlah di atas rumput basah atau tanah berpasir selama sepuluh menit di bawah sinar pagi.",
     "Bumi adalah tempat asal penciptaan ragamu dan penyembuh alami bagi kelelahanmu. Sebelum beraktivitas hari ini, ingat ini:",
     "💬 Rasanya gimana pas telapak kaki telanjang nginjak rumput basah pagi hari? Sejuk dan bikin tenang kan? 👇",
     "Journal of Environmental Health", "Earthing & Free Electron Neutralization", "Transfer elektron bebas transkutan menetralkan spesies oksigen reaktif (ROS) sistemik."),
    ("Urutan Makan Anti-Spike: Jangan Telan Karbohidrat Terlebih Dahulu",
     "Sering merasa sangat mengantuk dan lemas satu jam setelah makan siang? Urutan makanmu keliru fatal!",
     "Karbohidrat sederhana yang masuk ke lambung kosong diserap sangat cepat, memicu lonjakan tajam glukosa dan insulin di darah.",
     "Serat sayuran yang dimakan pertama kali melapisi dinding usus halus, memperlambat pemecahan glukosa dan menjaga energi stabil.",
     "Terapkan aturan baku ini: santap sayuran berserat terlebih dahulu, lanjutkan dengan lauk berprotein, dan akhiri dengan nasi.",
     "Mengatur urutan piringmu adalah biohacking paling sederhana tanpa biaya untuk menjaga fokus harimu. Siang ini saat makan, ingat ini:",
     "💬 Kamu kalau makan biasanya habisin nasinya duluan, sayurnya dulu, atau diaduk campur semua? Tulis di bawah! 👇",
     "Jessie Inchauspe", "Glucose Revolution", "Viscous fiber mesh menghambat difusi glukosa trans-mukosa usus halus mencegah glycemic spike."),
    ("Satu Sendok Cuka Apel: Trik Penjinak Gula Darah Sebelum Makan",
     "Mau makan mie atau makanan berkarbohidrat tinggi tanpa merasa bersalah? Minum ramuan asam lembut ini dua menit sebelumnya!",
     "Asam asetat alami dalam cuka sari apel menonaktifkan sementara enzim alfa-amilase di air liur dan cairan lambung.",
     "Penonaktifan sementara ini memperlambat pemecahan karbohidrat menjadi gula darah hingga tiga puluh persen.",
     "Larutkan satu sendok makan cuka apel murni ke dalam segelas air hangat, minum perlahan sebelum menyantap hidangan utama.",
     "Kearifan herbal kuno selalu menyimpan sains cerdas untuk menjaga keseimbangan tubuhmu. Sebelum menyentuh hidanganmu, ingat trik ini:",
     "💬 Pernah rutin minum cuka apel sebelum makan berat? Sensasi kenyangnya terasa lebih tahan lama kan? 👇",
     "American Diabetes Association", "Acetic Acid & Glycemic Attenuation", "Penghambatan enzim disakaridase usus oleh asam asetat menurunkan puncak kurva insulin."),
    ("Kontraksi Otot Soleus: Membakar Gula Darah Sambil Duduk",
     "Harus duduk berjam-jam di depan komputer setelah makan siang? Aktifkan otot ajaib di betismu ini!",
     "Otot soleus di betis manusia memiliki karakteristik metabolisme unik yang mampu membakar glukosa darah tanpa memicu kelelahan asam laktat.",
     "Mengangkat tumit berulang kali sambil duduk meningkatkan laju oksidasi lemak dan membersihkan glukosa darah hingga lima puluh persen.",
     "Duduk tegak, tempelkan telapak kaki ke lantai, lalu angkat tumitmu ke atas dan turunkan kembali secara ritmis selama sepuluh menit.",
     "Tubuhmu dirancang cerdas untuk terus membakar energi bahkan di sela rutinitas dudukmu. Sambil membaca postingan ini, coba lakukan ini:",
     "💬 Coba gerakkan angkat tumit kakimu naik-turun sekarang sambil duduk. Terasa ada otot betis yang hangat bekerja? 👇",
     "Dr. Marc Hamilton", "University of Houston Soleus Pushup Studies", "Metabolisme oksidatif otot soleus memanfaatkan glukosa sirkulasi lokal tanpa menguras glikogen."),
]

# 26 Curated Topics for Pillar 5: Penyejuk Hati: Muhasabah, Syukur & Tawakal (JUMAT)
P5_TOPICS = [
    ("Saat Hatimu Lelah Berlari: Beri Jiwamu Izin untuk Berhenti Sejenak",
     "Saat langkahmu terasa begitu berat dan hatimu dipenuhi sesak, berhentilah sejenak. Kamu bukan mesin yang tak boleh lelah.",
     "Banyak jiwa menjadi hancur bukan karena beratnya ujian, melainkan karena enggan mengakui bahwa dirinya hanyalah manusia yang rapuh.",
     "Keikhlasan sejati dimulai saat kamu melepaskan kendali atas apa yang memang tidak pernah berada di dalam genggaman tanganmu.",
     "Tarik napas perlahan di hari Jumat yang berkah ini. Ucapkan terima kasih pada ragamu yang telah bertahan sejauh ini, lalu serahkan segalanya pada Tuhan.",
     "Ketenangan batin tidak hadir saat semua masalahmu selesai, melainkan saat hatimu ridha pada ketetapan-Nya. Hari ini, ingat baik-baik hikmah ini:",
     "💬 Kapan terakhir kali kamu duduk diam tanpa memikirkan pekerjaan dan berkata pada dirimu: 'Terima kasih sudah bertahan'? 👇",
     "Hikmah Nabawi & Psikologi Kontemplatif", "Adab Jiwa & Muhasabah Diri", "Penerimaan spiritual mendalam menenangkan sistem limbik dan memutus siklus kecemasan eksistensial."),
    ("Melepas Beban yang Bukan Milikmu: Kunci Ketenangan Kalbu",
     "Berapa banyak beban orang lain yang selama ini kamu paksakan pikul di atas pundakmu yang sudah rapuh?",
     "Kecemasan sering kali lahir dari keinginan ego untuk membahagiakan semua orang dan memperbaiki hal-hal yang bukan tugasmu.",
     "Tawakal yang hakiki adalah kemampuan untuk membedakan antara ikhtiar yang menjadi kewajibanmu, dan takdir yang menjadi hak mutlak Tuhan.",
     "Malam ini, letakkan ransel kekhawatiran itu di atas sajadahmu. Maafkan ketidaksempurnaan harimu, dan biarkan hatimu bernapas lega.",
     "Beban di pundakmu akan terasa ringan saat kamu sadar bahwa alam semesta ini ada yang mengurus dengan sempurna. Ingatlah kebenaran ini:",
     "💬 Hal apa yang belakangan ini paling sering bikin kepalamu pusing padahal sebenarnya di luar kendalimu? Yuk lepas di sini! 👇",
     "Ibnu Qayyim Al-Jauziyyah", "Madarijus Salikin", "Penyerahan tawakal batin mereduksi aktivasi aksis HPA kortisol dan menghadirkan ketenangan kalbu."),
    ("Syukur Atas Hal-Hal Kecil yang Kerap Terlupakan",
     "Kita begitu sibuk meratapi satu pintu yang tertutup, sampai lupa mensyukuri seribu jendela nikmat yang masih terbuka lebar.",
     "Pikiran manusia memiliki bias negatif purba yang selalu memperbesar kekurangan dan membutakan mata dari limpahan rezeki harian.",
     "Satu tarikan napas tanpa rasa sesak, seteguk air sejuk yang membasahi kerongkongan, dan sepasang mata yang masih bisa melihat adalah kemewahan tak ternilai.",
     "Luangkan lima menit sore ini. Tuliskan tiga nikmat paling sederhana yang kamu rasakan hari ini, dan rasakan kehangatan yang mengalir di dadamu.",
     "Kekayaan sejati bukanlah tentang seberapa banyak yang kamu miliki, melainkan seberapa dalam rasa syukur di hatimu. Hari ini, renungi ini:",
     "💬 Apa satu hal paling sederhana hari ini yang bikin kamu merasa sangat bersyukur masih diberi hidup? Tulis di komentar! 👇",
     "Imam Al-Ghazali", "Ihya Ulumuddin: Kitab Asy-Syukr", "Praktik syukur memicu neuroplastisitas positif di ventral striatum otak dan meningkatkan dopamin alami."),
    ("Berdamai dengan Rencana Hidup yang Tidak Sesuai Harapan",
     "Kecewa karena impianmu belum terwujud tahun ini? Barangkali Tuhan sedang menjauhkanmu dari bahaya yang tak kamu ketahui.",
     "Keterbatasan akal manusia sering kali mengira apa yang ia inginkan adalah yang terbaik, padahal pandangannya terhalang tabir masa depan.",
     "Ketenangan jiwa hadir saat kamu percaya bahwa ketetapan Tuhan untukmu selalu jauh lebih indah daripada rencana terbaik yang kamu susun.",
     "Lepaskan rasa sesal atas pintu yang tertutup. Tataplah jalan di depanmu dengan prasangka baik dan senyum yang tulus.",
     "Apa yang ditakdirkan untukmu tidak akan pernah melewatkanmu, dan apa yang melewatkanmu memang bukan milikmu. Renungi pesan sejuk ini:",
     "💬 Pernah nggak kamu baru sadar bertahun-tahun kemudian kalau kegagalan masa lalumu ternyata menyelamatkan hidupmu? Ceritakan! 👇",
     "Ibnu Athaillah As-Sakandari", "Al-Hikam", "Penerimaan takdir (ridha) menstabilkan fluktuasi emosional dan mencegah depresi reaktif."),
]

# 26 Curated Topics for Pillar 6: Pengingat Diri & Melepas Ekspektasi (SABTU)
P6_TOPICS = [
    ("Berhenti Membandingkan Hidupmu dengan Linimasa Orang Lain",
     "Scrolling medsos di akhir pekan bukannya bikin rileks malah bikin insecure dan merasa tertinggal? Matikan layarmu sekarang!",
     "Kamu sedang membandingkan proses di balik layarmu yang berantakan dengan cuplikan terbaik orang lain yang telah dipoles rapi.",
     "Setiap jiwa memiliki garis waktu dan musim mekarnya masing-masing; bunga mawar tidak pernah iri pada bunga melati yang mekar lebih dulu.",
     "Letakkan ponselmu di laci meja sore ini. Tataplah kehidupan nyatamu, rawatlah apa yang ada di hadapanmu dengan penuh cinta.",
     "Kedamaian hidup dimulai saat kamu berhenti mencari validasi dari mata manusia. Mulai akhir pekan ini, ingat baik-baik pesan ini:",
     "💬 Pernah ngerasa sedih atau insecure gara-gara lihat postingan orang lain di medsos? Yuk sadari dan lepas beban itu! 👇",
     "Sosiologi & Psikologi Digital", "Social Comparison Theory", "Penghentian komparasi sosial digital memulihkan harga diri dan meredam kelelahan dopaminergik."),
    ("Menghapus Toxic Productivity: Istirahat Bukanlah Dosa",
     "Merasa bersalah dan cemas saat sedang duduk santai tanpa melakukan pekerjaan apa pun? Jiwamu sedang diracuni ilusi produktivitas beracun!",
     "Dunia modern mendidik manusia untuk mengukur harga dirinya hanya dari seberapa sibuk dan lelah raganya bekerja.",
     "Padahal, pohon terbaik pun membutuhkan musim gugur untuk mengumpulkan getah baru sebelum kembali berbuah lebat di musim semi.",
     "Beri izin pada dirimu untuk rebahan, menikmati secangkir teh hangat, atau sekadar menatap dedaunan tanpa harus menghasilkan karya apa pun.",
     "Kamu berharga karena kamu adalah manusia, bukan karena tumpukan tugas yang kamu selesaikan. Sore ini, nikmati istirahatmu dan ingat ini:",
     "💬 Siapa yang kalau lagi libur rebahan malah kepikiran kerjaan terus ngerasa bersalah? Yuk buang rasa bersalah itu di sini! 👇",
     "Dr. Devon Price", "Laziness Does Not Exist", "Dekonstruksi rasa bersalah somatik memulihkan tonus parasimpatis dan mencegah adrenal exhaustion."),
    ("Seni Merasa Cukup (Qana'ah): Penawar Haus Duniawi yang Melelahkan",
     "Merasa hidupmu selalu kurang dan terus mengejar standar yang tak pernah ada ujungnya? Jiwamu hanya butuh rasa cukup.",
     "Nafsu manusia ibarat meminum air laut; semakin banyak diteguk, semakin membakar rasa haus di kerongkonganmu.",
     "Qana'ah adalah benteng ketenangan batin yang membuatmu merasa kaya raya meskipun hanya memiliki sepiring nasi dan atap berteduh.",
     "Tataplah orang-orang yang berada di bawahmu dalam urusan materi dunia, agar hatimu tidak meremehkan nikmat Tuhan yang melimpah padamu.",
     "Kekayaan yang hakiki bukanlah banyaknya harta benda, melainkan jiwa yang merasa cukup atas segala pemberian. Renungi hikmah ini:",
     "💬 Apa satu hal sederhana di rumahmu hari ini yang bikin kamu merasa: 'Alhamdulillah, hidupku sebenarnya sudah sangat cukup'? 👇",
     "Kearifan Sufistik Klasik", "Konsep Qana'ah & Zuhud", "Pergeseran lokus evaluasi dari eksternal ke internal mereduksi stres finansial kronis."),
]

# 26 Curated Topics for Pillar 7: Penyejuk Jiwa: Jeda Suci & Istirahat Total (MINGGU)
P7_TOPICS = [
    ("Keheningan Sepertiga Malam: Rumah Bagi Jiwa yang Hampa",
     "Pernahkah kamu terbangun di keheningan sepertiga malam saat seluruh dunia terlelap sunyi? Itu bukan sekadar kebetulan biologis.",
     "Keheningan fajar adalah saat gelombang elektromagnetik bumi berada pada titik paling tenang dan doa menembus langit tanpa hijab.",
     "Duduklah di tepi tempat tidurmu, basuh wajahmu dengan air dingin yang sejuk, dan ceritakan seluruh luka hatimu pada Sang Maha Mendengar.",
     "Di saat tidak ada manusia yang mengerti bebanmu, Tuhan selalu membuka pintu bagi hamba-Nya yang bersujud dalam hening.",
     "Air mata yang jatuh dalam keheningan malam adalah pembersih terbaik bagi jiwa yang lelah mengarungi debu dunia. Ingatlah kebenaran ini:",
     "💬 Pernah nggak bangun jam 3 pagi terus duduk hening berdoa sambil menangis lega? Rasanya seperti beban terangkat semua ya? 👇",
     "Tradisi Kontemplasi Fajar", "Sufism & Night Vigil (Tahajjud)", "Kombinasi keheningan akustik malam dan kesadaran spiritual meningkatkan pelepasan melatonin dan endorfin."),
    ("Hak Tubuh untuk Rehat: Menyongsong Pekan Baru dengan Hati Tenang",
     "Sebelum besok kembali menghadapi rutinitas dunia yang bising, malam ini berikan tubuhmu haknya untuk beristirahat penuh.",
     "Ragamu adalah amanah pinjaman dari Sang Pencipta; jangan zalimi ia dengan memaksanya memikirkan hal-hal yang belum terjadi esok hari.",
     "Rebahkan punggungmu di atas kasur, lepaskan seluruh ambisi dan kekhawatiran pekan depan, dan pasrahkan takdirmu pada perlindungan-Nya.",
     "Tidurlah dengan hati yang bersih dari rasa benci, pikiran yang tenang dari rasa cemas, dan bibir yang membasahi doa kepulangan.",
     "Malam ini tidurlah dengan tenang, karena Yang Menjaga hidupmu tidak pernah mengantuk dan tidak pernah tidur. Selamat beristirahat:",
     "💬 Sebelum pejamkan mata malam ini, yuk maafkan semua orang yang sempat bikin kamu kesal pekan ini biar tidurmu pulas. Bisa? 👇",
     "Etika Jiwa & Restorasi Tidur", "Sunnah & Sleep Hygiene", "Relaksasi neuromuskular total yang didasari pelepasan beban psikologis memperdalam fase delta sleep."),
    ("Menemukan Damai di Tengah Badai Kehidupan",
     "Kedamaian sejati bukanlah ketiadaan badai di sekelilingmu, melainkan ketenangan di dalam hatimu saat badai sedang berkecamuk.",
     "Dunia ini memang tempat ujian dan kelelahan; mencari kesempurnaan di bumi adalah kesia-siaan yang hanya melahirkan luka batin.",
     "Saat kapal hidupmu diguncang ombak cobaan, jangkar terbaik adalah kepasrahan kalbu kepada Yang Maha Menguasai lautan.",
     "Tarik napas panjang di malam Minggu ini. Apapun yang terjadi besok, yakinlah bahwa kamu tidak pernah berjalan sendirian.",
     "Kekuatan jiwamu terletak pada seberapa erat hatimu bersandar pada perlindungan Tuhan. Sebelum mematikan lampumu malam ini, ingatlah ini:",
     "💬 Apa doa atau harapan terbesarmu untuk menyongsong pekan yang baru besok pagi? Tuliskan harapan baikmu di bawah! 👇",
     "Psikologi Transpersonal", "Inner Peace in Chaos", "Kekuatan resiliensi spiritual menstabilkan tonus vagal dan mencegah kecemasan antisipatif."),
]

def generate_packet_data(day_num):
    day_in_week = day_num % 7  # 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat, 0=Sun
    week_num = (day_num - 1) // 7 + 1
    cycle_num = week_num

    if day_in_week == 1:
        # Senin: P1 - Sirkadian
        t = P1_TOPICS[(week_num - 1) % len(P1_TOPICS)]
        pillar_id = "P1"
        pillar_name = "Ritme Sirkadian & Arsitektur Tidur Dalam"
        cat_badge = "🌿 RITME SIRKADIAN & RESET SEMANGAT"
    elif day_in_week == 2:
        # Selasa: P2 - Meredam Kortisol & Overthinking
        t = P2_TOPICS[(week_num - 1) % len(P2_TOPICS)]
        pillar_id = "P2"
        pillar_name = "Regulasi Saraf & Meredam Overthinking"
        cat_badge = "🧠 SOMA-BATIN: MEREDAM OVERTHINKING"
    elif day_in_week == 3:
        # Rabu: P3 - Usus Sehat & Emosi Bersih
        t = P3_TOPICS[(week_num - 1) % len(P3_TOPICS)]
        pillar_id = "P3"
        pillar_name = "Kesehatan Usus & Kejernihan Emosi"
        cat_badge = "🍵 RAGA-EMOSI: USUS SEHAT & HATI TENANG"
    elif day_in_week == 4:
        # Kamis: P4 - Biohack Lembut & Slow Living
        t = P4_TOPICS[(week_num - 1) % len(P4_TOPICS)]
        pillar_id = "P4"
        pillar_name = "Biohacking Lembut & Seni Melambat"
        cat_badge = "🍃 SLOW LIVING: BIOHACK LEMBUT RP 0"
    elif day_in_week == 5:
        # Jumat: P5 - Penyejuk Hati: Muhasabah & Hikmah
        t = P5_TOPICS[(week_num - 1) % len(P5_TOPICS)]
        pillar_id = "P5"
        pillar_name = "Penyejuk Hati: Muhasabah, Ikhlas & Tawakal"
        cat_badge = "🕯️ PENYEJUK HATI: MUHASABAH & TAWAKAL"
    elif day_in_week == 6:
        # Sabtu: P6 - Pengingat Diri: Melepas Ekspektasi
        t = P6_TOPICS[(week_num - 1) % len(P6_TOPICS)]
        pillar_id = "P6"
        pillar_name = "Pengingat Diri: Melepas Beban Ekspektasi"
        cat_badge = "🕊️ PENGINGAT DIRI: HAPUS TOXIC PRODUCTIVITY"
    else:
        # Minggu (0): P7 - Penyejuk Jiwa: Jeda Suci & Istirahat Total
        t = P7_TOPICS[(week_num - 1) % len(P7_TOPICS)]
        pillar_id = "P7"
        pillar_name = "Penyejuk Jiwa: Jeda Suci & Istirahat Total"
        cat_badge = "🌙 PENYEJUK JIWA: JEDA SUCI & ISTIRAHAT TOTAL"

    title, hook, why, mechanism, protocol, loop_end, friction, expert, pub, hf_spec = t
    clean_title = f"{title.split('?')[0].split('!')[0].strip()} 🌿✨"

    packet = {
        "metadata": {
            "channel_id": "DITA-03",
            "channel_name": "Dita Gentle Wellness & Penyejuk Hati",
            "handle": "@ditawellness",
            "day_number": day_num,
            "cycle_number": cycle_num,
            "cycle_theme": pillar_name,
            "topic_pillar_id": pillar_id,
            "topic_pillar_name": pillar_name,
            "narrative_format_id": "F5" if "Penyejuk" in pillar_name else "F1",
            "narrative_format_name": "Refleksi Jiwa & Penyejuk Hati" if "Penyejuk" in pillar_name else "Protokol Harian Siap Tiru",
            "emotional_trigger": "Kedamaian Batin & Restorasi Alami" if "Penyejuk" in pillar_name else "Pencerahan Menenangkan & Solusi Biologis Tanpa Biaya",
            "visual_pacing": "Transisi Sinematik Estetik Zen menuju Visual Sains dan Kalbu yang Tenang",
            "target_duration_range": "48-53 detik",
            "cta_hook_type": "Simpan Renungan & Praktikkan Hari Ini",
            "target_audience": "Profesional muda, pekerja kantoran, pria & wanita usia 22-45 tahun",
            "created_by": "Content Research & Narrative Architect (@content-researcher)",
            "reviewed_by": "Herman (Command Point / CEO)",
            "intended_executor": "Director (@fullmontage) & Fleet Operator (@social-operator)"
        },
        "scientific_research_dossier": {
            "core_topic": title,
            "academic_citations": [
                {
                    "author": expert,
                    "publication": pub,
                    "key_findings": f"{why} {mechanism}"
                }
            ],
            "psychological_mechanism_breakdown": {
                "neurobiological_state": mechanism,
                "cognitive_limitation": "Kebiasaan modern sering mengabaikan panggilan istirahat alami raga dan ketenangan jiwa.",
                "common_trap": why,
                "solution_formula": protocol
            }
        },
        "script_architecture_breakdown": {
            "anatomy": [
                {
                    "segment_id": "SEG_01",
                    "phase": "Thumb-Stopping Shock Hook",
                    "timestamp_range": "00:00 - 00:05",
                    "duration_seconds": 5,
                    "spoken_text": hook,
                    "word_count": len(hook.split()),
                    "visual_direction": "Kamera gerak lambat estetik: sudut ruangan tenang, fajar pagi atau twilight. Bebas wajah frontal. Teks peringatan kontras emas-merah di sepertiga atas layar.",
                    "audio_design": {
                        "voice_inflection": "Tegas, bersahabat, intim, scroll-stopping.",
                        "sfx": "Sub-bass soft impact thud pada detik 0.0.",
                        "bgm": "Petikan dawai akustik dan ambient synth lembut."
                    }
                },
                {
                    "segment_id": "SEG_02",
                    "phase": "Emotional & Biological Anchor",
                    "timestamp_range": "00:05 - 00:16",
                    "duration_seconds": 11,
                    "spoken_text": why,
                    "word_count": len(why.split()),
                    "visual_direction": "Close-up macro estetik: seduhan teh, cangkir keramik, atau dedaunan basah berembun dengan pencahayaan alami.",
                    "audio_design": {
                        "voice_inflection": "Empatik, menenangkan, mengurai rasa lemas atau cemas yang dirasakan penonton.",
                        "sfx": "Whoosh lembut pada transisi cut visual.",
                        "bgm": "Alunan dawai mengalir hangat."
                    }
                },
                {
                    "segment_id": "SEG_03",
                    "phase": "HyperFrames Scientific Mechanism",
                    "timestamp_range": "00:16 - 00:32",
                    "duration_seconds": 16,
                    "spoken_text": mechanism,
                    "word_count": len(mechanism.split()),
                    "visual_direction": f"Klip animasi vektor HyperFrames / Estetika Zen: {hf_spec}",
                    "audio_design": {
                        "voice_inflection": "Jernih, edukatif berwibawa, membuka wawasan biologis dan kalbu penonton.",
                        "sfx": "Chime rendah lembut dan suara desau alam.",
                        "bgm": "Harmoni piano ambient mengembang anggun."
                    }
                },
                {
                    "segment_id": "SEG_04",
                    "phase": "Actionable Rp 0 Micro-Routine",
                    "timestamp_range": "00:32 - 00:43",
                    "duration_seconds": 11,
                    "spoken_text": protocol,
                    "word_count": len(protocol.split()),
                    "visual_direction": "Gestur tangan tanpa wajah yang mempraktikkan protokol sehat atau bersedekap tenang di alam.",
                    "audio_design": {
                        "voice_inflection": "Hangat, mengajak aksi konkret dan ketenangan batin tanpa beban.",
                        "sfx": "Foley alami (gemericik air, gesekan dedaunan, uap teh).",
                        "bgm": "Melodi semakin rileks dan menenangkan."
                    }
                },
                {
                    "segment_id": "SEG_05",
                    "phase": "Empowerment & Seamless Loop Climax",
                    "timestamp_range": "00:43 - 00:52",
                    "duration_seconds": 9,
                    "spoken_text": loop_end,
                    "word_count": len(loop_end.split()),
                    "visual_direction": "Outro Card Zen Dita Gentle Wellness & Penyejuk Hati dengan palet sage green & emas, bersiap menyambung ulang ke detik ke-0.",
                    "audio_design": {
                        "voice_inflection": "Menutup tuntas dan mengalir mulus ke kalimat pembuka.",
                        "sfx": "Bell chime zen lembut di ujung video.",
                        "bgm": "Fade-out anggun yang beresonansi harmonis."
                    }
                }
            ]
        },
        "verbatim_script_master": {
            "full_spoken_text_id": f"{hook} {why} {mechanism} {protocol} {loop_end}",
            "target_audio_duration_seconds": 50.5,
            "word_count": len(f"{hook} {why} {mechanism} {protocol} {loop_end}".split()),
            "friction_comment_question": friction
        },
        "social_fleet_distribution_metadata": {
            "title": f"{clean_title} #Shorts",
            "youtube_shorts_title": f"{clean_title[:85]} #Shorts",
            "caption_instagram_tiktok": (
                hook + "\n\n" +
                "Secara mendalam: " + why + " " + mechanism + "\n\n" +
                "🌿 Renungan & Protokol Hari Ini:\n" + protocol + "\n\n" +
                friction + "\n\n" +
                "Simpan video ini biar nggak lupa, dan share ke orang tersayang yang butuh ketenangan raga & jiwa hari ini! ✨\n\n" +
                "#ditawellness #gentlewellness #penyejukhati #ketenanganbatin #muhasabah #biohackingindonesia #hidupsehatalami #polahidupsehat #sainskesehatan"
            ),
            "hook_category": cat_badge,
            "tags": ["DitaWellness", "PenyejukHati", "KetenanganBatin", "Biohacking", "Muhasabah", "GentleWellness", "Shorts"]
        }
    }
    return packet

def main():
    print("Generating holistic curriculum for Days 005 to 180...")
    count = 0
    for day in range(5, 181):
        packet = generate_packet_data(day)
        day_str = f"{day:03d}"
        file_path = os.path.join(CURRICULUM_PATH, f"content_packet_day_{day_str}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(packet, f, indent=2, ensure_ascii=False)
        count += 1
    print(f"Successfully generated {count} holistic content packets (Day 005 to Day 180)!")

if __name__ == "__main__":
    main()
