# habitica-py-api
Python client for habitica api

For correct work follow steps:
- `pip install -r requirements.txt`
- Create .env file by template
```
habitica_user_id = "YOUR_USER_ID"
habitica_token = "YOUR_TOKEN"
```
- test your code
```PYTHONPATH=. pytest -v```


## Dev:
To check your fixes before commit install pre-commit
```
pre-commit install
pre-commit run --all-files
```
