

from re import S
import sys
import os
import os.path
import glob
import csv
from datetime import datetime
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Detection_support
import yagmail
import os.path
import glob
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    Detection_support.set_Tk_var()
    top = Detection (root)
    Detection_support.init(root, top)
    root.mainloop()

w = None
def create_Detection(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    Detection_support.set_Tk_var()
    top = Detection (w)
    Detection_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Detection():
    global w
    w.destroy()
    w = None

class Detection:
    def __init__(self, top=None):

        self.index = 0
        self.ChallanImg = -1
        self.yag = yagmail.SMTP("gusainshristi06@gmail.com", "fizfqtpsrakjyylq")
        #self.yag = yagmail.SMTP("omkarjavali1@gmail.com", "bajhlabrqmmsvfay")

        self.listFiles = glob.glob('output/*.txt')

        def sendChalan(event):

            try:
                helmet = self.cmbHelmetStatus.get()
                plateNumber = self.txtPlateNumber.get()
                noOfPassengers = self.txtPassengers.get()

                amount = 0
                challanBreaked = ''
                if helmet == "Not Wearing":
                    amount = amount + 500
                    challanBreaked = challanBreaked + '<br><br><b>Not Wearing Helmet (500 Rs)</b>'

                if noOfPassengers != '':
                    if int(noOfPassengers) >= 3:
                        amount = amount + 1000
                        challanBreaked = challanBreaked + '<br><br><b>There were 3 Passengers in your vehicle (1000 Rs)</b>'

                message = "Hi, User<br><br>You have violated the following traffic rules " + challanBreaked + "<br><br>Now you have to pay <b>" + str(
                amount) + "Rs.</b> as Challan using the attached QR CODE."
                data = open(self.listFiles[self.ChallanImg]).read().split('\n')
                self.yag.send(to='gusainshristi06@gmail.com', subject="Traffic Rule Challan", contents=message)
                self.yag.close()
                messagebox.showinfo('Challan Send', 'Challan mail send Successfully')

            except Exception as e:
                messagebox.showerror('Error', 'Mail not send due to ' + str(e))


        def showOutput(event):
            try:
                data = open(self.listFiles[self.index]).read().split('\n')
                print(data)
                self.img = tk.PhotoImage(file=data[0])
                self.lblRider.configure(image=self.img)


                if data[1]=="None":
                    self.cmbHelmetStatus.set('Not Found')
                    
                if data[1]=="True":
                    self.cmbHelmetStatus.set('Wearing')
                    
                if data[1]=="False":
                    self.cmbHelmetStatus.set('Not Wearing')
                


                if data[3]!="None":
                    self.txtPlateNumber.delete(0,"end")
                    self.txtPlateNumber.insert(0, data[3])  


                self.txtPassengers.delete(0,"end")
                self.txtPassengers.insert(0, data[4])  


                if data[2]=="None":
                    self.cmbPlateStatus.set('Not Found')
                    
                if data[2]=="True":
                    self.cmbPlateStatus.set('Visible')
                    
                if data[2]=="False":
                    self.cmbPlateStatus.set('Not Visible')

                # if 'Breaked' in data[5]:
                #     self.cmbSignal.set('Breaked')
                # else:
                #     self.cmbSignal.set('Not Breaked')


                    
                self.index +=1
                self.ChallanImg +=1
            except Exception as e:
                messagebox.showinfo('Limit Exceed','Images over\n'+str(e))

        def close(event):
            top.destroy()
            import Home
            Home.vp_start_gui()
        

        def generate_excel():

            listFiles = glob.glob('output/*.txt')

            # Get current date and time in format yyyy-mm-dd_HH-MM-SS
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

            # Open new file with current date and time as filename
            filename = f'excels/{now}_output.csv'
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)

                # Write headers for columns
                writer.writerow(['Helmet Status', 'LP Status', 'LP Number', 'No of passengers'])

                # Modify data and write rows to file
                for file in listFiles:
                    try:
                        data = open(file).read().split('\n')

                        # Determine helmet status
                        if data[1] == "None":
                            helmet_status = "Not Found"
                        elif data[1] == "True":
                            helmet_status = "Wearing"
                        elif data[1] == "False":
                            helmet_status = "Not Wearing"
                        else:
                            helmet_status = ""

                        # Determine LP status and number
                        if data[2] == "None":
                            lp_status = "Not Found"
                            lp_number = "Not Found"
                        elif data[2] == "True":
                            lp_status = "Found"
                            lp_number = data[3]
                        elif data[2] == "False":
                            lp_status = "Not Found"
                            lp_number = "Not Found"
                        else:
                            lp_status = ""
                            lp_number = "Not Found"

                        # Determine number of passengers
                        num_passengers = data[4] if data[4] != "None" else ""

                        # Write row to file
                        writer.writerow([helmet_status, lp_status, lp_number, num_passengers])

                    except Exception as e:
                        print(e)


        generate_excel()
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font15 = "-family {Schadow BT} -size 32 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Schadow BT} -size 19 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font17 = "-family {Segoe UI} -size 19 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font19 = "-family {Segoe UI} -size 19 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1469x907+249+68")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.state("zoomed")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.048, rely=0.011, height=56, width=1309)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font15)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Smart Traffic Violation Detection System''')
        self.Label1.configure(width=1309)

        self.lblRider = tk.Label(top)
        self.lblRider.place(relx=0.027, rely=0.132, height=732, width=634)
        self.lblRider.configure(background="#d2d2d2")
        self.lblRider.configure(disabledforeground="#a3a3a3")
        self.lblRider.configure(foreground="#000000")
        self.lblRider.configure(text='''Label''')
        self.lblRider.configure(width=634)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.504, rely=0.132, relheight=0.81, relwidth=0.446)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=655)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.084, rely=0.048, height=45, width=229)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font16)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(justify='right')
        self.Label3.configure(text='''Helmet Status:''')
        self.Label3.configure(width=229)

        self.Label3_2 = tk.Label(self.Frame1)
        self.Label3_2.place(relx=0.076, rely=0.197, height=45, width=229)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#d9d9d9")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font=font16)
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(justify='right')
        self.Label3_2.configure(text='''Number Plate:''')

        self.Label3_4 = tk.Label(self.Frame1)
        self.Label3_4.place(relx=0.076, rely=0.354, height=45, width=229)
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(activeforeground="black")
        self.Label3_4.configure(background="#d9d9d9")
        self.Label3_4.configure(disabledforeground="#a3a3a3")
        self.Label3_4.configure(font=font16)
        self.Label3_4.configure(foreground="#000000")
        self.Label3_4.configure(highlightbackground="#d9d9d9")
        self.Label3_4.configure(highlightcolor="black")
        self.Label3_4.configure(text='''Plate Number:''')

        self.Label3_6 = tk.Label(self.Frame1)
        self.Label3_6.place(relx=0.069, rely=0.497, height=45, width=249)
        self.Label3_6.configure(activebackground="#f9f9f9")
        self.Label3_6.configure(activeforeground="black")
        self.Label3_6.configure(background="#d9d9d9")
        self.Label3_6.configure(disabledforeground="#a3a3a3")
        self.Label3_6.configure(font=font16)
        self.Label3_6.configure(foreground="#000000")
        self.Label3_6.configure(highlightbackground="#d9d9d9")
        self.Label3_6.configure(highlightcolor="black")
        self.Label3_6.configure(text='''No. Passengers:''')
        self.Label3_6.configure(width=249)



        # self.Label3_6 = tk.Label(self.Frame1)
        # self.Label3_6.place(relx=0.069, rely=0.58, height=45, width=249)
        # self.Label3_6.configure(activebackground="#f9f9f9")
        # self.Label3_6.configure(activeforeground="black")
        # self.Label3_6.configure(background="#d9d9d9")
        # self.Label3_6.configure(disabledforeground="#a3a3a3")
        # self.Label3_6.configure(font=font16)
        # self.Label3_6.configure(foreground="#000000")
        # self.Label3_6.configure(highlightbackground="#d9d9d9")
        # self.Label3_6.configure(highlightcolor="black")
        # self.Label3_6.configure(text='''Signal Status:''')
        # self.Label3_6.configure(width=249)

        self.cmbPlateStatus = ttk.Combobox(self.Frame1)
        self.cmbPlateStatus.place(relx=0.557, rely=0.204, relheight=0.061
                , relwidth=0.35)
        self.cmbPlateStatus.configure(font=font17)
        self.cmbPlateStatus.configure(justify='center')
        self.cmbPlateStatus.configure(takefocus="")
        self.cmbPlateStatus['values'] = ['Visible','Not Visible','Not Found']

        self.cmbHelmetStatus = ttk.Combobox(self.Frame1)
        self.cmbHelmetStatus.place(relx=0.557, rely=0.048, relheight=0.063
                , relwidth=0.347)
        self.cmbHelmetStatus.configure(font=font17)
        self.cmbHelmetStatus.configure(justify='center')
        self.cmbHelmetStatus.configure(width=227)
        self.cmbHelmetStatus.configure(takefocus="")
        self.cmbHelmetStatus['values'] = ['Wearing','Not Wearing','Not Found']

        self.txtPassengers = tk.Entry(self.Frame1)   
        self.txtPassengers.place(relx=0.55, rely=0.47, height=49
                , relwidth=0.357)
        self.txtPassengers.configure(background="white")
        self.txtPassengers.configure(disabledforeground="#a3a3a3")
        self.txtPassengers.configure(font=font17)
        self.txtPassengers.configure(foreground="#000000")
        self.txtPassengers.configure(insertbackground="black")
        self.txtPassengers.configure(justify='center')
        self.txtPassengers.configure(width=234)


        # self.cmbSignal = ttk.Combobox(self.Frame1)
        # self.cmbSignal.place(relx=0.55, rely=0.58, height=49
        #         , relwidth=0.357)
        # self.cmbSignal.configure(font=font17)
        # self.cmbSignal.configure(justify='center')
        # self.cmbSignal.configure(width=227)
        # self.cmbSignal.configure(takefocus="")
        # self.cmbSignal['values'] = ['Breaked','Not Breaked']


        self.txtPlateNumber = tk.Entry(self.Frame1)
        self.txtPlateNumber.place(relx=0.557, rely=0.354, height=45
                , relwidth=0.35)
        self.txtPlateNumber.configure(background="white")
        self.txtPlateNumber.configure(disabledforeground="#a3a3a3")
        self.txtPlateNumber.configure(font=font17)
        self.txtPlateNumber.configure(foreground="#000000")
        self.txtPlateNumber.configure(highlightbackground="#d9d9d9")
        self.txtPlateNumber.configure(highlightcolor="black")
        self.txtPlateNumber.configure(insertbackground="black")
        self.txtPlateNumber.configure(justify='center')
        self.txtPlateNumber.configure(selectbackground="#c4c4c4")
        self.txtPlateNumber.configure(selectforeground="black")

        self.btnSendChallan = tk.Button(self.Frame1)
        self.btnSendChallan.place(relx=0.107, rely=0.7, height=53, width=236)
        self.btnSendChallan.configure(activebackground="#ececec")
        self.btnSendChallan.configure(activeforeground="#000000")
        self.btnSendChallan.configure(background="#d9d9d9")
        self.btnSendChallan.configure(disabledforeground="#a3a3a3")
        self.btnSendChallan.configure(font=font19)
        self.btnSendChallan.configure(foreground="#000000")
        self.btnSendChallan.configure(highlightbackground="#d9d9d9")
        self.btnSendChallan.configure(highlightcolor="black")
        self.btnSendChallan.configure(pady="0")
        self.btnSendChallan.configure(text='''Send Challan''')
        self.btnSendChallan.configure(width=236)
        self.btnSendChallan.bind('<Button-1>',sendChalan)

        self.btnNextImage = tk.Button(self.Frame1)
        self.btnNextImage.place(relx=0.5, rely=0.7, height=53, width=256)
        self.btnNextImage.configure(activebackground="#ececec")
        self.btnNextImage.configure(activeforeground="#000000")
        self.btnNextImage.configure(background="#d9d9d9")
        self.btnNextImage.configure(disabledforeground="#a3a3a3")
        self.btnNextImage.configure(font=font19)
        self.btnNextImage.configure(foreground="#000000")
        self.btnNextImage.configure(highlightbackground="#d9d9d9")
        self.btnNextImage.configure(highlightcolor="black")
        self.btnNextImage.configure(pady="0")
        self.btnNextImage.configure(text='''Next Image''')
        self.btnNextImage.configure(width=236)
        self.btnNextImage.bind('<Button-1>',showOutput)


        self.btnExit = tk.Button(self.Frame1)
        self.btnExit.place(relx=0.321, rely=0.857, height=53, width=256)
        self.btnExit.configure(activebackground="#ececec")
        self.btnExit.configure(activeforeground="#000000")
        self.btnExit.configure(background="#d8368c")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(font=font19)
        self.btnExit.configure(foreground="#ffffff")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        self.btnExit.configure(pady="0")
        self.btnExit.configure(text='''EXIT''')
        self.btnExit.bind('<Button-1>',close)
        
        
        showOutput(None)


