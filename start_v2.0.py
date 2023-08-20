from PIL import Image
picture = Image.open('..\JPEG to PDF\pic1.jpg')   #Путь к файлу и название файла
picture.format   # returns the image format
# output: 'JPEG'
picture.size   # returns the size of the image as (x pixels, y pixels)
# output: (3487, 5230)
picture.mode   # returns the image bands
# output: 'RGB'
# picture.show()  
page_size = [int(8.3 * 200), int(11.7 * 200)]
target_width, target_height = page_size
current_width, current_height = picture.size
scale = max(current_width /target_width, current_height/target_height)
final_image_size = [round(current_width / scale), round(current_height / scale)]
final_image_size
resized_image = picture.resize(size=final_image_size, resample=Image.LANCZOS)
resized_image.size
canvas_image = Image.new(mode='RGB', size=page_size, color='white')
# canvas_image.show()

canvas_image.paste(resized_image, box=(1,1))
canvas_image.show()
# canvas_image.save('PDF.jpeg', format='JPEG', quality=85, optimize=True)
canvas_image.save('Document.pdf', format='PDF', quality=300)   # Можно изменить название итоговорго файла
