# hymnsing

Requirements: `bottle`, `pymysql`, `>=python 3.6`

Create `auth.py` with following contents:
```python
auth = {
    'host': DATABASE_HOST,
    'user': DATABASE_USER,
    'password': DATABASE_PASSWORD,
    'db': DATABASE_NAME
}
```
Replace the appropriate fields with actual values

DATABASE_PASSWORD will be the password used to login as an admin on the site

Run in debug mode with `python hymnsing.py`
