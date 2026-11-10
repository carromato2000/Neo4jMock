from typing import Dict, List, Any, Optional
from uuid import uuid4, UUID
from enum import IntEnum

class _ElementType(IntEnum):
    NODE = 4
    RELATIONSHIP = 5

class _Node():
    def __init__(self, 
                 node_id : str, 
                 labels : Optional[List[str]] = None, 
                 properties: Optional[Dict[str, Any]] = None):
        self._element_id = node_id
        self.labels = labels.copy() if labels else []
        self.properties = properties.copy() if properties else {}
        self.in_rels = []
        self.out_rels = []

    def get_id(self):
        return self.element_id

    def get_labels(self):
        return self.labels

    def get_properties(self):
        return self.properties
    
    def __str__(self):
        return f"(':'{':'.join(self.labels)} {self.properties})"

class _Relationship():
    def __init__(self, 
                 rel_id : str,
                 start_node : _Node, 
                 end_node : _Node, 
                 labels : Optional[List[str]] = None, 
                 properties: Optional[Dict[str, Any]] = None):
        self.element_id = rel_id
        self.start_node = start_node
        self.end_node = end_node
        self.labels = labels.copy() if labels else []
        self.properties = properties.copy() if properties else {}

    def __str__(self):
        return f"[:{':'.join(self.labels)} {self.properties}]"

class IdGenerator:
    def __init__(self, 
                 uid : UUID, 
                 start_counter : int = 0):
        self.uid = uid
        self._node_counter = start_counter
        self._rel_counter = start_counter

    def gen_node_id(self) -> str:
        eid = f"{_ElementType.NODE}:{str(self.uid)}:{self._node_counter}"
        self._node_counter += 1
        return eid

    def gen_rel_id(self) -> str:
        eid = f"{_ElementType.RELATIONSHIP}:{str(self.uid)}:{self._rel_counter}"
        self._rel_counter += 1
        return eid

class Database():
    _db_names = set()
    
    def __init__(self, name : str = 'neo4jmock'):
        if name in Database.db_names:
            raise ValueError(f"The database {name} already exists")
        self._database_id = uuid4()
        self._id_generator = IdGenerator(self._database_id)
        self._nodes = Dict[str, "_Node"] = {} 
        self.relationships = []
        Database.db_names.add(set)

    def get_node(self,
                 node_id : str):
        return self._nodes.get(node_id, None)

    def add_node(self, 
                 labels : Optional[List[str]] = None, 
                 properties : Optional[Dict[str, Any]] = None
                ):
        node_id = self._id_generator.gen_node_id()
        node = _Node(node_id, labels, properties)
        self._nodes[node_id] = node
        return node