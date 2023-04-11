from sensor_model import Sensor
from bson.objectid import ObjectId


class SensorServices:

    def __init__(self, sensor_repository) -> None:
        self.sensor_repository = sensor_repository

    def create(self, sensor: Sensor) -> Sensor:
        try:
            result = self.sensor_repository.insert_one(sensor.serialize())
            return self.findOneById(result.inserted_id)
        except Exception as e:
            print(f'Erro ao criar sensor: {e}')
            return None

    def update(self, sensor: Sensor) -> Sensor:
        try:
            result = self.sensor_repository.update_one(
                {'_id': ObjectId(sensor._id)}, {'$set': sensor.serialize()})
            if result.modified_count == 0:
                return None
            return self.findOneById(sensor._id)
        except Exception as e:
            print(f'Erro ao atualizar sensor: {e}')
            return None

    def findOneById(self, id) -> Sensor:
        try:
            result = self.sensor_repository.find_one({'_id': ObjectId(id)})
            if result is None:
                return None
            return Sensor.deserialize(result)
        except Exception as e:
            print(f'Erro ao buscar sensor: {e}')
            return None

    def findAll(self) -> list:
        try:
            result = self.sensor_repository.find()
            return [Sensor.deserialize(sensor) for sensor in result]
        except Exception as e:
            print(f'Erro ao buscar sensores: {e}')
            return None

    def deleteOneById(self, id) -> bool:
        try:
            result = self.sensor_repository.delete_one({'_id': ObjectId(id)})
            if result.deleted_count == 0:
                return False
            return True
        except Exception as e:
            print(f'Erro ao deletar sensor: {e}')
            return False
