import os
import uuid

import azure.cosmos.cosmos_client as cosmos_client


class CosmosDb:
    def __init__(self):
        self.client = cosmos_client.CosmosClient(os.environ.get('COSMOS_URI'),
                                                 os.environ.get('COSMOS_KEY'))
        self.database = self.client.get_database_client('data')
        self.container = self.database.get_container_client('pets')

    def all(self):
        data = self.container.query_items(query='SELECT * FROM pets',
                                          enable_cross_partition_query=True)
        data = self.to_dict(data)

        return data

    def get(self, uuid):
        data = self.container.query_items(query='SELECT * FROM pets p WHERE p.id = @id',
                                          parameters = [dict(name='@id', value=uuid)],
                                          enable_cross_partition_query=True)
        data = self.to_dict(data)

        return data[0]

    def create(self, name, description, src=None):
        return self.container.create_item(
            {
                "id": uuid.uuid4().__str__(),
                'name': name,
                'description': description,
                'photo': src
            }
        )

    def update(self, obj):
        return self.container.upsert_item(obj)

    def delete(self, uid):
        self.container.delete_item(item=uid, partition_key="/nnbzh")

        return True

    def to_dict(self, arr):
        result = []
        for item in arr:
            obj = {
                'id': item['id'] if 'id' in item else None,
                'name': item['name'] if 'name' in item else None,
                'description': item['description'] if 'description' in item else None,
                'photo': item['photo'] if 'photo' in item else None
            }

            result.append(obj)
        return result
