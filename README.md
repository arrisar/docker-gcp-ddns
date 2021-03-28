# arrisar/gcp-ddns

A simple container to update a Google Cloud DNS record when the host networks public IP has changed.

## How to use

Firstly, create a directory in which to store your `config.yaml` and your Google Cloud service account key under `service-account-key.json`.

From there, you can run `docker run -v $PWD/data:/app/data arrisar/gcp-ddns`.

If no `config.yaml` exists, the container will generate one and exit. Simply update this file and run again.