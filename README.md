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
- **GOAL**: Create an API that'll prompt homeowners if home has a septic system.
- not Client facing
- Aggregate information in the BE
- Leverage an API to retrieve info from Housecanary

* What went well?
    - Setting up Django and the fake HouseCanary service to handle Data Mocking

* What could be improved in the project?
    - Honestly wanted to be able to leverage Django Restframework with more fluidity, opted to just use Django as is due to time constraints.
    - More tests, I have a simple unit test for the `get_have_septic` call but I'd prefer having more unit tests for the services and even different edge cases based on environment.