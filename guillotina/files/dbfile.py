from .field import BaseCloudFile
from guillotina.interfaces import IDBFile
from zope.interface import implementer


@implementer(IDBFile)
class DBFile(BaseCloudFile):
    """File stored in a DB using blob storage"""

    _blob = None

    @property
    def valid(self):
        return self._blob is not None

    def get_actual_size(self):
        return self._blob.size

    @property
    def size(self):
        return self._blob.size

    @size.setter
    def size(self, val):
        pass
