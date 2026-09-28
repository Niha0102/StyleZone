from PIL import Image
from pathlib import Path

# Original images folder
input_folder = Path("shop/static/shop/images")

# New folder for normalized images
output_folder = input_folder / "normalized"
output_folder.mkdir(parents=True, exist_ok=True)

# Standard image size
WIDTH = 600
HEIGHT = 750

for image_path in input_folder.iterdir():

    if image_path.is_file() and image_path.suffix.lower() in [".png", ".jpg", ".jpeg"]:

        try:
            image = Image.open(image_path).convert("RGBA")

            # Resize while keeping the complete image
            image.thumbnail((WIDTH, HEIGHT))

            # Create standard canvas
            canvas = Image.new("RGBA", (WIDTH, HEIGHT), "white")

            # Center the product image
            x = (WIDTH - image.width) // 2
            y = (HEIGHT - image.height) // 2

            canvas.paste(image, (x, y), image)

            # Save as PNG
            output_path = output_folder / f"{image_path.stem}.png"
            canvas.save(output_path)

            print(f"Done: {image_path.name}")

        except Exception as e:
            print(f"Skipped: {image_path.name} - {e}")

print("\nAll images normalized successfully!")