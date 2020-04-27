import re
import os
import tkinter as tk

from tkinter import filedialog
from zeep import Client


# defining maximum number of lines in the input file
MAX_INPUT_LINES = 100

# setup tkinter
root = tk.Tk()
root.withdraw()
# get the file path from the user
input_path = filedialog.askopenfilename(title="Select File for VAT-ID check",
                                        filetypes=(("text files", "txt"),))

# setting up the wsdl
print("Setting up WSDL Client")
client = Client(wsdl="http://ec.europa.eu/taxation_customs/vies/"
                "checkVatService.wsdl")

# create output path in the same folder as input_path
output_path = f"{os.path.split(input_path)[0]}/vatcheck_output.txt"

# creating a results file
with open(output_path, "w") as write_file:
    # opening the check file (has to be one ID per line)
    with open(input_path, "r") as read_file:
        # checking amount of lines in the file and preserve to much lines
        lines = read_file.readlines()
        if len(lines) > MAX_INPUT_LINES:
            print(f"Input file is too long. Maximum lines: {MAX_INPUT_LINES}")
            quit()

        print("Checking the VAT-IDs...")
        for line in lines:
            # split id after two characters to seperate country and vatno
            id = re.split(r"(\S\S)", line.strip(), 1)
            try:
                # check the vat with wsdl (THE ACTUAL CHECK)
                response = client.service.checkVat(id[1], id[2])
            except Exception as e:
                # if error print the error
                write_file.write(f"{line.strip()}\t{e}\n")
            else:
                # else print the returned valid-status
                write_file.write(f"{line.strip()}\t{response['valid']}\n")

# open the results file
print("Check done! Opening results...")
os.system(f"notepad {output_path}")
