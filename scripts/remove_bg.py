from PIL import Image

def remove_white_bg(input_path, output_path, threshold=240):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()

    new_data = []
    for item in data:
        # Check if the pixel is white-ish
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            # Change all white-ish pixels to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Saved transparent image to {output_path}")

remove_white_bg("c:/Users/Shashwat Upadhyay/Downloads/sargam readme/assets/brand/hero.jpg", "c:/Users/Shashwat Upadhyay/Downloads/sargam readme/assets/brand/hero.png")
