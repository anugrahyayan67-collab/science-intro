# Membangun adegan

## API
```ts
const {t, cue, cueEnd, wordOf, dur} = useScene();
// t: detik sejak awal adegan · cue(i): mulai baris i · cueEnd(i) · wordOf(i, 'kata', nth=0): saat kata diucapkan
```
Helper `src/anim.ts`: `ramp(t,a,b,ease)`, `win(t,a,b)` (masuk–keluar), `slot(t,a,b)` (kartu bergantian di satu posisi tanpa tumpang), `cyc(ph)` (siklus berulang tanpa muncul mendadak), `osc`, `mix`, `EASE` (lembut), `EASE_IN_OUT` (untuk fade keluar).

## Komponen (`src/components/primitives.tsx` dkk.)
`Stage` (SVG 1920×1080), `Label`, `Arrow`, `DrawPath`, `Glow`, `Atom`, `Bond`, `Ripple`, `Spark`, `Motes` (SVG) · `Card`, `Formula`, `Frac`, `Sqrt`, `Sub`, `Sup`, `Badge` (HTML, **di luar** `<Stage>`). `viz.tsx`: `wlColor(nm)`, `PhotonPacket`, `Electron`, `project` (3D). Komponen per video di `src/components/<grup>.tsx`.

## Aturan tata letak
- Grid jelas (kiri visual/kanan rumus, atau visual tengah + kartu bawah); margin ≥ 80 px; jarak antar-elemen ≥ 32 px.
- Zona bawah 180 px untuk subtitle — tidak ada konten.
- Rumus ≥ 56 px, pecahan bertumpuk (`Frac`), satu kartu utama per momen.
- Subskrip SVG: `<tspan baselineShift="sub">`; HTML: `Sub`/`Sup`; isi `Formula` baris inline (bukan flex).
- Tanda ⟨ ⟩ hanya di kartu HTML.

## Aturan kemulusan
- Tanpa CSS `filter: blur` (Chrome menerapkannya mendadak). Transisi adegan: translate + opacity (SceneShell).
- Tanpa `x > c ? A : B` untuk teks/warna/elemen → silang-pudar dua versi atau `interpolateColors`.
- Tanpa `filter="url(#glow)"` pada garis lurus tegak/datar (garis lenyap).
- Siklus berulang pakai `cyc`, bukan `(t*k) % n` pada posisi terlihat.
- Peta panas: canvas → `toDataURL` → `<image>`, bukan ribuan `<rect>`.

## Prompt agen paralel (templat)
> Kamu membangun adegan untuk video Remotion "<Judul>" di /home/user/video-<topik> (branch BR). KELOMPOKMU: `<id>` (src/scenes/<Komp>.tsx), … Baca CLAUDE.md, naskah/AUDIT.md, baris naskahmu di src/script.ts. Komponen: … Adegan rujukan berkualitas: /home/user/<repo-sebelumnya>/src/scenes (…). API useScene … Isi visual: <per adegan, konkret: apa yang bergerak, angka, label>. Aturan wajib: <tata letak + kemulusan>. Kerjakan HANYA berkasmu (boleh src/components/<grup>.tsx); jangan ubah script.ts/komponen bersama/adegan lain; JANGAN commit. QA wajib: `npx tsc --noEmit`, `npm run check`, `qa-lines` adeganmu + `contact.py … 3`, baca semua lembar, perbaiki. Bila bundling gagal karena berkas grup lain, tunggu lalu ulangi. Laporan akhir singkat.

Pembagian yang baik: A pembuka + 2–3 adegan awal; B & C inti teori; D penerapan + rangkuman + rapikan outro. Kelompok berisi visual 3D/berat diberi lebih sedikit adegan.
