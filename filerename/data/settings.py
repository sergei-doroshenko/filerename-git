# Simple class
import configparser
from datetime import date


class Settings:
    config = {}

    def __init__(self) -> None:
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.read('./resources/config.ini')

    def now(self):
        # print(self.config['DATABASE']['HOST'])
        today = date.today()
        return today
