FROM python:3.10

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/my_fastapi_project-0.0.1-py3-none-any.whl /code/my_fastapi_project-0.0.1-py3-none-any.whl

RUN pip install --no-cache-dir --upgrade /code/my_fastapi_project-0.0.1-py3-none-any.whl


CMD ["uvicorn", "demo.my_fastapi.main:app", "--host", "0.0.0.0", "--port", "80"]
