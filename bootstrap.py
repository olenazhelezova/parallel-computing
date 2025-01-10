IMAGE_FILES = [
    "alpaca.jpg",
    "cat.jpg",
    "dog.jpg",
    "donkey.jpg",
    "duck.jpg",
    "fox.jpg",
    "giraffe.jpg",
    "monkeys.jpg",
]


def scale_image_array(target_size: int):
    image_paths = list(map(lambda x: "images/" + x, IMAGE_FILES))
    return (
        image_paths * (target_size // len(image_paths))
        + image_paths[: (target_size % len(image_paths))]
    )
