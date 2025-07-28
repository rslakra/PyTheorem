#
# Author: Rohtash Lakra
#
import os

import requests

from configs.base import Config

CHUNK_SIZE = 8192
OK_STATUS = 200
DOWNLOAD_PATH = os.path.join(os.path.expanduser('~'), 'Downloads')


class FileHandler:
    """File Handler"""

    def __init__(self, baseUrl: str):
        self.baseUrl = baseUrl

    def download(self, fileName: str, outputFile: str = None, isStream: bool = True) -> None:
        """Stream the download to avoid loading the whole file into memory"""
        try:
            outputFilePath = "/".join([DOWNLOAD_PATH, outputFile if outputFile else fileName])
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

        #     print(f"Download complete: {outputFilePath}")
        # else:
        #     print(f"Failed to download file. Status code: {response.status_code}")


if __name__ == '__main__':
    # print(IOUtils.getDownloadFolderPath())
    # Replace with the actual URL of your choice
    serverUrl = "https://example.com"
    serverUrl = Config.GOOGLE_API_VIDEO_FILES_URL
    # fileName = 'video.mp4'  # Name of the download file
    video_file_names = Config.VIDEO_FILE_NAMES
    print(video_file_names)
    if video_file_names:
        video_file_names = [part.strip() for part in video_file_names.split(",")]
        fileName = video_file_names[0]
        # outputFile = 'video.mp4'  # Name of the local file
        fileHandler = FileHandler(serverUrl)
        fileHandler.download(fileName)
    else:
        print("Missing video file names!")
