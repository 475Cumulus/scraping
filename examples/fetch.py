#!/usr/bin/env python
# encoding: utf-8

import asyncio
import aiohttp
from bs4 import BeautifulSoup

SELECTED_URL = 'http://cnn.com'

async def get_site_content(url) -> BeautifulSoup:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.read()

    return BeautifulSoup(text.decode('utf-8'), 'html.parser')

def get_title(soup: BeautifulSoup)-> str:
    title = soup.find('title')
    if title:
        return title.string
    return ''