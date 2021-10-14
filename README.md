# lucky-numbers-api

Install dependencies
```pipenv install```
Shell environment
```pipenv shell```
Lock requirements if needed.
```pipenv lock -r > requirements.txt ```
Start server
```uvicorn src.app:app --reload ```
Docker commands
```docker build -t lucky-numbers .```
```docker run -d --name luckynumbers -p 80:80 lucky-numbers``