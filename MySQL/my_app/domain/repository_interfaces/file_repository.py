from abc import ABC, abstractmethod
from typing import BinaryIO

class FileRepository(ABC):
    @abstractmethod
    def get_file_text(self, file: BinaryIO)-> str:
        pass
    
    
    
    