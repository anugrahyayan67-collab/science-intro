# GitHub & serah terima

- Repo video baru dibuat **pengguna** (kosong atau berisi README). Minta nama di awal pekerjaan agar tidak menunggu di akhir. Cek dengan `list_repos`.
- Folder kerja dibuat lebih dulu: `git init -q -b BR`. Setelah repo ada:
  ```bash
  # add_repo(owner, repo, access: push) dulu
  git remote add origin https://github.com/anugrahyayan67-collab/<repo>
  git fetch -q origin
  git merge -q origin/main --allow-unrelated-histories -X ours -m "Gabung README awal repo"   # bila origin/main ada
  git push -q -u origin BR
  ```
  Jangan clone di atas folder lokal yang sudah ada. Lalu `register_repo_root`.
- PR **draft** dengan `mcp__github__create_pull_request` (isi: ringkasan bagian, angka dicek di AUDIT, hasil QA, nama workflow render), lalu `subscribe_pr_activity`. Repo video tidak punya CI otomatis — event biasanya hanya "ready for review" dan "merged".
- Setelah merged: beri link `https://github.com/anugrahyayan67-collab/<repo>/actions`, nama workflow ("Render … 2K 30FPS"), branch `main`, cara unduh artefak di iPad. **Jangan** menjalankan workflow sendiri.
- Trailer commit & badan PR mengikuti instruksi sistem sesi (Co-Authored-By / Claude-Session; PR diakhiri baris "Generated with Claude Code"). Jangan menulis id model di commit/PR.
- Secret GitHub tetap aman walau repo publik. Repo publik = menit Actions gratis tanpa batas; repo private = kuota terbatas (render 2K bisa ratusan menit).
