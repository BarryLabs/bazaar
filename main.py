import json
import os
import sys

import customtkinter
import requests

url = "https://www.cheapshark.com/api/1.0/"
top15deals = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"


# class App(customtkinter.CTk):
#     def __init__(self):
#         self.NAME = "Papyrus"
#         self.HEIGHT = 300
#         self.WIDTH = 500
#         self.STYLE = "Dark"
#         self.COLOR = "green"

#         self.customtkinter.set_appearance_mode(self.STYLE)
#         self.customtkinter.set_default_color_theme(self.COLOR)

#         self.app = customtkinter.CTk()
#         self.app.title(self.NAME)
#         self.app.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT))

#         self.button = customtkinter.CTkButton(
#             App, text="Get Deals", command=topFifteen()
#         )
#         self.button.pack(pady=80)

#         self.app.mainloop()
#         return App.mainloop()


def getRequest(url):
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        print("Website is Down. <Non-200>")
        sys.exit()


def postRequest(url, params):
    params = []

    # Handle Parameter Manipualtion

    r = requests.post(url, params)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        print("Website is Down. <Non-200>")
        sys.exit()


def writeData(data):
    try:
        with open("data.json", "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.close()
    except FileNotFoundError:
        print("File Not Found.")
        sys.exit()


def cleanData(file):
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            f.seek(0)

            titles = dict(data["title"])
            storeIDs = dict(data["storeID"])

            print(titles)

    except FileNotFoundError:
        sys.exit()


def main():
    cleanData("data.json")


if __name__ == "__main__":
    main()
