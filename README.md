# pyquora

Fetches user profiles and data from Quora.

![GitHub](https://img.shields.io/github/license/TheShubhendra/pyquora)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyquora)

![GitHub last commit](https://img.shields.io/github/last-commit/TheShubhendra/pyquora)

![Build Status](https://img.shields.io/github/workflow/status/TheShubhendra/pyquora/Python%20package)
![Requires.io (branch)](https://img.shields.io/requires/github/TheShubhendra/pyquora/master)
![GitHub repo size](https://img.shields.io/github/repo-size/TheShubhendra/pyquora)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyquora)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pyquora)
![PyPI](https://img.shields.io/pypi/v/pyquora)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![PyPI - Status](https://img.shields.io/pypi/status/pyquora)
![PyPI - Format](https://img.shields.io/pypi/format/pyquora)


# installation

`pip install pyquora`

# Usage

```python
import asyncio
from quora import User

async def main():
    user = User(<Quora-Username>)
    profile = await user.profile()
    print(profile.followerCount)
asyncio.run(main())

```