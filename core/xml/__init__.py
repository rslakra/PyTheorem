#
# Author: Rohtash Lakra
#

class XmlHandler:

    def getObjects(self):
        """Returns the list of objects"""
        pass


class XmlParser:
    """Xml Parser"""

    def parse(self, xmlHandler: XmlHandler = None):
        return xmlHandler.getObjects()

    def getObjects(self):
        pass
