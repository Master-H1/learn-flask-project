#!/usr/bin/env bash

PROJECT_NAME="myproject"

# Create directories
mkdir -p $PROJECT_NAME/app/{models,routes,templates,static}
mkdir -p $PROJECT_NAME/{migrations,tests}

# Create files
touch $PROJECT_NAME/app/__init__.py
touch $PROJECT_NAME/app/extensions.py
touch $PROJECT_NAME/app/models/user.py
touch $PROJECT_NAME/app/routes/auth.py
touch $PROJECT_NAME/app/config.py

touch $PROJECT_NAME/tests/test_auth.py
touch $PROJECT_NAME/.env
touch $PROJECT_NAME/run.py
touch $PROJECT_NAME/requirements.txt

echo "Project structure for '$PROJECT_NAME' created!"
