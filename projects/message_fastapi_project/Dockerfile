FROM python:3.10

ARG wheel=message_fastapi_project-0.1.0-py3-none-any.whl

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/$wheel /code/$wheel
RUN pip install --no-cache-dir --upgrade /code/$wheel

CMD ["uvicorn", "example.message_api.core:app", "--host", "0.0.0.0", "--port", "8000"]
