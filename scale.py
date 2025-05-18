from PIL import Image
import os


def resize_image(input_path, output_path, new_width):
    image = Image.open(input_path)
    width, height = image.size
    ratio = new_width / width
    new_height = int(height * ratio)
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resized_image.save(input_path)


if __name__ == '__main__':
    input_file = 'images/Python.png'
    file_name, file_ext = os.path.splitext(input_file)
    new_file_name = file_name + '_resized' + file_ext
    new_width = 64  # 修改宽度为 64
    resize_image(input_file, input_file, new_width)
    input_file = './images/BeeD600.png'
    file_name, file_ext = os.path.splitext(input_file)
    new_file_name = file_name + '0' + file_ext
    new_width = 200  # 可根据需要修改宽度
    resize_image(input_file, input_file, new_width)