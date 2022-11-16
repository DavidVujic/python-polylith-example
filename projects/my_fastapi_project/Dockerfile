FROM python:3.10

ARG = my_fastapi_project-0.0.1-py3-none-any.whl

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/$ARG /code/$ARG
RUN pip install --no-cache-dir --upgrade /code/$ARG

CMD ["uvicorn", "demo.greet_api.core:app", "--host", "0.0.0.0", "--port", "80"]
