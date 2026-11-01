# Pipeline video baru (langkah & perintah)

Variabel: `TOPIK` (mis. `ikatan-valensi`), `KOMP` (id komposisi PascalCase, mis. `IkatanValensi`), `BASE` (repo mesin terbaru, lihat `gaya.md`), `BR` = branch kerja sesi.

## 1. Bahan
- Baca `materi/RINGKASAN.md` & `CLAUDE.md` repo `science-intro`. Untuk PDF modul: `pdfinfo` lalu `pdftotext -layout -f A -l B file.pdf -` hanya bab yang dipakai. PDF hasil pindai (teks kosong) → `Read` dengan `pages`.
- RPS: cocokkan materi per pertemuan; sebelum/sesudah UTS.

## 2. Naskah
- Salin `scripts/gen_template.py` ke scratchpad sebagai `gen_<topik>.py`, isi `SCRIPT` (lihat `naskah.md`). Jalankan dengan argumen tujuan: `python3 gen_<topik>.py /home/user/video-<topik>/src/script.ts`.
- Target: 20–26 adegan, 100–130 baris, 14–20 menit (≈ 5,3 suku kata/detik).

## 3. Salin mesin
```bash
bash /home/user/science-intro/.claude/skills/video-sains/scripts/new-video.sh BASE TOPIK KOMP "Judul Workflow"
```
Skrip: `git archive` dari `BASE`, `git init -b BR`, symlink `node_modules` dari BASE (atau `npm ci` bila dependensi beda — cek `@fontsource/*`), ganti id komposisi di `Root.tsx`, `Composition.tsx`, `render-video.yml`, `assemble.sh`, `render-chunk.ts`, `qa-*.mjs`, `package.json`.

## 4. Kerangka
- Hapus adegan lama, buat stub per id (komponen `Label` di `Stage`), tulis ulang `src/scenes/index.ts` dan `scripts/scene-files.ts` (id → nama berkas).
- Ganti merek: `Title.tsx`, `Outro.tsx` (REFS rujukan nyata + catatan kaki), `Thumbnail.tsx`, `ChapterHeading` PARTS (label bagian), latar (`Background` GHOSTS), `package.json` description, `export-timeline.ts` judul, `make-music.py` (BEAT/seed beda agar musik baru), `brand.ts` bila ada.
- `src/tts.ts`: tambah ejaan nama tokoh & huruf tunggal baru.
- `npx tsc --noEmit` → `npm run timeline` (menulis `naskah/` + `public/timeline.json`, tampilkan durasi) → `npm run music` (latar belakang; pakai 128 kbps agar < 25 MB).

## 5. AUDIT & dokumen
- `naskah/AUDIT.md`: tabel adegan | klaim | nilai | sumber. Setiap angka di layar/narasi harus ada di sini.
- `CLAUDE.md` repo baru: judul, gaya, benang merah cerita, kode warna, aturan konten, perintah QA. `README.md`: isi + cara render.
- Commit "Kerangka …".

## 6. Adegan (agen paralel)
- 4 agen Opus, masing-masing 5–7 adegan berurutan (lihat prompt di `adegan.md`). Agen tidak commit; sesi utama commit per kelompok setelah laporan.
- Bila agen kena batas pemakaian: commit WIP, lalu lanjutkan agen yang sama dengan SendMessage setelah reset (pekerjaannya tersimpan). Bila pengguna minta berhenti: TaskStop semua agen + commit WIP.

## 7. QA menyeluruh (sesi utama) — lihat `qa.md`
`npm run check` → `qa-lines` seluruh film → baca SEMUA lembar → perbaiki → `qa-film` + `qa-glitch`.

## 8. GitHub — lihat `github.md`
Pengguna membuat repo kosong → `add_repo` (push) → `git remote add` + merge README awal (`--allow-unrelated-histories -X ours`) → push → `register_repo_root` → PR draft → `subscribe_pr_activity`.

## 9. Serah terima
Link PR + "setelah merge: Actions → <Workflow> → Run workflow" + cara unduh artefak (iPad: tekan lama → Unduh Tautan Tertaut). Perbarui catatan di `science-intro`.
