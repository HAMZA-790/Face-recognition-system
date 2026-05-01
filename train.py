from tkinter import *
from tkinter import ttk, messagebox
import cv2
import os
import numpy as np
from PIL import Image, ImageTk

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")
        self.root.state('zoomed')

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Button to Train Data
        b1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1.place(x=0, y=380, width=1530, height=60)

    def train_classifier(self):
        data_dir = r"D:\chrome downloads\face recognition\data"
        
        # Check if directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory not found:\n{data_dir}", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg") or file.endswith(".png")]
        
        if len(path) == 0:
            messagebox.showerror("Error", "No training images found in the data directory!", parent=self.root)
            return

        faces = []
        ids = []

        for image in path:
            try:
                # Convert image to grayscale
                img = Image.open(image).convert('L') 
                imageNp = np.array(img, 'uint8')
                
                # The ID is the second part of the filename: user.ID.IMG_NUM.jpg
                filename = os.path.split(image)[1]
                id = int(filename.split('.')[1])
                
                faces.append(imageNp)
                ids.append(id)
                
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1) == 13
            except Exception as e:
                print(f"Skipping {image}: {str(e)}")

        ids = np.array(ids)

        # Train the classifier and save
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training datasets completed successfully!", parent=self.root)
        except Exception as e:
            cv2.destroyAllWindows()
            messagebox.showerror("Error", f"Failed to train model: {str(e)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
