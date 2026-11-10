---
name: video-sains
description: Membuat video edukasi sains/kimia (Kimia Kuantum, Fisika Umum, renungan, dll.) dengan Remotion — animasi vektor yang terus bergerak, subtitle kata-per-kata, render 2K di GitHub Actions, versi dengan & tanpa narasi. Pakai saat pengguna minta "bikin video modul N", "video materi kuliah", "video seri fisika", atau video edukasi apa pun berdurasi panjang (10–25 menit).
---

# Video edukasi sains — pipeline lengkap

Pemilik: Yayan (Septian Anugrah Dwi Putra), S1 Kimia UNESA. Bahasa Indonesia santai, menonton di iPad.
Skill ini merangkum cara kerja yang sudah terbukti di ±15 video. Baca berkas rujukan sesuai tahap — jangan baca semuanya sekaligus.

## Peta berkas
| Berkas | Kapan dibaca |
|---|---|
| `references/pipeline.md` | Membuat video baru dari nol (langkah 1–10, perintah persis). |
| `references/naskah.md` | Menulis naskah: struktur cerita, aturan teks TTS, generator `gen_<topik>.py`. |
| `references/gaya.md` | Memilih/menjaga gaya visual & kode warna per seri; mesin mana yang disalin. |
| `references/adegan.md` | Membangun adegan: API `useScene`, helper animasi, komponen, aturan tata letak & kemulusan, prompt agen paralel. |
| `references/qa.md` | Audit: check-cues, qa-lines + lembar kontak, qa-moments, uji glitch seluruh film. |
| `references/narasi.md` | Suara (ElevenLabs suara klon / Edge TTS), `tts.ts`, cek pengucapan Whisper. |
| `references/github.md` | Repo baru, PR, workflow render, cara memberi tahu pengguna. |
| `references/pelajaran.md` | Daftar "jangan lakukan ini" — cek sebelum menyerahkan pekerjaan. |
| `scripts/gen_template.py` | Kerangka generator naskah (salin ke scratchpad, isi `SCRIPT`). |
| `scripts/new-video.sh` | Menyalin mesin dari repo video sebelumnya ke folder baru + mengganti nama komposisi. |

## Aturan inti (selalu berlaku)
1. **Claude tidak menjalankan workflow GitHub Actions.** Setelah merge ke `main`, beri link Actions + nama workflow; pengguna yang menekan *Run workflow*.
2. **Jangan pernah meminta atau menampilkan kunci API.** Kunci ada di secret GitHub per repo.
3. Modul kuliah = referensi, bukan naskah. Cerita memikat: hook → pertanyaan → jawaban visual → penerapan. Fakta luar modul harus nyata & dicek (catat di `naskah/AUDIT.md`) **sebelum** narasi direkam.
4. Visual harus **bergerak sesuai fisika** (posisi dihitung per frame), bukan slide statis. Semua animasi dari frame (`interpolate`/`ramp`), tanpa animasi CSS.
5. Rumus utama ≥ 56 px, satu kartu per momen; zona subtitle (bawah 180 px) selalu kosong; margin ≥ 80 px.
6. Kemulusan: tanpa CSS blur, tanpa ganti elemen berdasarkan ambang (silang-pudar), tanpa filter pada garis lurus.
7. Selalu sediakan versi **tanpa narasi** (subtitle + musik).
8. Commit & push WIP sebelum pekerjaan panjang (render, agen paralel) — sesi bisa dimulai ulang / kena batas pemakaian.
9. Jawab ringkas dalam bahasa Indonesia, beri link yang bisa diketuk di iPad. Kirim pratinjau (lembar kontak) lewat SendUserFile.
10. Setelah selesai: perbarui `materi/RINGKASAN.md` & `CLAUDE.md` repo `science-intro` (status + pelajaran baru), dan perbarui skill ini bila ada cara kerja baru.

## Alur singkat
naskah (`gen_<topik>.py`) → salin mesin (`new-video.sh`) → stub adegan & ganti merek → AUDIT angka → 4 agen paralel per kelompok adegan → commit per kelompok → `npm run check` → `qa-lines` (baca semua lembar) → perbaiki → `qa-film` + `qa-glitch` → repo GitHub (dibuat pengguna) → PR draft → pengguna merge & render.
Durasi kerja ±1–2 jam untuk video 15–20 menit.
