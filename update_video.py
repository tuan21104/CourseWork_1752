import tkinter as tk
from tkinter import messagebox
from video_library import get_name, get_rating, get_play_count, set_rating

# UpdateVideos class for the Update Videos section
class UpdateVideos:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x200")
        self.window.title("Update Videos")

        # Setup the layout with grid
        self.create_widgets()

    def create_widgets(self):
        # Label for video number
        tk.Label(self.window, text="Video Number:").grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Entry for video number
        self.video_number_entry = tk.Entry(self.window)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Label for new rating
        tk.Label(self.window, text="New Rating (1-5):").grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Entry for new rating
        self.new_rating_entry = tk.Entry(self.window)
        self.new_rating_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Button to update the rating
        tk.Button(self.window, text="Update Rating", command=self.update_rating).grid(row=2, column=0, columnspan=2, pady=10)

        # Label to display results or errors
        self.result_label = tk.Label(self.window, text="", fg="blue")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def update_rating(self):
        video_number = self.video_number_entry.get()
        new_rating = self.new_rating_entry.get()

        try:
            video_name = get_name(video_number)
            if video_name:
                new_rating = int(new_rating)
                if not 1 <= new_rating <= 5:
                    raise ValueError("Rating must be between 1 and 5.")

                set_rating(video_number, new_rating)
                play_count = get_play_count(video_number)
                self.result_label.config(text=f"Video: {video_name}\nNew Rating: {new_rating}\nPlay Count: {play_count}", fg="blue")
            else:
                raise ValueError(f"Video {video_number} not found")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.result_label.config(text="", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateVideos(root)
    root.mainloop()


