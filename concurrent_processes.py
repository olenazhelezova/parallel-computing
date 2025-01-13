from fakes.api_client import SeqApiClient
from fakes.image_tools import rotate_image
from fakes.cpu_heavy import is_prime
from concurrent.futures import ProcessPoolExecutor
from PIL import Image
from bootstrap import scale_image_array


def actual_processing(ids: list[int]):
    client = SeqApiClient()
    for id in ids:
        data = client.get_important_data_by_id(id)
        if data["id"] % 3 == 1:
            data["company_name"] = "EPAM SYSTEMS TURBO SOLUTION PRO MAX"
            client.put_important_data_by_id(id, data)


def remote_api_task(reps: int, batch_size: int = 1, process_limit: int = 8) -> None:
    ids = range(1, reps, batch_size)

    with ProcessPoolExecutor(max_workers=process_limit) as executor:
        for from_id in ids:
            executor.submit(
                actual_processing, list(range(from_id, min(from_id + batch_size, reps)))
            )


def rotate_image_task(reps: int, img_qty: int = 8, process_limit: int = 8) -> None:
    image_list = scale_image_array(img_qty)

    with ProcessPoolExecutor(max_workers=process_limit) as executor:
        for image_filename in image_list:
            img = Image.open(image_filename)
            executor.submit(rotate_image, img, reps)


def subtask(complexity: int) -> None:
    for i in range(complexity):
        is_prime(i)


def first_primes_task(reps: int, complexity: int = 1_000_000, process_limit: int = 8) -> None:
    with ProcessPoolExecutor(max_workers=process_limit) as executor:
        for i in range(reps): 
            executor.submit(subtask, complexity)
