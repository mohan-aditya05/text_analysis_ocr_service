from typing import Protocol


class OCR(Protocol):
    """_summary_

    Args:
        Protocol (_type_): _description_
    """

    def get_text_response(self, images: list):
        pass

    # @abstractmethod
    # def get_bboxes(images:list):
    #     pass
