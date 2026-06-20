# ==============================
# Simple Image Caption Generator
# ==============================

image_objects = {
    "dog.jpg": ["dog", "ball", "park"],
    "cat.jpg": ["cat", "sofa"],
    "car.jpg": ["car", "road", "city"],
    "bike.jpg": ["bike", "helmet", "road"],
    "flower.jpg": ["flower", "garden"],
    "bird.jpg": ["bird", "tree", "sky"],
    "beach.jpg": ["beach", "sea", "sun"],
    "mountain.jpg": ["mountain", "trees", "river"],
    "book.jpg": ["book", "table", "lamp"],
    "laptop.jpg": ["laptop", "desk", "coffee"],
    "nature.jpg": ["nature", "trees", "river", "mountains", "sky"]
}

def generate_caption(image_name):

    if image_name not in image_objects:
        return "Image not found."

    objects = image_objects[image_name]

    if "dog" in objects:
        return "A happy dog is playing with a ball in the green park."

    elif "cat" in objects:
        return "A cute cat is relaxing comfortably on the sofa."

    elif "car" in objects:
        return "A modern car is driving smoothly through the busy city road."

    elif "bike" in objects:
        return "A biker is riding a sports bike safely wearing a helmet."

    elif "flower" in objects:
        return "A colorful flower is blooming beautifully in the garden."

    elif "bird" in objects:
        return "A small bird is flying freely across the blue sky."

    elif "beach" in objects:
        return "People are enjoying the sunny day at the beautiful beach."

    elif "mountain" in objects:
        return "A peaceful mountain landscape is surrounded by trees and a river."

    elif "book" in objects:
        return "An open book is placed neatly on the study table."

    elif "laptop" in objects:
        return "A laptop is kept on the desk beside a cup of coffee."
    
    elif "nature" in objects:
        return "A beautiful natural landscape with green trees, flowing river, majestic mountains, and a clear blue sky."

    else:
        return "No caption available."

# -----------------------------
# Main Program
# -----------------------------
image = input("Enter image name: ")

caption = generate_caption(image)

print("\nGenerated Caption:")
print(caption)