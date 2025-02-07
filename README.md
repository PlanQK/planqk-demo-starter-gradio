# PLANQK Demo Starter using Gradio

This is a simple example of a PLANQK Demo created with [Gradio](https://www.gradio.app).

The demo creates a web user interface for a service generating real random numbers.
Users are able to request the amount of random numbers they want to generate.

## Run it locally:

```bash
uv venv
uv sync

source .venv/bin/activate

gradio app.py
```

## Run with Docker

```bash
docker build -t planqk-demo-starter-gradio .
docker run -p 8080:8080 planqk-demo-starter-gradio
```

> PLANQK also uses the Dockerfile to build and run the container image.
> Verifying that the Docker container runs correctly locally makes sure that it runs correctly on PLANQK ;-)
