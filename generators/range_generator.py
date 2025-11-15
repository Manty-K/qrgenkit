from generators.base_generator import BaseGenerator
from qr.qr_generator import QRGenerator
from pathlib import Path

class RangeGenerator(BaseGenerator):
    def __init__(self, input_data: dict, generator: QRGenerator, output_dir: str | Path):
        super().__init__(generator,output_dir)
        self.prefix = input_data.get('prefix','')
        self.suffix = input_data.get('suffix','')
        self.start = input_data['start']
        self.end = input_data['end']


    def _generate(self):
        for i in range(self.start, self.end+1):
            data = self.prefix + str(i) + self.suffix
            self._save_qr(data)

