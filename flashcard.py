import tkinter as tk
import pandas
import random
num = 0
random_row_num =0

data_frame=pandas.read_csv("datafile.csv")
data= data_frame.to_dict()
# =============================================================================
                            # flip card
# =============================================================================
def flip_card():
    global random_row_num
    pre_eng_word =data["English"][random_row_num]
    my_canvus.itemconfigure(pin,image=canvus_back)
    my_canvus.itemconfigure(txt1,text="English")
    my_canvus.itemconfig(txt2,text=pre_eng_word)
    right_but.config(state="normal")
    wrong_but.config(state="normal")
# =============================================================================
                            # tick# 
# =============================================================================
def change():
    global num
    global random_row_num
    
    right_but.config(state="disable")
    wrong_but.config(state="disable")
    random_row_num =random.randint(0, 100)
    pre_french_word = data["French"][random_row_num]
    my_canvus.itemconfigure(pin,image=canvus_front)
    my_canvus.itemconfig(txt2,text=pre_french_word)
    my_canvus.itemconfig(txt1,text="French")
    my_canvus.after(3000,flip_card)
    
# =============================================================================
                            # window # 
# =============================================================================

my_window = tk.Tk()
my_window.title("password manager")
my_window.minsize(1000,1000)
my_window.configure(padx=100,pady=100,bg="#B1DDC6")

# =============================================================================
                            # canvus #
# =============================================================================

my_canvus = tk.Canvas(width=820,height=530,bg="#B1DDC6",highlightthickness=0)

canvus_front= tk.PhotoImage(file="C:/Users/JAGATH/U_1/Flash_card/card_front.png")
canvus_back= tk.PhotoImage(file="C:/Users/JAGATH/U_1/Flash_card/card_back.png")

pin=my_canvus.create_image(400,263,image=canvus_front)
my_canvus.grid(column=1,row=1)

pre_french_word = data["French"][num]
# --------------------------- # Canvus txts # ---------------------------------
txt1 =my_canvus.create_text(400,150,text="French",fill="Black",font=("arial",30,"bold"))
txt2 =my_canvus.create_text(400,263,text=f"{pre_french_word}",fill="Black",font=("arial",50,"bold"))
# =============================================================================
                            # Buttons #
# =============================================================================

#right button
right_img=tk.PhotoImage(file="C:/Users/JAGATH/U_1/Flash_card/right.png")
right_but=tk.Button(image=right_img,highlightthickness=0,bg="#B1DDC6",padx=50,pady=50,command=change)
right_but.grid(column=1,row=2,sticky="w",columnspan=2)

#wrong button
wrong_img = tk.PhotoImage(file="C:/Users/JAGATH/U_1/Flash_card/wrong.png")
wrong_but=tk.Button(image=wrong_img,highlightthickness=0,bg="#B1DDC6",padx=50,pady=50,command=change)
wrong_but.grid(column=1,row=2,sticky="e")

# count(n=3)
my_window.mainloop()