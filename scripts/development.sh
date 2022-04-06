#!/bin/sh

cd scripts

if [ "$1" = "down" ]; then
  docker-compose -f development-docker-compose.yml down --volumes --rmi local
  exit
fi

if [ "$1" = "new" ]; then
  docker-compose -f development-docker-compose.yml down --volumes --rmi local
fi

sleep 2

if [ "$1" = "new" ]; then
  cd ..
  python manage.py migrate
  python manage.py shell <scripts/init_project_user.py
fi
