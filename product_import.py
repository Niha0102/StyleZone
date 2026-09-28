import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stylezone.settings")
django.setup()

from django.db import connection

IMAGE_FOLDER = os.path.join(
    "shop",
    "static",
    "shop",
    "images"
)

# Category mapping
CATEGORY_MAP = {
    "women_dress": 1,
    "women_jeans": 1,
    "women_skirt": 1,
    "women_top": 1,
    "women_tshirt": 1,
    "women_trouser": 1,

    "saree": 2,
    "suit": 2,
    "kurti": 2,
    "lehenga": 2,
    "ethnic_dress": 2,

    "men_shirt": 3,
    "men_tshirt": 3,
    "men_jeans": 3,
    "men_trouser": 3,
    "men_kurta": 3,
    "men_jacket": 3,
    "coord": 1,
    "crop_top": 1,
    "jumpsuit": 1,
}


# Different descriptions for different product types
DESCRIPTIONS = {
    "women_dress": [
        "A stylish women's dress designed for an elegant everyday look.",
        "A versatile women's dress for creating effortless fashion looks.",
        "A fashionable dress that adds a modern touch to your wardrobe.",
        "A stylish women's outfit suitable for casual and special occasions.",
    ],

    "women_jeans": [
        "A versatile pair of women's jeans for comfortable everyday styling.",
        "Modern women's jeans designed for easy and fashionable outfits.",
        "A casual denim essential for creating effortless everyday looks.",
        "Stylish women's jeans that pair easily with different tops.",
    ],

    "women_skirt": [
        "A stylish women's skirt for creating fashionable casual outfits.",
        "A versatile skirt designed for effortless everyday styling.",
        "A fashionable women's skirt that adds a modern touch to your wardrobe.",
        "A comfortable skirt suitable for creating different casual looks.",
    ],

    "women_tshirt": [
        "A stylish women's T-shirt for comfortable everyday wear.",
        "A versatile casual T-shirt that pairs easily with different outfits.",
        "A modern women's T-shirt designed for effortless everyday styling.",
        "A comfortable everyday tee for simple and fashionable looks.",
    ],

    "women_top": [
        "A stylish women's top designed for effortless everyday outfits.",
        "A versatile top that adds a fashionable touch to casual looks.",
        "A modern women's top suitable for creating different everyday styles.",
        "A comfortable and stylish top for easy wardrobe combinations.",
    ],

    "women_trouser": [
        "A versatile women's trouser designed for effortless everyday styling.",
        "A modern trouser that adds a polished touch to casual outfits.",
        "A comfortable women's trouser for easy day-to-day fashion.",
        "A stylish trouser that pairs easily with different tops.",
    ],

    "men_shirt": [
        "A stylish men's shirt designed for a smart everyday look.",
        "A versatile shirt suitable for casual and everyday outfits.",
        "A modern men's shirt for effortless wardrobe styling.",
        "A comfortable shirt that works well with different everyday looks.",
    ],

    "men_tshirt": [
        "A comfortable men's T-shirt designed for everyday casual wear.",
        "A versatile casual tee for effortless everyday styling.",
        "A modern men's T-shirt that pairs easily with casual outfits.",
        "A stylish everyday tee designed for a relaxed look.",
    ],

    "men_jeans": [
        "A versatile pair of men's jeans for comfortable everyday styling.",
        "Modern men's jeans designed for casual everyday outfits.",
        "A classic denim essential for effortless men's fashion.",
        "Stylish men's jeans suitable for different casual looks.",
    ],

    "men_trouser": [
        "A versatile men's trouser designed for everyday styling.",
        "A modern trouser suitable for smart and casual outfits.",
        "Comfortable men's trousers for effortless everyday fashion.",
        "A stylish trouser that pairs well with different shirts and tops.",
    ],

    "men_kurta": [
        "A stylish men's kurta inspired by traditional Indian fashion.",
        "A versatile kurta designed for a refined traditional look.",
        "A comfortable men's kurta suitable for festive and everyday occasions.",
        "A traditional-inspired kurta with a contemporary fashion appeal.",
    ],

    "men_jacket": [
        "A stylish men's jacket designed to add a modern layer to outfits.",
        "A versatile jacket suitable for creating fashionable casual looks.",
        "A modern men's jacket for effortless everyday styling.",
        "A stylish outer layer that complements different casual outfits.",
    ],

    "kurti": [
        "A stylish kurti designed for an elegant traditional-inspired look.",
        "A versatile women's kurti suitable for everyday ethnic styling.",
        "A fashionable kurti that adds a graceful touch to your wardrobe.",
        "A comfortable kurti for creating effortless Indian wear looks.",
    ],

    "saree": [
        "A graceful saree designed for an elegant Indian fashion look.",
        "A versatile saree suitable for traditional and special occasions.",
        "A stylish saree that adds an elegant touch to your wardrobe.",
        "A beautiful Indian wear essential for creating a refined look.",
    ],

    "lehenga": [
        "A stylish lehenga designed for elegant traditional occasions.",
        "A graceful Indian outfit suitable for festive and special events.",
        "A fashionable lehenga for creating a statement ethnic look.",
        "A traditional-inspired lehenga designed for special occasions.",
    ],

    "suit": [
        "A stylish Indian suit designed for an elegant traditional look.",
        "A versatile suit suitable for festive and special occasions.",
        "A graceful Indian outfit for creating a refined ethnic look.",
        "A fashionable suit designed for comfortable traditional styling.",
    ],

    "ethnic_dress": [
        "A stylish ethnic dress inspired by traditional Indian fashion.",
        "A graceful ethnic outfit suitable for festive occasions.",
        "A fashionable Indian-inspired dress for elegant everyday styling.",
        "A versatile ethnic dress for creating a refined traditional look.",
    ],

    "jumpsuit": [
        "A stylish jumpsuit designed for an effortless modern look.",
        "A versatile jumpsuit suitable for fashionable casual outfits.",
        "A contemporary jumpsuit that brings effortless style to your wardrobe.",
        "A fashionable one-piece outfit for modern everyday styling.",
    ],

    "crop_top": [
        "A stylish crop top designed for modern casual outfits.",
        "A versatile crop top for creating trendy everyday looks.",
        "A fashionable crop top that pairs easily with different bottoms.",
        "A modern wardrobe essential for effortless casual styling.",
    ],

    "coord": [
        "A stylish coordinated outfit designed for effortless fashion.",
        "A versatile co-ord set for creating a polished modern look.",
        "A fashionable coordinated outfit that makes everyday styling easy.",
        "A contemporary co-ord set for comfortable and stylish dressing.",
    ],
}


def get_product_type(filename):
    name = filename.lower().replace(".png", "")

    for product_type in CATEGORY_MAP:
        if name.startswith(product_type + "_"):
            return product_type

    return None


def get_product_name(product_type, number):
    names = {
        "women_dress": [
            "Elegant Everyday Dress",
            "Modern Casual Dress",
            "Effortless Style Dress",
            "Classic Women's Dress",
            "Contemporary Fashion Dress",
            "Graceful Casual Dress",
            "Chic Everyday Dress",
            "Versatile Women's Dress",
        ],

        "women_jeans": [
            "Classic Women's Jeans",
            "Modern Casual Jeans",
            "Everyday Style Jeans",
            "Versatile Denim Jeans",
            "Contemporary Women's Jeans",
            "Essential Casual Jeans",
            "Effortless Style Jeans",
        ],

        "women_skirt": [
            "Elegant Everyday Skirt",
            "Modern Casual Skirt",
            "Versatile Style Skirt",
            "Classic Women's Skirt",
            "Contemporary Skirt",
            "Effortless Fashion Skirt",
            "Chic Everyday Skirt",
        ],

        "women_tshirt": [
            "Classic Everyday T-Shirt",
            "Casual Comfort T-Shirt",
            "Modern Women's T-Shirt",
            "Essential Casual Tee",
            "Everyday Style T-Shirt",
        ],

        "women_top": [
            "Classic Casual Top",
            "Modern Everyday Top",
            "Elegant Women's Top",
            "Versatile Style Top",
            "Everyday Fashion Top",
        ],

        "women_trouser": [
            "Classic Women's Trousers",
            "Modern Casual Trousers",
            "Everyday Style Trousers",
            "Versatile Women's Trousers",
            "Contemporary Trousers",
            "Elegant Everyday Trousers",
        ],
    }

    if product_type in names:
        name_list = names[product_type]

        if number <= len(name_list):
            return name_list[number - 1]

    return product_type.replace("_", " ").title() + f" {number}"


# Import images
files = sorted(
    file for file in os.listdir(IMAGE_FOLDER)
    if file.lower().endswith(".png")
)

inserted = 0
skipped = 0

with connection.cursor() as cursor:

    for filename in files:

        product_type = get_product_type(filename)

        if not product_type:
            print("Skipped:", filename)
            continue

        category_id = CATEGORY_MAP[product_type]

        number = int(
            filename.split("_")[-1].replace(".png", "")
        )

        product_name = get_product_name(
            product_type,
            number
        )

        description_list = DESCRIPTIONS.get(
            product_type,
            ["A stylish fashion item from StyleZone."]
        )

        description = description_list[
            (number - 1) % len(description_list)
        ]

        image_url = "images/" + filename

        # Prevent duplicate image records
        cursor.execute(
            """
            SELECT product_id
            FROM products
            WHERE image_url = %s
            """,
            [image_url]
        )

        if cursor.fetchone():
            print("Already exists:", filename)
            skipped += 1
            continue

        cursor.execute(
            """
            INSERT INTO products
            (
                category_id,
                product_name,
                description,
                brand,
                color,
                price,
                discount_percent,
                image_url,
                is_active,
                is_best_seller
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            [
                category_id,
                product_name,
                description,
                "StyleZone",
                "Multi",
                999.00,
                10.00,
                image_url,
                1,
                0
            ]
        )

        print("Inserted:", product_name, "→", filename)
        inserted += 1

print()
print("Import completed!")
print("Inserted:", inserted)
print("Skipped:", skipped)