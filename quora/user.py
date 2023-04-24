import aiohttp
import asyncio
import logging
from .profile import Profile
from ._parsers import (
    parse_page,
    parse_answers,
    parse_topics,
)
from .cache import cache

subdomains = {
    "en": "English",
    "hi": "हिंदी",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
    "ja": "日本語",
    "id": "Indonesia",
    "pt": "Português",
    "nl": "Nederlands",
    "da": "Dansk",
    "fi": "Suomi",
    "no": "Norsk",
    "sv": "Svenska",
    "mr": "मराठी",
    "bn": "বাংলা",
    "ta": "தமிழ்",
    "ar": "العربية",
    "he": "עברית",
    "gu": "ગુજરાતી",
    "kn": "ಕನ್ನಡ",
    "ml": "മലയാളം",
    "te": "తెలుగు",
    "pl": "Polski",
}


class User:
    """Represents a Quora user."""

    def __init__(
        self,
        username,
        session=None,
        logger=logging.getLogger(__name__),
        cache_manager=None,
        cache_exp=None,
    ):
        self.username = username
        self._session = session
        self.logger = logger
        self.htmlLogger = logging.getLogger("pyquora-html")
        self._cache = cache_manager
        self._cache_exp = cache_exp

    def profileUrl(self, language="en"):
        if language == "en":
            apiEndPoint = "https://www.quora.com"
        elif language.lower() in subdomains.keys():
            apiEndPoint = f"https://{language.lower()}.quora.com"
        else:
            raise ValueError(f"{language} language is not found.")
        return apiEndPoint + f"/profile/{self.username}"

    async def _create_session(self) -> None:
        """Creates a aiohttp client session."""
        self._session = aiohttp.ClientSession()

    async def _request(self, url) -> str:
        if self._session is None:
            await self._create_session()
        async with self._session.get(url) as response:
            text = await response.text()
            self.htmlLogger.debug(text)
            return text

    @cache(cache_exp=5)
    async def profile(self, *args, **kwargs):
        """Fetch profile of the user."""
        lang = kwargs.get("language", "en")
        html_data = await self._request(self.profileUrl(language=lang))
        json_data = parse_page(html_data, self)
        return Profile(self, json_data, lang)

    @cache(cache_exp=30)
    async def answers(self, *args, **kwargs):
        """Fetch answers of the User."""
        lang = kwargs.get("language", "en")
        html_data = await self._request(self.profileUrl(language=lang) + "/answers")
        json_data = parse_page(html_data, self)
        answers = parse_answers(json_data, self, lang)
        return answers

    @cache(cache_exp=3600)
    async def knows_about(self, *args, **kwargs):
        """Fetch expertise topics."""
        lang = kwargs.get("language", "en")
        html_data = await self._request(self.profileUrl(language=lang) + "/knows_about")
        json_data = parse_page(html_data, self)
        topics = parse_topics(json_data, lang)
        return topics

    def __eq__(self, other):
        return self.username == other.username

    def __del__(self):
        loop = asyncio.get_event_loop()
        task = loop.create_task(self._session.close())
        if not loop.is_running():
            loop.run_untill_complete(task)
