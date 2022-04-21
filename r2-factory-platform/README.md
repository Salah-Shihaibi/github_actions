git config --global submodule.recurse true
git submodule update --init

DOCKER_BUILDKIT=0 docker build -f r2-factory-platform/Dockerfile -t backend-examplea .

docker compose -f r2-factory-platform/docker-compose.yaml --project-directory $PWD up -d


go to http://localhost:8081/#/

explore http://localhost:8080/spec

#to do 
customise swagger  ui page

