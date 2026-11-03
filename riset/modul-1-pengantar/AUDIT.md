# Audit angka & klaim — *Lampu Merah di Kamar Gelap* (Kimia Kuantum Modul 1: Pengantar)

Dicek 3 Nov 2026. Konstanta dari tabel CODATA 2022 NIST (`physics.nist.gov/cuu/Constants/Table/allascii.txt`, diunduh langsung). Tahun & nama Nobel dari halaman ringkasan nobelprize.org (diunduh langsung, kutipan motivasi resmi). Makalah asli dicek lewat metadata Crossref (judul, jurnal, volume, halaman, tanggal terbit). Hitungan turunan dibuat ulang dengan Python dari konstanta CODATA.
Legenda: ✓ = cocok dengan sumber primer/resmi · ✓ (hitung) = diturunkan dari konstanta yang sudah dicek · ⚠ = sumber sekunder / ada catatan.

## Konstanta (CODATA 2022)

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Tetapan Planck h | 6,626 070 15 × 10⁻³⁴ J·s (eksak); narasi "6,62 × 10⁻³⁴" | https://physics.nist.gov/cuu/Constants/Table/allascii.txt | ✓ |
| ħ = h/2π | 1,054 571 817… × 10⁻³⁴ J·s (eksak) | idem | ✓ |
| Laju cahaya c | 299 792 458 m/s (eksak) | idem | ✓ |
| Muatan elementer e | 1,602 176 634 × 10⁻¹⁹ C (eksak) | idem | ✓ |
| Massa elektron mₑ | 9,109 383 7139 × 10⁻³¹ kg | idem | ✓ |
| Tetapan Boltzmann k | 1,380 649 × 10⁻²³ J/K (eksak) | idem | ✓ |
| Tetapan pergeseran Wien b | 2,897 771 955… × 10⁻³ m·K (kartu: 2,898 × 10⁻³) | idem | ✓ |
| Tetapan Stefan–Boltzmann σ | 5,670 374 419… × 10⁻⁸ W m⁻² K⁻⁴ | idem | ✓ |
| Panjang gelombang Compton h/(mₑc) | 2,426 310 235 38 × 10⁻¹² m ≈ 2,43 pm | idem | ✓ |
| hc | 1239,84 eV·nm (kartu: ≈ 1240) | dari h, c, e | ✓ (hitung) |

## Benda hitam & Planck

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Lord Kelvin "dua awan" abad ke-19 | Kuliah Royal Institution 27 Apr 1900, terbit "Nineteenth century clouds over the dynamical theory of heat and light", Phil. Mag. 2, 1–40 (Jul 1901); awan ke-2 = ekuipartisi energi (radiasi/panas jenis) | https://doi.org/10.1080/14786440109462664 (Crossref) | ✓ makalah; ⚠ tanggal kuliah dari sumber sekunder. Narasi "Salah satunya menyangkut panas dan cahaya" = penyederhanaan (awan ke-2 ialah ekuipartisi Maxwell–Boltzmann, termasuk radiasi termal). |
| Titik Draper: padatan mulai berpijar merah redup | ≈ 525 °C (798 K), Draper 1847 | https://en.wikipedia.org/wiki/Draper_point | ⚠ sekunder (ensiklopedia; konsisten dengan tabel boiler 1905 "just visible red" 525 °C) |
| Hukum Wien λmaks T = b | modul pers. (5) | Modul 1 hlm. 4; CODATA | ✓ |
| Matahari T_eff ≈ 5772 K → λmaks ≈ 502 nm | 2,8978 × 10⁻³ / 5772 = 5,02 × 10⁻⁷ m | IAU 2015 Resolution B3 (nominal T_eff = 5772 K): https://www.iau.org/common/Uploaded%20files/IAUGA2015-Resolution-B3-recommended-nominal-conversion.pdf · arXiv:1510.07674 | ✓ (narasi "sekitar 5700 K", "sekitar 500 nm") |
| Tubuh ≈ 310 K → λmaks ≈ 9,3 µm | 2,8978 × 10⁻³ / 310 = 9,35 µm | hitung | ✓ (hitung) |
| Suhu 2× → daya 16× | M = σT⁴ | Modul 1 hlm. 4 | ✓ |
| Rayleigh–Jeans → katastrofe ultraviolet | jatah kT per mode, jumlah mode ∝ ν² | Modul 1 hlm. 5–6 | ✓. Catatan: istilah "katastrofe ultraviolet" baru dipakai Ehrenfest (1911) — narasi menulis "kelak dijuluki". Rumus Rayleigh–Jeans lengkap (1900/1905) muncul sezaman/sesudah Planck; urutan dramatis di video disederhanakan (⚠ historis). |
| "Semua oven akan memancarkan sinar-X" | konsekuensi retoris RJ (energi menumpuk di frekuensi tinggi) | — | ⚠ retoris, boleh diganti "memancarkan ultraviolet tanpa batas" |
| Planck 14 Des 1900, Deutsche Physikalische Gesellschaft Berlin | makalah "Ueber das Gesetz der Energieverteilung im Normalspectrum", Ann. Phys. 309 (4), 553–563 (1901) | https://doi.org/10.1002/andp.19013090310 (Crossref); APS News "This Month in Physics History" https://www.aps.org/apsnews/2002/10/this-month-in-physics-history | ✓ makalah; ⚠ tanggal kuliah dari sumber sekunder (konvensi umum) |
| E = nhν | modul pers. (6) | Modul 1 hlm. 6 | ✓ |
| Nobel Fisika 1918 — Planck ("discovery of energy quanta"; diumumkan 1919) | — | https://www.nobelprize.org/prizes/physics/1918/summary/ | ✓ ("delapan belas tahun kemudian" = 1900 → 1918) |

## Efek fotolistrik & foton

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Einstein 1905, kuanta cahaya | "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt", Ann. Phys. 322 (6), 132–148 (1905) | https://doi.org/10.1002/andp.19053220607 (Crossref) | ✓ |
| K_maks = hν − Φ; intensitas → jumlah elektron, frekuensi → K_maks | modul pers. (10) | Modul 1 hlm. 8–10 | ✓ (model satu foton; serapan multi-foton laser intens tidak dibahas) |
| Fungsi kerja cesium ≈ 2,14 eV → λ₀ ≈ 579 nm (kuning) | 1239,84 / 2,14 = 579 nm | Tabel CRC Handbook via HyperPhysics https://hyperphysics.gsu.edu/hbase/Tables/photoelec.html ; pulsedpower.net (Cs 2,14 eV, merujuk CRC) | ⚠ CRC tidak dapat diakses langsung; nilai literatur Cs berkisar 1,9–2,1 eV tergantung permukaan. Narasi "sekitar 2,1 eV", "sekitar 580 nm". |
| (Pembanding) Na 2,36 eV, K 2,29 eV (polikristal, CRC) | — | HyperPhysics (CRC) | ⚠ Modul memakai Na = 1,82 eV (contoh 4). Berbeda dari CRC — narasi sengaja memakai Cs. |
| Kemiringan K_maks–ν = h; Millikan 1916 | "A Direct Photoelectric Determination of Planck's h", Phys. Rev. 7, 355–388 (Mar 1916) | https://doi.org/10.1103/PhysRev.7.355 (Crossref) | ✓. "Ingin membantah Einstein" = cerita Millikan sendiri (sekunder, ⚠ tetapi sangat umum dikutip). |
| Nobel Fisika 1921 — Einstein, "especially for his discovery of the law of the photoelectric effect" (diserahkan 1922) | — | https://www.nobelprize.org/prizes/physics/1921/summary/ | ✓ |
| Nobel Fisika 1923 — Millikan (muatan elementer & efek fotolistrik) | — | https://www.nobelprize.org/prizes/physics/1923/summary/ | ✓ (tidak disebut di narasi; cadangan) |
| Foton 650 nm ≈ 1,91 eV; 450 nm ≈ 2,76 eV; 300 nm ≈ 4,13 eV | E = 1239,84/λ | hitung | ✓ (hitung) |

## Kamar gelap (benang merah)

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Kertas foto hitam-putih: kristal perak halida (AgBr) | — | datasheet Ilford Multigrade (EMS Diasum) | ✓ umum |
| Tepi serapan / celah tak langsung AgBr ≈ 2,68–2,69 eV (suhu kriogenik); nilai rujukan umum ≈ 2,5 eV; tepi ≈ 460–495 nm | narasi: "sekitar dua setengah eV" | UCL (A. H. Harker, data kristal AgBr: celah tak langsung 2,68 eV, langsung 4,29 eV) https://www.ucl.ac.uk/~ucapahh/research/crystal/agbr.htm ; disertasi Illinois "Optical absorption of pure and mixed silver halides at low temperatures" (ambang 2,691 eV pada 4,2 K) https://www.ideals.illinois.edu/items/25205 | ⚠ bergantung suhu; pada suhu kamar sedikit lebih rendah. Kesimpulan kualitatif aman: merah (1,9 eV) jauh di bawah, biru (2,8 eV) di atas. |
| Lampu aman (safelight) merah/jingga; kertas kontras-variabel modern juga peka hijau (perlu filter coklat muda/amber, Ilford 902) | — | Ilford Multigrade IV RC datasheet https://physics.wisc.edu/instructional/phys109/yoshi/Photography_Lab/ILFORD_Info/ILFORD_Multi_Grade_IV_RC.pdf | ⚠ Narasi menyebut "lampu merah" (klasik untuk kertas peka biru). Kalau ingin akurat untuk kertas modern: "lampu merah atau jingga". |
| Mekanisme bayangan laten: elektron tereksitasi → Ag⁺ + e⁻ → Ag; gugus beberapa atom Ag; pengembang memperkuat | teori Gurney–Mott (1938) | buku teks fotokimia (mis. James, *The Theory of the Photographic Process*) | ⚠ belum dicek ke sumber primer daring; deskripsi standar |
| Pewarna pemeka membuat film peka hijau/merah (pankromatik → gelap total) | — | — | tidak dipakai di narasi |

## Foton dalam kimia

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Foton 300 nm ≈ 399 kJ/mol; foton 650 nm ≈ 184 kJ/mol | N_A·hc/λ | hitung (N_A = 6,022 140 76 × 10²³, CODATA) | ✓ (hitung) |
| Energi ikatan rata-rata C–C ≈ 348 kJ/mol (≈ 3,6 eV) | tabel energi ikatan rata-rata (Atkins/Chang; nilai 346–348 kJ/mol) | buku teks | ⚠ nilai rata-rata, bukan energi disosiasi spesifik |
| Klorofil menyerap merah & biru, memantulkan hijau; pusat reaksi P680/P700 | — | buku teks biokimia | ⚠ belum dicek daring (pengetahuan baku) |
| Warna uji nyala: Na kuning, Cu hijau-kebiruan, Sr merah | — | buku teks kimia analitik | ✓ umum; garis D Na 589,0/589,6 nm sudah dicek di video simbol-term |
| Celah pita Si ≈ 1,12 eV (300 K) → λ ≈ 1107 nm | 1239,84/1,12 | Ioffe Institute, Si band structure https://www.ioffe.ru/SVA/NSM/Semicond/Si/bandstr.html | ✓ (lewat cuplikan pencarian; situs Ioffe gagal TLS dari sandbox) |
| LED merah ≈ 1,9 eV (≈ 650 nm), biru ≈ 2,7 eV (≈ 460 nm); warna ≈ celah pita | E = hc/λ | hitung | ✓ (hitung; LED nyata memancar sedikit di atas/sekitar celah) |
| Nobel Fisika 2014 — Akasaki, Amano, Nakamura, "efficient blue light-emitting diodes" | — | https://www.nobelprize.org/prizes/physics/2014/summary/ | ✓ |

## Compton

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Compton 1923, "A Quantum Theory of the Scattering of X-rays by Light Elements" | Phys. Rev. 21, 483–502 (Mei 1923) | https://doi.org/10.1103/PhysRev.21.483 (Crossref) | ✓ |
| Sinar-X Mo Kα ≈ 0,0709 nm dihamburkan grafit pada 90° | — | HyperPhysics "Compton Scattering Data" https://hyperphysics.gsu.edu/hbase/quantum/compdat.html (merujuk Phys. Rev. 21, 483 & 22, 409) | ⚠ sekunder |
| Δλ = (h/mₑc)(1 − cos θ); pada 90° Δλ = 2,43 pm; maks (180°) 4,85 pm | — | CODATA | ✓ (hitung) |
| Momentum foton p = h/λ | modul hlm. 16 | Modul 1 | ✓ |
| Nobel Fisika 1927 — Compton (dibagi dengan C. T. R. Wilson) | — | https://www.nobelprize.org/prizes/physics/1927/summary/ | ✓ |

## de Broglie & Davisson–Germer

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| de Broglie, disertasi 1924; λ = h/p | — | Modul 1 pers. (20); Leopoldina CV https://www.leopoldina.org/fileadmin/redaktion/Mitglieder/CV_Broglie_Louis_de_EN.pdf | ✓ |
| Langevin mengirim disertasi ke Einstein; Einstein terkesan (surat 16 Des 1924) | — | Pengantar Collected Papers of Albert Einstein vol. 15, arXiv:1803.10662 | ⚠ sekunder ilmiah; waktu pasti pengiriman diperdebatkan |
| Nobel Fisika 1929 — de Broglie, "discovery of the wave nature of electrons" | — | https://www.nobelprize.org/prizes/physics/1929/summary/ | ✓ |
| Bola bisbol 145 g, 40 m/s → λ ≈ 1,1 × 10⁻³⁴ m | h/(0,145·40) | hitung | ✓ (hitung) |
| Elektron 54 eV → λ = h/√(2mₑE) = 0,167 nm | 0,1669 nm | hitung | ✓ (hitung) |
| Davisson & Germer: puncak hamburan 54 eV pada φ = 50°; jarak baris atom Ni d = 0,215 nm; d sin φ = 0,165 nm (ukur) vs 0,167 nm (prediksi) | — | Nature 119, 558–560 (Apr 1927) https://doi.org/10.1038/119558a0 ; Phys. Rev. 30, 705–740 (Des 1927) https://doi.org/10.1103/PhysRev.30.705 ; HyperPhysics https://hyperphysics.gsu.edu/hbase/quantum/davger2.html | ✓ judul/tahun makalah (Crossref); angka 54 eV/50°/0,165 nm ⚠ dari sumber sekunder yang konsisten (teks makalah berbayar). 0,215 × sin 50° = 0,1647 nm ✓ (hitung) |
| Kecelakaan April 1925: botol udara cair meledak, target teroksidasi, pemanasan lama di H₂ & vakum → rekristalisasi menjadi beberapa kristal besar | — | kutipan Phys. Rev. 30, 705 (1927) dalam cetak ulang (USP) & deskripsi katalog cetak ulang | ⚠ dari kutipan teks asli lewat sumber sekunder; detail "di laboratorium Bell" (Western Electric/Bell Labs, 1925 masih Western Electric Engineering Dept; Bell Labs berdiri Jan 1925) |
| G. P. Thomson: difraksi elektron menembus lapisan tipis (Aberdeen, Skotlandia, 1927) | — | https://www.nobelprize.org/prizes/physics/1937/summary/ | ✓ Nobel; ⚠ lokasi Aberdeen dari pengetahuan umum |
| Nobel Fisika 1937 — Davisson & G. P. Thomson, "experimental discovery of the diffraction of electrons by crystals" | — | idem | ✓ |
| J. J. Thomson (ayah) Nobel Fisika 1906 (konduksi listrik dalam gas; dikenal sebagai penemu elektron) | — | https://www.nobelprize.org/prizes/physics/1906/summary/ | ✓ |

## Mikroskop elektron

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Elektron 100 kV → λ ≈ 3,70 pm (relativistik); cahaya hijau 550 nm → rasio ≈ 1,5 × 10⁵ | p = √(2mE(1 + E/2mc²)) | hitung | ✓ (hitung). Narasi "lebih dari seratus ribu kali". |
| Ruska & Knoll: mikroskop elektron pertama 1931; 1933 melampaui resolusi mikroskop cahaya | — | Biografi Nobel Ruska https://www.nobelprize.org/prizes/physics/1986/ruska/biographical/ | ✓ (narasi "awal 1930-an") |
| Nobel Fisika 1986 — Ruska (setengah; setengah lagi Binnig & Rohrer, STM) | — | https://www.nobelprize.org/prizes/physics/1986/summary/ | ✓ |
| Nobel Kimia 2017 — Dubochet, Frank, Henderson, krio-mikroskopi elektron biomolekul | — | https://www.nobelprize.org/prizes/chemistry/2017/summary/ | ✓ |

## Heisenberg

| Klaim / angka | Nilai | Sumber | Dicek |
|---|---|---|---|
| Heisenberg 1927, "Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik" | Z. Phys. 43, 172–198 (Mar 1927) | https://doi.org/10.1007/BF01397280 (Crossref) | ✓ |
| Δx Δp ≥ ħ/2 (Δ = simpangan baku; bukan keterbatasan alat) | modul pers. (25) | Modul 1 hlm. 19–20 | ✓ |
| Elektron dalam Δx = 0,1 nm → Δp ≥ 5,27 × 10⁻²⁵ kg m/s, Δv ≥ 5,8 × 10⁵ m/s | ħ/(2Δx), /mₑ | hitung | ✓ (hitung; narasi "sekitar enam ratus ribu m/s") |
| Energi kurungan berorde beberapa eV | (ħ/Δx)²/2mₑ ≈ 3,8 eV untuk 0,1 nm | hitung | ✓ (perkiraan orde besaran; heuristik) |
| Nobel Fisika 1932 — Heisenberg, "creation of quantum mechanics… led to the discovery of the allotropic forms of hydrogen" (diserahkan 1933) | — | https://www.nobelprize.org/prizes/physics/1932/summary/ | ✓ (H₂ orto/para) |

## Lain-lain

| Klaim | Catatan |
|---|---|
| "Dari 1900 sampai 1927 = 27 tahun" | ✓ (Planck → Heisenberg/Davisson–Germer) |
| ψ, |ψ|² = kerapatan peluang | Modul 1 hlm. 18 ✓ |
| Spektrum garis & Bohr | sengaja tidak dihitung di video ini (video Fisika Atom & Atom Hidrogen) |

## Belum dapat diverifikasi ke sumber primer

1. Angka eksperimen Davisson–Germer (54 eV, 50°, 0,165 nm, d = 0,215 nm) — makalah Phys. Rev. berbayar; dicek lewat beberapa sumber sekunder yang konsisten + hitungan ulang.
2. Fungsi kerja Cs 2,14 eV (tabel CRC tidak terakses; nilai literatur 1,9–2,14 eV).
3. Celah AgBr pada suhu kamar (data primer yang ditemukan pada suhu kriogenik 2,68–2,69 eV; nilai rujukan umum 2,5 eV).
4. Tanggal kuliah Planck 14 Des 1900 dan kuliah Kelvin 27 Apr 1900 (sumber sekunder; makalah terbitnya ✓).
5. Kisah "Millikan ingin membantah Einstein", detail kecelakaan Davisson 1925 (kutipan makalah lewat sumber sekunder), Langevin → Einstein.
6. Titik Draper 525 °C (ensiklopedia).
7. Energi ikatan C–C, klorofil P680/P700, mekanisme Gurney–Mott — pengetahuan buku teks, belum dicek ke rujukan spesifik.
8. Situs Ioffe (TLS gagal dari sandbox) — nilai Si 1,12 eV diambil dari cuplikan pencarian halaman Ioffe.
