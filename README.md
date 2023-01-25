# hometap-api
## Getting Started

1. Navigate to project root
   ```bash
   $ cd app
   ```

2. Copy env file
   ```bash
   $ cp example.env .env
   # to view if successfully copied
   $ vim .env
   ```

3. Install dependencies
    ```bash
    $ pip install -r requirements.txt
    ```

4. OPTIONAL - Run Migrations
    ```bash
    $ python manage.py migrate
    ```

5. Run server
    ```bash
    $ python manage.py runserver
    ```

6. Curl the following for result
    ```bash
    curl "http://127.0.0.1:8000/property/septic?address=123+main-st&zipcode=12345"
    ```
## Testing
```bash
$ python manage.py test
```

## Notes
