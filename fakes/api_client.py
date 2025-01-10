from asyncio import sleep as async_sleep
from time import sleep as blocking_sleep
from faker import Faker
from random import triangular


class BaseApiClient:
    def __init__(self, max_timeout: float = 0.66):
        self._max_timeout = max_timeout
        self._faker = Faker("en_GB")

    def _fake_data(self, id: int) -> dict:
        return {
            "id": id,
            "name": self._faker.name(),
            "email": self._faker.email(),
            "address": self._faker.address(),
            "birthday": self._faker.date_of_birth(),
        }

    def _wait(self) -> None:
        pass


class SeqApiClient(BaseApiClient):
    def __wait(self) -> None:
        blocking_sleep(triangular(0, self._max_timeout))

    def get_important_data_by_id(self, id: int) -> dict:
        self.__wait()
        return self._fake_data(id)

    def put_important_data_by_id(self, id: int, data: dict) -> None:
        self.__wait()


class AsyncApiClient(BaseApiClient):
    async def __wait(self) -> None:
        await async_sleep(
            triangular(0, self._max_timeout)
        )  # Emulate network delays and processing time

    async def get_important_data_by_id(self, id: int) -> dict:
        await self.__wait()
        return self._fake_data(id)

    async def put_important_data_by_id(self, id: int, data: dict) -> None:
        await self.__wait()
