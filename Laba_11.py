from PIL import Image, ImageFilter
import os
import csv

#11.1
def process_images_in_folder(input_folder, output_folder, name_filter):
    try:
        os.makedirs(output_folder, exist_ok=True)
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(input_folder, filename)
                try:
                    img = Image.open(filepath)
                    processed_img = img.filter(name_filter)
                    output_filepath = os.path.join(output_folder, filename)
                    processed_img.save(output_filepath)
                    print(f"Обработано изображение: {filename}")
                except Exception as e:
                    print(f"Ошибка при обработке {filename}: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

process_images_in_folder("images_input", "images_output", ImageFilter.BLUR)

#11.2
def image_info(image_path):
    try:
        if image_path.lower().endswith(('.jpg', '.png')):
            img = Image.open(image_path)
            print(f"Размер изображения: {img.width}x{img.height}")
            print(f"Формат изображения: {img.format}")
            print(f"Цветовая модель: {img.mode}")
        else:
            print(f"Файл {image_path} не является JPG или PNG изображением.")
    except FileNotFoundError:
        print(f"Файл {image_path} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")

def process_images_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.jpg', '.png')):
                file_path = os.path.join(folder_path, filename)
                print(f"Информация о файле: {filename}")
                image_info(file_path)
                print("-" * 20)
    except FileNotFoundError:
        print(f"Папка {folder_path} не найдена.")
    except Exception as e:
         print(f"Ошибка при обработке папки: {e}")
process_images_in_folder("images_input")

#11.3
def Raschet_csv(csv_filepath):
    try:
        total_sum = 0
        shopping_list = []
        csvfile = open(csv_filepath)
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = row['Продукт']
            quantity = int(row['Количество'])
            price = int(row['Цена'])
            cost = quantity * price
            total_sum += cost
            shopping_list.append(f"{product} - {quantity} шт. за {price} руб.")
        csvfile.close()
        print("Нужно купить:")
        for item in shopping_list:
            print(item)
        print(f"Итоговая сумма: {total_sum} руб.")
    except FileNotFoundError:
        print(f"Ошибка: Файл {csv_filepath} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке CSV: {e}")

Raschet_csv("shopping_list.csv")
