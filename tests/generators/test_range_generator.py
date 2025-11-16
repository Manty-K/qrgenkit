from src.qrgenkit import QrConfig,QRGenerator, RangeGenerator


config = QrConfig(box_size=10, border=1, fill_color="blue", back_color="transparent")
qr_generator = QRGenerator(config=config)

def progress_callback(data):
    print(f"Generated QR for {data}")

range_generator = RangeGenerator(input_data={'prefix':'K','start':1, 'end':3}, generator=qr_generator, output_dir='outputs/range',progress_callback=progress_callback)

range_generator.generate()