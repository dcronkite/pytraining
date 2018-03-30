# Building an Executable #

## Build Batch Script ##

* Create a file called `run.bat`
* Add text to file: `python tk_gui.py`
    * Optionally, add `pause` to the end of the file
* Double click `run.bat` to run the program

## Pyinstaller ##

### Download ###

#### Pypi (works within firewall) ####

* Go to https://www.lfd.uci.edu/~gohlke/pythonlibs/
* Search on page for "pyinstaller"
* Download
* Open terminal (cmd prompt/powershell) and run `pip install PyInstaller‑3.3.1‑py2.py3‑none‑any.whl`

#### Pip ####

* Open terminal and run: `pip install pyinstaller`

### Build ###

* Run `pyinstaller tk_gui.spec`
* You may need to modify `tk_gui.spec`

## Cx_freeze ##

### Download ###

#### Pypi (works within firewall) ####

* Go to https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze
* Download relevant `whl` file
* Open terminal (cmd prompt/powershell) and run `pip install cx_Freeze‑5.1.1‑cp36‑cp36m‑win_amd64.whl`

#### Pip ####

* Open terminal and run: `pip install cx_freeze`

### Run ###

* Open terminal and run: `python build.py build`
