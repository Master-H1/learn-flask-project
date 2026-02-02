from pathlib import Path

PROJECT_NAME= Path().cwd()


paths = [
    f"{PROJECT_NAME}/app/models",
    f"{PROJECT_NAME}/app/routes",
    f"{PROJECT_NAME}/app/templates",
    f"{PROJECT_NAME}/app/static",
    f"{PROJECT_NAME}/migrations",
    f"{PROJECT_NAME}/tests"
]

files = [
    f"{PROJECT_NAME}/app/__init__.py",
    f"{PROJECT_NAME}/app/extensions.py",
    f"{PROJECT_NAME}/app/models/user.py",
    f"{PROJECT_NAME}/app/routes/auth.py",
    f"{PROJECT_NAME}/app/config.py",
    f"{PROJECT_NAME}/tests/test_auth.py",
    f"{PROJECT_NAME}/.env",
    f"{PROJECT_NAME}/run.py",
    f"{PROJECT_NAME}/requirements.txt"
]

# create directories
for path in paths:
    Path(path).mkdir(parents=True, exist_ok=True)
    
# create project files
for file in files:
    Path(file).touch(exist_ok=True) 

print(f"The project structure for {PROJECT_NAME} created!")

print(f" cd {PROJECT_NAME}/app")