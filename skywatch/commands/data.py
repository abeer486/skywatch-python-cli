"""The data command."""


from json import dumps

from .base import Base


class data(Base):
    """Return Data API"""

    def run(self):
        print('DATA API')
        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
