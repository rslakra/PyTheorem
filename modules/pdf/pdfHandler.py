#
# Author: Rohtash Lakra
#
import os
from io import BytesIO
from typing import Union

from pypdf import PdfReader, PdfWriter
from requests import api, Response, exceptions

from configs.base import Config


# Read .env local file

def build_url(base_url, *path_segments) -> str:
    """Returns the request URL string for the given path_segments"""
    # validate iterable api uri_path is not missing
    if not base_url:
        raise ValueError("'base_url' should provide!")

    uri_path = base_url
    if path_segments:
        request_path = "/".join(str(path) for path in path_segments if path is not None)
        uri_path = f"{uri_path}/{request_path}"

    return uri_path


class PdfHandler:

    def split(self, filePath: str):
        parentFolder = os.path.dirname(filePath)
        print(f'parentFolder={parentFolder}')
        fileName = os.path.splitext(os.path.basename(filePath))[0]
        pdfReader = PdfReader(filePath)
        for pdfPage in range(len(pdfReader.pages)):  # Use len(pdfReader.pages) for Python 3.x with pypdf
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdfReader.pages[pdfPage])  # Use pdfReader.pages[pdfPage] for Python 3.x with pypdf
            outputFilename = f'{parentFolder}/{fileName}_page_{pdfPage + 1}.pdf'
            with open(outputFilename, 'wb') as out:
                pdf_writer.write(out)
            print('Created: {}'.format(outputFilename))

    def split_pdf_pages(self, src_path: str, pages: int = 1):
        """Splits a PDF into the given pages (default: 1) and saves each as a separate PDF."""
        parentFolder = os.path.dirname(src_path)
        print(f'parentFolder={parentFolder}')
        fileName = os.path.splitext(os.path.basename(src_path))[0]
        pdfReader = PdfReader(src_path)
        pageCounter = 1;
        count = 0
        pdfWriter = PdfWriter()
        for i, page in enumerate(pdfReader.pages):
            print(f"page={i}")
            pdfWriter.add_page(page)
            count += 1
            if count == pages:
                outputFilename = f'{parentFolder}/{fileName}_{pageCounter}.pdf'
                with open(outputFilename, 'wb') as output:
                    pdfWriter.write(output)
                print(f"Created: {outputFilename}")
                pageCounter += 1
                count = 0
                pdfWriter = PdfWriter()

        # handle remaining pages
        if count > 0:
            outputFilename = f'{parentFolder}/{fileName}_{pageCounter}.pdf'
            with open(outputFilename, 'wb') as output:
                pdfWriter.write(output)

            print(f"Created: {outputFilename}")

    # def split_pdf_pages(src_path:str, target_path:str):
    #     """
    #     Splits a PDF into individual pages, saving each as a separate PDF.
    #
    #     Args:
    #         src_path (str): The path to the source PDF file.
    #         target_path (str): The base path for the output PDF files.
    #         (e.g., 'output_doc' will create 'output_doc_0.pdf', 'output_doc_1.pdf', etc.)
    #     """
    #     pdfReader = PdfReader(src_path)
    #
    #     for i, page in enumerate(pdfReader.pages):
    #         dst_pdf = PdfWriter()
    #         dst_pdf.add_page(page)
    #         with open(f'{target_path}_{i}.pdf', 'wb') as output_file:
    #             dst_pdf.write(output_file)
    #         print(f"Created: {target_path}_{i}.pdf")

    @staticmethod
    def is_success(response: Union[dict, Response, None]) -> bool:
        """Returns true if the provided response has status = 2xx or JSON response['code'] = 'Success'."""
        if response:
            if isinstance(response, Response):
                return 200 <= response.status_code < 300

        return False

    def read_pdf_from_url(self, document_id: str, parentFolder: str, is_lyft_michigan: bool = False) -> None:
        """
        Downloads a PDF from a URL using requests and extracts its text content.

        Args:
            pdf_url (str): The URL of the PDF file.

        Returns:
            str: The extracted text content from the PDF, or an error message.
        """
        try:
            request_headers = {
                "Authorization": f"Api-Key {Config.PANDADOC_API_KEY}",
                "Content-Type": "application/json"
            }

            # 1. Download the PDF content
            # GET https://api.pandadoc.com/public/v1/documents/document_id/download
            response = api.get(
                url=build_url(Config.PANDADOC_BASE_URL, f"public/v1/documents/{document_id}/download"),
                headers=request_headers,
            )

            # Raise an exception for HTTP errors (4xx or 5xx)
            response.raise_for_status()

            # Check PandaDoc response's status_code and response type and JSON.
            print(f"PandaDoc response status={response.status_code}")
            # Step 2-A: On Success Response, update DB with the current document status and version
            # if self.is_success(response):
            #     contents = response.content.decode('utf-8')

            # 2. Use io.BytesIO to handle the PDF data in memory
            # This prevents the need to save the PDF to a file first.
            with BytesIO(response.content) as pdf_data:
                # 3. Create a PdfReader object
                pdfReader = PdfReader(pdf_data)
                pdfWriter = PdfWriter()
                for i, page in enumerate(pdfReader.pages):
                    print(f"page={i}")
                    pdfWriter.add_page(page)
                    if is_lyft_michigan and i < 1:
                        continue
                    else:
                        break

                # write the contents only (exclude certificate page)
                outputFilename = f'{parentFolder}/{document_id}.pdf'
                with open(outputFilename, 'wb') as output:
                    pdfWriter.write(output)
                print(f"Created: {outputFilename}")

        except exceptions.RequestException as e:
            return f"Error downloading PDF: {e}"
        except Exception as e:
            return f"Error processing PDF: {e}"


if __name__ == '__main__':
    pdfHandler = PdfHandler()
    # pdfFilePath = "/Users/rlakra/Downloads/PDFs/lyft-vehicle-inspection-form-california.pdf"
    # # pdfHandler.split(pdfFilePath)
    # pdfHandler.split_pdf_pages(pdfFilePath)
    # pdfFilePath = "/Users/rlakra/Downloads/PDFs/lyft-vehicle-inspection-form-michigan.pdf"
    # # pdfHandler.split(pdfFilePath)
    # pdfHandler.split_pdf_pages(pdfFilePath, 2)

    PANDADOC_DOC_IDS = os.getenv("PANDADOC_DOC_IDS", None)
    if not PANDADOC_DOC_IDS:
        raise ValueError("PANDADOC_DOC_IDS should provide!")

    PANDADOC_DOC_IDS = [part.strip() for part in PANDADOC_DOC_IDS.split(",")]
    print(PANDADOC_DOC_IDS)
    document_id = PANDADOC_DOC_IDS[0]
    pdfHandler.read_pdf_from_url(document_id, "/Users/rlakra/Downloads/PDFs", True)
    document_id = PANDADOC_DOC_IDS[1]
    pdfHandler.read_pdf_from_url(document_id, "/Users/rlakra/Downloads/PDFs")
