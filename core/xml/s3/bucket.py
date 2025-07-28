#
# Author: Rohtash Lakra
#
from enum import unique

from core.enums import BaseEnum
from core.xml import XmlParser


@unique
class ContentEnum(BaseEnum):
    KEY = "Key"
    GENERATION = "Generation"
    META_GENERATION = "MetaGeneration"
    LAST_MODIFIED = "LastModified"
    ETAG = "ETag"
    SIZE = "Size"

class Content:
    """Contents Object

    <Contents>
        <Key>10-minutes-platform-demo-invoice-audit-and-routing-2025-04-11-english.mp4</Key>
        <Generation>1744436646047369</Generation>
        <MetaGeneration>1</MetaGeneration>
        <LastModified>2025-04-12T05:44:06.064Z</LastModified>
        <ETag>"5587e7b1423b1d085612ad6791bef7ed"</ETag>
        <Size>22835510</Size>
    </Contents>
    """

    def __init__(self, key: str, generation: int = None, metaGeneration: int = None, lastModified: str = None,
                 eTag: str = None, size: int = None):
        self.key = key
        self.generation = generation
        self.metaGeneration = metaGeneration
        self.lastModified = lastModified
        self.eTag = eTag
        self.size = size

    def __str__(self):
        """Returns the string representation of this object."""
        return f"{type(self).__name__} <key={self.key}, generation={self.generation}, metaGeneration={self.metaGeneration}, lastModified={self.lastModified}, eTag={self.eTag}, size={self.size}>"

    def __repr__(self):
        return str(self)

    @classmethod
    def fromXml(cls, content):
        return Content(content.get('Key'),
                       content.find('Generation').text,
                       content.find('MetaGeneration').text,
                       content.find('LastModified').text,
                       content.find('ETag').text,
                       content.find('Size').text)


class ListBucketResult:
    """ListBucketResult

    <Name>public-video-files</Name>
    <Prefix/>
    <Marker/>
    <IsTruncated>false</IsTruncated>
    <Contents></Contents>

    """

    def __init__(self, name: str, prefix: str = None, marker: str = None, isTruncated: bool = False,
                 contents: list[Content] = None):
        self.xmlns = "http://doc.s3.amazonaws.com/2006-03-01"
        self.name = name
        self.prefix = prefix
        self.marker = marker
        self.isTruncated = isTruncated
        self.contents = contents


class S3BucketParser(XmlParser):
    """S3 Bucket Parser
    https://storage.googleapis.com/public-video-files
    """

    def __init__(self):
        pass
