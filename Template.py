# Author: Jayendra Matarage
# Title: Sketch to Code




class Template:
    def generate_data(self, data, width, height):

        avg_height = 100

        # divide page height with avg height
        page_height_parts = round(height / avg_height)

        # add image height sections into array
        height_cats = []
        avg_first = 0
        for x in range(page_height_parts):
            avg_first = avg_first + avg_height
            height_cats.append(avg_first)

        # get dives
        divs = data[0]['DIVS']
        selected_rows = []
        # add row id
        # loop divs
        for div in divs:
            # loop through height section array to find what is the section of array
            for row in range(len(height_cats)):
                # if center Y of div is less than to section add section array index to div
                if div['MID_Y'] <= height_cats[row]:
                    div['R'] = row
                    # add selected section id array
                    selected_rows.append(row)
                    break

        # remove duplicated section id
        selected_rows = list(set(selected_rows))

        # devide dives into rows
        row_splitted = []

        # loop through selected sections
        for row in range(len(selected_rows)):
            div_of_row = []
            for div in divs:
                # if selected divs R id equals into row id add div into array
                if div['R'] == selected_rows[row]:
                    div_of_row.append(div)
            # add selected rows with divs into main array

            row_splitted.append(div_of_row)

        return row_splitted

    def generate_items_of_div(self, items, rows):

        paragraphs_of_page = items[0]['PARAS']
        images_of_page = items[0]['IMAGES']
        list_of_page = items[0]['LISTS']

        rows_of_page = rows

        # add paragraphs to div
        for row in rows_of_page:
            row_divs = row
            for div in range(len(row_divs)):
                paras_of_div = []
                for paras in paragraphs_of_page:
                    if paras['P1'][0] > row_divs[div]['P1'][0] and paras['P1'][1] > row_divs[div]['P1'][1] and \
                                    paras['P2'][0] < row_divs[div]['P2'][0] and paras['P2'][1] < row_divs[div]['P2'][1]:
                        paras_of_div.append(paras)
                        break
                row_divs[div]['PARAS'] = paras_of_div

        # add image to div
        for row in rows_of_page:
            row_divs = row
            for div in range(len(row_divs)):
                images_of_div = []
                for images in images_of_page:
                    if images['P1'][0] > row_divs[div]['P1'][0] and images['P1'][1] > row_divs[div]['P1'][1] and \
                                    images['P2'][0] < row_divs[div]['P2'][0] and images['P2'][1] < row_divs[div]['P2'][
                        1]:
                        images_of_div.append(images)
                        break
                row_divs[div]['IMAGES'] = images_of_div

        # add list to div
        for row in rows_of_page:
            row_divs = row
            for div in range(len(row_divs)):
                list_of_div = []
                for lists in list_of_page:
                    if lists['P1'][0] > row_divs[div]['P1'][0] and lists['P1'][1] > row_divs[div]['P1'][1] and \
                                    lists['P2'][0] < row_divs[div]['P2'][0] and lists['P2'][1] < row_divs[div]['P2'][1]:
                        list_of_div.append(lists)
                        break
                row_divs[div]['LISTS'] = list_of_div

        return rows_of_page
