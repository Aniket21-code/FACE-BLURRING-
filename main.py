import tkinter
import tkinter.ttk
from tkinter.filedialog import askopenfilename
import cv2
import faceblur
def blurFile():
    path=askopenfilename()
    img=cv2.imread(path)
    img=faceblur.blurFaces(img)
    cv2.imshow("Blurred Image",img)
def blurWebcam():
    cam=cv2.VideoCapture(0)
    while True:
        ret,img=cam.read()
        img=faceblur.blurFaces(img)
        cv2.imshow("Webcam",img)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()
window=tkinter.Tk()
window.title("Face Blur Software")
window.minsize(80,40)
logo=tkinter.PhotoImage(file="mandala.png")
window.iconphoto(False,logo)
background=tkinter.PhotoImage(file="face.png")
imageLabel=tkinter.ttk.Label(image=background)
imageLabel.grid()
textLabel=tkinter.ttk.Label(window,text="Face Blur Software\nPress a button to start blurring")
textLabel.grid()
fileButton=tkinter.ttk.Button(window,text="BLUR IMAGE FILE",command=blurFile)
fileButton.grid()
webcamButton=tkinter.ttk.Button(window,text="BLUR WEBCAM",command=blurWebcam)
webcamButton.grid()
window.mainloop()
