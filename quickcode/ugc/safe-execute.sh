SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SUBMISSION_DIR="$(dirname "$SCRIPT_DIR")/submissions/$1/"
CONTAINER_NAME="ugc-docker-$1"

docker run -it -d --name $CONTAINER_NAME ugc-docker /bin/bash

docker cp $SUBMISSION_DIR/tests/ $CONTAINER_NAME:/project/tests/
docker cp $SUBMISSION_DIR/submission.cpp $CONTAINER_NAME:/project/submission.cpp
docker cp $SCRIPT_DIR/runner.sh $CONTAINER_NAME:/project/runner.sh

timeout 10 docker exec $CONTAINER_NAME /project/runner.sh

docker cp $CONTAINER_NAME:/project/output/ $SUBMISSION_DIR/

docker exec $CONTAINER_NAME poweroff
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
