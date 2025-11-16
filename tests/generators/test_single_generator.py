from src.qrgenkit import QrConfig,QRGenerator, SingleGenerator


config = QrConfig(box_size=10, border=1, fill_color="blue", back_color="transparent")
qr_generator = QRGenerator(config=config)
def progress_callback(data):
    print(f"Generated QR for {data}")
single_generator = SingleGenerator(input_data='Manthan', generator=qr_generator, output_dir='outputs/single',progress_callback=progress_callback)

single_generator.generate()