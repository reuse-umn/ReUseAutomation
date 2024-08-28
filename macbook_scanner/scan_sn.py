import tkinter as tk
from PIL import ImageTk, Image
import numpy as np
import cv2
import re
from google.cloud import vision


class sn_scan():
    def __init__(self, root, camera_ind):
        self.client = vision.ImageAnnotatorClient()
        self.vid = cv2.VideoCapture(camera_ind)
        self.video_on = False
        root.title('MacBook SN Detector')
        self.display_image = tk.Label(root)
        self.show_sn = tk.Entry(root)
        self.current_frame = None

        self.video_button = tk.Button(root, text='Start Video/Capture (Hotkey: Q)', command=self.on_press)
        self.right_rotate = tk.Button(root, text='Rotate Right', command=self.r_rotate)
        self.left_rotate = tk.Button(root, text='Rotate Left', command=self.l_rotate)
        root.bind('<F1>',self.on_press)

        self.display_image.pack()
        self.right_rotate.pack(side='right')
        self.left_rotate.pack(side='left')
        self.show_sn.pack()
        self.video_button.pack()


    def show_video(self):
        _, frame = self.vid.read()
        PIL_image = Image.fromarray(cv2.cvtColor(np.rot90(frame,k=2), cv2.COLOR_BGR2RGB))
        UI_image = ImageTk.PhotoImage(PIL_image)
        self.display_image.image = UI_image
        self.display_image.configure(image=UI_image)
        if self.video_on:
            self.display_image.after(10,self.show_video)
        else:
            self.capture_handler(frame)


    def capture_handler(self, frame):
        frame = np.rot90(frame,k=2)
        _, frame_data = cv2.imencode('.jpg', frame)
        PIL_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        self.current_frame = PIL_image
        UI_image = ImageTk.PhotoImage(PIL_image)
        self.display_image.image = UI_image
        self.display_image.configure(image=UI_image)
        self.show_sn.delete(0, 'end')
        self.show_sn.insert('end', 'Loading')
        sn = self.query(frame_data.tobytes())
        self.show_sn.delete(0, 'end')
        root.clipboard_clear()
        root.clipboard_append(sn)
        self.display_image.focus()
        if sn is None:
            self.show_sn.insert('end', 'No SN Found')
        else:
            self.show_sn.insert('end', sn)


    def query(self, content):
        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)
        texts = response.text_annotations

        if response.error.message:
            raise Exception(
                f"{response.error.message}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors"
            )

        for text in texts:
            if bool(re.search(r'^[0-9A-Z]{12}$', text.description)):
                sn = text.description.replace('O','0')
                sn = sn.replace('I','1')
                return sn
        return None


    def on_press(self, *args):
        if not self.video_on:
            self.video_on = True
            self.show_video()
        else:
            self.video_on = False


    def r_rotate(self):
        if self.current_frame is None and not self.video_on:
            return
        self.current_frame = self.current_frame.rotate(270)
        UI_image = ImageTk.PhotoImage(self.current_frame)
        self.display_image.image = UI_image
        self.display_image.configure(image=UI_image)


    def l_rotate(self):
        if self.current_frame is None and not self.video_on:
            return
        self.current_frame = self.current_frame.rotate(90)
        UI_image = ImageTk.PhotoImage(self.current_frame)
        self.display_image.image = UI_image
        self.display_image.configure(image=UI_image)



if __name__=='__main__':
    root = tk.Tk()
    app = sn_scan(root,0)
    root.mainloop()
    app.vid.release()