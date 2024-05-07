# Standard Library
from abc import ABC
from abc import abstractmethod

# My Stuff
from src.utils.client import db

from bson import ObjectId
from fastapi import Body
from fastapi import HTTPException
from fastapi import status
from pymongo import ReturnDocument
from motor.core import AgnosticCollection
from fastapi.responses import Response


class BaseRepository(ABC):
    def __init__(self, collection_name: str) -> None:
        """
        Initializes a new instance of the Common class.
        """
        # Get the collection from the database
        self.collection: AgnosticCollection = db.get_collection(collection_name)

    @abstractmethod
    def create_document(self):
        """
        Creates a new document.

        This method is responsible for creating a new document in the repository.
        """
        pass

    @abstractmethod
    def list_documents(self):
        """
        Retrieves a list of documents from the repository.

        Returns:
            list: A list of documents.
        """
        pass

    @abstractmethod
    def show_document(cls):
        """
        This class method is intended to display a document.

        As a class method, it operates on the class rather than instances of the class.
        Currently, this method does nothing and needs to be implemented.
        """
        pass

    @abstractmethod
    def update_document(cls):
        """
        This class method is intended to update a document

        As a class method, it operates on the class rather than instances of the class.
        Currently, this method does nothing and needs to be implemented.
        """
        pass

    @abstractmethod
    def delete_document(cls):
        """
        This class method is intended to delete a document.

        As a class method, it operates on the class rather than instances of the class.
        Currently, this method does nothing and needs to be implemented.
        """
        pass
