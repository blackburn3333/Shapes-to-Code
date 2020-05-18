# Author: Jayendra Matarage
# Title: Sketch to Code


import cv2



class Sketch:
    div_map = [
        {'SIZE': 0, 'COL_SIZE': 2},
        {'SIZE': 16.6, 'COL_SIZE': 2},
        {'SIZE': 24.9, 'COL_SIZE': 4},
        {'SIZE': 33.2, 'COL_SIZE': 4},
        {'SIZE': 41.5, 'COL_SIZE': 6},
        {'SIZE': 49.8, 'COL_SIZE': 6},
        {'SIZE': 58.1, 'COL_SIZE': 8},
        {'SIZE': 66.4, 'COL_SIZE': 8},
        {'SIZE': 74.7, 'COL_SIZE': 10},
        {'SIZE': 83.0, 'COL_SIZE': 10},
        {'SIZE': 91.3, 'COL_SIZE': 12},
        {'SIZE': 99.6, 'COL_SIZE': 12}
    ]

    def find_main_divs(self, img):
        print("|Detecting Divs...")
        image_to_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # detect edges of image using canny
        edges_of_image = cv2.Canny(image_to_gray, 50, 150, apertureSize=3)
        # find contours using canny image
        cont, hierarachy = cv2.findContours(edges_of_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        div_count = 0
        unknown_count = 0
        position_of_div = []
        all_divs_of_page = []

        for c in cont:
            approx = cv2.approxPolyDP(c, 0.03 * cv2.arcLength(c, True), True)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(c)
                if w > 10 and h > 10:
                    if x not in position_of_div:
                        position_of_div.append(x)
                        M = cv2.moments(c)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        cv2.circle(img, (cX, cY), 3, (255, 255, 0), -1)
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                        width_of_rec_in_percentage = (w / img.shape[1]) * 100

                        for point in reversed(self.div_map):
                            if point['SIZE'] < width_of_rec_in_percentage:
                                cv2.putText(img, 'DIV size : ' + str(point['COL_SIZE']), (int(x + 10), int(y + 20)),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                            (0, 0, 255), 1,
                                            cv2.LINE_AA)
                                cv2.putText(img, 'DIV' + str(div_count), (int(x), int(y + h)),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            0.5, (255, 0, 0), 1, cv2.LINE_AA)

                                all_divs_of_page.append({
                                    "DIV_ID": div_count,"BT_SIZE": point['COL_SIZE'], "W": w,"H": h,"P1": [x, y], "P2": [x + w, y + h],"MID_X": cX, "MID_Y": cY,
                                })

                                break
                        div_count += 1
            else:
                unknown_count += 1

        print("|Main DIV count : " + str(div_count))

        div_data = [{
            "DIV_COUNT": div_count,
            "DIV_DATA": all_divs_of_page,
            "IMAGE": img,
        }]

        return div_data

    def find_paras(self, img):
        print("|Detecting Paragraphs...")

        # make image window
        #cv2.namedWindow('Paras of page', cv2.WINDOW_AUTOSIZE)

        # make gray image
        image_to_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # detect edges of image using canny
        edges_of_image = cv2.Canny(image_to_gray, 50, 150, apertureSize=3)

        # find contours using canny image
        cont, hierarachy = cv2.findContours(edges_of_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # sort image contours
        cont = sorted(cont, key=lambda ctr: cv2.boundingRect(ctr)[1])

        para_count = 0
        unknown_count = 0
        p_array_position = []
        all_paras_of_page = []

        for c in cont:
            approx = cv2.approxPolyDP(c, 0.03 * cv2.arcLength(c, True), True)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(c)
                if w > 10 and h > 10:
                    if w < 50 and h < 50:
                        if x not in p_array_position:
                            M = cv2.moments(c)
                            cX = int(M["m10"] / M["m00"])
                            cY = int(M["m01"] / M["m00"])
                            cv2.circle(img, (cX, cY), 3, (255, 255, 0), -1)
                            p_array_position.append(x)
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                            all_paras_of_page.append({
                                "P_ID": para_count,"W": w, "H": h,
                                "P1": [x, y],"P2": [(x + w), (y + h)],"MID_X": cX,"MID_Y": cY,
                            })
                            cv2.putText(img, 'Paragraph ' + str(para_count), (int(x + w), int(y)),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.5, (255, 0, 0), 1, cv2.LINE_AA)
                            para_count += 1
            else:
                unknown_count += 1

        print("|Paragraph count : " + str(para_count))

        para_data = [{
            "PARA_COUNT": para_count,
            "PARA_DATA": all_paras_of_page,
            "IMAGE": img,
        }]

        return para_data

    def find_images(self, img):
        print("|Detecting Images...")
        # make image window
        #cv2.namedWindow('Images of page', cv2.WINDOW_AUTOSIZE)

        # make gray image
        image_to_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # detect edges of image using canny
        edges_of_image = cv2.Canny(image_to_gray, 50, 150, apertureSize=3)

        # find contours using canny image
        cont, hierarachy = cv2.findContours(edges_of_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # sort image contours
        cont = sorted(cont, key=lambda ctr: cv2.boundingRect(ctr)[1])

        img_count = 0
        unknown_count = 0
        i_array_position = []
        all_images_of_page = []

        for c in cont:
            approx = cv2.approxPolyDP(c, 0.03 * cv2.arcLength(c, True), True)
            if len(approx) == 3:
                x, y, w, h = cv2.boundingRect(c)
                if w > 10 and h > 10:
                    if x not in i_array_position:
                        cv2.drawContours(img, [c], 0, (255, 0, 0), 1)
                        i_array_position.append(x)
                        M = cv2.moments(c)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        cv2.circle(img, (cX, cY), 3, (255, 255, 0), -1)
                        all_images_of_page.append({
                            "IMAGE_ID": img_count,
                            "W": w,
                            "H": h,
                            "P1": (x, y),
                            "P2": (x + w, y + h),
                            "MID_X": cX,
                            "MID_Y": cY,
                        })

                        cv2.putText(img, "img " + str(img_count), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (255, 0, 0), 1, cv2.LINE_AA)
                        img_count += 1
            else:
                unknown_count += 1

        print("|Images count : " + str(img_count))

        image_data = [{
            "IMAGE_COUNT": img_count,
            "IMAGE_DATA": all_images_of_page,
            "IMAGE": img,
        }]

        return image_data

    def find_lists(self, img):
        print("|Detecting Lists...")
        # make image window
        #cv2.namedWindow('Lists of page', cv2.WINDOW_AUTOSIZE)

        # make gray image
        image_to_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # detect edges of image using canny
        edges_of_image = cv2.Canny(image_to_gray, 50, 150, apertureSize=3)

        # find contours using canny image
        cont, hierarachy = cv2.findContours(edges_of_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # sort image contours
        cont = sorted(cont, key=lambda ctr: cv2.boundingRect(ctr)[1])

        list_count = 0
        unknown_count = 0
        l_array_position = []
        all_lists_of_page = []

        for c in cont:
            approx = cv2.approxPolyDP(c, 0.03 * cv2.arcLength(c, True), True)
            if len(approx) == 5:
                x, y, w, h = cv2.boundingRect(c)
                if w > 10 and h > 10:
                    if x not in l_array_position:
                        cv2.drawContours(img, [c], 0, (0, 0, 255), 1)
                        l_array_position.append(x)
                        M = cv2.moments(c)
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        cv2.circle(img, (cX, cY), 3, (255, 255, 0), -1)
                        all_lists_of_page.append({
                            "LIST": list_count,
                            "W": w,
                            "H": h,
                            "P1": (x, y),
                            "P2": (x + w, y + h),
                            "MID_X": cX,
                            "MID_Y": cY,
                        })

                        cv2.putText(img, "list " + str(list_count), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (255, 0, 0), 1, cv2.LINE_AA)
                        list_count += 1
            else:
                unknown_count += 1

        print("|Lists count : " + str(list_count))
        list_data = [{
            "LIST_COUNT": list_count,
            "LIST_DATA": all_lists_of_page,
            "IMAGE": img,
        }]

        return list_data
