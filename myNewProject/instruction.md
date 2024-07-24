When creating a 'template' folder at Root Level
    -- Open settings.py file
        -- Find 'TEMPLATES = '
        -- Add the value inside 'DIRS' key i.e., 'DIRS' : ['template']

    ** templates folder for html files

When creating a 'static' folder at Root Level
    -- Open settings.py file
        -- Find 'STATIC_URL = '
        -- Create new variable
            -- STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

    ** static folder for js, css, etc.

To inject personalised code inside the html file
    -- Use '{% your code %}'
        -- e.g., 
            {% load static %}  --> To load static assets
            <link rel="stylesheet" href="{% static 'style.css' %}">

When creating new App for our project
    -- manage.py startapp app_name
        -- This will provide us with few files
    -- Once the app folder is ready, we need to update settings.py
    -- Open settings.py file
        -- Find 'INSTALLED_APPS =  '
        -- Add the value inside the list followed by comma : 'app_name',


Even though we have a 'templates' folder at root level, but in industry standard it is preferred to have 'templates' folder inside each application we create, since each app can work as a standalone app.
    -- Create 'template' folder inside a app level
        -- Create another folder by the name of the app itself.

Inside the newly created app we wont be availed by emmet by default inside vscode.
    -- Press [ Ctrl + , ] to open settings
    -- search emmet
        -- search for Include language section
            -- Add Item
                Item key > django-html
                value > html
    Now, html emmet suggestion will be availed and still be remained as a django template.
