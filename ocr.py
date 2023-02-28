from abc import ABCMeta, abstractmethod

class OCR(ABCMeta):

    @abstractmethod
    def get_text_response(images:list):
        pass
    
    @abstractmethod
    def get_bboxes(images:list):
        pass
        