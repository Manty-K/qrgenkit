from pathlib import Path

from src.qrgenkit import  QRGenerator, QrConfig, RangeGenerator, ListGenerator,SingleGenerator


def main():
    config = QrConfig( box_size=10, border=1, fill_color="blue", back_color="transparent")
    qr_generator = QRGenerator(config=config)
    range_generator = RangeGenerator(input_data={'start':1, 'end':3}, generator=qr_generator, output_dir=Path('outputs/range'))
    list_generator = ListGenerator(input_data=['Item1', 'Item2', 'Item3'], generator=qr_generator, output_dir='outputs/list')
    single_generator = SingleGenerator(input_data='Manthan', generator=qr_generator, output_dir='outputs/single')
    range_generator.generate()
    list_generator.generate()
    single_generator.generate()

if __name__ == '__main__':
    main()

