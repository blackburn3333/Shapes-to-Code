# Author: Jayendra Matarage
# Title: Sketch to Code

class File:
    def save_file(self, data_string):
        #print(data_string)

        file_data = ""
        file_data = file_data + "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8' />"
        file_data = file_data + "<meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no' />"
        file_data = file_data + "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'/>"
        file_data = file_data + "<title>Template</title></head><body>"

        file_data = file_data + data_string

        file_data = file_data + "<script src='https://code.jquery.com/jquery-3.2.1.slim.min.js' integrity = 'sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN' crossorigin = 'anonymous'> </script>"

        file_data = file_data + "<script src = 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js' integrity = 'sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q' crossorigin = 'anonymous'> </script >"
        file_data = file_data + "<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js' integrity = 'sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl' crossorigin = 'anonymous'></script>"
        file_data = file_data + "</body></html>"

        f = open("template.html", "w")
        f.write(file_data)
        f.close()
