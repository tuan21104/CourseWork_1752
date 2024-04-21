import tkinter as tk # Importing the tkinter library and call it as tk
import tkinter.scrolledtext as tkst # Importing the scrolledtext module from tkinter and call it as tkst

import font_manager as fonts # Importing a file named font_manager and call it as fonts
import video_library as lib # Importing a file named video_library and call it as lib
from PIL import Image, ImageTk

video_images = {
    "01" : r"D:\OOP_Coursework\tom_-_jerry.png",
    "02" : r"D:\OOP_Coursework\Breakfast_at_Tiffany's_(1961_poster).png",
    "03" : r"D:\OOP_Coursework\CasablancaPoster-Gold.png",
    "04" : r"D:\OOP_Coursework\Sound_of_music.png",
    "05" : r"D:\OOP_Coursework\Poster_-_Gone_With_the_Wind_01.png",  
}


# Function to set text content in a text area
def set_text(text_area, content): # inserts content into the text_area  
    text_area.delete("1.0", tk.END) # First, the existing content is deleted
    text_area.insert(1.0, content) # Then, the new content is inserted

# CheckVideos class for the Check Videos section
class CheckVideos():
    def __init__(self, window): # Constructor method for initializing the main application window.
        window.geometry("750x350") # Set window size
        window.title("Check Videos") # Set window title

        # Create List All Videos button
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked) # Create a 'List all videos' button
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) # Place  the "List All Videos" button in row 0, column 0 of the window grid with 10 pixels of padding on both sides

        # Create Enter Video Number label
        enter_lbl = tk.Label(window, text="Enter Video Number") # Create a label for enter video number
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) # Place the label in the window in row 0, column 1 of the window grid with 10 pixels of padding on both sides

        # Create Entry field for video number
        self.input_txt = tk.Entry(window, width=3) # Create an entry widget for enter video number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) # Place the entry widget in the window in row 0, column 2 of the window grid with 10 pixels of padding on both sides

        # Create Check Video button
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked) # Create a button for check video details
        check_video_btn.grid(row=0, column=3, padx=10, pady=10) # Place the button in the window in row 0, column 3 of the window grid with 10 pixels of padding on both sides

         # Create scrolled text area for video list
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") # Create a scrolled text area for list videos
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) # Place the scrolled text area in the window spanning 3 columns, start from column 0, row 1, with 10 pixels of padding on both sides
        

        # Create text area for video details
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none") # Create a regular text area for display video details
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) # Place the text area in the window at row 1, column 3 of the grid with sticky position "NW" and 10 pixels of padding on both left and top

        # Create status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a label for display status messages
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)  # Place the label in the window span 4 columns at row 2, column 0 of the grid with sticky position "W" and 10 pixels of padding on both left and top

        # Create label for displaying video image
        self.video_image_label = tk.Label(window) 
        self.video_image_label.grid(row=1, column=3, sticky="SW", padx=10, pady=10)

        self.list_videos_clicked() # Call the list_videos_clicked function to display video list initially
    
     # Function to handle Check Video button click
    def check_video_clicked(self): # Method fired when "Check Video" button is clicked
        key = self.input_txt.get() # Get the text entered in the entry widget
        name = lib.get_name(key) # Get the name of the video based on the entered key
        if name is not None: # If video is found
            director = lib.get_director(key) # Get the director of the video
            rating = lib.get_rating(key) # Get the rating of the video
            play_count = lib.get_play_count(key) # Get the play count of the video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"  # Create a string with video details
            set_text(self.video_txt, video_details) # Set the text in the video text area
            image_path = video_images.get(key)
            if image_path:
                self.display_image(image_path)
            else:
                self.video_image_label.config(image=None)
        else: # If video is not found
            set_text(self.video_txt, f"Video {key} not found") # Set a message indicating that the video is not found
            self.video_image_label.config(image=None)
        self.status_lbl.configure(text="Check Video button was clicked!") # Update the text of the status label
    # Function to display the video image
    def display_image(self, image_path):

        thumbnail = Image.open(image_path)
        thumbnail = thumbnail.resize((200, 135), Image.LANCZOS)
        photo = ImageTk.PhotoImage(thumbnail)

        self.video_image_label.config(image=photo)
        self.video_image_label.image=photo

    # Function to list all videos
    def list_videos_clicked(self): # Method fired when "List all videos" button is clicked
        video_list = lib.list_all() # Get a list of all videos
        set_text(self.list_txt, video_list) # Call the function to set text in the scrolled text area
        self.status_lbl.configure(text="List Videos button was clicked!") # Update the text of the status label


if __name__ == "__main__":  # Main entry point of the program
    window = tk.Tk()  # Create the main application window
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # Create an application of the CheckVideos class
    window.mainloop()  #  run the window main loop