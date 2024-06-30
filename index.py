import os

from PIL import Image

images_folder = "./images-to-convert"
converted_images_folder = "./converted-images"
images_list = []


def clear_converted_folder():
    if os.path.exists(converted_images_folder):
        print(f"\n Clearing folder from files... \n")
        for filename in os.listdir(converted_images_folder):
            current_image_path = os.path.join(converted_images_folder, filename)
            try:
                if os.path.isfile(current_image_path):
                    os.unlink(current_image_path)
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (current_image_path, e))


def get_images_name():
    for dirpath, dirnames, filenames in os.walk(images_folder):
        images_list.extend(filenames)
        break


def convert_images():
    for index, img in enumerate(images_list):
        print(f"processing image # {index + 1} / {len(images_list)}", end="\n")
        image_name = os.path.splitext(img)[0]
        print(image_name)
        current_image = Image.open(os.path.join(images_folder, img))
        current_image.convert("RGB")
        current_image.save(
            os.path.join(converted_images_folder, f"{image_name}.webp"),
            "webp",
        )

        os.unlink(os.path.join(images_folder, img))


if __name__ == "__main__":
    if not os.path.exists(converted_images_folder):
        os.makedirs(converted_images_folder)

    clear_converted_folder()
    get_images_name()
    convert_images()

    print("\n  All images converted (: \n")
