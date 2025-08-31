#
# Author: Rohtash Lakra
#
import json
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(frozen=True)
class TokenPair:
    """"""
    name: str
    value: str

    def __str__(self):
        """Converts the dataclass instance to a string."""
        return f"{self.__class__.__name__} <name={self.name}, value={self.value}>"

    def __repr__(self):
        return str(self)

    def as_dict(self) -> dict[str, str]:
        """Generate a dictionary representation of the model."""
        return asdict(self)

    def to_json(self) -> str:
        """Converts the dataclass instance to a JSON string."""
        return json.dumps(self.as_dict(), indent=2)  # Using indent for pretty printing


@dataclass
class TokenList:
    """The list of token pairs"""
    tokens: Optional[TokenPair] = None

    def add_token_pair(self, token_pair: TokenPair):
        """
        Adds a new record (dictionary) to the list.
        Performs basic validation to ensure the record is a dictionary with string keys and values.
        """
        if token_pair and (not token_pair.name or len(token_pair.name) == 0):
            raise ValueError("The token_pair's name should provide.")

        if self.tokens is None:
            self.tokens = []

        self.tokens.append(token_pair)

    def add_pairs(self, name: str, value: str):
        """
        Adds a new record (dictionary) to the list.
        Performs basic validation to ensure the record is a dictionary with string keys and values.
        """
        self.add_token_pair(TokenPair(name, value))

    def __len__(self):
        """
        Returns the number of tokens in the 'tokens' list.
        """
        return len(self.tokens)

    def __str__(self):
        """Converts the dataclass instance to a string."""
        return f"{self.__class__.__name__} <tokens={self.tokens}>"

    def __repr__(self):
        return str(self)

    def as_dict(self) -> dict[str, str]:
        """Generate a dictionary representation of the model."""
        return asdict(self)

    def to_json(self) -> str:
        """Converts the dataclass instance to a JSON string."""
        return json.dumps(self.as_dict(), indent=2)  # Using indent for pretty printing
