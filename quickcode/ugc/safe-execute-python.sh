SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
SUBMISSION_DIR="$(dirname "$SCRIPT_DIR")/submissions/$1/"
CONTAINER_NAME="ugc-docker-python-$1"
docker run -it -d --name "$CONTAINER_NAME" ugc-docker-python /bin/bash

docker cp "$SUBMISSION_DIR"/tests/ "$CONTAINER_NAME":/project/tests/
docker cp "$SUBMISSION_DIR"/submission "$CONTAINER_NAME":/project/submission
docker cp "$SCRIPT_DIR"/runner-python.sh "$CONTAINER_NAME":/project/runner-python.sh

timeout "$2" docker exec "$CONTAINER_NAME" /project/runner-python.sh

docker cp "$CONTAINER_NAME":/project/output/ "$SUBMISSION_DIR"/

docker exec "$CONTAINER_NAME" poweroff
docker stop "$CONTAINER_NAME"
docker rm "$CONTAINER_NAME"
