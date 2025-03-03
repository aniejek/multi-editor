import re


from dataclasses import dataclass
from typing import Optional


@dataclass
class FindResult:
    path: str
    searches: list[re.Match]


class Finder:
    def __init__(self, files: list[str] = [], regexp: Optional[str] = None):
        self.files = files
        self.regexp = regexp if regexp is not None else ""

    def set_files(self, files):
        self.files = files

    def set_regexp(self, regexp):
        self.regexp = regexp

    def __iter__(self):
        for file in self.files:
            with open(file) as processed:
                searches = []
                while True:
                    content = processed.read(4096)
                    if not content:
                        break
                    search = re.search(self.regexp, content)
                    if search:
                        searches.append(search)
            if searches:
                yield FindResult(path=file, searches=searches)
