#
# Author: Rohtash Lakra
#
import os

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from configs.base import Config

CHUNK_SIZE = 8192
OK_STATUS = 200
DOWNLOAD_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')


class FileHandler:
    """File Handler"""

    def __init__(self, baseUrl: str):
        self.baseUrl = baseUrl

    def download(self, fileName: str, outputFolder: str = None, isStream: bool = True) -> None:
        """Stream the download to avoid loading the whole file into memory"""
        try:
            outputFolderPath = "/".join([DOWNLOAD_PATH, outputFolder]) if outputFolder else DOWNLOAD_PATH
            # Check if the folder exists
            if not os.path.exists(outputFolderPath):
                # Create the folder if it doesn't exist
                os.makedirs(outputFolderPath)
                print(f"Folder '{outputFolderPath}' created.")

            # append filename to save a file
            outputFilePath = "/".join([outputFolderPath, fileName])
            requestUri = self.baseUrl
            name, extension = os.path.splitext(fileName)
            if self.baseUrl:
                if not self.baseUrl.endswith(fileName):
                    requestUri = "/".join([self.baseUrl, fileName])

            print(f"requestUri={requestUri}")
            response = requests.get(requestUri, stream=isStream)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

            # Check if the request was successful
            if response.status_code == OK_STATUS:
                with open(outputFilePath, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:  # Filter out keep-alive chunks
                            file.write(chunk)
            else:
                print(f"Status Code={response.status_code}, Error: {response.content}")

            fileSize = os.path.getsize(outputFilePath)
            print(f"File '{outputFilePath}' downloaded successfully.")
            print(f"File size: {fileSize} bytes")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
        except OSError as e:
            print(f"Error getting file size: {e}")


class DomParser:
    """DOM Parser"""

    @classmethod
    def isTag(cls, element) -> bool:
        return element and isinstance(element, Tag)

    @classmethod
    def getContentPair(cls, element) -> bool:
        if element:
            return element.name, element.contents[0] if element.contents else None

        return None, None

    @classmethod
    def readContents(cls, filePath: str):
        contentVideoFiles = None
        # Load and parse the XML file
        with open('public-video-files.xml', 'r') as file:
            contentVideoFiles = file.read()

        return contentVideoFiles


apiVideoFilesUrl = Config.GOOGLE_API_VIDEO_FILES_URL
fileHandler = FileHandler(apiVideoFilesUrl)

# Reference: https://www.crummy.com/software/BeautifulSoup/bs4/doc

# # Load and parse the XML file
# with open('public-video-files.xml', 'r') as file:
#     contentVideoFiles = file.read()

# Reads the contents of the given file.
videoFiles = DomParser.readContents('public-video-files.xml')

# soup = BeautifulSoup(contentVideoFiles, 'html.parser')
soup = BeautifulSoup(videoFiles, 'html.parser')
# print(soup.prettify())
listBucketResult = soup.listbucketresult
# print(f"listBucketResult={soup.listBucketResult}")
# listBucketResult = soup.get('listbucketresult')
# print(f"listBucketResult={soup.listBucketResult}")
# listBucketResult = soup.find_all('listbucketresult')
# print(f"listBucketResult={soup.listBucketResult}")
# print(f"attr={soup.name}")
print(f"parent={soup.parent}")
print(f"parents={soup.parents}")
contents = soup.contents
# print(f"contents={contents}")
listBucketResult = soup.contents[0]
# print(f"listBucketResult={listBucketResult}")
print(f"xmlns={listBucketResult.get('xmlns')}")
print()
parentFolder = None
# childrend nodes
for child in listBucketResult.children:
    # read only tags
    if DomParser.isTag(child):
        # print(f"type={type(child)}, child={child}")
        # print(f"child.name={child.name}")
        # print(f"child.contents={child.contents}")
        # print(f"{child.name}={child.contents[0] if child.contents else None}")
        name, content = DomParser.getContentPair(child)
        print(f"{name}={content}")
        if name == 'name':
            parentFolder = content

        # for content in child.contents:
        #     print(f"content={content}")
        # print(f"child.descendants={child.descendants}")
        for descendant in child.descendants:
            if DomParser.isTag(descendant):
                # print(f"type={type(descendant)}, descendant={descendant}")
                name, content = DomParser.getContentPair(descendant)
                print(f"{name}={content}")
                if name == 'key':
                    # download the video file
                    fileHandler.download(content, parentFolder)

        print()
        # if child.contents:
        #     print(f"child.contents={child.contents}")

        # if child.children:
        #     print(f"child.children={child.children}")

    # print(f"child.contents={child.contents}")
    # print(child)

# print(f"attrs={soup.attrs}")
# print(f"attr={soup.attrs.keys()}")
# print()
# print(f"contents['name']={contents[0]['name']}")


# ListBucketResult
#     <Name>public-video-files</Name>
#     <Prefix/>
#     <Marker/>
#     <IsTruncated>false</IsTruncated>

# Find all person elements
# contents = soup.find_all('contents')
# print(contents)

# iterate each contents node.
# for content in contents:
#     # key = content.get('key')
#     key = content.find('key').text
#     generation = content.find('generation').text
#     metaGeneration = content.find('metageneration').text
#     lastModified = content.find('lastmodified').text
#     eTag = content.find('etag').text
#     size = content.find('size').text
#     print(
#         f"Content key={key}, generation={generation}, metaGeneration={metaGeneration}, lastModified={lastModified}, eTag={eTag}, size={size}")
#     # contentObject = Content.fromXml(content)
#     # print(f"contentObject={contentObject}")
