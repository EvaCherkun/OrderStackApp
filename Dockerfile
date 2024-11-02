FROM python:alpine

COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["order_stack.py"]
