from fastapi import APIRouter, Response, Request, Depends

from urllib.parse import unquote

from db.termci_graph import TermCIGraph
from termci_api.utils import decode_uri

router = APIRouter(
    prefix='/conceptreferences',
    tags=['ConceptReferences'],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


def build_jsonld_link_header(resource):
    uri = f'/static/contexts/{resource}.context.jsonld'
    params = {
        'rel': 'http://www.w3.org/ns/json-ld#context',
        'type': 'application/ld+json'
    }
    return f'<{uri}>; ' + '; '.join([f'{k}="{v}"' for k, v in params.items()])


@router.get('/{uri}')
def get_concept_references(uri: str, request: Request, response: Response):
    graph: TermCIGraph = request.app.state.graph
    uri = decode_uri(uri)
    # node = graph.get_code_entry(unquote(uri))
    records = graph.get_concept_references(unquote(uri))
    node = records[0]
    # if node is not None:
    #     node['type'] = 'skos:Concept'
    response.headers['Link'] = build_jsonld_link_header('ConceptReference')
    return node


