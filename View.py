# Author: Jayendra Matarage
# Title: Sketch to Code
import random



class View:
    def random_color(self):
        r = lambda: random.randint(0, 255)
        return '#%02X%02X%02X' % (r(), r(), r())

    def generate_html_code(self, element_object,image_height):
        elements = element_object

        max_height = 0
        for row in elements:
            for div in row:
                if max_height < div['H']:
                    max_height = div['H']

        view_string = ""
        for row in elements:
            view_string = view_string + "<div class='row'>"
            for div in row:
                if len(div['IMAGES']) >= 1:
                    view_string = view_string + "<div style='height:" + str(max_height) + "px;background-color: " + str(
                        self.random_color()) + "' class='col-" + str(div['BT_SIZE']) + " p-0'>"
                else:
                    view_string = view_string + "<div style='height:" + str(max_height) + "px;background-color: " + str(
                        self.random_color()) + "' class='col-" + str(div['BT_SIZE']) + "'>"

                for paras in div['PARAS']:
                    view_string = view_string + "<p>This is paragraph</p>"

                for images in div['IMAGES']:
                    view_string = view_string + "<img style='height:" + str(
                        max_height) + "px;width:100%' src=https://dummyimage.com/" + str(div['W']) + "x" + str(max_height) + "/000/fff' />"

                for lists in div['LISTS']:
                    view_string = view_string + "<ul>"
                    view_string = view_string + "<li>One</li>"
                    view_string = view_string + "<li>Two</li>"
                    view_string = view_string + "<li>Three</li>"
                    view_string = view_string + "</ul>"

                view_string = view_string + "</div>"

            view_string = view_string + "</div>"
        return view_string
