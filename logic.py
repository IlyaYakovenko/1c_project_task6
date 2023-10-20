from PIL import ImageTk, Image

def map_create():
    map_raw = Image.open("map.jpg")
    width = 1000
    ratio = (width / float(map_raw.size[0]))
    height = int((float(map_raw.size[1]) * float(ratio)))
    app_map = map_raw.resize((width, height), Image.LANCZOS)
    app_map = ImageTk.PhotoImage(app_map)
    return app_map, width, height
