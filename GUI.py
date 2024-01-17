# Import the required libraries
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from win32api import GetSystemMetrics
from tkinter import filedialog
global compress
global folder
folder='Path will be show here'
import numpy as np
import cv2
#import jpeg as jp
import jpegne as jp
import JPEG2k as jp2
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio as psnr
import skimage.io as io
import Bits_to_DNA as Encoder
import DNA_to_Bits as Decoder
op='None'
compress="Compression option will show here"
w=GetSystemMetrics(0)
h=GetSystemMetrics(1)
# Create an instance of Tkinter Frame
win = tk.Tk()
# Set the geometry of Tkinter Frame
win.geometry(str(w)+'x'+str(h))
# Open the Image File
bg = ImageTk.PhotoImage(file="sample.jpg")
# Create a Canvas
canvas = Canvas(win, width=w, height=h)
canvas.pack(fill=BOTH, expand=True)
# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')
# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("sample.jpg")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')
def cJPEG():
       text4.delete("1.0","end")
       qu=slider.get()
       print(qu)
       img=jp.file(folder,qu)
       image = Image.open(folder)
       image = image.resize((512, 300))
       photo = ImageTk.PhotoImage(image)
       label6.config(image=photo)
       label6.image = photo
       original_image = io.imread(folder, as_gray=True)
       compressed_image = io.imread("compressed.jpg", as_gray=True)
       psnr_value = psnr(original_image, compressed_image)
       text4.delete("1.0","end")
       text4.insert('end',psnr_value)
       print(psnr_value)
def cJPEG2000():
    text4.delete("1.0","end")
    qu=slider.get()
    print(qu)
    img=jp2.save_as_jpeg2000(folder,qu)
    image = Image.open("output_image.jp2")
    image = image.resize((512, 300))
    photo = ImageTk.PhotoImage(image)
    label6.config(image=photo)
    label6.image = photo
    original_image = io.imread(folder, as_gray=True)
    compressed_image = io.imread("output_image.jp2", as_gray=True)
    psnr_value = psnr(original_image, compressed_image)
    text4.delete("1.0","end")
    text4.insert('end',psnr_value)
def path():
    global folder
    folder = filedialog.askopenfilename()
    text1.delete("1.0","end")
    text1.insert("end",folder)
    image = Image.open(folder)
    image = image.resize((512, 300))
    photo = ImageTk.PhotoImage(image)
    #photo=cv2.resize(photo,(512,512))
    label5.config(image=photo)
    label5.image = photo
def JPEG():
    label9.place(x=w-500,y=270)
    slider.place(x=w-300,y=260)
    global op
    op='JPEG'
    text2.delete("1.0","end")
    text2.insert("end","Compression is JPEG")
def JPEG2000():
    label9.place(x=w-500,y=270)
    slider.place(x=w-300,y=260)
    global op
    op='JPEG2000'
    text2.delete("1.0","end")
    text2.insert("end","Compression is JPEG2000")
def JPEGXT():
    global op
    op='JPEGXT'
    text2.delete("1.0","end")
    text2.insert("end","Compression is JPEG XT")
def JPEGXL():
    global op
    op='JPEGXL'
    text2.delete("1.0","end")
    text2.insert("end","Compression is JPEG XL")
def JPEGAI():
    label9.destroy()
    slider.destroy()
    global op
    op='JPEGAI'
    text2.delete("1.0","end")
    text2.insert("end","Compression is JPEG AI")
def work():
    if op=="JPEG":
        text3.delete("1.0","end")
        text3.insert("end","JPEG Starting")
        cJPEG()
    elif op=='JPEG2000':
        text3.delete("1.0","end")
        text3.insert("end","JPEG2000 Starting")
        cJPEG2000()
    elif op=='JPEGXT':
        text3.delete("1.0","end")
        text3.insert("end","JPEGXT Starting")
    elif op=='JPEGXL':
        text3.delete("1.0","end")
        text3.insert("end","JPEGXL Starting")
        cJPEGXL()
    elif op=='JPEGAI':
        text3.delete("1.0","end")
        text3.insert("end","JPEGAI Starting")
        cJPEGAI()
    elif op=='None':
        pass
def encoder():
    if op=="JPEG":
        img=cv2.imread('compressed.jpg')
    if op=="JPEG2000":
        img=Image.open('output_image.jp2')
        jp2_image_rgb = img.convert('RGB')
        np_image = np.array(jp2_image_rgb)
        img= cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
    global img_small
    img_small = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4))
    # Convert the bytes to bitstream
    bitstream_str =Encoder.to_bitstream_parallel(img_small)
    dna=Encoder.bits_to_dna_optimized(bitstream_str)
def decoder():
    bitstream_str=Decoder.dna_to_bits('dna_sequence.txt')
    # Convert the recovered bitstream back to bytes
    image_shape = img_small.shape  # This should match the shape of the downscaled image
    restored_image =Decoder.bitstream_to_image(bitstream_str, image_shape)
    # Save the restored image
    cv2.imwrite('restored_image.jpg', restored_image)
    if op=="JPEG":
        print("yes")
        t='compressed.jpg'
    if op=='JPEG2000':
        t='output_image.jp2'
    #compressed_image = io.imread(t, as_gray=True)
    #psnr_value = psnr(compressed_image, restored_image)
    #text5.delete("1.0","end")
    #text5.insert('end',psnr_value)
    image = Image.open('restored_image.jpg')
    image = image.resize((512, 300))
    photo = ImageTk.PhotoImage(image)
    label13.config(image=photo)
    label13.image = photo
# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)
#labels
label1 = tk.Label(text="Image Selection Part",foreground="white",background='#1A272F',font=("Arial", 30))
label2 = tk.Label(text="Compression Type",foreground="white",background='#1A272F',font=("Arial", 30))
label3 = tk.Label(text="Input Image",foreground="white",background='#1A272F',font=("Arial", 15))
label4 = tk.Label(text="Compress Image",foreground="white",background='#1A272F',font=("Arial", 15))
label5 = tk.Label(text="Here",background='#1A272F',foreground="white")
label6=tk.Label(text="Here",background='#1A272F',foreground="white")
label7 = tk.Label(text="Image Quality Metrics",foreground="white",background='#1A272F',font=("Arial", 30))
label8 = tk.Label(text="PSNR with compressed Image",background='#1A272F',foreground="white")
label9 = tk.Label(text="Select Quality",background='#1A272F',foreground="white",font=("Arial", 18))
label10 = tk.Label(text="DNA TO Binary and Binary To DNA Conversion Part",foreground="white",background='#1A272F',font=("Arial", 30))
label11 = tk.Label(text="Restore Image",foreground="white",background='#1A272F',font=("Arial", 15))
label12 = tk.Label(text="PSNR Compress/Restored Image",background='#1A272F',foreground="white")
label13 = tk.Label(text="Here",background='#1A272F',foreground="white")
#buttons
button1=tk.Button(text='Upload Image',bg='#6FA7C9',fg='white',command=path)
button2=tk.Button(text='JPEG',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='red',command=JPEG)
button3=tk.Button(text='JPEG 2000',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='red',command=JPEG2000)
button4=tk.Button(text='JPEG XL',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='red',command=JPEGXL)
button5=tk.Button(text='JPEG XT',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='red',command=JPEGXT)
button6=tk.Button(text='JPEG AI',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='red',command=JPEGAI)
button7=tk.Button(text='Compress',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='green',command=work)
button8=tk.Button(text='Encoder',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='green',command=encoder)
button9=tk.Button(text='Decoder',bg='#6FA7C9',fg='white',width=10,height=1,activebackground='green',command=decoder)
#Text boxes
text1=tk.Text(win, height = 1, width = 35)
text2=tk.Text(win, height = 1, width = 35)
text3=tk.Text(win, height = 20, width = 80,bg='#5A909A',fg='green')
text4=tk.Text(win, height = 1, width = 35)
text5=tk.Text(win, height = 1, width = 35)
text3.pack()

#label Placement
label1.place(x=w-450,y=30)
label2.place(x=w-450,y=150)
label3.place(x=w-w+30,y=35)
label4.place(x=w-w+30,y=445)
label5.place(x=30,y=70)
label6.place(x=30,y=480)
label7.place(x=w-480,y=650)
label8.place(x=w-580,y=720)
label10.place(x=w-950,y=350)
label11.place(x=w-950,y=445)
#label12.place(x=w-580,y=760)
label13.place(x=w-950,y=480)
#button placement
button1.place(x=w-150,y=100)
button2.place(x=w-500,y=230)
button3.place(x=w-400,y=230)
button4.place(x=w-300,y=230)
button5.place(x=w-200,y=230)
button6.place(x=w-100,y=230)
button7.place(x=w-150,y=318)
button8.place(x=w-120,y=420)
button9.place(x=w-120,y=458)
#Text placement
text1.place(x=w-445,y=105)
text2.place(x=w-445,y=320)
text4.place(x=w-400,y=720)
#text5.place(x=w-400,y=760)
#slider placement
slider = tk.Scale(win, from_=0, to=100, orient="horizontal", length=200)
#Data show
text1.insert("end",folder)
text2.insert("end",compress)
text3.insert("end",op)
text4.insert("end",op)
text5.insert("end",op)
win.mainloop()




