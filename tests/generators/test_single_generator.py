from src.qrgen import QrConfig,QRGenerator, SingleGenerator


config = QrConfig(box_size=10, border=1, fill_color="blue", back_color="transparent")
qr_generator = QRGenerator(config=config)

single_generator = SingleGenerator(input_data='Manthan', generator=qr_generator, output_dir='outputs/single')

single_generator.generate()