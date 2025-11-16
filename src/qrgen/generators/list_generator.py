from src.qrgen.generators.base_generator import BaseGenerator
from src.qrgen.qr.qr_generator import QRGenerator

class ListGenerator(BaseGenerator):
    def __init__(self, input_data: list[str], generator: QRGenerator, output_dir: str, progress_callback=None):
        super().__init__(generator, output_dir,progress_callback)
        self.data_list = input_data

    # def _generate(self):
    #     for data in self.data_list:
    #         self._save_qr(data)
    #         if self.progress_callback:
    #             callback_data = {
    #                 'current_data': data,
    #                 'percent_complete': ''# todo
    #             }
    #             self.progress_callback(callback_data)

    def _generate(self):
        total = len(self.data_list)

        for idx, data in enumerate(self.data_list, start=1):
            self._save_qr(data)

            if self.progress_callback:
                percent = (idx / total) * 100
                callback_data = {
                    "current_data": data,
                    "percent_complete": percent
                }
                self.progress_callback(callback_data)


