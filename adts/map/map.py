#
# Author: Rohtash Lakra
#
import json


class Map(dict):
    """Map"""

    def __repr__(self) -> str:
        """Returns the string representation of this object."""
        return json.dumps(self)
