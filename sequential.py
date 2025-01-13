from fakes.api_client import SeqApiClient
from fakes.image_tools import rotate_image
from fakes.cpu_heavy import is_prime
from bootstrap import scale_image_array
from PIL import Image


# Simple example of IO-heavy task,
#   scanning entities by id and making updates to some of them.
def remote_api_task(reps: int) -> None:
    client = SeqApiClient()
    ids = range(1, reps + 1)
    for id in ids:
        data = client.get_important_data_by_id(id)
        if id % 3 == 1:
            data["company_name"] = "EPAM SYSTEMS TURBO SOLUTION PRO MAX"
            client.put_important_data_by_id(id, data)


def image_rotate_task(reps: int, img_qty: int = 8) -> None:
    for image_filename in scale_image_array(img_qty):
        img = Image.open(image_filename)
        rotate_image(img, reps)


def first_primes_task(reps: int, complexity: int = 1_000_000) -> None:
    for i in range(reps): 
        for j in range(complexity):
            is_prime(j)
