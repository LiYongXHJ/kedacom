# coding=utf-8
import configparser, os


class Config():
    def get_config(self, section, option):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '\config\config.ini'
        config.read(file_path)
        return config.get(section=section, option=option)

    @property
    def ip(self):
        return self.get_config('serverIp', 'ip')

    @property
    def username(self):
        return self.get_config('uerName', 'username')

    @property
    def password(self):
        return self.get_config('password', 'password')
