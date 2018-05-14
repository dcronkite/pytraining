0. Setup environment
    * In powershell/cmd, add the parent directory to path
        * On Command Prompt: `C:\path\to\app>set FLASK_APP=hello.py`
        * And on PowerShell: `PS C:\path\to\app> $env:FLASK_APP = "hello.py"`
    * Then, run the app using `python app.py`
1. Create basic `app.py` with 'hello world' view
    * Add bold (or other html)
    * Lookup View Source in web browser (Ctrl + U)
2. Move views into a separate directory
    * Directory for package
    * Add views file
    * Add initialization file
3. Create sqlalchemy models in a `models.py`
    * Requires installation of flask-sqlalchemy
4. Create templates
    * Template directory within package
    * Add template
5. Create login
    * Use a form to automatically clean data
        * form.hidden_tag()
        * set CSRF token (secret_key)
    * Use the session to store username
6. Create abstraction form
    * Create new template, form
    * Use session to keep track of record_id