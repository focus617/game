#!/usr/bin/env python
# -*- Coding：utf-8 -*-
"""
《python应用开发实战》
"""


class GameUnitError(Exception):
    """Custom exception class for the 'AbstractGameUnit' and its subclasses"""
    def __init__(self, message='', code=000):
        super().__init__(message)
        self.error_message = '~' * 50 + '\n'
        self.error_dict = {
            000: 'error-000: unspecified error',
            101: 'error-101: health meter problem',
            102: 'error-102: attack issue ignored'
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~' * 50










