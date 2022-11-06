from abc import abstractmethod, ABC


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(path: str) -> str:
        raise NotImplementedError()
