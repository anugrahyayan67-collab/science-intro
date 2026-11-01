# Menulis naskah

## Struktur cerita (wajib)
Pembuka (hook misteri konkret) → judul (`fixed: 7`) → peta video → **Bagian 1** prinsip & teori → **Bagian 2** implementasi dalam kimia → **Bagian 3** penerapan nyata/industri → rangkuman → penutup (`fixed: 15`, rujukan).
- Satu **benang merah** yang muncul di awal dan dipecahkan di tengah/akhir (contoh: dua garis D natrium di Modul 7; O₂ paramagnetik sebagai cliffhanger video VBT → MOT).
- Tiap adegan 30–60 dtk, satu ide, 4–7 baris narasi.
- Seri fisika: Bagian 2 "di dunia kimia" yang menjembatani ke kimia kuantum.
- Video renungan/agama: dalil & renungan dipisah, pil sumber untuk tiap dalil, label "Renungan · bukan tafsir", tanpa sosok/wajah tokoh suci, penutup *wallahu a'lam*.

## Bentuk data (`src/script.ts`)
```ts
{id, chapter: '01' | '', part?: 1|2|3, title, mood, lead?, tail?, fixed?, lines: [{text, hl?, pause?, tts?}]}
```
- `mood`: mystery | title | wonder | build | quantum | tension | bright | resolve | outro (warna latar & musik).
- `hl`: frasa yang **benar-benar ada** di `text` (disorot emas).
- `pause` 0,6–1,0 dtk; baris terakhir adegan sedikit lebih panjang.

## Aturan teks
- `text` = subtitle. Angka & simbol ditulis sebagai kata ("tujuh puluh empat pikometer") agar subtitle = ucapan.
- `tts` hanya bila ejaan TTS beda: huruf tunggal (S → "es", J → "je", L → "el"), nama tokoh ("Heitler" → "Haitler", "Hund" → "Hun"), singkatan ("UTS" → "u te es"). Huruf tunggal & nama umum juga dieja otomatis oleh `src/tts.ts` — tambah kamus di sana.
- "≈" untuk perkiraan, "±" hanya plus-minus. Koma desimal.
- Hindari kata yang sama dua kali dalam satu baris bila akan dipakai `wordOf` (atau pakai `nth`).

## Generator
`scripts/gen_template.py` berisi helper `L(text, hl, pause, tts)` dan `S(id, chapter, title, mood, lines, part, lead, tail, **kw)`, memeriksa id unik, menulis `script.ts` dengan kepala (tipe + komentar) dari repo mesin, dan mencetak jumlah adegan/baris/karakter. Edit naskah = edit generator lalu jalankan ulang (bukan edit `script.ts` langsung).

## Cek fakta sebelum narasi
Sumber primer: NIST (ASD, CCCBDB, CODATA), CRC, buku teks (Atkins, Levine, McQuarrie, Housecroft), makalah asli, nobelprize.org. Tulis ke AUDIT. Mengubah angka setelah rekam = rekam ulang baris.
