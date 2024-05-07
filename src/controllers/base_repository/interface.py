"""interface.py"""
# Standard Library
from abc import ABC, abstractmethod

from motor.core import AgnosticCollection

# My Stuff
from src.utils.client import db


class BaseRepository(ABC):
    """
    The base repository class.

    This class defines the common interface for all repositories.
    """

    def __init__(self, collection_name: str) -> None:
        """
        Initializes a new instance of the Common class.
        """
        # Get the collection from the database
        self.collection: AgnosticCollection = db.get_collection(collection_name)

    @abstractmethod
    async def create_document(self):
        """
        Creates a new document.

        This method is responsible for creating a new document in the repository.
        """

    @abstractmethod
    async def list_documents(self):
        """
        Retrieves a list of documents from the repository.

        Returns:
            list: A list of documents.
        """

    @abstractmethod
    async def show_document(self):
        """
        This class method is intended to display a document.

        As a class method, it operates on the class rather than instances of the class.
        Currently, this method does nothing and needs to be implemented.
        """

    @abstractmethod
    async def update_document(self):
        """
        This class method is intended to update a document

        As a class method, it operates on the class rather than instances of the class.
        Currently, this method does nothing and needs to be implemented.
        """

    @abstractmethod
    def delete_document(self):
        """
        This class method is intended to delete a document.

        As a class method, it operates on the class rather than instances of the class.
        Currently, this method does nothing and needs to be implemented.
        """
