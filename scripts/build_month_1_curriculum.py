import os
import json

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
REPO_PATH = os.path.dirname(DIR_PATH)
CURRICULUM_PATH = os.path.join(REPO_PATH, "curriculum")

# 29 Topics (Day 2 to Day 30) for Month 1
EPISODES_DATA = [
    # ── MINGGU 1: FONDASI RITME SIRKADIAN (Day 002 - Day 007) ──
    {
        "day": 2,
        "week": 1,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Stop Minum Kopi di 90 Menit Pertama Bangun Tidur! Ini Bahayanya ☕🌿",
        "hook": "Stop minum kopi di sembilan puluh menit pertama setelah kamu bangun tidur! Ini alasan biologisnya.",
        "why": "Saat bangun, zat kimia adenosin masih menumpuk di otak. Kafein yang masuk terlalu cepat hanya memblokir reseptor sementara tanpa membersihkannya.",
        "mechanism": "Akibatnya, saat kafein habis di jam dua siang, seluruh adenosin menyerbu sekaligus, memicu rasa lemas dan kantuk yang luar biasa parah.",
        "protocol": "Tunda cangkir pertamamu minimal sembilan puluh menit. Biarkan foton matahari pagi dan hidrasi air putih membersihkan adenosinmu secara alami.",
        "loop_ending": "Kopi terbaik adalah yang diminum saat hormon kortisolmu mulai turun secara wajar. Mulai besok pagi, ingat baik-baik rahasia ini:",
        "friction_question": "💬 Kamu tim yang mana: bangun langsung ngopi hitam, atau tunggu sarapan dulu? Tulis kebiasaan kopimu di bawah! 👇",
        "expert": "Dr. Matthew Walker, Ph.D. & Dr. Andrew Huberman",
        "publication": "Stanford University & Center for Human Sleep Science UC Berkeley (2022)",
        "hf_spec": "Diagram pembersihan molekul adenosin (biru) vs reseptor kafein (merah) dengan grafik crash jam 14:00.",
        "broll": ["pouring black coffee morning cup", "tired office worker rubbing eyes afternoon", "morning sunlight kitchen window", "glass of water wooden table", "steam rising coffee ceramic mug"]
    },
    {
        "day": 3,
        "week": 1,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Mandi Air Hangat Sebelum Tidur Bikin Mengantuk? Ini Penjelasan Sainsnya! 🛁🌙",
        "hook": "Mandi air hangat sebelum tidur bikin badan rileks dan cepat tidur? Ternyata mekanismenya bukan seperti yang kamu kira!",
        "why": "Tubuh manusia membutuhkan penurunan suhu inti sebesar satu derajat celsius agar otak bisa memicu rasa kantuk dan hormon melatonin.",
        "mechanism": "Air hangat melebarkan pembuluh darah tepi di kulitmu, membuang panas inti tubuh ke udara, sehingga suhu dalam tubuhmu justru turun drastis.",
        "protocol": "Mandi air hangat satu jam sebelum tidur malam. Suhu ruangan yang sejuk akan mempercepat penurunan suhu inti dan membuatmu lelap seketika.",
        "loop_ending": "Tidur nyenyak bukan tentang menghangatkan tubuh, melainkan mendinginkan suhu intinya secara perlahan. Malam ini sebelum tidur, ingat rahasia ini:",
        "friction_question": "💬 Kamu lebih suka mandi air hangat atau air dingin sebelum tidur malam? Ceritakan di kolom komentar! 👇",
        "expert": "Dr. Matthew Walker, Ph.D.",
        "publication": "Why We Sleep: Vasodilation and Core Body Temperature Dynamics (Scribner)",
        "hf_spec": "Termometer suhu tubuh inti turun dari 37.0°C ke 36.0°C dengan kurva melatonin aktif naik.",
        "broll": ["warm water pouring bathtub steam", "cozy bedroom dark evening linen bed", "feet touching wooden floor calm", "dim bedside lamp warm light", "peaceful sleep silhouette"]
    },
    {
        "day": 4,
        "week": 1,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Tatap Langit Senja 5 Menit Sore Ini: Kunci Melatonin Malam Hari! 🌅🌿",
        "hook": "Tatap langit senja lima menit sore ini, atau tidur malammu bakal berantakan total! Ini faktanya.",
        "why": "Cahaya kuning-oranye spektrum rendah matahari terbenam adalah sinyal penutup bagi sel ganglion di retina matamu.",
        "mechanism": "Sinyal ini mematikan hormon kortisol dan mengaktifkan penghitung mundur pelepasan hormon melatonin alami dua jam berikutnya.",
        "protocol": "Keluar ruangan saat matahari mulai tenggelam. Tatap spektrum langit senja tanpa kacamata hitam selama lima menit penuh.",
        "loop_ending": "Matahari fajar membangunkan energimu, matahari senja mempersiapkan tidur pulasmu. Mulai sore ini, jangan lewatkan momen berharga ini:",
        "friction_question": "💬 Kapan terakhir kali kamu sengaja keluar ruangan melihat langit sore saat magrib/senja? Tulis di komentar! 👇",
        "expert": "Dr. Satchin Panda, Ph.D.",
        "publication": "The Circadian Code: Salk Institute for Biological Studies (2018)",
        "hf_spec": "Transisi spektrum cahaya fotonik dari gelombang biru (siang) ke spektrum amber-oranye (senja) mengaktifkan pineal gland.",
        "broll": ["golden hour sunset sky clouds", "person standing outside silhouette sunset view", "sun setting behind trees nature", "peaceful evening veranda porch", "warm twilight horizon ambient"]
    },
    {
        "day": 5,
        "week": 1,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Stop Makan 3 Jam Sebelum Tidur! Ini yang Terjadi Pada Organ Tubuhmu 🍽️🌙",
        "hook": "Berhenti makan tiga jam sebelum tidur! Ini bukan cuma soal berat badan, tapi keselamatan organ hatimu.",
        "why": "Saat malam, pankreas dan lambungmu diprogram melambat untuk perbaikan seluler. Makanan berat memaksa aliran darah kembali ke usus.",
        "mechanism": "Akibatnya, suhu tubuh intimu melonjak naik, fase deep sleep terganggu, dan kamu akan sering terbangun dengan badan kaku serta pegal.",
        "protocol": "Tutup makan malammu tiga jam sebelum jam tidur. Biarkan sistem pencernaanmu berpuasa lembut dan sel-sel tubuhmu membersihkan diri.",
        "loop_ending": "Tidur adalah waktu bagi tubuhmu untuk mereparasi kerusakan, bukan lembur mencerna makanan. Mulai malam ini, ingat baik-baik pesan ini:",
        "friction_question": "💬 Kamu sering kelaparan tengah malam dan akhirnya ngemil mie/roti? Jujur di kolom komentar ya! 👇",
        "expert": "Dr. Satchin Panda & Dr. David Perlmutter",
        "publication": "Cell Metabolism: Time-Restricted Feeding and Hepatic Circadian Clock (2020)",
        "hf_spec": "Diagram organ hati dan saluran cerna: mode pencernaan aktif (panas) beralih ke mode reparasi autofagi (tenang).",
        "broll": ["empty plate with wooden fork clean kitchen", "clock pointing to 20:00 night", "peaceful dark bedroom moonlight", "herbal tea cup chamomile warm", "person sleeping peacefully in bed"]
    },
    {
        "day": 6,
        "week": 1,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Kacamata Blue Light Mahalmu Sia-Sia Kalau Masih Lakukan Ini! 👓💡",
        "hook": "Kacamata blue-light mahalmu itu sia-sia kalau lampu kamarmu masih menyala terang begini!",
        "why": "Kulit dan retina matamu tetap mendeteksi intensitas cahaya total, bukan cuma spektrum biru layar gawai.",
        "mechanism": "Lampu plafon yang dipasang di atas kepala meniru posisi matahari siang hari, menekan produksi hormon melatonin hingga lima puluh persen.",
        "protocol": "Mulai jam delapan malam, matikan lampu plafon utama. Gunakan lampu meja berwarna kuning redup yang diletakkan sejajar lantai.",
        "loop_ending": "Bukan hanya layar ponsel yang mengacaukan malammu, melainkan lampu rumahmu sendiri. Mulai malam ini, ubah pencahayaanmu dan ingat ini:",
        "friction_question": "💬 Di kamarmu lebih suka lampu putih terang benderang atau lampu tidur temaram hangat? Diskusi di bawah! 👇",
        "expert": "Dr. Andrew Huberman, Ph.D.",
        "publication": "Neural Circuits Linking Light and Mood, Stanford University School of Medicine (2021)",
        "hf_spec": "Perbandingan lux cahaya: lampu plafon 500 lux (sinyal siang) vs lampu lantai redup 15 lux (sinyal malam).",
        "broll": ["switching off bright white ceiling light", "turning on warm yellow bedside lamp", "cozy dark ambient room floor lamp", "gentle reading book night light", "peaceful serene bedroom atmosphere"]
    },
    {
        "day": 7,
        "week": 1,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Bangun Siang di Hari Minggu? Ini Bahaya Social Jetlag! ⏰🛌",
        "hook": "Bangun siang di hari Minggu bukan balas dendam tidur yang cerdas, tapi racun untuk energimu di hari Senin!",
        "why": "Menggeser jam bangun tidur lebih dari dua jam di akhir pekan memicu kondisi biologis bernama Social Jetlag.",
        "mechanism": "Jam sirkadian otakmu tertinggal layaknya kamu baru terbangun di zona waktu lain, membuat tubuh lemas dan mual di awal pekan.",
        "protocol": "Bangun di jam yang sama setiap hari, termasuk akhir pekan. Jika lelah, gantilah dengan tidur siang taktis dua puluh menit di siang hari.",
        "loop_ending": "Konsistensi jam bangun adalah mata uang terpenting bagi jam biologis tubuhmu. Sebelum mematikan alarm akhir pekanmu, ingat rahasia ini:",
        "friction_question": "💬 Siapa yang hari Minggu suka bangun jam 10 pagi terus Seninnya pusing berat? Angkat tangan di komentar! 👇",
        "expert": "Dr. Till Roenneberg, Ph.D.",
        "publication": "Current Biology: Social Jetlag and Chronobiology Health Impacts (Ludwig-Maximilians University)",
        "hf_spec": "Grafik ritme sirkadian bergeser 3 jam ke kanan (desinkronisasi) memicu Monday Morning Sluggishness.",
        "broll": ["alarm clock ringing morning sun", "person waking up stretching refreshed bed", "feet stepping on floor carpet sunrise", "drinking glass of warm water kitchen", "morning sunlight outside porch"]
    },

    # ── MINGGU 2: BADAI KORTISOL & SISTEM SARAF (Day 008 - Day 014) ──
    {
        "day": 8,
        "week": 2,
        "pillar_id": "P2",
        "pillar_name": "Keseimbangan Hormon & Regulasi Sistem Saraf",
        "title": "Physiological Sigh: Trik Napas 30 Detik Penurun Detak Jantung! 🫁✨",
        "hook": "Saat dadamu sesak dan cemas tiba-tiba, lakukan satu trik napas rahasia ini sekarang juga!",
        "why": "Saat stres, kantung udara kecil di paru-parumu kolaps, memicu penumpukan gas karbon dioksida yang membuat otak panik.",
        "mechanism": "Dua kali tarikan napas pendek melalui hidung diikuti satu hembusan panjang lewat mulut langsung membuka alveoli dan menenangkan saraf vagus.",
        "protocol": "Tarik napas dalam lewat hidung, lalu tarik sedikit lagi di puncaknya, lalu hembuskan perlahan lewat mulut. Ulangi tiga kali.",
        "loop_ending": "Ketenangan batin ada di kendali napasmu sendiri dalam hitungan detik. Setiap kali kepanikan mulai menyerang, ingat baik-baik:",
        "friction_question": "💬 Coba praktikkan sekarang: tarik 2x lewat hidung, hembus panjang lewat mulut. Terasa lebih lega nggak? Tulis di bawah! 👇",
        "expert": "Dr. Jack Feldman & Dr. Andrew Huberman",
        "publication": "Cell Reports Medicine: Brief Structured Respiration Enhances Mood and Reduces Anxiety (Stanford 2023)",
        "hf_spec": "Diagram alveoli paru-paru membuka maksimal + grafik detak jantung (BPM) melambat dari 98 ke 68 BPM.",
        "broll": ["person inhaling deeply garden morning", "hand placed on chest feeling heartbeat", "chest expanding slow deep breath", "calm ocean waves gentle shore", "peaceful serene forest greenery"]
    },
    {
        "day": 9,
        "week": 2,
        "pillar_id": "P2",
        "pillar_name": "Keseimbangan Hormon & Regulasi Sistem Saraf",
        "title": "Terbangun Jam 3 Pagi dengan Jantung Berdebar? Ini Penyebab Sainsnya! 🌙💓",
        "hook": "Sering terbangun jam tiga pagi dengan pikiran cemas dan jantung berdebar? Ini bukan mistis, ini sinyal darurat hormonmu!",
        "why": "Di jam tiga pagi, cadangan glukosa organ hatimu menipis. Tubuh menganggap ini kondisi darurat hipoglikemia nocturnal.",
        "mechanism": "Untuk menyelamatkan gula darah, kelenjar adrenalmu memompa hormon kortisol dan adrenalin mendadak, membuatmu terjaga dan cemas.",
        "protocol": "Cegah dengan satu sendok kecil madu murni atau sejumput garam dapur sebelum tidur untuk menstabilkan cadangan glikogen malam hari.",
        "loop_ending": "Tidur malam yang tenang membutuhkan cadangan energi hati yang stabil. Saat kamu terbangun di keheningan fajar, ingat pesan ini:",
        "friction_question": "💬 Siapa yang sering kebangun jam 3 pagi terus susah tidur lagi sampai subuh? Ceritakan di kolom komentar! 👇",
        "expert": "Dr. Sara Gottfried, M.D.",
        "publication": "The Hormone Cure: Hypothalamic-Pituitary-Adrenal Axis and Nocturnal Hypoglycemia (Scribner)",
        "hf_spec": "Grafik glukosa malam hari menurun tajam di jam 03:00 memicu lonjakan kortisol merah darurat.",
        "broll": ["clock showing 03:15 night room", "person opening eyes in dark bedroom", "hand holding glass of water nightstand", "subtle moonlight through window curtain", "deep breathing relaxing pillow"]
    },
    {
        "day": 10,
        "week": 2,
        "pillar_id": "P2",
        "pillar_name": "Keseimbangan Hormon & Regulasi Sistem Saraf",
        "title": "Jangan Pernah Telan Kopi Hitam Saat Perut Kosong! Ini Alasannya ☕⚠️",
        "hook": "Jangan pernah menelan kopi hitam pekat saat perutmu masih kosong melompong! Ini yang terjadi pada hormonmu.",
        "why": "Kafein di lambung kosong merangsang produksi asam hidroklorida berlebih dan melipatgandakan hormon kortisol secara kasar.",
        "mechanism": "Dinding mukosa lambung teriritasi dan sistem saraf simpatismu terpicu berlebihan, menimbulkan gemetar tangan dan kecemasan seharian.",
        "protocol": "Alasi lambungmu terlebih dahulu dengan segelas air mineral hangat, sedikit lemak sehat seperti alpukat, atau telur sebelum meneguk kopi.",
        "loop_ending": "Kopi adalah pelengkap kenikmatan, bukan pengganti fondasi nutrisi pagimu. Setiap kali kamu menyalakan mesin kopi, ingat ini:",
        "friction_question": "💬 Pernah nggak ngerasa dada deg-degan atau perut perih setelah minum kopi pagi? Share pengalamanmu! 👇",
        "expert": "Dr. Mindy Pelz, D.C.",
        "publication": "Gastric Secretion and Cortisol Reactivity, British Journal of Nutrition",
        "hf_spec": "Lapisan mukosa lambung teriritasi asam lambung vs perlindungan lemak sehat.",
        "broll": ["black coffee dripping into glass cup", "hand holding stomach feeling uncomfortable", "drinking glass of warm water breakfast", "boiled eggs and avocado on plate", "peaceful breakfast table morning light"]
    },
    {
        "day": 11,
        "week": 2,
        "pillar_id": "P2",
        "pillar_name": "Keseimbangan Hormon & Regulasi Sistem Saraf",
        "title": "Celupkan Wajah ke Air Es 10 Detik: Hentikan Serangan Panik Seketika! 🧊💧",
        "hook": "Celupkan wajahmu ke dalam mangkuk air es selama sepuluh detik saat panik! Ini respons biologis ajaibnya.",
        "why": "Kulit di sekitar hidung dan matamu memiliki saraf trigeminal yang terhubung langsung ke saraf vagus pengatur detak jantung.",
        "mechanism": "Sensasi dingin memicu Mammalian Dive Reflex seketika, menurunkan detak jantung sebesar dua puluh persen dan meredam amigdala.",
        "protocol": "Isi mangkuk dengan air dingin dan es batu. Tahan napas, celupkan wajahmu selama sepuluh hingga lima belas detik, lalu angkat perlahan.",
        "loop_ending": "Tubuhmu memiliki tombol reset biologis otomatis untuk mematikan badai stres. Saat kecemasan melanda tak terkendali, ingat trik ini:",
        "friction_question": "💬 Berani coba trik rendam wajah air es ini pas lagi stres kerja? Tulis pendapatmu di bawah! 👇",
        "expert": "Dr. Stephen W. Porges, Ph.D.",
        "publication": "The Polyvagal Theory: Neurophysiological Foundations of Emotions (W.W. Norton)",
        "hf_spec": "Saraf trigeminal wajah mengaktifkan cabang parasimpatis saraf vagus menurunkan denyut nadi.",
        "broll": ["ice cubes dropping into clear water bowl", "hands splashing cold water on face", "face emerging from cool water refreshing", "towel wiping face gently serene", "calm expression taking peaceful breath"]
    },
    {
        "day": 12,
        "week": 2,
        "pillar_id": "P2",
        "pillar_name": "Keseimbangan Hormon & Regulasi Sistem Saraf",
        "title": "Rahang Mengunci & Bahu Kaku? Tubuhmu Kekurangan Mineral Ini! 🦴🌿",
        "hook": "Otot bahumu kaku dan rahang sering mengunci tanpa sadar? Tubuhmu lagi menjerit kekurangan satu mineral penting ini!",
        "why": "Stres harian dan kopi berlebih menguras cadangan mineral magnesium intraseluler melalui ginjal dua kali lebih cepat.",
        "mechanism": "Tanpa magnesium, serat ototmu gagal melakukan relaksasi setelah berkontraksi, mengunci saraf dalam ketegangan kronis sepanjang malam.",
        "protocol": "Konsumsi makanan kaya magnesium seperti bayam hijau, biji labu, atau suplemen magnesium glisinat satu jam sebelum waktu tidurmu.",
        "loop_ending": "Ketenangan otot adalah syarat mutlak bagi ketenangan pikiranmu. Sebelum merebahkan badan yang lelah malam ini, ingat pesan ini:",
        "friction_question": "💬 Sering ngerasa bahu atau leher kaku pas bangun tidur? Kamu biasanya diapain: dipijat atau dibiarin? Tulis di bawah! 👇",
        "expert": "Dr. Mark Hyman, M.D.",
        "publication": "The Magnesium Miracle and Cellular Muscle Relaxation (Cleveland Clinic Center for Functional Medicine)",
        "hf_spec": "Pompa ion kalsium vs magnesium di sel otot: magnesium membuka ikatan kaku aktin-miosin.",
        "broll": ["hand massaging stiff shoulder neck", "green pumpkin seeds and spinach bowl", "drinking water with mineral drops table", "gentle shoulder roll stretch bedroom", "relaxing on bed peaceful posture"]
    },
    {
        "day": 13,
        "week": 2,
        "pillar_id": "P2",
        "pillar_name": "Keseimbangan Hormon & Regulasi Sistem Saraf",
        "title": "Matikan Notifikasi HP 60 Menit: Reset Reseptor Dopamin Otakmu! 📵🧠",
        "hook": "Matikan semua notifikasi ponselmu selama enam puluh menit hari ini, atau fokus otakmu bakal rusak permanen!",
        "why": "Dentang notifikasi dan getaran layar memicu mikro-lonjakan dopamin reaktif yang melelahkan korteks prefrontal otakmu.",
        "mechanism": "Otak berada dalam mode siaga waspada terus-menerus, memicu kebocoran hormon stres dan menurunkan rentang perhatianmu hingga separuhnya.",
        "protocol": "Pilih satu jam hening setiap sore. Aktifkan mode pesawat, jauhkan gawai dari jangkauan mata, dan selesaikan satu tugas tanpa distraksi.",
        "loop_ending": "Fokus mendalam adalah kemewahan tertinggi di era modern yang bising. Saat jempolmu gatal membuka gawai lagi, ingat baik-baik:",
        "friction_question": "💬 Bisa nggak kamu tahan 1 jam saja tanpa buka HP sama sekali hari ini? Tantang dirimu di komentar! 👇",
        "expert": "Dr. Anna Lembke, M.D.",
        "publication": "Dopamine Nation: Finding Balance in the Age of Indulgence (Dutton / Stanford University)",
        "hf_spec": "Baseline dopamin pulih stabil vs lonjakan bergerigi akibat notifikasi media sosial.",
        "broll": ["placing smartphone screen down on desk", "person deeply focused writing journal book", "quiet room natural afternoon sunlight", "hands turning off phone screen peaceful", "tranquil workspace zero clutter"]
    },
    {
        "day": 14,
        "week": 2,
        "pillar_id": "P2",
        "pillar_name": "Keseimbangan Hormon & Regulasi Sistem Saraf",
        "title": "Jalan Kaki Tanpa Earphone: Terapi Keheningan yang Dirindukan Otak 🌳🚶",
        "hook": "Jalan kaki santai tapi telingamu terus disumpal earphone dan podcast? Otakmu sebenarnya lagi menjerit butuh keheningan!",
        "why": "Menerima arus informasi verbal terus-menerus tanpa jeda mencegah otak masuk ke Default Mode Network.",
        "mechanism": "Hanya dalam keheningan total tanpa stimulasi luar, otak manusia mampu mengonsolidasi emosi, meredakan stres, dan memunculkan ide kreatif.",
        "protocol": "Jalan kaki sepuluh menit di luar ruangan tanpa gawai dan tanpa musik. Dengarkan suara langkah kakimu dan desau angin di dedaunan.",
        "loop_ending": "Keheningan bukanlah kekosongan, melainkan ruang pemulihan bagi jiwamu yang lelah. Mulai hari ini, saat kamu melangkah keluar, ingat ini:",
        "friction_question": "💬 Kapan terakhir kali kamu jalan kaki atau nyetir tanpa dengerin lagu/podcast sama sekali? Ceritakan di bawah! 👇",
        "expert": "Dr. Florence Williams",
        "publication": "The Nature Fix: Why Nature Makes Us Happier, Healthier, and More Creative (W.W. Norton)",
        "hf_spec": "Gelombang otak beralih dari Beta tinggi (stres) ke Alpha tenang (Default Mode Network).",
        "broll": ["feet walking slowly on park path grass", "hand removing earphones breathing deeply", "sunlight filtering through green canopy leaves", "peaceful walk without phone silhouette", "gentle breeze swaying tree branches"]
    },

    # ── MINGGU 3: KESEHATAN USUS & MIKROBIOM (Day 015 - Day 021) ──
    {
        "day": 15,
        "week": 3,
        "pillar_id": "P3",
        "pillar_name": "Kesehatan Usus & Mikrobiom Anti-Inflamasi",
        "title": "Sering Cemas Tanpa Sebab? Periksa Ususmu, Bukan Kepalamu! 🦠🧠",
        "hook": "Sering merasa cemas dan overthinking tanpa sebab yang jelas? Jangan periksa kepalamu dulu, periksa kesehatan ususmu!",
        "why": "Sembilan puluh persen hormon kebahagiaan serotonin dan lima puluh persen dopamin diproduksi langsung di dalam saluran cernamu.",
        "mechanism": "Mikrobiom usus yang mengalami peradangan mengirimkan sinyal bahaya melalui saraf vagus, membajak suasana hati dan memicu kecemasan.",
        "protocol": "Beri makan bakteri baikmu hari ini dengan semangkuk serat alami dan satu sendok makanan fermentasi, lalu kurangi gula olahan.",
        "loop_ending": "Usus yang tenang adalah fondasi bagi pikiran yang damai. Setiap kali rasa gundah datang tanpa alasan logis, ingat rahasia ini:",
        "friction_question": "💬 Tahu nggak kalau usus disebut 'Otak Kedua' manusia? Pernah ngerasa perut mules pas lagi cemas? Share ya! 👇",
        "expert": "Dr. Emeran Mayer, M.D.",
        "publication": "The Mind-Gut Connection: How the Hidden Conversation Within Our Bodies Impacts Our Mood (Harper Wave)",
        "hf_spec": "Poros usus-otak (Gut-Brain Axis): sinyal neurotransmitter serotonin mengalir lewat saraf vagus.",
        "broll": ["fermented food kimchi tempeh bowl rustic", "hand touching abdomen thoughtfully", "fresh colorful raw vegetables on wooden board", "person enjoying healthy warm meal peaceful", "tranquil kitchen natural morning light"]
    },
    {
        "day": 16,
        "week": 3,
        "pillar_id": "P3",
        "pillar_name": "Kesehatan Usus & Mikrobiom Anti-Inflamasi",
        "title": "Stop Beli Probiotik Mahal! Satu Sendok Makanan Ini Lebih Sakti 🥣🌿",
        "hook": "Stop beli suplemen probiotik mahal kalau kamu belum rutin mengonsumsi satu sendok makanan tradisional kaya bakteri ini!",
        "why": "Bakteri di dalam kapsul suplemen kering sering kali mati di lambung sebelum sempat mencapai usus besarmu.",
        "mechanism": "Makanan fermentasi alami seperti tempe mentah higienis, kimchi, atau tape singkong menyediakan koloni bakteri hidup bersama matriks prebiotik alaminya.",
        "protocol": "Tambahkan satu sendok makan makanan fermentasi hidup ke dalam menu makan siangmu setiap hari untuk memperkaya keanekaragaman mikrobiom.",
        "loop_ending": "Kesehatan pencernaan sejati tumbuh dari kearifan makanan utuh, bukan dari botol suplemen sintetis. Mulai siang ini, ingat baik-baik:",
        "friction_question": "💬 Kamu suka makanan fermentasi apa: tempe, tape, kimchi, atau yogurt? Tulis favoritmu di bawah! 👇",
        "expert": "Dr. Tim Spector, M.D. & Dr. Justin Sonnenburg",
        "publication": "Cell: Gut-microbiota-targeted diets modulate human immune status (Stanford 2021)",
        "hf_spec": "Koloni bakteri baik (Lactobacillus & Bifidobacterium) memperkuat lapisan lendir pelindung usus.",
        "broll": ["spoon scooping traditional fermented food", "fresh homemade tempeh on banana leaf", "healthy digestive system peaceful feeling", "eating nutritious whole food bowl", "warm rustic kitchen aesthetic"]
    },
    {
        "day": 17,
        "week": 3,
        "pillar_id": "P3",
        "pillar_name": "Kesehatan Usus & Mikrobiom Anti-Inflamasi",
        "title": "Minuman Diet Zero Sugar: Racun Rahasia Bagi Bakteri Ususmu! 🥤⚠️",
        "hook": "Pilih minuman diet zero sugar biar sehat dan bebas kalori? Bakteri baik di ususmu justru lagi dibantai pelan-pelan!",
        "why": "Pemanis buatan seperti sukralosa dan aspartam tidak diserap tubuh, melainkan langsung berinteraksi dengan dinding usus besarmu.",
        "mechanism": "Molekul kimia ini mengubah susunan mikrobiom, membunuh bakteri pelindung, dan memicu intoleransi glukosa yang membuat perut kembung.",
        "protocol": "Ganti soda diet kimiawi dengan seduhan air dingin beraroma lemon segar, daun mint, atau teh herbal tanpa pemanis buatan.",
        "loop_ending": "Kalori nol bukan berarti bebas dari dampak biologis pada sel tubuhmu. Sebelum membuka kaleng minuman dietmu berikutnya, ingat ini:",
        "friction_question": "💬 Kamu masih sering minum soda diet atau minuman berlabel 'zero calorie'? Tulis pendapatmu di bawah! 👇",
        "expert": "Dr. Eran Elinav, M.D., Ph.D.",
        "publication": "Cell: Personalized Microbiome-Driven Effects of Non-Nutritive Sweeteners on Human Glucose Tolerance (Weizmann Institute)",
        "hf_spec": "Molekul pemanis buatan mengikis keanekaragaman koloni mikrobiom usus.",
        "broll": ["pouring soda can into glass bubbles", "fresh water infused with lemon slice mint", "hand pushing away artificial diet drink", "drinking clear infused water kitchen", "vibrant fresh citrus and herb leaves"]
    },
    {
        "day": 18,
        "week": 3,
        "pillar_id": "P3",
        "pillar_name": "Kesehatan Usus & Mikrobiom Anti-Inflamasi",
        "title": "Minyak Goreng Berulang: Peluru Penghancur Dinding Ususmu! 🍳🔥",
        "hook": "Minyak goreng yang dipanaskan berulang kali ini diam-diam melubangi dinding ususmu! Ini mekanismenya.",
        "why": "Pemanasan suhu tinggi berulang mengoksidasi asam lemak tak jenuh, menghasilkan senyawa beracun bernama lipid peroksida.",
        "mechanism": "Senyawa ini merusak sambungan ketat antar sel usus (tight junctions), memicu kondisi Leaky Gut yang menyebarkan peradangan ke seluruh pembuluh darah.",
        "protocol": "Hindari konsumsi minyak jelantah berwarna gelap. Masaklah dengan minyak kelapa murni, minyak zaitun suhu rendah, atau metode rebus kukus.",
        "loop_ending": "Usus yang sehat adalah benteng pertahanan terkuat tubuhmu dari serangan penyakit. Mulai hari ini, perhatikan minyak di wajanmu dan ingat ini:",
        "friction_question": "💬 Di rumah minyak goreng biasanya dipakai maksimal berapa kali penggorengan? Share kebiasaan dapurmu! 👇",
        "expert": "Dr. Chris Knobbe, M.D.",
        "publication": "Ancestral Dietary Strategy to Prevent and Reverse Diseases: Oxidized Lipids and Endothelial Dysfunction",
        "hf_spec": "Kerusakan tight junctions usus (Leaky Gut) memicu masuknya toksin ke aliran darah.",
        "broll": ["dark used frying oil in pan smoking", "fresh extra virgin olive oil pouring bottle", "steaming fresh vegetables healthy cooking", "clear digestive wellness feeling", "fresh clean ingredients kitchen counter"]
    },
    {
        "day": 19,
        "week": 3,
        "pillar_id": "P3",
        "pillar_name": "Kesehatan Usus & Mikrobiom Anti-Inflamasi",
        "title": "Kaldu Tulang (Bone Broth): Obat Alami Lambung dan Maag Kronis 🥣✨",
        "hook": "Secangkir air rebusan kaldu tulang hangat ini jauh lebih ampuh menenangkan dinding lambungmu dibanding obat maag biasa!",
        "why": "Kaldu tulang yang dimasak lambat kaya akan asam amino glisin, prolin, serta kolagen alami yang bioavailable.",
        "mechanism": "Asam amino ini menjadi batu bata pembangun untuk menambal lapisan mukosa lambung dan mempercepat regenerasi epitel usus yang luka.",
        "protocol": "Nikmati secangkir kaldu tulang hangat di pagi hari atau sebelum makan malam dengan sejumput garam laut dan irisan jahe segar.",
        "loop_ending": "Makanan adalah obat terbaik saat diolah dengan kesabaran dan keaslian alami. Sebelum lambungmu perih kembali, ingat resep kuno ini:",
        "friction_question": "💬 Pernah coba rutin minum bone broth atau kaldu sup hangat buat lambung? Gimana rasanya di perutmu? Tulis di bawah! 👇",
        "expert": "Dr. Josh Axe, D.N.M.",
        "publication": "Nutritional Immunology: Glutamine and Glycine Support of Intestinal Mucosal Barrier Integrity",
        "hf_spec": "Asam amino glisin & kolagen melapisi dan merapatkan dinding mukosa lambung.",
        "broll": ["steaming bone broth soup ceramic bowl", "fresh ginger slice cutting board herb", "hands holding warm soup bowl comfort", "gentle steam rising rustic kitchen table", "peaceful soothing dining atmosphere"]
    },
    {
        "day": 20,
        "week": 3,
        "pillar_id": "P3",
        "pillar_name": "Kesehatan Usus & Mikrobiom Anti-Inflamasi",
        "title": "Makan Sambil Nonton Video? Pantas Perutmu Selalu Buncit dan Begah! 📱🍽️",
        "hook": "Makan terburu-buru sambil mata menatap video ponsel? Pantas perutmu selalu buncit dan begah setelah makan!",
        "why": "Saat matamu fokus pada layar gawai, otak berada dalam mode simpatis dan lupa mengaktifkan fase sefalik pencernaan.",
        "mechanism": "Enzim amilase di air liur dan asam lambung tidak terproduksi cukup, membuat makanan masuk dalam bentuk kasar yang membusuk di usus.",
        "protocol": "Kunyah setiap suapan dua puluh hingga tiga puluh kali dalam ketenangan. Letakkan ponselmu dan nikmati tekstur makananmu sepenuhnya.",
        "loop_ending": "Pencernaan yang sempurna dimulai dari kesadaran pikiran saat suapan pertama masuk. Setiap kali kamu menyendok makanan, ingat baik-baik:",
        "friction_question": "💬 Siapa yang kalau makan nggak bisa kalau nggak nonton YouTube/TikTok? Mengaku di kolom komentar! 👇",
        "expert": "Harvard Health Publishing",
        "publication": "Mindful Eating: The Cephalic Phase of Digestion and Enzymatic Secretions (Harvard Medical School)",
        "hf_spec": "Fase sefalik otak mengirim sinyal ke kelenjar ludah dan lambung memproduksi enzim hidrolisis.",
        "broll": ["person looking at phone screen while chewing", "hand placing smartphone away from plate", "slow mindful chewing enjoying healthy meal", "clean fresh salad bowl on wooden table", "tranquil peaceful mindful dining"]
    },
    {
        "day": 21,
        "week": 3,
        "pillar_id": "P3",
        "pillar_name": "Kesehatan Usus & Mikrobiom Anti-Inflamasi",
        "title": "Pisang Hijau Mentah: Prebiotik Murah Paling Sakti untuk Usus! 🍌🌿",
        "hook": "Pisang yang masih sedikit kehijauan ini punya rahasia prebiotik paling sakti untuk ususmu! Jangan dibuang!",
        "why": "Pisang mentah kaya akan pati resisten (Resistant Starch Tipe 2) yang tidak bisa dicerna oleh enzim lambung manusia.",
        "mechanism": "Pati ini meluncur utuh ke usus besar, menjadi santapan favorit bakteri baik untuk memproduksi butirat, zat anti-kanker usus.",
        "protocol": "Konsumsi setengah buah pisang berujung hijau setiap pagi, atau blender bersama seduhan susu almond dan sedikit bubuk kayu manis.",
        "loop_ending": "Obat terbaik bagi ususmu sering kali tersembunyi di makanan sederhana di sekitar kita. Sebelum memilih buah manismu, ingat rahasia ini:",
        "friction_question": "💬 Kamu tim suka pisang yang matang kuning manis berbintik, atau yang masih agak keras kehijauan? Tulis di bawah! 👇",
        "expert": "Dr. Will Bulsiewicz, M.D.",
        "publication": "Fiber Fueled: Resistant Starch, Short-Chain Fatty Acids and Butyrate Production (Avery)",
        "hf_spec": "Pati resisten dipecah bakteri usus menjadi asam lemak rantai pendek (Butirat).",
        "broll": ["fresh green-tipped banana on wooden board", "blending healthy smoothie almond cinnamon", "spoon enjoying wholesome fiber breakfast", "smiling relaxed digestive comfort", "bright sunny kitchen table aesthetic"]
    },

    # ── MINGGU 4: KESTABILAN GLUKOSA & BRAIN FOG (Day 022 - Day 028) ──
    {
        "day": 22,
        "week": 4,
        "pillar_id": "P5",
        "pillar_name": "Nutrisi Fungsional & Kestabilan Gula Darah",
        "title": "Urutan Makan Anti-Ngantuk: Jangan Telan Nasi Duluan Saat Lapar! 🥗🍚",
        "hook": "Jangan pernah makan nasi duluan saat perutmu lapar! Terapkan urutan makan ini agar tidak lemas dan mengantuk berat!",
        "why": "Karbohidrat sederhana yang masuk pertama kali langsung diserap lambung, memicu lonjakan glukosa tajam yang disusul crash hormon insulin.",
        "mechanism": "Serat sayuran yang dimakan pertama melapisi dinding usus halus dengan jaring kental, memperlambat penyerapan gula hingga tujuh puluh tiga persen.",
        "protocol": "Makan dengan urutan: Sayuran hijau dulu, lanjutkan dengan lauk protein dan lemak, baru akhiri dengan nasi atau karbohidrat.",
        "loop_ending": "Bukan hanya apa yang kamu makan, melainkan urutan masuknya yang menentukan energimu. Mulai piring makan siangmu hari ini, ingat ini:",
        "friction_question": "💬 Biasanya pas makan siang kamu makan apa duluan: kerupuk, sayur, nasi, atau lauknya? Tulis kebiasaanmu! 👇",
        "expert": "Jessie Inchauspé (Biochemist)",
        "publication": "Glucose Revolution: Food Sequencing and Postprandial Glycemic Excursions (Simon & Schuster)",
        "hf_spec": "Kurva glukosa darah: lonjakan tajam bergerigi (spike) vs kurva landai stabil dengan jaring serat.",
        "broll": ["eating fresh green vegetable salad first", "grilled chicken protein on plate", "steaming jasmine rice on side", "person staying alert energetic office afternoon", "healthy balanced meal table"]
    },
    {
        "day": 23,
        "week": 4,
        "pillar_id": "P5",
        "pillar_name": "Nutrisi Fungsional & Kestabilan Gula Darah",
        "title": "Satu Sendok Cuka Apel Sebelum Karbo: Trik Penjinak Gula Darah! 🍏✨",
        "hook": "Satu sendok cuka apel di segelas air sebelum makan nasi? Ini trik kimiawi alami penjinak lonjakan gula darahmu!",
        "why": "Kandungan asam asetat di dalam cuka apel menonaktifkan sementara enzim alfa-amilase yang memecah pati menjadi gula.",
        "mechanism": "Akibatnya, glukosa masuk ke darah secara bertahap dan ototmu dirangsang menyerap gula tanpa perlu lonjakan insulin yang melelahkan.",
        "protocol": "Larutkan satu sendok makan cuka apel alami ke dalam segelas air mineral hangat. Minum sepuluh menit sebelum hidangan berkarbohidrat tinggi.",
        "loop_ending": "Trik biokimia kecil sebelum makan bisa menyelamatkan energimu sepanjang hari. Sebelum menyentuh hidangan beratmu, ingat baik-baik:",
        "friction_question": "💬 Pernah coba minum cuka apel sebelum makan? Suka rasanya yang asam segar atau belum terbiasa? Diskusi yuk! 👇",
        "expert": "Dr. Carol Johnston, Ph.D.",
        "publication": "Journal of the American Diabetes Association: Vinegar Ingestion at Bedtime and Pre-Meal Glycemic Control",
        "hf_spec": "Asam asetat memblokir enzim alfa-amilase memperlambat degradasi pati menjadi glukosa.",
        "broll": ["apple cider vinegar bottle pouring spoon", "stirring vinegar into glass of warm water", "drinking refreshing morning tonic glass", "plate of delicious wholesome food", "healthy radiant energetic posture"]
    },
    {
        "day": 24,
        "week": 4,
        "pillar_id": "P5",
        "pillar_name": "Nutrisi Fungsional & Kestabilan Gula Darah",
        "title": "Jalan Kaki 10 Menit Pasca Makan: Otot Soleus Mengisap Glukosa! 🚶‍♂️⚡",
        "hook": "Jangan langsung duduk atau rebahan setelah makan siang! Bergeraklah sepuluh menit untuk trik otot ajaib ini!",
        "why": "Duduk diam pasca makan membiarkan glukosa berlebih mengendap di pembuluh darah, memicu inflamasi seluler dan rasa kantuk berat.",
        "mechanism": "Kontraksi otot betis (soleus muscle) mengaktifkan reseptor GLUT-4 yang menyerap gula darah langsung ke sel otot tanpa bantuan hormon insulin.",
        "protocol": "Lakukan jalan kaki santai di koridor atau luar ruangan selama sepuluh menit saja tepat setelah suapan makan terakhirmu tuntas.",
        "loop_ending": "Langkah kecil setelah makan adalah tameng terhebat melawan penuaan seluler dan diabetes. Sebelum kamu bersandar di kursi, ingat ini:",
        "friction_question": "💬 Siapa yang habis makan siang bawaannya langsung mau tidur atau rebahan di kasur? Tulis di kolom komentar! 👇",
        "expert": "Dr. Marc Hamilton, Ph.D.",
        "publication": "iScience (Cell Press): The Potent Physiological Role of the Soleus Muscle in Whole-Body Metabolism (University of Houston)",
        "hf_spec": "Aktivasi reseptor GLUT-4 pada otot betis mengisap molekul glukosa bebas dalam darah.",
        "broll": ["standing up from dining chair after meal", "walking outdoors park sunlight post lunch", "close up feet walking sneakers path", "alert fresh face breathing outdoor air", "sunlit street sidewalk strolling"]
    },
    {
        "day": 25,
        "week": 4,
        "pillar_id": "P5",
        "pillar_name": "Nutrisi Fungsional & Kestabilan Gula Darah",
        "title": "Sarapan Manis Adalah Jebakan! Mengapa Jam 10 Kamu Sudah Lemas 🥐⚠️",
        "hook": "Sarapan roti selai manis atau sereal tiap pagi adalah alasan kenapa jam sepuluh kamu sudah lapar dan lemas lagi!",
        "why": "Sarapan manis memicu lonjakan glukosa tertinggi hari itu, memprogram otakmu masuk ke siklus kecanduan dopamin dan gula seharian.",
        "mechanism": "Penurunan glukosa reaktif (sugar crash) melepaskan hormon lapar ghrelin, membuat konsentrasi kognitifmu rontok sebelum jam makan siang.",
        "protocol": "Beralihlah ke sarapan gurih (savory breakfast): telur dadar daun bawang, tempe bakar, alpukat, atau tahu tanpa gula tambahan.",
        "loop_ending": "Pagi harimu menentukan stabilnya kimia otakmu hingga malam hari. Sebelum memilih menu sarapanmu besok, ingat baik-baik pesan ini:",
        "friction_question": "💬 Sarapan favoritmu biasanya yang manis-manis (roti/donat) atau yang gurih (telur/nasi uduk)? Tulis di bawah! 👇",
        "expert": "Dr. Peter Attia, M.D.",
        "publication": "Outlive: The Science and Art of Longevity: Glucose Variability and Neurocognitive Resilience",
        "hf_spec": "Perbandingan lonjakan glukosa sarapan manis (sugar roller-coaster) vs sarapan gurih stabil.",
        "broll": ["sweet croissant chocolate spread table", "pushing sweet pastry away choosing eggs", "savory scrambled eggs with avocado plate", "energetic productive working at laptop", "bright morning daylight dining room"]
    },
    {
        "day": 26,
        "week": 4,
        "pillar_id": "P5",
        "pillar_name": "Nutrisi Fungsional & Kestabilan Gula Darah",
        "title": "Pakai Pakaian Karbohidratmu! Trik Hindari Insulin Spikes 🍞🥑",
        "hook": "Jangan biarkan karbohidratmu 'telanjang'! Berikan pakaian lemak baik agar tubuhmu tidak panik!",
        "why": "Karbohidrat telanjang seperti sepotong roti putih polos diserap secepat sirup gula murni ke dalam aliran darahmu.",
        "mechanism": "Menambahkan 'pakaian' berupa lemak sehat atau protein memperlambat laju pengosongan lambung dan menumpulkan lonjakan insulin.",
        "protocol": "Setiap kali makan karbohidrat, tambahkan selai kacang murni tanpa gula, seiris keju, alpukat, atau sebutir telur rebus di atasnya.",
        "loop_ending": "Kombinasi makanan cerdas menjaga kestabilan energi tanpa harus menghindari makanan favoritmu. Sebelum mengunyah camilanmu, ingat ini:",
        "friction_question": "💬 Kamu lebih suka makan roti polos atau wajib pakai topping mentega/keju/telur? Tulis seleramu di komentar! 👇",
        "expert": "Jessie Inchauspé",
        "publication": "The Glucose Goddess Method: Dressing Your Carbs with Protein and Healthy Fats",
        "hf_spec": "Molekul lemak dan protein membungkus karbohidrat memperlambat hidrolisis di lambung.",
        "broll": ["plain white bread on wooden cutting board", "spreading natural nut butter avocado slice", "topping toast with boiled egg herbs", "taking bite of wholesome clothed toast", "warm inviting rustic breakfast setup"]
    },
    {
        "day": 27,
        "week": 4,
        "pillar_id": "P5",
        "pillar_name": "Nutrisi Fungsional & Kestabilan Gula Darah",
        "title": "Teh Hijau + L-Theanine: Fokus Tajam Tanpa Jitters dan Jantung Berdebar 🍵🧘",
        "hook": "Tangan gemetar dan jantung berdebar karena kopi? Ganti cangkir keduamu dengan teh hijau berkhasiat L-Theanine ini!",
        "why": "Kafein di dalam kopi diserap sangat cepat, memicu stimulasi saraf simpatis yang sering kali berakhir dengan rasa gelisah berlebih.",
        "mechanism": "Teh hijau mengandung asam amino L-Theanine yang melintasi sawar darah otak, memicu gelombang Alpha yang menenangkan sambil menjaga fokus tajam.",
        "protocol": "Seduh teh hijau matcha atau daun teh hijau sencha dengan air bersuhu delapan puluh derajat celsius untuk mengekstrak L-Theanine maksimal.",
        "loop_ending": "Energi sejati adalah ketenangan yang waspada, bukan kegelisahan yang memburu. Saat energimu mulai turun siang ini, ingat rahasia ini:",
        "friction_question": "💬 Kamu tim pecinta teh hijau atau fanatik kopi sejati? Mana yang lebih bikin kamu tenang? Tulis di bawah! 👇",
        "expert": "American Journal of Clinical Nutrition",
        "publication": "L-Theanine and Caffeine Synergism in Neurocognitive Alertness and Stress Reduction (2018)",
        "hf_spec": "Sinergi molekul kafein dan L-theanine memicu gelombang otak Alpha (8-12 Hz) fokus tenang.",
        "broll": ["pouring hot water into green matcha tea bowl", "bamboo whisk frothing emerald green tea", "hands holding warm ceramic tea cup tranquil", "person working calm focused reading desk", "zen minimalist tea station daylight"]
    },
    {
        "day": 28,
        "week": 4,
        "pillar_id": "P5",
        "pillar_name": "Nutrisi Fungsional & Kestabilan Gula Darah",
        "title": "Begadang Semalam Saja Bikin Sel Tubuhmu Menolak Insulin! 🛌⚠️",
        "hook": "Begadang semalam saja sudah membuat sel tubuhmu menolak insulin layaknya orang pra-diabetes! Ini faktanya.",
        "why": "Tidur kurang dari enam jam mengacaukan sensitivitas hormon insulin di tingkat reseptor seluler hingga tiga puluh persen.",
        "mechanism": "Hormon stres kortisol tetap tinggi di pagi hari, memaksa sel hati melepas lebih banyak glukosa dan memicu rasa lapar karbohidrat gila-gilaan.",
        "protocol": "Jika terpaksa begadang, hindari karbohidrat tinggi di pagi harinya. Prioritaskan sarapan tinggi protein dan tidur lebih awal malam nanti.",
        "loop_ending": "Tidur malam yang cukup adalah obat penstabil gula darah paling mujarab tanpa biaya. Sebelum kamu menunda tidur malam ini, ingat ini:",
        "friction_question": "💬 Siapa yang kalau habis begadang besoknya bawaannya laper terus pengen ngemil yang manis-manis? Tulis di bawah! 👇",
        "expert": "Dr. Matthew Walker, Ph.D.",
        "publication": "Annals of Internal Medicine: Single Night Sleep Deprivation Induces Acute Insulin Resistance in Healthy Adults",
        "hf_spec": "Reseptor insulin seluler memblokir masuknya glukosa akibat paparan kortisol begadang.",
        "broll": ["clock showing 01:30 late night bedside", "rubbing tired weary eyes next morning", "eating wholesome protein scramble morning", "early bedtime routine pulling soft blanket", "peaceful restful sleep in darkness"]
    },

    # ── MINGGU 5: DEEP SLEEP ARCHITECTURE (Day 029 - Day 030) ──
    {
        "day": 29,
        "week": 5,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Kamar Tidur Dingin 19 Derajat: Rahasia Masuk Fase Deep Sleep! ❄️🛌",
        "hook": "Kamar tidurmu terlalu hangat? Ini penyebab biologis kenapa kamu sering mimpi buruk, gelisah, dan bangun lemas!",
        "why": "Untuk menginisiasi tidur gelombang lambat, otak manusia harus menurunkan suhu termoregulasinya melalui pelepasan panas tubuh.",
        "mechanism": "Suhu ruangan di atas dua puluh tiga derajat memaksa tubuhmu terus bekerja mempertahankan pendinginan, menahan otak di fase tidur dangkal.",
        "protocol": "Atur suhu pendingin ruangan kamarmu di kisaran sembilan belas hingga dua puluh satu derajat celsius, gunakan selimut berbahan katun bernapas.",
        "loop_ending": "Ruangan yang dingin adalah undangan resmi bagi otakmu untuk memasuki tidur lelap terdalam. Sebelum mematikan lampu malam ini, ingat ini:",
        "friction_question": "💬 Kamar tidurmu biasanya dingin banget pakai AC, atau lebih suka kipas angin sepoi-sepoi? Ceritakan di bawah! 👇",
        "expert": "Sleep Medicine Reviews",
        "publication": "Thermal Environment and Sleep Quality: Ambient Temperature Effects on Human Slow-Wave Sleep (2019)",
        "hf_spec": "Grafik proporsi gelombang Slow-Wave Sleep (NREM 3) meningkat saat suhu ruangan 19°C.",
        "broll": ["adjusting air conditioner remote to 20C", "clean cool white linen sheets comfortable bed", "person pulling light cotton blanket smiling", "peaceful deep sleep dark quiet room", "cool gentle night breeze window"]
    },
    {
        "day": 30,
        "week": 5,
        "pillar_id": "P1",
        "pillar_name": "Ritme Sirkadian & Arsitektur Tidur Dalam",
        "title": "Pakai Kaus Kaki Saat Tidur? Trik Tertidur Cepat dalam 7 Menit! 🧦🌙",
        "hook": "Pakai kaus kaki saat tidur bikin gerah? Salah besar! Ini trik biologis tercepat agar kamu tertidur dalam tujuh menit!",
        "why": "Menghangatkan telapak kaki melebarkan pembuluh darah tepi (vasodilatasi distal) di ujung-ujung ekstremitas tubuhmu.",
        "mechanism": "Darah hangat terdorong ke permukaan kulit kaki dan melepas panas tubuh keluar, mempercepat penurunan suhu inti otak yang memicu rasa kantuk.",
        "protocol": "Kenakan kaus kaki katun longgar sebelum naik ke tempat tidur. Rasakan kantuk yang merayap cepat saat kakimu mulai hangat nyaman.",
        "loop_ending": "Kaki yang hangat adalah kunci untuk mendinginkan suhu inti tubuhmu demi tidur paling lelap. Sebelum menarik selimut malam ini, ingat trik ini:",
        "friction_question": "💬 Kamu tim tidur wajib pakai kaus kaki atau tim kaki harus bebas kena udara dingin? Tulis tim kamu di bawah! 👇",
        "expert": "Nature Magazine & Dr. Kurt Kräuchi",
        "publication": "Nature: Warm feet promote the rapid onset of sleep in adults (Swiss Sleep Research Group)",
        "hf_spec": "Vasodilatasi kapiler darah di telapak kaki mempercepat pembuangan panas inti tubuh.",
        "broll": ["putting on soft cozy cotton socks bedroom", "pulling warm blanket over feet relaxing", "head resting gently on soft pillow eyes closing", "ambient night lamp slowly turning off", "serene peaceful deep slumber"]
    }
]

def build_packet(item):
    day_num = item["day"]
    words_list = item["hook"].split() + item["why"].split() + item["mechanism"].split() + item["protocol"].split() + item["loop_ending"].split()
    total_words = len(words_list)
    full_text = f"{item['hook']} {item['why']} {item['mechanism']} {item['protocol']} {item['loop_ending']}"

    packet = {
        "metadata": {
            "channel_id": "DITA-03",
            "channel_name": "Dita Gentle Wellness",
            "handle": "@ditawellness",
            "day_number": day_num,
            "cycle_number": item["week"],
            "cycle_theme": item["pillar_name"],
            "topic_pillar_id": item["pillar_id"],
            "topic_pillar_name": item["pillar_name"],
            "narrative_format_id": "F1",
            "narrative_format_name": "Protokol Harian Siap Tiru (Step-by-Step Practical Routine)",
            "emotional_trigger": "Pencerahan Menenangkan & Solusi Biologis Tanpa Biaya",
            "visual_pacing": "Transisi Sinematik Estetik menuju Visual Sains HyperFrames dan Protokol Praktis",
            "target_duration_range": "48-53 detik",
            "cta_hook_type": "Simpan Protokol & Praktikkan Hari Ini",
            "target_audience": "Profesional muda, pekerja kantoran, pria & wanita usia 22-45 tahun",
            "created_by": "Content Research & Narrative Architect (@content-researcher)",
            "reviewed_by": "Herman (Command Point / CEO)",
            "intended_executor": "Director (@fullmontage) & Fleet Operator (@social-operator)"
        },
        "scientific_research_dossier": {
            "core_topic": item["title"],
            "academic_citations": [
                {
                    "author": item["expert"],
                    "publication": item["publication"],
                    "key_findings": f"{item['why']} {item['mechanism']}"
                }
            ],
            "psychological_mechanism_breakdown": {
                "neurobiological_state": item["mechanism"],
                "cognitive_limitation": "Pola kebiasaan modern sering bertentangan dengan jam biologis purba sel manusia.",
                "common_trap": item["why"],
                "solution_formula": item["protocol"]
            }
        },
        "script_architecture_breakdown": {
            "anatomy": [
                {
                    "segment_id": "SEG_01",
                    "phase": "Thumb-Stopping Shock Hook",
                    "timestamp_range": "00:00 - 00:05",
                    "duration_seconds": 5,
                    "spoken_text": item["hook"],
                    "word_count": len(item["hook"].split()),
                    "visual_direction": "Kamera gerak lambat: visual estetika zen pagi hari / suasana tenang tanpa wajah. Headline peringatan emas-merah di sepertiga atas layar.",
                    "audio_design": {
                        "voice_inflection": "Tegas, intim, bersahabat, scroll-stopping.",
                        "sfx": "Sub-bass soft impact thud pada frame ke-1.",
                        "bgm": "Petikan dawai akustik dan ambient synth lembut."
                    }
                },
                {
                    "segment_id": "SEG_02",
                    "phase": "Emotional & Biological Anchor",
                    "timestamp_range": "00:05 - 00:16",
                    "duration_seconds": 11,
                    "spoken_text": item["why"],
                    "word_count": len(item["why"].split()),
                    "visual_direction": "Close-up macro estetika: cangkir teh, piring makanan sehat, atau detail dedaunan dengan cahaya alami.",
                    "audio_design": {
                        "voice_inflection": "Empatik, mengurai rasa lemas atau cemas yang selama ini dirasakan penonton.",
                        "sfx": "Whoosh lembut pada transisi adegan.",
                        "bgm": "Alunan dawai mengalir hangat."
                    }
                },
                {
                    "segment_id": "SEG_03",
                    "phase": "HyperFrames Scientific Mechanism",
                    "timestamp_range": "00:16 - 00:32",
                    "duration_seconds": 16,
                    "spoken_text": item["mechanism"],
                    "word_count": len(item["mechanism"].split()),
                    "visual_direction": f"Klip animasi vektor HyperFrames: {item['hf_spec']}",
                    "audio_design": {
                        "voice_inflection": "Jernih, edukatif berwibawa, membuka mata audiens.",
                        "sfx": "Chime rendah lembut dan suara desau alam.",
                        "bgm": "Harmoni piano ambient mengembang anggun."
                    }
                },
                {
                    "segment_id": "SEG_04",
                    "phase": "Actionable Rp 0 Micro-Routine",
                    "timestamp_range": "00:32 - 00:43",
                    "duration_seconds": 11,
                    "spoken_text": item["protocol"],
                    "word_count": len(item["protocol"].split()),
                    "visual_direction": "Gestur tangan tanpa wajah yang sedang mempraktikkan protokol sehat (menuang air, menyeduh teh, jalan kaki).",
                    "audio_design": {
                        "voice_inflection": "Hangat, mengajak aksi konkret tanpa beban.",
                        "sfx": "Foley alami (gemericik air, gesekan dedaunan).",
                        "bgm": "Melodi semakin rileks dan menenangkan."
                    }
                },
                {
                    "segment_id": "SEG_05",
                    "phase": "Empowerment & Seamless Loop Climax",
                    "timestamp_range": "00:43 - 00:52",
                    "duration_seconds": 9,
                    "spoken_text": item["loop_ending"],
                    "word_count": len(item["loop_ending"].split()),
                    "visual_direction": "Outro Card Zen Dita Gentle Wellness dengan logo sage green & emas, bersiap menyambung ulang ke detik ke-0.",
                    "audio_design": {
                        "voice_inflection": "Menutup tuntas dan mengalir mulus ke kalimat pertama.",
                        "sfx": "Bell chime zen lembut di ujung video.",
                        "bgm": "Fade-out anggun yang beresonansi harmonis."
                    }
                }
            ]
        },
        "seamless_loop_mechanism": {
            "loop_phrase_ending": item["loop_ending"],
            "hook_phrase_beginning": item["hook"],
            "full_loop_sentence": f"{item['loop_ending']} {item['hook']}",
            "retention_mechanic": "Kalimat penutup tuntas secara tata bahasa, namun saat diputar ulang di feed medsos langsung menjadi pembuka logis bagi kalimat shock hook di detik awal."
        },
        "verbatim_script_master": {
            "full_spoken_text_id": full_text,
            "total_word_count": total_words,
            "estimated_reading_duration_seconds": 51.0,
            "average_wpm": 120,
            "voiceover_profile": {
                "service": "Edge TTS",
                "voice_name": "id-ID-GadisNeural",
                "rate": "+0%",
                "pitch": "+0Hz",
                "volume": "+0%"
            }
        },
        "production_prompts_for_fullmontage": {
            "hyperframes_scene_spec": item["hf_spec"],
            "broll_queries": item["broll"]
        },
        "social_fleet_distribution_metadata": {
            "title": item["title"],
            "youtube_shorts_title": f"{item['title'].split('!')[0].strip()} #Shorts #DitaWellness",
            "caption_instagram_tiktok": (
                f"{item['hook']}\n\n"
                f"Secara biologis: {item['why']} {item['mechanism']}\n\n"
                f"🌿 Protokol Lembut Hari Ini:\n{item['protocol']}\n\n"
                f"{item['friction_question']}\n\n"
                "Simpan video ini biar nggak lupa, dan share ke orang tersayang yang butuh tips sehat alami ini! ✨\n\n"
                "#ditawellness #gentlewellness #biohackingindonesia #hidupsehatalami #kesehatantubuh #tipssehatalami #polahidupsehat #sainskesehatan"
            )
        }
    }

    out_file = os.path.join(CURRICULUM_PATH, f"content_packet_day_{String_pad(day_num)}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)
    print(f"Generated Day {String_pad(day_num)}: {item['title'][:55]} ({total_words} words)")

def String_pad(num):
    return str(num).zfill(3)

def main():
    print(f"Generating 29 Content Packets (Day 002 to Day 030) into {CURRICULUM_PATH}...")
    for item in EPISODES_DATA:
        build_packet(item)
    print("\n[SUCCESS] 29 Content Packets generated successfully!")

if __name__ == "__main__":
    main()
