import os
from typing import Any

import requests


class Session(requests.Session):
    
    def __init__(self, year: int, day: int) -> None:
        super().__init__()
        self.year = year
        self.day = day
        self.cookies = requests.cookies.cookiejar_from_dict({'session': os.environ['AOC_SESSION']})
    
    @property
    def url(self) -> str:
        return f'https://adventofcode.com/{self.year}/day/{self.day}'
    
    def problem(self) -> str:
        return self.get(f'{self.url}/input').text

    def solution(self, level: int, answer: Any) -> requests.Response:
        return self.post(f'{self.url}/answer', data={
            'level': level, 
            'answer': answer
        })
