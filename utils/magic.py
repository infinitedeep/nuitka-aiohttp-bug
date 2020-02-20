import aiohttp
from utils import network

async def get_message():
    print('utils.magic:get_message entry')
    await network.get()
    print('utils.magic:get_message exit')
