from tkinter import *
from tkinter import ttk
import time
import datetime
from PIL import ImageTk, Image
import requests


# API calling
def getdata():
    symbol1 ="°C"
    symbol2 = " mb"
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9ef5bb9fa129d512aa67b080b1c12224").json()

    #Displaying details
    min_temp = str(int(data["main"]["temp_min"]-273.15))
    label3A.config(text=(min_temp,symbol1),font=("Arial", 10, "bold","italic"))

    max_temp = str(int(data["main"]["temp_max"]-273.15))
    label4A.config(text=(max_temp,symbol1),font=("Arial", 10, "bold","italic"))

    feel_like = str(int(data["main"]["feels_like"]-273.15))
    label5A.config(text=(feel_like,symbol1),font=("Arial", 10, "bold","italic"))

    current_temp =str(int(data["main"]["temp"]-273.15))
    label13.config(text=(current_temp,symbol1),font=("Arial", 60, "bold","italic"))

    pressure = data["main"]["pressure"]
    label6A.config(text=(pressure),font=("Arial", 10, "bold","italic"))

    label7A.config(text=data["main"]["humidity"],font=("Arial", 10, "bold","italic"))
    label8A.config(text=data["visibility"],font=("Arial", 10, "bold","italic"))
    label9A.config(text=data["wind"]["speed"],font=("Arial", 10, "bold","italic"))
    label10A.config(text=data["sys"]["sunrise"],font=("Arial", 10, "bold","italic"))
    label11A.config(text=data["weather"][0]["main"],font=("Arial", 10, "bold","italic"))


root = Tk()

# Window width and height
root.geometry("850x500")

# Creating title
root.title("Project AIM")

# Creating background image
bg = PhotoImage(file="weather1.png")
canvas1 = Canvas(root, width=800, height=500)
canvas1.pack(fill="both", expand="true")
canvas1.create_image(0, 0, image=bg, anchor="nw")

state_list = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha","Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]

# search box
city_name = StringVar()
search_box = ttk.Combobox(root, values=state_list, font=("Arial", 10,"italic"),textvariable=city_name)
search_box.place(x=15, height=25, width=230)

# Date & time
dtm = time.strftime("%I:%M:%S %p")


# weather image
img1 = PhotoImage(file="weather2.png")
label2 = Label(image=img1, height=200, width=600)
label2.pack()
label2.place(x=250)


# weather details

# min temp
label3 = Label(root, font=("Arial", 10, "bold","italic"), text="Min Temp")
label3.place(x=15, y=100, height=15, width=90)

# data
label3A = Label(root, font=("Arial", 10, "bold"))
label3A.place(x=150, y=100, height=15, width=90)

# max temp
label4 = Label(root, font=("Arial", 10, "bold","italic"), text="Max Temp")
label4.place(x=15, y=140, height=15, width=90)

# data
label4A = Label(root, font=("Arial", 10, "bold"))
label4A.place(x=150, y=140, height=15, width=90)

# feel like
label5 = Label(root, font=("Arial", 10, "bold","italic"), text="Feel's Like")
label5.place(x=15, y=180, height=15, width=90)

# data
label5A = Label(root, font=("Arial", 10, "bold"))
label5A.place(x=150, y=180, height=15, width=90)

# pressure
label6 = Label(root, font=("Arial", 10, "bold","italic"), text="Pressure")
label6.place(x=15, y=220, height=15, width=90)

# data
label6A = Label(root, font=("Arial", 10, "bold"))
label6A.place(x=150, y=220, height=15, width=90)

# Humidity
label7 = Label(root, font=("Arial", 10, "bold","italic"), text="Humidity")
label7.place(x=15, y=260, height=15, width=90)

# Data
label7A = Label(root, font=("Arial", 10, "bold"))
label7A.place(x=150, y=260, height=15, width=90)

# Visibility
label8 = Label(root, font=("Arial", 10, "bold","italic"), text="Visibility")
label8.place(x=15, y=300, height=15, width=90)

# Data
label8A = Label(root, font=("Arial", 10, "bold"))
label8A.place(x=150, y=300, height=15, width=90)

# Wind Speed
label9 = Label(root, font=("Arial", 10, "bold","italic"), text="Wind Speed")
label9.place(x=15, y=340, height=15, width=90)

# Data
label9A = Label(root, font=("Arial", 10, "bold"))
label9A.place(x=150, y=340, height=15, width=90)

# Sunrise
label10 = Label(root, font=("Arial", 10, "bold","italic"), text="Sunrise")
label10.place(x=15, y=380, height=15, width=90)

# Data
label10A = Label(root, font=("Arial", 10, "bold"))
label10A.place(x=150, y=380, height=15, width=90)

# Climate
label11 = Label(root, font=("Arial", 10, "bold","italic"), text="Climate")
label11.place(x=15, y=420, height=15, width=90)

# data
label11A = Label(root, font=("Arial", 10, "bold"))
label11A.place(x=150, y=420, height=15, width=90)

# Current Temp label
label12 =Label(root,font=("Arial",20,"bold","italic"),text="Current Temperature")
label12.place(height=40,width=290,x=390,y=250)

# current temp showing label
label13 =Label(root,font=("Arial",10,"bold"))
label13.place(height=150,width=400,x=330,y=300)

#Search button creation
but1 = Button(root,text="search",font=("Arial",10,"bold","italic"),cursor="hand2",command=getdata)
but1.place(x=80,y=40,height=40,width=80)


root.mainloop()