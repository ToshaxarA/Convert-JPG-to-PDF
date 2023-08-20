from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

def convert_jpeg_to_pdf(image_path, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    image = Image(image_path)
    image.drawHeight = 636  # Вы можете настроить размер изображения
    image.drawWidth = 456
    story = [image]
    doc.build(story)

# Пример использования
jpeg_path = 'Bank account.jpg'
pdf_path = 'output2.pdf'

convert_jpeg_to_pdf(jpeg_path, pdf_path)



# # Разрешение в пикселях на дюйм (dpi)
# dpi = 300

# # Размеры страницы A4 в миллиметрах
# page_width_mm = 210
# page_height_mm = 297

# # Конвертация размеров страницы A4 из миллиметров в пиксели
# page_width_px = int((page_width_mm / 25.4) * dpi)
# page_height_px = int((page_height_mm / 25.4) * dpi)

# print("Ширина страницы A4 в пикселях:", page_width_px)
# print("Высота страницы A4 в пикселях:", page_height_px)

# 