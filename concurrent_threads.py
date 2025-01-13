from fakes.api_client import SeqApiClient
from fakes.image_tools import rotate_image
from fakes.cpu_heavy import is_prime
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from bootstrap import scale_image_array


def remote_api_task(reps: int, thread_limit: int = 256) -> None:
    client = SeqApiClient()
    ids = range(1, reps + 1)

    def actual_processing(id):
        data = client.get_important_data_by_id(id)
        if data["id"] % 3 == 1:
            data["company_name"] = "EPAM SYSTEMS TURBO SOLUTION PRO MAX"
            client.put_important_data_by_id(id, data)

    with ThreadPoolExecutor(max_workers=thread_limit) as executor:
        for id in ids:
            executor.submit(actual_processing, id)


def rotate_image_task(reps: int, img_qty: int = 8, thread_limit: int = 256) -> None:
    image_list = scale_image_array(img_qty)

    with ThreadPoolExecutor(max_workers=thread_limit) as executor:
        for image_filename in image_list:
            img = Image.open(image_filename)
            executor.submit(rotate_image, img, reps)

def first_primes_task(reps: int, complexity: int = 1_000_000, thread_limit: int = 256) -> None:
    def subtask():
        for i in range(complexity):
            is_prime(i)

    with ThreadPoolExecutor(max_workers=thread_limit) as executor:
        for i in range(reps): 
            executor.submit(subtask)
