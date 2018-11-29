
#=============================== Library ===================================

from Tkinter import*
import random
import time;
import RPi.GPIO as GPIO
import sys
#from hx711 import HX711
import threading

GPIO.setwarnings(False)


#=============================== Global Variables ==============================

global val
global val2
global flag_w
global flag_s
global localtime

flag_w = 0
flag_s = 0

#==================== Scrren =================================

root = Tk()
root.geometry("1200x700+0+0")
#pad = 3
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))
#root.bind('<Escape>', self.toggle_geom)
root.title("Packaging Material Cross-Verification System")


text_Input = StringVar()
operator = ""

#============================== Frames =============================================

Tops = Frame(root, width = 1000, height = 50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

bottoms = Frame(root, width = 400, height = 50, bg="powder blue", relief=SUNKEN)
bottoms.pack(side=BOTTOM)

f1 = Frame(root, width = 300, height = 600, relief=SUNKEN)
f1.pack(side=LEFT)


f2 = Frame(root, width = 200, height = 600, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

#============================ Load Cell Decelration ===================================

#hx = HX711(5, 6)
#hx.set_reading_format("LSB", "MSB")
#hx.set_reference_unit(21580)
#hx.reset()
#hx.tare()


#================================= Info =================================================================


lblInfo = Label(Tops, font=('arial', 30, 'bold'), text="Devgiri Forgings PVT. LTD.", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)

lblInfo = Label(f1, font=('arial', 20, 'bold'), text="Select Mode", fg="blue", bd=10, anchor='w')
lblInfo.grid(row=13,column=1)

#========================================== Clear Display ==============================================================

def ClearDisplay():
    
    customer_name.set("")
    part_name.set("")
    quantity.set("")
    invoice_no.set("")
    packed_by.set("")
    checked_by.set("")
    
    part_no.set("")
    weight_per_part.set("")
    invoice_date.set("")
    box_weight.set("")
    calculated_weight = 0.0
    count = 0
   

#========================= Save Data ==========================================================================

def save():
    customer_name1 = customer_name.get()
    print customer_name1
    customer_name.set(customer_name1)

    customer_address1 = customer_address.get()
    print customer_address1
    customer_address.set(customer_address1)

    part_name1 = part_name.get()
    print part_name1
    part_name.set(part_name1)

    part_no1 = part_no.get()
    print part_no1
    part_no.set(part_no1)

    invoice_no1 = invoice_no.get()
    print invoice_no
    invoice_no.set(invoice_no1)

    packed_by1 = packed_by.get()
    print packed_by
    packed_by.set(packed_by1)

    weight_per_part1 = weight_per_part.get()
    print weight_per_part1
    weight_per_part.set(weight_per_part1)

    box_weight1 = box_weight.get()
    print box_weight1
    box_weight.set(box_weight1)

    quantity1 = quantity.get()
    print quantity1
    quantity.set(quantity1)

   # calculated_weight1 = calculated_weight.get()
    #print calculated_weight1
    #calculated_weight.set(calculated_weight1)


#========================= Measure Weight ===============================================================
    
def measure():
    global val
    global val2
    global flag_w
    global flag_s
    global localtime
    
    print " "
    while True:
        print "Function"
        time.sleep(0.1)
        if flag_w == 10:
            #val = hx.get_weight(3)
            #val2 = val
            #print ("{0:.3f}".format(round(val2,3)))
            #val2 = "{0:.3f}".format(round(val2,3))
            #calculated_weight.set(" ")
            #weight.set(val2)
            time.sleep(0.5)

        if flag_s == 10:
            #val = hx.get_weight(3)
            #val2 = val
            #print ("{0:.3f}".format(round(val2,3)))
            #val2 = "{0:.3f}".format(round(val2,3))
            #weight.set(" ")
            #calculated_weight.set(val2)
            time.sleep(0.5)
            	
        localtime=time.asctime(time.localtime(time.time()))
        lblInfo = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
        lblInfo.grid(row=1,column=0)
            
    
#======================== Weight Mode ==================================================================

def weight_mode():
    global flag_w
    global flag_s
    flag_w = 10
    flag_s = 0
    print "Weight Function"
    time.sleep(0.5)

    lblInfo = Label(f1, font=('arial', 20, 'bold'), text="Weight Mode", fg="blue", bd=10, anchor='w')
    lblInfo.grid(row=13,column=1)

    #lblInfo = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
    #lblInfo.grid(row=1,column=0)
    #measure()


#=============================== System Mode =============================================================

def system_mode():
    global flag_w
    global flag_s
    flag_s = 10
    flag_w = 0
    print "System Function"
    time.sleep(0.5)
    lblInfo = Label(f1, font=('arial', 20, 'bold'), text="System Mode", fg="blue", bd=10, anchor='w')
    lblInfo.grid(row=13,column=1)


#===================================== Variables =====================================================================================

customer_name = StringVar()
part_name = StringVar()
quantity = StringVar()
invoice_no = StringVar()
packed_by = StringVar()

part_no = StringVar()
weight_per_part = StringVar()
invoice_date = StringVar()
box_weight = StringVar()
calculated_weight = StringVar()
checked_by = StringVar()
weight = StringVar()

calculated_weight = 000.0
count = 0
localtime = StringVar()


#=====================================Colum 1 Start Here =================================================

#-------------------------- Customer Name -----------------------------------------

lblcustomer_name = Label(f1,font=('arial', 16, 'bold'), text="Customer Name ", bd=16, anchor='w')
lblcustomer_name.grid(row=0,column=0)

txtcustomer_name=Entry(f1,font=('arial', 16, 'bold'), textvariable=customer_name, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtcustomer_name.grid(row=0,column=1)

#---------------------------- Part Name -----------------------------------------------

lblpart_name = Label(f1,font=('arial', 16, 'bold'), text="Part Name ", bd=16, anchor='w')
lblpart_name.grid(row=1,column=0)

txtpart_name=Entry(f1,font=('arial', 16, 'bold'), textvariable=part_name, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtpart_name.grid(row=1,column=1)


#---------------------------- Quantity -----------------------------------------------

lblquantity = Label(f1,font=('arial', 16, 'bold'), text="Quantity (Nos)", bd=16, anchor='w')
lblquantity.grid(row=2,column=0)

txtquantity=Entry(f1,font=('arial', 16, 'bold'), textvariable=quantity, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtquantity.grid(row=2,column=1)


#---------------------------- Invoice No -----------------------------------------------

lblcustomer_address = Label(f1,font=('arial', 16, 'bold'), text="Invoice No. ", bd=16, anchor='w')
lblcustomer_address.grid(row=3,column=0)

txtcustomer_address=Entry(f1,font=('arial', 16, 'bold'), textvariable=invoice_no, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtcustomer_address.grid(row=3,column=1)

#---------------------------- Packed by. -----------------------------------------------

lblcustomer_address = Label(f1,font=('arial', 16, 'bold'), text="Packed by. ", bd=16, anchor='w')
lblcustomer_address.grid(row=4,column=0)

txtcustomer_address=Entry(f1,font=('arial', 16, 'bold'), textvariable=packed_by, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtcustomer_address.grid(row=4,column=1)

#---------------------------- Checked by. -----------------------------------------------

lblcustomer_address = Label(f1,font=('arial', 16, 'bold'), text="Checked by. ", bd=16, anchor='w')
lblcustomer_address.grid(row=5,column=0)

txtcustomer_address=Entry(f1,font=('arial', 16, 'bold'), textvariable=checked_by, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtcustomer_address.grid(row=5,column=1)

#===================================Colum 1 END ===========================================================================================



#================================ Colum 2 Start here ============================================

#---------------------------- Part No -----------------------------------------------

lblpart_no = Label(f1,font=('arial', 16, 'bold'), text="Part No ", bd=16, anchor='w')
lblpart_no.grid(row=0,column=2)

txtpart_no=Entry(f1,font=('arial', 16, 'bold'), textvariable=part_no, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtpart_no.grid(row=0,column=3)

#---------------------------- Weight / Part -----------------------------------------------

lblweight_per_part = Label(f1,font=('arial', 16, 'bold'), text="Weight / Part (Kg) ", bd=16, anchor='w')
lblweight_per_part.grid(row=1,column=2)

txtweight_per_part=Entry(f1,font=('arial', 16, 'bold'), textvariable=weight_per_part, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtweight_per_part.grid(row=1,column=3)


#---------------------------- Invoice Date -----------------------------------------------

lblbox_weight = Label(f1,font=('arial', 16, 'bold'), text="Invoice Date", bd=16, anchor='w')
lblbox_weight.grid(row=2,column=2)

txtbox_weight=Entry(f1,font=('arial', 16, 'bold'), textvariable=invoice_date, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtbox_weight.grid(row=2,column=3)


#---------------------------- Box Weight -----------------------------------------------

lblbox_weight = Label(f1,font=('arial', 16, 'bold'), text="Box Weight (Kg)", bd=16, anchor='w')
lblbox_weight.grid(row=3,column=2)

txtbox_weight=Entry(f1,font=('arial', 16, 'bold'), textvariable=box_weight, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtbox_weight.grid(row=3,column=3)


#---------------------------- Calculated Weight -----------------------------------------------

lblcalculated_weight = Label(f1,font=('arial', 16, 'bold'), text="Cal.Weight (Kg)", bd=16, anchor='w')
lblcalculated_weight.grid(row=4,column=2)

lblInfo = Label(f1, font=('arial', 16, 'bold'), text=calculated_weight, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=4,column=3)

#txtcalculated_weight=Entry(f1,font=('arial', 16, 'bold'), textvariable=calculated_weight, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
#txtcalculated_weight.grid(row=4,column=3)


#---------------------------- Box Count No. -----------------------------------------------

lblweight = Label(f1,font=('arial', 16, 'bold'), fg="black", text="Box No. Count", bd=16, anchor='w')
lblweight.grid(row=5,column=2)

lblInfo = Label(f1, font=('arial', 16, 'bold'), text=count, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=5,column=3)

#txtweight=Entry(f1,font=('arial', 16, 'bold'), textvariable=count, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
#txtweight.grid(row=5,column=3)


#---------------------------- Weight -----------------------------------------------

lblweight = Label(bottoms,font=('arial', 16, 'bold'), fg="red", text="Weight (Kg)", bd=16, anchor='w')
lblweight.grid(row=4,column=1)

txtweight=Entry(bottoms,font=('arial', 16, 'bold'), textvariable=weight, bd=10, insertwidth=4, bg="powder blue", justify = 'left')
txtweight.grid(row=4,column=2)

#===================================== Buttons ==============================================


btn1=Button(f1, padx=16,pady=8,bd=16, fg="black", font=('arial',20, 'bold'), width=7, text="Test", bg="powder blue", command=save).grid(row=14,column=3)

btn2=Button(f1, padx=16,pady=8,bd=16, fg="black", font=('arial',20, 'bold'), width=10, text="Weight Mode", bg="powder blue", command=weight_mode).grid(row=14,column=0)

btn3=Button(f1, padx=16,pady=8,bd=16, fg="black", font=('arial',20, 'bold'), width=10, text="System Mode", bg="powder blue", command=system_mode).grid(row=14,column=1)

btn3=Button(f1, padx=16,pady=8,bd=16, fg="black", font=('arial',20, 'bold'), width=10, text="Clear", bg="powder blue", command=ClearDisplay).grid(row=14,column=2)


#================================= Threading =================================================

thread = threading.Thread(target = measure)
thread.start()

root.mainloop()
