import re
import os

from zeep import Client


# setting up the path for input and output file
INPUT_PATH = "check/VATids.txt"
OUTPUT_PATH = "check/results.txt"

print("Setting up WSDL Client")
# setting up the wsdl
client = Client(wsdl="http://ec.europa.eu/taxation_customs/vies/"
                "checkVatService.wsdl")

# getting the dir path of this script
dir_path = os.path.dirname(__file__)

# creating a results file
with open(OUTPUT_PATH, "w") as write_file:
    # opening the check file (has to be one ID per line)
    with open(INPUT_PATH, "r") as read_file:
        print("Checking the VAT-IDs...")
        for line in read_file:
            # split id after two characters to seperate country and vatnumber
            id = re.split(r"(\S\S)", line.strip(), 1)
            try:
                # check the vat with wsdl
                r = client.service.checkVat(id[1], id[2])
            except Exception as e:
                # if error print the error
                write_file.write(f"{line.strip()}\t{e}\n")
            else:
                # else print the returned valid-status
                write_file.write(f"{line.strip()}\t{r['valid']}\n")

# open the results file
print("Check done! Opening results...")
os.system(f"notepad {dir_path}/OUTPUT_PATH")
