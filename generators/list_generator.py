from generators.base_generator import BaseGenerator
from qr.qr_generator import QRGenerator

class ListGenerator(BaseGenerator):
    def __init__(self, input_data: list[str], generator: QRGenerator, output_dir: str):
        super().__init__(generator, output_dir)
        self.data_list = input_data

    def _generate(self):
        for data in self.data_list:
            self._save_qr(data)


