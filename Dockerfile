FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install sentence-transformers

RUN pip install Flask

EXPOSE 5000

ENTRYPOINT ["python", "embeddingServer.py"]

CMD ["sentence-transformers/all-mpnet-base-v2"]