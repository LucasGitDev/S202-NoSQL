from database import Database
from neo4j import *


class DatabaseController:

    def __init__(self, db: Database):
        self.db = db

    def create_node(self, labels, properties):
        labels_str = ":".join(labels)
        properties_str = ", ".join(
            f"{key}: ${key}" for key in properties.keys())
        query = f"CREATE (n:{labels_str} {{ {properties_str} }})"
        self.db.execute_query(query, properties)

        # Retornar o nó criado
        node = self.find_node_by_properties(labels, properties)
        return node

    def create_label(self, node, label):
        query = f"MATCH (n) WHERE id(n) = {node.id} SET n:{label}"
        self.db.execute_query(query)

    def create_relationship(self, start_node, end_node, relationship_type, properties=None):
        if properties is None:
            properties = {}
        query = f"MATCH (a) WHERE id(a) = {start_node.id} MATCH (b) WHERE id(b) = {end_node.id} CREATE (a)-[r:{relationship_type} {{ {', '.join(f'{key}: ${key}' for key in properties.keys())} }}]->(b) RETURN r"
        return self.db.execute_query(query, properties)

    def find_node_by_properties(self, labels, properties):
        labels_str = ":".join(labels)
        properties_str = " AND ".join(
            f"n.{key} = ${key}" for key in properties.keys())
        query = f"MATCH (n:{labels_str}) WHERE {properties_str} RETURN n"
        record = self.db.execute_query(query, properties)
        node = record[0]["n"]
        return node

    def get_nodes(self):
        query = "MATCH (n) RETURN n"
        return self.db.execute_query(query)

    def get_relationships(self):
        query = "MATCH ()-[r]->() RETURN r"
        return self.db.execute_query(query)

    def find_family_members_with_label(self, label):
        query = f"MATCH (n:{label}) RETURN n"
        return self.db.execute_query(query)

    def find_parents_of(self, person_name):
        query = "MATCH (child)-[:PARENT_OF]->(parent) WHERE child.name = $person_name RETURN parent"
        return self.db.execute_query(query, {"person_name": person_name})

    def find_children_of(self, person_name):
        query = "MATCH (parent)<-[:PARENT_OF]-(child) WHERE parent.name = $person_name RETURN child"
        return self.db.execute_query(query, {"person_name": person_name})

    def find_partner_of(self, person_name):
        query = "MATCH (person)-[r:PARTNER_OF]->(partner) WHERE person.name = $person_name RETURN partner, r"
        return self.db.execute_query(query, {"person_name": person_name})
