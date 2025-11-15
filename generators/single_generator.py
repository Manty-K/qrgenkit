from generators.base_generator import BaseGenerator
from pathlib import Path

class SingleGenerator(BaseGenerator):
    def __init__(self, input_data: str, generator, output_dir: str | Path):
        super().__init__(generator, output_dir)
        self.data = input_data

    def _generate(self):
        self._save_qr(self.data)