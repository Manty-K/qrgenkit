from src.qrgenkit import QrConfig,QRGenerator, ListGenerator


config = QrConfig(box_size=10, border=1, fill_color="blue", back_color="transparent")
qr_generator = QRGenerator(config=config)

def progress_callback(data):
    print(f"Generated QR for {data}")

range_generator = ListGenerator(input_data=['hello','there'], generator=qr_generator, output_dir='outputs/list',progress_callback=progress_callback)

range_generator.generate()