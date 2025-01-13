from fakes.api_client import AsyncApiClient
from fakes.image_tools import rotate_image
from fakes.cpu_heavy import is_prime
from bootstrap import scale_image_array
from PIL import Image
from asyncio import gather


async def remote_api_task_bad(reps: int) -> None:
    client = AsyncApiClient()
    ids = range(1, reps + 1)
    for id in ids:
        data = await client.get_important_data_by_id(id)
        if data["id"] % 3 == 1:
            data["company_name"] = "EPAM SYSTEMS TURBO SOLUTION PRO MAX"
            await client.put_important_data_by_id(id, data)


async def remote_api_task_good(reps: int) -> None:
    client = AsyncApiClient()
    ids = range(1, reps + 1)

    async def actual_processing(id):
        data = await client.get_important_data_by_id(id)
        if data["id"] % 3 == 1:
            data["company_name"] = "EPAM SYSTEMS TURBO SOLUTION PRO MAX"
            await client.put_important_data_by_id(id, data)

    await gather(*[actual_processing(id) for id in ids])


async def rotate_image_task(reps: int, img_qty: int = 8) -> None:
    async def wrapper(filename: str, reps):  # There's nothing really async here
        img = Image.open(
            filename
        )  # unfortunately there's no async version of this library
        return rotate_image(img, reps)

    await gather(
        *[
            wrapper(image_filename, reps)
            for image_filename in scale_image_array(img_qty)
        ]
    )


async def first_primes_task(reps: int, complexity: int = 1_000_000) -> None:
    for i in range(reps): 
        for j in range(complexity):
            is_prime(j)
