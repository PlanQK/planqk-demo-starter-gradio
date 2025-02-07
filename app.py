import os
import sys
from random import randint, seed

import gradio as gr
from loguru import logger


# setup logging
logging_level = os.environ.get("LOG_LEVEL", "DEBUG")
logger.configure(handlers=[{"sink": sys.stdout, "level": logging_level}])
logger.info("Demo started")


# The function that will be called when the user interacts with the web interface.
def run(n_numbers: int):
    """
    This is a simple implementation generating pseudo random numbers using Python's random package.

    You may employ and talk to a PLANQK Service that generates real random numbers using a quantum computer.
    The code below shows how you could use the PLANQK Service SDK to call a service:

    consumer_key = os.getenv("CONSUMER_KEY", None)
    consumer_secret = os.getenv("CONSUMER_SECRET", None)
    service_endpoint = os.getenv("SERVICE_ENDPOINT", "<service endpoint URL>")  # found in the application details after subscribing to a service

    client = PlanqkServiceClient(service_endpoint, consumer_key, consumer_secret)

    data = {"n_numbers": n_numbers}
    params = {"n_bits": 4, "backend": "qasm_simulator", ...}
    job = client.start_execution(data=data, params=params)

    result = client.get_result(job.id)

    random_numbers = result["random_number_lists"]
    """
    seed(1)

    random_numbers = []

    for _ in range(n_numbers):
        value = randint(0, 10000)
        random_numbers.append(value)

    return "\n".join([str(x) for x in random_numbers])


title = "PLANQK Demo Starter using Gradio"
description = """
    This is a simple example of a PLANQK Demo created with [Gradio](https://www.gradio.app).

    The demo creates a web user interface for a service generating real random numbers.
    Users are able to request the amount of random numbers they want to generate.
    """

# The Interface class allows you to create a web-based GUI / demo in a few lines of code.
# You must specify three parameters: (1) the function to create a GUI for (2) the desired input components and (3) the desired output components.
# Additional parameters can be used to control the appearance and behavior of the demo.
#
# Take a look to the Gradio documentation at https://www.gradio.app/docs/gradio/interface
demo = gr.Interface(
    run,
    gr.Number(label="The amount of random numbers to be generated:", value=10),
    gr.Text(
        label="The (pseudo) random numbers:",
    ),
    examples=[10, 50, 100],
    title=title,
    description=description,
    flagging_mode="never",
)

demo.launch()
