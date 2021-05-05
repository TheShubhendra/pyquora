import json
import re
import asyncio
import aiohttp

from .profile import Profile
from .exceptions import ProfileNotFoundError


class User:
    def __init__(self, username, session=None):
        self.username = username
        self.profileUrl = f"https://www.quora.com/profile/{username}"
        self._session = session

    async def _create_session(self) -> None:
        self._session = aiohttp.ClientSession()

    async def _fetch_profile_html(self) -> str:
        if self._session is None:
            await self._create_session()
        async with self._session.get(self.profileUrl) as response:
            return await response.text()

    async def _parse_page(self, html_data):
        try:
            data = re.findall(
                r'window\.ansFrontendGlobals\.data\.inlineQueryResults\.results\[".*?"\] = ("{.*}");',
                html_data,
            )[-1]
            data = json.loads(json.loads(data))
        except Exception:
            raise ProfileNotFoundError("No profile found with this username.")
        return data["data"]["user"]

    async def profile(self):
        html_data = await self._fetch_profile_html()
        json_data = await self._parse_page(html_data)
        return Profile(self, json_data)
