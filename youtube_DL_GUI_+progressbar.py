import tkinter 
import customtkinter
from pytube import YouTube

#function to download the Youtube video.
    #The on_progress_callback parameter in the YouTube class of the pytube library 
        #allows you to specify a function that will be called whenever there is a 
        #progress update in the download.
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        video.download()
        print("Download Complete!")
        finishLabel.configure(text="Download Complete!", text_color="green")  
    except Exception as e:
        print(f"An error occurred: {e}")
        finishLabel.configure(text=f"An error occurred: {e}", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

#System Settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue") 

# Our App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)  

#Link InputBox
url_var = tkinter.StringVar()   
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var) 
link.pack()

#Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)    # where 0= 0%, 0.5= 50%, 1 = 100%
progressBar.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="Progress")  
finishLabel.pack()

#Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()

