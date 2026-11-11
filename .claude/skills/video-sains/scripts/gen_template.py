"""Kerangka generator naskah video. Salin ke scratchpad sebagai gen_<topik>.py, isi SCRIPT, lalu:
    python3 gen_<topik>.py /home/user/video-<topik>/src/script.ts [repo_mesin]
repo_mesin (default kuantum-07-simbol-term) dipakai untuk mengambil kepala berkas (tipe + komentar).
"""
import json, sys

P = 0.7  # jeda bawaan setelah baris (detik)

def L(text, hl=None, pause=P, tts=None):
    """Satu baris narasi. text = subtitle (angka ditulis sebagai kata); tts = ejaan khusus mesin suara."""
    d = {"text": text}
    if hl:
        missing = [h for h in hl if h not in text]
        assert not missing, f"hl tidak ada di teks: {missing} :: {text}"
        d["hl"] = hl
    d["pause"] = pause
    if tts: d["tts"] = tts
    return d

def S(id, chapter, title, mood, lines, part=None, lead=1.2, tail=1.4, **kw):
    """Satu adegan. chapter '' = tanpa heading; part 1/2/3 = bagian video; fixed=detik untuk adegan tanpa narasi."""
    d = {"id": id, "chapter": chapter, "title": title, "mood": mood}
    if part: d["part"] = part
    if lines: d["lead"] = lead; d["tail"] = tail
    d.update(kw); d["lines"] = lines
    return d

TITLE = "Judul Video"          # untuk komentar kepala berkas
SUBJECT = "Mata kuliah: topik"  # idem

SCRIPT = [
    S("hook", "", "Pembuka", "mystery", [
        L("Kalimat pembuka yang memancing rasa ingin tahu.", ["rasa ingin tahu"], 0.9),
    ], lead=1.6, tail=1.2),
    S("title", "", TITLE, "title", [], fixed=7),
    S("roadmap", "", "Peta video", "wonder", [
        L("Perjalanan kita punya tiga bagian.", None, 0.6),
    ], lead=0.8),
    # S("konsep1", "01", "Judul bab", "build", [L(...), ...], part=1),
    S("recap", "20", "Merangkai semuanya", "resolve", [
        L("Mari rangkum.", None, 0.6),
    ], lead=1.0, tail=2.4),
    S("outro", "", "Penutup", "outro", [], fixed=15),
]

if __name__ == "__main__":
    ids = [s["id"] for s in SCRIPT]
    assert len(ids) == len(set(ids)), "id adegan ganda"
    dst = sys.argv[1]
    base = sys.argv[2] if len(sys.argv) > 2 else "kuantum-07-simbol-term"
    src = open(f"/home/user/{base}/src/script.ts").read()
    head = src[:src.index("export const SCRIPT")]
    first = head.splitlines()[0]
    head = head.replace(first, f'// Naskah narasi "{TITLE}" — {SUBJECT}.', 1)
    out = head + "export const SCRIPT: SceneScript[] = " + json.dumps(SCRIPT, ensure_ascii=False, indent=2) + ";\n"
    open(dst, "w").write(out)
    n = sum(len(s["lines"]) for s in SCRIPT)
    chars = sum(len(l["text"]) for s in SCRIPT for l in s["lines"])
    print(f"{len(SCRIPT)} adegan · {n} baris · {chars} karakter (≈ {chars / 12.5 / 60:.1f} menit narasi)")
