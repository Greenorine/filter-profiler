from PIL import Image
from numpy import array


def get_grayscale(i, j):
    result = 0
    for step_x in range(i, min(i + width // mosaic_size, width)):
        for step_y in range(j, min(j + height // mosaic_size, height)):
            red = image_array[step_x][step_y][0]
            green = image_array[step_x][step_y][1]
            blue = image_array[step_x][step_y][2]
            result += (int(red) + int(green) + int(blue)) // 3
    return int(result // 100)


def append_grey_to_picture(i, j, greyscale):
    for step_x in range(i, min(i + width // mosaic_size, width)):
        for step_y in range(j, min(j + height // mosaic_size, height)):
            image_array[step_x][step_y] = [int(greyscale // 50 * scale_step) * scale_step * 50] * 3


def create_mosaic():
    i = 0
    while i < width - 1:
        j = 0
        while j < height - 1:
            append_grey_to_picture(i, j, get_grayscale(i, j))
            j = j + width // mosaic_size
        i = i + height // mosaic_size
    res = Image.fromarray(image_array)
    res.save(result_file)


print("Введите метосположение исходного файла в полном формате: ")
source_file = input()
print("Введите метосположение результативного файла в полном формате: ")
result_file = input()
image_array = array(Image.open(source_file))
width = len(image_array)
height = len(image_array[1])
print("Введите размер ячейки: ")
mosaic_size = int(input())
print("Введите шаг градации серого: ")
scale_step = int(input())
create_mosaic()
