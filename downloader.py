import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
import os
import threading

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video İndirici")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')

        # Stil ayarları
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 20, 'bold'), background='#f0f0f0')
        style.configure('Info.TLabel', font=('Arial', 10), background='#f0f0f0')
        style.configure('Download.TButton', font=('Arial', 12, 'bold'))

        # Başlık
        self.title_label = ttk.Label(
            root,
            text="YouTube Video İndirici",
            style='Title.TLabel'
        )
        self.title_label.pack(pady=20)

        # URL girişi
        self.url_frame = ttk.Frame(root)
        self.url_frame.pack(fill='x', padx=20)

        self.url_label = ttk.Label(
            self.url_frame,
            text="Video URL:",
            style='Info.TLabel'
        )
        self.url_label.pack(side='left')

        self.url_entry = ttk.Entry(self.url_frame, width=50)
        self.url_entry.pack(side='left', padx=10, fill='x', expand=True)

        # Kayıt yeri seçimi
        self.path_frame = ttk.Frame(root)
        self.path_frame.pack(fill='x', padx=20, pady=10)

        self.path_label = ttk.Label(
            self.path_frame,
            text="Kayıt Yeri:",
            style='Info.TLabel'
        )
        self.path_label.pack(side='left')

        self.path_entry = ttk.Entry(self.path_frame, width=40)
        self.path_entry.pack(side='left', padx=10, fill='x', expand=True)
        self.path_entry.insert(0, os.path.join(os.path.expanduser("~"), "Downloads"))

        self.browse_button = ttk.Button(
            self.path_frame,
            text="Gözat",
            command=self.browse_location
        )
        self.browse_button.pack(side='left', padx=5)

        # Kalite seçimi
        self.quality_frame = ttk.Frame(root)
        self.quality_frame.pack(fill='x', padx=20, pady=10)

        self.quality_label = ttk.Label(
            self.quality_frame,
            text="Video Kalitesi:",
            style='Info.TLabel'
        )
        self.quality_label.pack(side='left')

        self.quality_var = tk.StringVar(value="720p")
        self.quality_combo = ttk.Combobox(
            self.quality_frame,
            textvariable=self.quality_var,
            values=["720p", "480p", "360p", "240p", "144p"],
            state="readonly",
            width=10
        )
        self.quality_combo.pack(side='left', padx=10)

        # İndirme butonu
        self.download_button = ttk.Button(
            root,
            text="İndir",
            style='Download.TButton',
            command=self.start_download
        )
        self.download_button.pack(pady=20)

        # İlerleme çubuğu
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            root,
            variable=self.progress_var,
            maximum=100
        )
        self.progress_bar.pack(fill='x', padx=20, pady=10)

        # Durum etiketi
        self.status_label = ttk.Label(
            root,
            text="",
            style='Info.TLabel'
        )
        self.status_label.pack(pady=10)

    def browse_location(self):
        directory = filedialog.askdirectory(
            initialdir=self.path_entry.get(),
            title="Kayıt Yerini Seçin"
        )
        if directory:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, directory)

    def update_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress_var.set(percentage)
        self.status_label.config(
            text=f"İndiriliyor... %{percentage:.1f}"
        )
        self.root.update()

    def download_complete(self):
        self.status_label.config(text="İndirme tamamlandı!")
        self.download_button.config(state='normal')
        messagebox.showinfo("Başarılı", "Video başarıyla indirildi!")

    def download_video(self):
        try:
            url = self.url_entry.get()
            if not url:
                messagebox.showerror("Hata", "Lütfen bir URL girin!")
                return

            save_path = self.path_entry.get()
            quality = self.quality_var.get()

            self.status_label.config(text="Video bilgileri alınıyor...")
            self.download_button.config(state='disabled')
            
            yt = YouTube(url, on_progress_callback=self.update_progress)
            video = yt.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first()

            if not video:
                messagebox.showerror("Hata", f"{quality} kalitesinde video bulunamadı!")
                self.download_button.config(state='normal')
                return

            self.status_label.config(text="İndirme başlıyor...")
            video.download(save_path)
            self.download_complete()

        except Exception as e:
            self.status_label.config(text="Hata oluştu!")
            self.download_button.config(state='normal')
            messagebox.showerror("Hata", str(e))

    def start_download(self):
        thread = threading.Thread(target=self.download_video)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
