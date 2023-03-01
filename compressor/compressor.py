import PySimpleGUI as sg
from zip_creator import make_archive

label_1 = sg.Text("Select files         ")
input_1 = sg.Input()
choose_files_button_1 = sg.FilesBrowse("Choose", key="files")

label_2 = sg.Text("Select destination")
input_2 = sg.Input()
choose_files_button_2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

output_message = sg.Text(key='message', text_color="lime")

window = sg.Window("File Compressor",
                   layout=[[label_1, input_1, choose_files_button_1],
                           [label_2, input_2, choose_files_button_2],
                           [compress_button, output_message]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["message"].update(value="All files completed.")
# sg.WIN_CLOSED:
window.close()
