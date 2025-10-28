import json
import sys

import customtkinter as ctk
import pandas
import requests

url = "https://www.cheapshark.com/api/1.0/"
top15deals = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

STYLE = "Dark"
COLOR = "green"
ctk.set_appearance_mode(STYLE)
ctk.set_default_color_theme(COLOR)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.NAME = "Bazaar"
        self.HEIGHT = 300
        self.WIDTH = 500

        self.data = self.load_data("data.json")

        self.frame = ctk.CTkFrame(self, corner_radius=10)
        self.frame.pack(pady=4, padx=4, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.frame, text=self.NAME)
        self.title_label.pack(fill="x")

        self.title_entry = ctk.CTkEntry(self.frame)
        self.title_entry.insert(0, self.data[0]["title"])
        self.title_entry.pack()

        self.sale_price_label = ctk.CTkLabel(self.frame, text="Sale Price")
        self.sale_price_label.pack(fill="x")

        self.sale_price_entry = ctk.CTkEntry(self.frame)
        self.sale_price_entry.insert(0, self.data[0]["salePrice"])
        self.sale_price_entry.pack()

        self.store_id_label = ctk.CTkLabel(self.frame, text="Store ID")
        self.store_id_label.pack(fill="x")

        self.store_id_entry = ctk.CTkEntry(self.frame)
        self.store_id_entry.insert(0, self.data[0]["storeID"])
        self.store_id_entry.pack()

    def load_data(self, file):
        try:
            with open(file) as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: File Not Found")
            return None


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
