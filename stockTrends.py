# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
import tkinter as tk
import threading
import queue
import time


class StocPriceTable(tk.Frame):
    nrCompanies = 0
    companies = []

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.update_company(self.nrCompanies)

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy, anchor="sw")
        self.quit.pack(side="top", pady=20)
        self.enterCompany = tk.Entry()
        self.enterCompany.pack(side="top")
        self.addCompany = tk.Button(self, text="ADD", fg="blue",
                                    command=lambda: self.add_company(self.nrCompanies), anchor="se")
        self.addCompany.pack(side="top", pady=20)

    def add_company(self, nrCompanies):
        currentStock = self.enterCompany.get()
        self.nrCompanies = self.nrCompanies + 1
        self.stock = tk.Label(self, text=currentStock.upper() + " " +
                              str(si.get_live_price(currentStock)), anchor="c")
        self.companies.append([currentStock, self.stock])
        self.stock.pack(side="bottom", pady=20)

    def update_company(self, nrCompanies):
        updateThread = threading.Timer(
            5.0, self.update_company, (self.nrCompanies,))
        updateThread.daemon = True
        updateThread.start()
        if (self.nrCompanies != 0):
            for index in range(self.nrCompanies):
                self.companies[index][1].config(text=self.companies[index][0].upper(
                ) + " " + str(si.get_live_price(self.companies[index][0])))


root = tk.Tk()
root.title("Stocks STONKS")
app = StocPriceTable(master=root)

# root.attributes("-fullscreen", True)
app.mainloop()
