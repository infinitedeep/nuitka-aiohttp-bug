#!/usr/bin/python3

import asyncio
import traceback

from utils import magic

async def sayHello():
    try:
        print('main: invoking get_magic message')
        await magic.get_message()
        print('main: invoked get_magic message')
    except Exception:
        traceback.print_exc()

loop = asyncio.get_event_loop()
loop.run_until_complete(sayHello())
