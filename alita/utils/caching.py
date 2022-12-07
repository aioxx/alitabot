from asyncio import locks
from time import perf_counter, time
from typing import List

from cachetools import TTLCache
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery
from pyrogram.types.messages_and_media.message import Message

from alita import LOGGER

THREAD_LOCK = locks.Lock()

# admins stay cached for 30 mins
ADMIN_CACHE = TTLCache(maxsize=512, ttl=(60 * 30), timer=perf_counter)
# Block from refreshing admin list for 10 mins
TEMP_ADMIN_CACHE_BLOCK = TTLCache(maxsize=512, ttl=(60 * 10), timer=perf_counter)


async def admin_cache_reload(m: Message or CallbackQuery, status=None) -> List[int]:
    start = time()
    async with THREAD_LOCK:

        if isinstance(m, CallbackQuery):
            m = m.message
        if status is not None:
            TEMP_ADMIN_CACHE_BLOCK[m.chat.id] = status

        try:
            if TEMP_ADMIN_CACHE_BLOCK[m.chat.id] in ("autoblock", "manualblock"):
                return []
        except KeyError:
            # Because it might be first time when admn_list is being reloaded
            pass

        admin_list = [
            (
                z.user.id,
                f"@{z.user.username}" if z.user.username else z.user.first_name,
                z.is_anonymous,
            )
            async for z in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS)
            if not z.user.is_deleted
        ]

        ADMIN_CACHE[m.chat.id] = admin_list
        LOGGER.info(
            f"Loaded admins for chat {m.chat.id} in {round((time() - start), 3)}s due to '{status}'",
        )
        TEMP_ADMIN_CACHE_BLOCK[m.chat.id] = "autoblock"

        return admin_list
