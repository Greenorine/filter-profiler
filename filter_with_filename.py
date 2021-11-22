from PIL import Image
from numpy import array


def get_grayscale(x, y):
    """Рассчитать оттенок серого по полученным координатам
    :param x: x координата пикселя по оси абсцис
    :param y: y координата пикселя по оси ординат
    :return: оттенок серого

    >>> get_grayscale(0,0)
    4275
    >>> get_grayscale(1,0)
    4389
    >>> get_grayscale(25,25)
    5862
    >>> get_grayscale(540,540)
    10143
    """
    result = 0
    for step_x in range(x, min(x + width // mosaic_size, width)):
        for step_y in range(y, min(y + height // mosaic_size, height)):
            red = image_array[step_x][step_y][0]
            green = image_array[step_x][step_y][1]
            blue = image_array[step_x][step_y][2]
            result += (int(red) + int(green) + int(blue)) // 3
    return int(result // 100)


def append_grey_to_picture(x, y, greyscale):
    """Применить оттенок серого на картинке;
    :param x: текущий индекс по оси абсцисс
    :param y: текущий индекс по оси ординат
    :param greyscale: оттенок серого
    """
    for step_x in range(x, min(x + width // mosaic_size, width)):
        for step_y in range(y, min(y + height // mosaic_size, height)):
            image_array[step_x][step_y] = [int(greyscale // 50 * scale_step) * scale_step * 50] * 3


def create_grey_mosaic():
    """Превратить картинку в мозаику с серым фильтром"""
    i = 0
    while i < width - 1:
        j = 0
        while j < height - 1:
            append_grey_to_picture(i, j, get_grayscale(i, j))
            j = j + width // mosaic_size
        i = i + height // mosaic_size
    res = Image.fromarray(image_array)
    res.save(result_file)


source_file = "F:\\Прога\\filter-profiler\\images\\image.jpg"
result_file = "F:\\Прога\\filter-profiler\\images\\image_r.jpg"
image_array = array(Image.open(source_file))
width = len(image_array)
height = len(image_array[1])
mosaic_size = 10
scale_step = 1
create_grey_mosaic()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
