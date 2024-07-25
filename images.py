import os
from tkinter import Tk, filedialog, Button, Label, Entry, StringVar, IntVar, Scale, Canvas, HORIZONTAL
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

class TextOnImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("إضافة نص إلى الصور")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.font_size = IntVar(value=36)
        self.location = StringVar(value="أسفل اليسار")
        self.save_directory = ""
        self.file_paths = []
        self.image_resolution = IntVar(value=100)

        self.init_ui()

        self.image = None
        self.tk_image = None
        self.canvas_image = None
        self.text_id = None
        self.text_position = (20, 20)
        self.dragging = False

    def init_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)

        font_size_label = ttk.Label(main_frame, text="حجم الخط:")
        font_size_label.grid(row=0, column=0, pady=5, sticky="w")
        font_size_entry = ttk.Entry(main_frame, textvariable=self.font_size)
        font_size_entry.grid(row=0, column=1, pady=5, sticky="e")

        select_button = ttk.Button(main_frame, text="اختر الصور", command=self.select_images)
        select_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(main_frame, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=5)

        save_directory_button = ttk.Button(main_frame, text="اختر مكان الحفظ", command=self.select_save_directory)
        save_directory_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.save_directory_label = ttk.Label(main_frame, text="")
        self.save_directory_label.grid(row=4, column=0, columnspan=2, pady=5)

        process_button = ttk.Button(main_frame, text="ابدأ المعالجة", command=self.process_images)
        process_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=6, column=0, columnspan=2, pady=10)

        self.resolution_label = ttk.Label(main_frame, text="تغيير الدقة:")
        self.resolution_label.grid(row=7, column=0, pady=5, sticky="w")
        self.resolution_slider = Scale(main_frame, from_=10, to=100, orient=HORIZONTAL, variable=self.image_resolution)
        self.resolution_slider.grid(row=7, column=1, pady=5, sticky="e")

        self.canvas = Canvas(main_frame, width=600, height=400, bg="gray")
        self.canvas.grid(row=8, column=0, columnspan=2, pady=10)
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)

    def select_images(self):
        self.file_paths = filedialog.askopenfilenames(
            filetypes=[("ملفات الصور", "*.jpeg;*.jpg;*.png;*.bmp;*.gif;*.tiff")])
        if self.file_paths:
            self.result_label.config(text=f"تم اختيار {len(self.file_paths)} صورة.")
            self.load_image(self.file_paths[0])

    def select_save_directory(self):
        self.save_directory = filedialog.askdirectory()
        if self.save_directory:
            self.save_directory_label.config(text=f"تم اختيار {self.save_directory}")

    def load_image(self, image_path):
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas_image = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)
        self.update_text()

    def update_text(self):
        if self.text_id:
            self.canvas.delete(self.text_id)
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", self.font_size.get())
        self.text_id = self.canvas.create_text(
            self.text_position[0], self.text_position[1], text=os.path.splitext(os.path.basename(self.file_paths[0]))[0],
            anchor="nw", font=("DejaVu Sans", self.font_size.get()), fill="black")

    def start_drag(self, event):
        self.dragging = True

    def drag(self, event):
        if self.dragging:
            self.text_position = (event.x, event.y)
            self.update_text()

    def stop_drag(self, event):
        self.dragging = False

    def add_text_to_image(self, image_path, save_directory, font_path="DejaVuSans-Bold.ttf", max_size_kb=500):
        margin = 20

        if os.path.isfile(font_path):
            font = ImageFont.truetype(font_path, self.font_size.get())
        else:
            print(f"لم يتم العثور على ملف الخط {font_path}، سيتم استخدام الخط الافتراضي.")
            font = ImageFont.load_default()

        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)

        text = os.path.splitext(os.path.basename(image_path))[0]
        text_position = self.text_position

        draw.text(text_position, text, font=font, fill="black")

        new_image_file = os.path.join(save_directory, os.path.basename(image_path))

        # Resize image based on slider value
        resolution_factor = self.image_resolution.get() / 100.0
        new_size = (int(img.width * resolution_factor), int(img.height * resolution_factor))
        img = img.resize(new_size, Image.LANCZOS)

        quality = 95
        while True:
            img.save(new_image_file, quality=quality)
            if os.path.getsize(new_image_file) <= max_size_kb * 1024 or quality <= 5:
                break
            quality -= 5

        print(f"تمت إضافة النص إلى {image_path} وحفظه في {new_image_file} بحجم {os.path.getsize(new_image_file) / 1024:.2f} KB.")

    def process_images(self):
        if not self.file_paths:
            messagebox.showwarning("تحذير", "يرجى اختيار الصور أولاً.")
            return
        if not self.save_directory:
            messagebox.showwarning("تحذير", "يرجى اختيار مكان الحفظ أولاً.")
            return

        self.progress_bar['value'] = 0
        self.progress_bar['maximum'] = len(self.file_paths)

        for i, file_path in enumerate(self.file_paths):
            self.add_text_to_image(file_path, self.save_directory)
            self.progress_bar['value'] += 1
            self.root.update_idletasks()

        messagebox.showinfo("نجاح", "تمت معالجة الصور بنجاح.")
        self.result_label.config(text="")

# Run the GUI
if __name__ == "__main__":
    root = Tk()
    app = TextOnImageApp(root)
    root.mainloop()
