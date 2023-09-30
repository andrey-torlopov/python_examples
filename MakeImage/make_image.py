from PIL import Image

# Создаем новое изображение с желтым цветом
image = Image.new("RGB", (100, 100), "yellow")

# Сохраняем изображение
image.save("yellow_image.png")
