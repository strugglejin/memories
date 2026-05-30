"""批量压缩照片，适合网页加载"""
from PIL import Image
import os

root = "D:/project/回忆/photos"
out_root = "D:/project/回忆/photos_small"

os.makedirs(out_root, exist_ok=True)
os.makedirs(f"{out_root}/batch2", exist_ok=True)

for folder, sub in [("", ""), ("batch2", "batch2")]:
    src_dir = os.path.join(root, folder) if folder else root
    dst_dir = os.path.join(out_root, sub) if sub else out_root

    for fname in os.listdir(src_dir):
        src = os.path.join(src_dir, fname)
        dst = os.path.join(dst_dir, fname)
        if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        try:
            img = Image.open(src).convert("RGB")
            w, h = img.size
            new_w = min(w, 800)
            new_h = int(h * new_w / w)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            img.save(dst, "JPEG", quality=70)
            old_mb = os.path.getsize(src) / 1024 / 1024
            new_kb = os.path.getsize(dst) / 1024
            print(f"{fname}: {old_mb:.1f}MB → {new_kb:.0f}KB")
        except Exception as e:
            print(f"跳过 {fname}: {e}")

print("\n完成！")
