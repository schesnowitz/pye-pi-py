import PySimpleGUI as sg
from extractor import extract_archive

sg.theme('Dark Teal 4')

label1 = sg.Text("Select Archive:      ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select Destination:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

output_label = sg.Text(key="output", text_color="white")
extract_button = sg.Button("Extract", key="archive")

window = sg.Window("The Un Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    input_path = values['archive']
    output_path = values["folder"]
    extract_archive(input_path, output_path)
    window['output'].update(value="All done...")
window.close()
