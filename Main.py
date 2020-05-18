# Author: Jayendra Matarage
# Title: Sketch to Code

from os import path

from Sketch import Sketch
from Template import Template
from View import View
from File import File
import cv2

image_process = Sketch()
generate_template = Template()
view = View()
file = File()

if __name__ == '__main__':
    print("|-------------------------------------------------------|")
    print("|\t\t\t\t\tShapes to </>code\t\t\t\t\t|")
    print("|-------------------------------------------------------|")

    image_file = input("|\tEnter image file name : ")
    while True:
        if image_file == "":
            image_file = input("|\tPlease enter image file name : ")
        else:
            if path.exists(image_file) != True:
                image_file = input("|\tFile not found or incorrect file name : ")
            else:
                break
    print("|-------------------------------------------------------|")
    print("|\tProcessing " + image_file + '....')


    img = cv2.imread(image_file)
    # resize image
    scale_percent = 12
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print("|Image size H " + str(img.shape[0]) + " | W " + str(img.shape[1]))
    print("|-------------------------------------------------------|")


    img_detect_divs = img.copy()
    divs_of_page = image_process.find_main_divs(img_detect_divs)
    cv2.imshow('Divs of page', divs_of_page[0]['IMAGE'])
    div_data = divs_of_page[0]['DIV_DATA']
    print("|-------------------------------------------------------|")

    img_detect_para = img.copy()
    paras_of_page = image_process.find_paras(img_detect_para)
    cv2.imshow('Paras of page', paras_of_page[0]['IMAGE'])
    para_data = paras_of_page[0]['PARA_DATA']
    print("|-------------------------------------------------------|")

    img_detect_images = img.copy()
    image_of_page = image_process.find_images(img_detect_images)
    cv2.imshow('Images of page', image_of_page[0]['IMAGE'])
    image_data = image_of_page[0]['IMAGE_DATA']
    print("|-------------------------------------------------------|")

    img_detect_lists = img.copy()
    list_of_page = image_process.find_lists(img_detect_lists)
    cv2.imshow('Lists of page', list_of_page[0]['IMAGE'])
    list_data = list_of_page[0]['LIST_DATA']
    print("|-------------------------------------------------------|")

    collected_div_data = [{
        "DIVS": div_data,
    }]
    collected_item_data = [{
        "PARAS": para_data,
        "IMAGES": image_data,
        "LISTS": list_data
    }]

    # add divs to rows
    divs_with_row = generate_template.generate_data(collected_div_data, width, height)

    # add div items
    items_to_divs = generate_template.generate_items_of_div(collected_item_data, divs_with_row)

    print("|Generating view.....")

    #for rows in items_to_divs:
     #   print(rows)

    # generate view
    generated_view = view.generate_html_code(items_to_divs, img.shape[0])

    print("|Saving view.....")
    file.save_file(generated_view)
    print("|Process done")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


