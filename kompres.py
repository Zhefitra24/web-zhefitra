from PIL import Image
import os

def optimasi_foto(input_folder, output_folder, max_size=(500, 500), quality=80):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            nama_tanpa_ekstensi = os.path.splitext(filename)[0]
            output_filename = f"{nama_tanpa_ekstensi}.webp"
            output_path = os.path.join(output_folder, output_filename)

            try:
                with Image.open(input_path) as img:
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    img.save(output_path, "webp", quality=quality)
                print(f"✅ Sukses: {filename} -> {output_filename}")
            except Exception as e:
                print(f"❌ Gagal memproses {filename}: {e}")

if __name__ == "__main__":
    optimasi_foto("input", "output")
    print("✨ Selesai! Semua foto di folder 'output' siap digunakan.")