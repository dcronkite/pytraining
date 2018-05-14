0. Setup environment
    * In powershell/cmd, add the parent directory to path
        * On Command Prompt: `C:\path\to\app>set PATH="%PATH%;C:\path\to\app"`
        * And on PowerShell: `PS C:\path\to\app> $env:PATH = $env:PATH + ";C:\path\to\app"`
    * Install packages required
        * `pip install flask_sqlalchemy flask_wtf wtforms`
        * If you're behind a proxy:
            * Run `pip install filename.whl filename2.whl` for the files from:
                * https://www.lfd.uci.edu/~gohlke/pythonlibs/
                * Locally, G:\CTRHS\CHS\pytraining\lib
    * Then, run the app using `python app.py`
    * If `pip` or `python` aren't found, specify the full path:
        * `C:\Anaconda3\python.exe`
        * `C:\Anaconda3\scripts\pip.exe`
        * `C:\ProgramData\Anaconda3\python.exe`
        * `C:\ProgramData\Anaconda3\scripts\pip.exe`
1. Create basic `app.py` with 'hello world' view
    * Add bold (or other html)
    * Lookup View Source in web browser (Ctrl + U)
2. Move views into a separate directory (a python package)
    * New packages contains files:
        * Add views file
        * Add initialization file
    * External `app.py` file is launched and uses these external files
3. Create sqlalchemy models in a `models.py`
    * Requires installation of flask-sqlalchemy
    * For more context, look back at `009-SQL`
4. Create templates
    * Create a directory called `templates` inside the package
    * Add template
        * Html file that uses Jinja2 syntax
            * http://jinja.pocoo.org/docs/2.10/
5. Create login
    * Use a form to automatically clean data
        * set CSRF token (secret_key)
        * form.hidden_tag()
    * Use the session to store username
        * A session is essentially automated cookie management
6. Create abstraction form
    * Create new template and form
    * Use session to keep track of record_id
