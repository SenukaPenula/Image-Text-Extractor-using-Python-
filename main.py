import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import pytesseract
import os
from ttkthemes import ThemedTk

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ResponsiveImageToTextConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")
        
        # Make the window responsive
        self.root.state('zoomed')  # Start maximized
        
        # Configure colors
        self.colors = {
            'primary': '#0066FF',
            'background': '#F8F9FD',
            'text': '#333333',
            'white': '#FFFFFF'
        }
        
        # Set theme and styles
        self.style = ttk.Style()
        self.style.configure('Main.TFrame', background=self.colors['background'])
        self.style.configure('Header.TLabel',
                           font=('Poppins', 16, 'bold'),
                           background=self.colors['background'],
                           foreground=self.colors['text'])
        self.style.configure('Modern.TButton',
                           font=('Poppins', 11),
                           padding=15)
        
        # Create main container with responsive padding
        self.container = ttk.Frame(self.root, style='Main.TFrame')
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Variables
        self.image_path = tk.StringVar()
        self.current_image = None
        
        # Bind resize event
        self.root.bind('<Configure>', self.on_window_resize)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create responsive main layout
        self.main_paned = ttk.PanedWindow(self.container, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill=tk.BOTH, expand=True)
        
        # Left frame (Image Preview)
        self.left_frame = ttk.Frame(self.main_paned, style='Main.TFrame')
        self.main_paned.add(self.left_frame, weight=1)
        
        # Right frame (Extracted Text)
        self.right_frame = ttk.Frame(self.main_paned, style='Main.TFrame')
        self.main_paned.add(self.right_frame, weight=1)
        
        # Headers with responsive padding
        ttk.Label(self.left_frame, text="Image Preview", style='Header.TLabel').pack(pady=(0, 20))
        ttk.Label(self.right_frame, text="Extracted Text", style='Header.TLabel').pack(pady=(0, 20))
        
        # Image preview area with responsive frame
        self.preview_frame = ttk.Frame(self.left_frame)
        self.preview_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 20))
        
        self.image_canvas = tk.Canvas(self.preview_frame, bg=self.colors['white'], highlightthickness=0)
        self.image_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons with responsive layout
        self.button_frame = ttk.Frame(self.left_frame, style='Main.TFrame')
        self.button_frame.pack(fill=tk.X, pady=20)
        
        # Configure button frame columns
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        
        select_btn = ttk.Button(self.button_frame, text="Select Image", 
                              command=self.select_image, style='Modern.TButton')
        select_btn.grid(row=0, column=0, padx=5, sticky='ew')
        
        convert_btn = ttk.Button(self.button_frame, text="Convert to Text", 
                               command=self.convert_to_text, style='Modern.TButton')
        convert_btn.grid(row=0, column=1, padx=5, sticky='ew')
        
        # Text output area with responsive layout
        self.text_frame = ttk.Frame(self.right_frame)
        self.text_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Configure text frame grid
        self.text_frame.grid_columnconfigure(0, weight=1)
        self.text_frame.grid_rowconfigure(0, weight=1)
        
        self.text_output = tk.Text(self.text_frame,
                                 wrap=tk.WORD,
                                 font=('Poppins', 11),
                                 bg=self.colors['white'],
                                 fg=self.colors['text'],
                                 padx=15,
                                 pady=15,
                                 relief=tk.FLAT)
        self.text_output.grid(row=0, column=0, sticky='nsew')
        
        scrollbar = ttk.Scrollbar(self.text_frame, orient=tk.VERTICAL, 
                                command=self.text_output.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.text_output['yscrollcommand'] = scrollbar.set
        
        # Save button with responsive positioning
        save_btn = ttk.Button(self.right_frame, text="Save", 
                            command=self.save_text, style='Modern.TButton')
        save_btn.pack(pady=20)

    def on_window_resize(self, event):
        # Only handle main window resize events
        if event.widget == self.root:
            self.update_image_display()
    
    def update_image_display(self):
        if self.current_image:
            # Get current canvas size
            canvas_width = self.image_canvas.winfo_width()
            canvas_height = self.image_canvas.winfo_height()
            
            # Calculate new image size maintaining aspect ratio
            img_width = self.original_image.width
            img_height = self.original_image.height
            
            # Calculate scaling factors
            width_factor = canvas_width / img_width
            height_factor = canvas_height / img_height
            scale_factor = min(width_factor, height_factor) * 0.9  # 90% of available space
            
            new_width = int(img_width * scale_factor)
            new_height = int(img_height * scale_factor)
            
            # Resize image
            resized_image = self.original_image.resize((new_width, new_height), 
                                                     Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(resized_image)
            
            # Update canvas
            self.image_canvas.delete("all")
            x = (canvas_width - new_width) // 2
            y = (canvas_height - new_height) // 2
            self.image_canvas.create_image(x, y, anchor='nw', image=self.photo)

    def select_image(self):
        file_types = [('Image files', '*.png *.jpg *.jpeg *.bmp *.gif')]
        file_path = filedialog.askopenfilename(filetypes=file_types)
        
        if file_path:
            self.image_path.set(file_path)
            self.original_image = Image.open(file_path)
            self.current_image = True
            self.update_image_display()
            
    def convert_to_text(self):
        if not self.image_path.get():
            messagebox.showerror("Error", "Please select an image first!")
            return
            
        try:
            self.root.config(cursor="wait")
            self.root.update()
            
            image = Image.open(self.image_path.get())
            text = pytesseract.image_to_string(image)
            
            self.text_output.delete(1.0, tk.END)
            self.text_output.insert(tk.END, text)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.root.config(cursor="")
            
    def save_text(self):
        if not self.text_output.get(1.0, tk.END).strip():
            messagebox.showerror("Error", "No text to save!")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text_output.get(1.0, tk.END))
                messagebox.showinfo("Success", "Text saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = ResponsiveImageToTextConverter(root)
    root.mainloop()
