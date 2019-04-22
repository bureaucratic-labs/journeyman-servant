# Servant

![HTTP API for Journeyman models](https://i.imgur.com/3cAJ7ES.png)

HTTP API for [Journeyman](https://github.com/bureaucratic-labs/journeyman) models


# Configuration

```bash
$ export MODEL_PARAMS_PATH=/path/to/params.json
$ export MODEL_PREPROCESSOR_PATH=/path/to/preprocessor.pickle
$ export MODEL_PATH=/path/to/model.h5
$ export SENTRY_DSN=https://...  # optional
```

# Start

```bash
$ gunicorn servant:create_app --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornUVLoopWebWorker --workers 1
```

# Example

Request:

```bash
$ curl -X POST "http://localhost:8080/api/v1/classify" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"items\": [    \"метро Лесная\",    \"на площади восстания\",    \"техноложка\"  ]}"
```

Response:

```json
{
  "items": [
    "lesnaya",
    "ploshchad-vosstaniya",
    "tekhnologicheskij-institut"
  ]
}
```
