from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math


IMAGE_FOLDER = Path(
    r"C:\StyleZone\shop\static\shop\images\normalized"
)

OUTPUT_FOLDER = Path(
    r"C:\StyleZone\contact_sheets"
)

OUTPUT_FOLDER.mkdir(exist_ok=True)


images = sorted(
    IMAGE_FOLDER.glob("*.png")
)


# Images per sheet
IMAGES_PER_SHEET = 25

# Size of each product image
IMAGE_WIDTH = 180
IMAGE_HEIGHT = 225

# Text area
TEXT_HEIGHT = 35

# Grid
COLUMNS = 5
ROWS = 5

SHEET_WIDTH = COLUMNS * IMAGE_WIDTH
SHEET_HEIGHT = ROWS * (IMAGE_HEIGHT + TEXT_HEIGHT)


for sheet_number in range(
    math.ceil(len(images) / IMAGES_PER_SHEET)
):

    start = sheet_number * IMAGES_PER_SHEET

    end = start + IMAGES_PER_SHEET

    batch = images[start:end]

    sheet = Image.new(
        "RGB",
        (SHEET_WIDTH, SHEET_HEIGHT),
        "white"
    )

    draw = ImageDraw.Draw(sheet)

    for index, image_path in enumerate(batch):

        row = index // COLUMNS
        column = index % COLUMNS

        x = column * IMAGE_WIDTH
        y = row * (IMAGE_HEIGHT + TEXT_HEIGHT)

        image = Image.open(image_path).convert("RGB")

        image.thumbnail(
            (IMAGE_WIDTH - 10, IMAGE_HEIGHT - 10)
        )

        image_x = x + (
            IMAGE_WIDTH - image.width
        ) // 2

        image_y = y + (
            IMAGE_HEIGHT - image.height
        ) // 2

        sheet.paste(
            image,
            (image_x, image_y)
        )

        filename = image_path.stem

        draw.text(
            (x + 5, y + IMAGE_HEIGHT + 5),
            filename,
            fill="black"
        )

    output_file = (
        OUTPUT_FOLDER
        / f"colour_sheet_{sheet_number + 1}.jpg"
    )

    sheet.save(
        output_file,
        quality=90
    )

    print(
        f"Created: {output_file}"
    )


print()
print("All contact sheets created.")