import aiohttp
import asyncio

from .profile import Profile
from ._parsers import (
    parse_page,
    parse_answers,
)


class User:
    """Represents a Quora user."""

    def __init__(self, username, session=None):
        self.username = username
        self.profileUrl = f"https://www.quora.com/profile/{username}"
        self._session = session

    async def _create_session(self) -> None:
        """Creates a aiohttp client session."""
        self._session = aiohttp.ClientSession()

    async def _request(self, url) -> str:
        if self._session is None:
            await self._create_session()
        async with self._session.get(url) as response:
            return await response.text()

    async def profile(self):
        """Fetch profile of the user."""
        html_data = await self._request(self.profileUrl)
        json_data = parse_page(html_data)
        return Profile(self, json_data)

    async def answers(self):
        """Fetch answers of the User."""
        html_data = await self._request(self.profileUrl + "/answers")
        json_data = parse_page(html_data)
        answers = parse_answers(json_data)
        return answers

    def __eq__(self, other):
        return self.username == other.username


def __del__(self):
    loop = asyncio.get_event_loop()
    task = loop.create_task(self._session.close())
    if not loop.is_running():
        loop.run_untill_complete(task)
