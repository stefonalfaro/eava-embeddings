# About
This is a Docker image for HuggingFace embedding models exposed with a Python HTTP API. Default behavior will be to pull sentence-transformers/all-mpnet-base-v2 however you can overide this startup command to any model hosted on HuggingFace repository.

## Docker
Default run
docker run -p 5000:5000 eava-embeddings

Run with a specified model
docker run -p 5000:5000 eava-embeddings sentence-transformers/all-mpnet-base-v2

## How to Build
sudo docker build . -t stefonalfaro/eava-embeddings

## Example Request
```
POST http://127.0.0.1:5000/embed
{
    "sentences": [
        "This is an example sentence", 
        "Each sentence is converted"
        ]
}
```

## To use with LangChain
Create a custom class that extends the Embeddings base. Use the eavaEmbeddings.ts as the example.