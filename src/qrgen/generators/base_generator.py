from abc import ABC, abstractmethod
from src.qrgen.qr.qr_generator import QRGenerator
from pathlib import Path

class BaseGenerator(ABC):
    def __init__(self, generator:QRGenerator, output_dir: str|Path, progress_callback=None):
        self.generator:QRGenerator = generator
        self.output_dir:Path = Path(output_dir)
        self.progress_callback = progress_callback

    def generate(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._generate()

    def _save_qr(self, data: str):
        safe_name = data.replace('/', '_').replace('\\', '_')
        file_path = self.output_dir / f"{safe_name}.png"
        self.generator.generate_qr(data, output_file_path=str(file_path))

    @abstractmethod
    def _generate(self):
        pass