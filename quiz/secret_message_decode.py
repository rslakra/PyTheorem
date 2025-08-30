#
# Author: Rohtash Lakra
#
# Decoding a Secret Message
#
# Problem
# You are given a published Google Doc like "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub" one that contains a list of Unicode characters and their positions in a 2D grid.
# Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters.
# When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

# The document specifies the Unicode characters in the grid, along with the x-coordinate and y-coordinate of each character.
# The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.
# Any positions in the grid that do not have a specified character should be filled with a space character.
# You can assume the document will always have the same format as the example document linked above.

# For example, the simplified example document linked above draws out the letter 'F':
# █▀▀▀
# █▀▀
# █

# Note that the coordinates (0, 0) will always correspond to the same corner of the grid as in this example, so make sure to understand in which directions the x-coordinate and y-coordinate increase.

# Specifications

# You may use external libraries.
# You may write helper functions, but there should be one function that:
# 1. Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND
# 2. When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.

from typing import NamedTuple, List

import requests
from bs4 import BeautifulSoup


class GridTuple(NamedTuple):
    """Represents a tuple of coordinates and a character."""
    x_coordinate: int
    character: str
    y_coordinate: int

    @classmethod
    def from_data(cls, row_data: List[str]):
        """
        Creates a GridTuple from row_data, converting numbers if necessary.

        Args:
            row_data: The list of strings representing a row of data.
        """
        # The constructor `cls()` is then called with the properly typed data
        return cls(x_coordinate=int(row_data[0]), character=row_data[1], y_coordinate=int(row_data[2]))

    def print_types(self):
        field_strings = [f"{key}={type(value)}" for key, value in self._asdict().items()]
        return f"{self.__class__.__name__} <{', '.join(field_strings)}>"

    def __str__(self):
        field_strings = [f"{key}={value}" for key, value in self._asdict().items()]
        return f"{self.__class__.__name__} <{', '.join(field_strings)}>"


class SecretMessageDecoder:
    """A class to decode a secret message."""

    def read_google_document(self, doc_url: str):
        """
        Retrieves data from a published Google Doc, constructs a 2D character grid,
        and prints it.

        Args:
            doc_url (str): The URL of the published Google Doc.
        """
        # 1. Fetch the document content as plain text.
        # We modify the URL to access a plain text version of the document.
        html_string = None
        try:
            response = requests.get(doc_url)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            # The raw content is in bytes
            # html_bytes = response.content
            # print(f"html_bytes={html_bytes}")

            # # requests can often guess the encoding for you
            html_string = response.text
            # html_string = html_string.strip().split('\n')
            # print(f"html_string={html_string}")

            # Or you can decode it yourself, using the encoding from the response
            # html_string = html_bytes.decode(response.encoding)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the document: {e}")

        return html_string

    def parser_html_read_grid_tuples(self, html_text: str) -> List[GridTuple]:
        """Parses the HTML text and returns a list of GridTuples."""
        soup = BeautifulSoup(html_text, 'html.parser')

        # Find the <table> tags in the document and all its rows
        table = soup.find('table')
        rows = table.find_all('tr')

        # Extract data into a list of lists
        gridTuples = []
        for row in rows:
            try:
                columns = row.find_all('td')
                row_data = [column.text.strip() for column in columns]
                if row_data[0] == 'x-coordinate':
                    continue
                else:
                    gridTuples.append(GridTuple.from_data(row_data))
            except ValueError as e:
                print(f"Skipping malformed line: '{row_data}'. Error: {e}")

        # Print the result
        # self.print_line()
        # print(f"gridTuples={gridTuples}")

        # for row in gridTuples:
        #     print(row)

        return gridTuples

    def print_unicode_grid_from_google_doc(self, doc_url):
        """
        Retrieves data from a published Google Doc, constructs a 2D character grid,
        and prints it.

        Args:
            doc_url (str): The URL of the published Google Doc.
        """
        # 1. Fetch the document content as plain text.
        html_string = self.read_google_document(doc_url)

        # 2. Parse the document content to extract characters and coordinates.
        gridTuples = self.parser_html_read_grid_tuples(html_string)

        if not gridTuples:
            print("No valid character data found in the document.")
            return

        # We find the max coordinates to determine the grid size.
        max_x = max(map(lambda x: int(x.x_coordinate), gridTuples))
        max_y = max(map(lambda x: int(x.y_coordinate), gridTuples))

        # 3. Initialize the grid with space characters.
        # Grid dimensions are based on max_x and max_y.
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        # 4. Populate the grid with the characters.
        for gridTuple in gridTuples:
            # print(f"gridTuple={gridTuple.print_types()}")
            if 0 <= gridTuple.y_coordinate <= max_y and 0 <= gridTuple.x_coordinate <= max_x:
                grid[gridTuple.y_coordinate][gridTuple.x_coordinate] = gridTuple.character

        # 5. Print the grid.
        for row in reversed(grid):
            print(''.join(row))


instance = SecretMessageDecoder()

# Example usage (using the URL from the problem description)
example_doc_url = 'https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub'
# example_doc_url = 'https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub'
instance.print_unicode_grid_from_google_doc(example_doc_url)
