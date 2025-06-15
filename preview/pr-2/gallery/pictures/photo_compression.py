import os
from PIL import Image

def compress_image(input_path, output_path, target_size=1024*1024, step=5, min_quality=10):
    img = Image.open(input_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    quality = 95
    img.save(output_path, "JPEG", quality=quality)
    while os.path.getsize(output_path) > target_size and quality > min_quality:
        quality -= step
        img.save(output_path, "JPEG", quality=quality)
    img.close()

def is_image_file(filename):
    ext = filename.lower().split('.')[-1]
    return ext in ['jpg', 'jpeg', 'png', 'bmp', 'gif']

def compress_images_in_dir(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if is_image_file(filename):
                file_path = os.path.join(dirpath, filename)
                output_path = file_path  # 覆盖原文件
                try:
                    compress_image(file_path, output_path)
                    print(f"Compressed: {file_path}")
                except Exception as e:
                    print(f"Failed: {file_path}, reason: {e}")

if __name__ == "__main__":
    # 这里直接指定你要压缩的图片目录
    dir_path = r"e:\TUP\tup-lab-website\gallery"
    compress_images_in_dir(dir_path)