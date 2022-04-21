git config --global submodule.recurse true
git submodule update --init

DOCKER_BUILDKIT=0 docker build -f backend-framework-library/Dockerfile -t backend-examplea .

docker compose -f backend-framework-library/docker-compose.yaml --project-directory $PWD up -d


go to http://localhost:8081/#/

explore http://localhost:8080/spec

#to do 
customise swagger  ui page

