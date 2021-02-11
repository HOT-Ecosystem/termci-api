## Getting Started with Docker

```
cd docker; docker-compose up
```


### Loader

Extract the skos-based RDF of ConceptReferences from OWL. 

```
robot query --input <ontology.owl> --query <sparql.rq> <turtle.ttl>
```


### DotEnv files

The `.env` file in the root directory is used only when running locally. The docker containers use the `.env`
file in the docker directory