# VAT-ID_Validation
Validate multiple VAT Numbers easily via the SOAP service of the [European Commission](https://ec.europa.eu/taxation_customs/vies/faq.html#item_18).

The [VIES](https://ec.europa.eu/taxation_customs/vies/vatRequest.html) website of the European Commission supports validation of a single VAT number only. With the VAT-ID Validation tool you can check up to 100 VAT Numbers in one go.

## Installation
You can use either a `exe` or the `validate.py`.

#### Windows EXE

This tool was released as an `exe` file for Windows and can be found and downloaded in the GitHub [release section](https://github.com/Mux-Mastermann/VAT-ID_Validation/releases). You just need to download the `exe` from the `Assets` and can run the programm without any installation.

#### Python / Command-line

This project uses `zeep` for the WSDL request. The project dependencies are stored in a `virtual environment`. To install dependencies you will first need to install `pipenv` if you haven't already.
```
$ pip install pipenv
```

From inside the project folder you can then type the following command to install all dependencies immediately:
```
$ pipenv install
```
To run the programm type the following command from inside the project directory:
```
$ pipenv run validate.py
```

## Usage
Before you start the programm put all the VAT numbers you want to test in a txt-file. Make sure to use a new line for every VAT number. The numbers themself should not contain any whitespace or seperators like `'-'` or `'/'` for example.

After starting the programm a file dialog pops-up. Here you can choose your input file.

PLEASE NOTE: The input file cannot contain more than 100 lines. Otherwise the programm would quit. So if you have more than 100 VAT numbers to test you can split them up in multiple files and check them individually.

After the programm has checked all numbers via the SOAP service of the European Commission it will create a `vatcheck_output.txt` file and opens it up immediately. At the end of each line you will see either `True` if the VAT number is valid or a `False` if it is invalid. In case of an `error` you will see the error-message raised by the programm instead of a True/False.

The output file will be stored in the same directory as your input file. You can save it as you like. If you leave it as it is, be aware that it will be overwritten as soon as you check another file from within this folder.

## Credits

Special thanks to this [YouTube Tutorial](https://www.youtube.com/watch?v=JBYEQjg_znI) from [JavaKing](https://www.youtube.com/channel/UCBbWDoFpLC77cjMyVhmwALw).

As a SOAP-Beginner the most helpful part was the following command:
```
$ python -mzeep [wsdl-adress]
```
After running it scroll down to `Service` and you find all `Operations`.
