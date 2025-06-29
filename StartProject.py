
import sys
import Home
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import filedialog
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
   # unknown_support.init(root, top)
    root.mainloop()
w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):

        def btnExit(event):
            top.destroy()
            sys.exit()

        def loginCheck():
            userName = self.txtUsername.get()
            password = self.txtPassword.get()
            if userName=='' or password =='':
                self.lblCredintialChk.configure(text='Please Provide all details')
            else:

                if userName =='lane' or userName=='LANE' or userName=='Lane':
                    if password == 'pass123' or userName=='PASS123' or userName== 'Pass123':
                        top.destroy()
                        os.system('python Single_Break_Detector.py')
                        # Single_Break_Detector.start()


                if userName =='admin' or userName=='ADMIN' or userName=='Admin':
                    if password == 'pass123' or userName=='PASS123' or userName== 'Pass123':
                        return 'Access'
                    else:
                        self.lblCredintialChk.configure(text='Incorrect Username & Password')
                        return 'Denied'
                else:
                    self.lblCredintialChk.configure(text='Incorrect Username & Password')
                    return 'Denied'

        def btnCompression(event):
            result = loginCheck()
            if result=='Access':
                top.destroy()
                Home.vp_start_gui()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Courier New} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("905x620")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        # top.resizable(False,False)
        # top.overrideredirect(1)
        # Gets the requested values of the height and widht.
        windowWidth = 905
        windowHeight = 620
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
        top.geometry("+{}+{}".format(positionRight, positionDown))


        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=-0.016, height=630, width=905)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "images", "back - Copy.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=self._img0)
        self.Label1.configure(text='''Label''')

        self.txtUsername = tk.Entry(top)
        self.txtUsername.place(relx=0.125, rely=0.350,height=44, relwidth=0.281)
        self.txtUsername.configure(background="white")
        self.txtUsername.configure(disabledforeground="#a3a3a3")
        self.txtUsername.configure(font=font11)
        self.txtUsername.configure(foreground="#000000")
        self.txtUsername.configure(insertbackground="black")
        self.txtUsername.configure(width=254)
        self.txtUsername.configure(justify='center')

        self.txtPassword = tk.Entry(top)
        self.txtPassword.place(relx=0.125, rely=0.478,height=44, relwidth=0.281)
        self.txtPassword.configure(background="white")
        self.txtPassword.configure(disabledforeground="#a3a3a3")
        self.txtPassword.configure(font=font11)
        self.txtPassword.configure(foreground="#000000")
        self.txtPassword.configure(highlightbackground="#d9d9d9")
        self.txtPassword.configure(highlightcolor="black")
        self.txtPassword.configure(insertbackground="black")
        self.txtPassword.configure(selectbackground="#c4c4c4")
        self.txtPassword.configure(selectforeground="black")
        self.txtPassword.configure(justify='center')
        self.txtPassword.configure(show='#')

        self.lblCredintialChk = tk.Label(top)
        self.lblCredintialChk.place(relx=0.120, rely=0.580, height=34, width=260)
        self.lblCredintialChk.configure(background="white")
        self.lblCredintialChk.configure(disabledforeground="#a3a3a3")
        self.lblCredintialChk.configure(font=font13)
        self.lblCredintialChk.configure(foreground="#ff0f3f")
        self.lblCredintialChk.configure(text='''Credintial''')

     #    self.btnDetection = tk.Button(top)
     #    self.btnDetection.place(relx=0.300, rely=0.650, height=86, width=86)
     #    self.btnDetection.configure(activebackground="#ececec")
     #    self.btnDetection.configure(activeforeground="#000000")
     #    self.btnDetection.configure(background="#ffffff")
     #    self.btnDetection.configure(disabledforeground="#a3a3a3")
     #    self.btnDetection.configure(foreground="#000000")
     #    self.btnDetection.configure(highlightbackground="#d9d9d9")
     #    self.btnDetection.configure(highlightcolor="black")
     #    photo_location = os.path.join(prog_location,r"Images/recognize icon.png")
     #    self._img1 = tk.PhotoImage(file=photo_location)
     #    self.btnDetection.configure(image=self._img1)
     #    self.btnDetection.configure(pady="0")
     #    self.btnDetection.configure(relief="flat")
     #    self.btnDetection.configure(text='''Button''')
     #    self.btnDetection.bind('<Button-1>',btnDetection)
     # #   self.btnDetection.configure(state='disable')

        self.btnComparission = tk.Button(top)
        self.btnComparission.place(relx=0.22, rely=0.650, height=86, width=86)
        self.btnComparission.configure(activebackground="#ececec")
        self.btnComparission.configure(activeforeground="#000000")
        self.btnComparission.configure(background="#ffffff")
        self.btnComparission.configure(disabledforeground="#a3a3a3")
        self.btnComparission.configure(foreground="#000000")
        self.btnComparission.configure(highlightbackground="#d9d9d9")
        self.btnComparission.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "images", "Algorithm-comparisson_icon.png")
        self._img2 = tk.PhotoImage(file=photo_location)
        self.btnComparission.configure(image=self._img2)
        self.btnComparission.configure(pady="0")
        self.btnComparission.configure(relief="flat")
        self.btnComparission.configure(text='''Button''')
       # self.btnComparission.configure(state='disable')
        self.btnComparission.bind('<Button-1>',btnCompression)


        self.lblCredintial = tk.Label(top)
        self.lblCredintial.place(relx=0.22, rely=0.790, height=34, width=86)
        self.lblCredintial.configure(background="white")
        self.lblCredintial.configure(disabledforeground="#a3a3a3")
        self.lblCredintial.configure(font=font13)
        self.lblCredintial.configure(foreground="blue")
        self.lblCredintial.configure(text='''Start System''')

        # self.lblCredintial = tk.Label(top)
        # self.lblCredintial.place(relx=0.300, rely=0.790, height=34, width=86)
        # self.lblCredintial.configure(background="white")
        # self.lblCredintial.configure(disabledforeground="#a3a3a3")
        # self.lblCredintial.configure(font=font13)
        # self.lblCredintial.configure(foreground="blue")
        # self.lblCredintial.configure(text='''Detection''')

        self.btnLogOut = tk.Button(top)
        self.btnLogOut.place(relx=0.1580, rely=0.860, height=35, width=200)
        self.btnLogOut.configure(activebackground="#ececec")
        self.btnLogOut.configure(activeforeground="#000000")
        self.btnLogOut.configure(background="blue")
        self.btnLogOut.configure(disabledforeground="#a3a3a3")
        self.btnLogOut.configure(font=font13)
        self.btnLogOut.configure(foreground="#ffffff")
        self.btnLogOut.configure(highlightbackground="#d9d9d9")
        self.btnLogOut.configure(highlightcolor="black")
        self.btnLogOut.configure(pady="0")
        self.btnLogOut.configure(text='''Log Out''')
        self.btnLogOut.configure(width=266)
        self.btnLogOut.bind('<Button-1>',btnExit)






vp_start_gui()
