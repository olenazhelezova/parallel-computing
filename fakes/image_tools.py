from PIL import ImageFile


def rotate_image(img: ImageFile, reps: int) -> None:
    h, w = img.size
    for _ in range(reps):
        img.rotate(1, center=(h / 2, w / 2))
