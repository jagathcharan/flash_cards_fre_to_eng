

def right():
    global right_count
    # global t
    right_count+=1
    # my_window.after_cancel(my_timer)
    change_txt()
    
def wrong():
    global wrong_count
    global t
    wrong_count+=1
    # print(t)
    change_txt()

    
# def next():
#     global t
#     if t is is False:
#         my_canvus.itemconfigure(pin,image=canvus_back)
#         my_canvus.itemconfig(txt1,text="French")
        
#     else:
        

# def count(n=3):
#      global t
#      global my_timer
#      if n>0: 
#         my_timer=my_window.after(1000,count,n-1)
#         t=True
#      else: 
#          t = False
#          rotate()
         
         
# def image_check():
    
# def rotate():
#     my_canvus.itemconfigure(pin,image=canvus_back)
#     my_canvus.itemconfig(txt2,text="hlo")