"""
Transcripted from https://github.com/n-y-z-o/nyzoVerifier/blob/master/src/main/java/co/nyzo/verifier/MessageObject.java
"""

from abc import ABC, abstractmethod
from pynyzo.helpers import base_app_log


class MessageObject(ABC):

    __slots__ = ('app_log', )

    def __init__(self, app_log: object=None):
        self.app_log = base_app_log(app_log)

    @abstractmethod
    def get_byte_size(self) -> int:
        # return len(self._bytes)
        pass

    @abstractmethod
    def get_bytes(self) -> bytes:
        #return self._bytes
        pass


class EmptyMessageObject(MessageObject):

    def get_byte_size(self) -> int:
        return 0

    def get_bytes(self) -> bytes:
        return b''