
class Sensor:

    def __init__(self, nomeSensor: str, valorSensor: float, unidadeMedida: str, sensorAlarmado: bool,  _id: str = None) -> None:
        self._id = _id
        self.nomeSensor: str = nomeSensor
        self.valorSensor: float = valorSensor
        self.unidadeMedida: str = unidadeMedida
        self.sensorAlarmado: bool = sensorAlarmado

    def serialize(self) -> dict:
        return {
            "nomeSensor": self.nomeSensor,
            "valorSensor": float(self.valorSensor),
            "unidadeMedida": self.unidadeMedida,
            "sensorAlarmado": self.sensorAlarmado
        }

    def deserialize(data: dict) -> None:
        return Sensor(data["nomeSensor"], data["valorSensor"], data["unidadeMedida"], data["sensorAlarmado"], data["_id"], )

    def getSchema():
        schema = {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['nomeSensor', 'valorSensor', 'unidadeMedida', 'sensorAlarmado'],
                'properties': {
                    'nomeSensor': {
                        'bsonType': 'string',
                        'description': 'Nome do sensor'
                    },
                    'valorSensor': {
                        'bsonType': 'double',
                        'description': 'Valor do sensor'
                    }, 'unidadeMedida': {
                        'bsonType': 'string',
                        'description': 'Unidade de medida do sensor'
                    },
                    'sensorAlarmado': {
                        'bsonType': 'bool',
                        'description': 'Sensor alarmado'
                    },
                },
            },
        }

        return schema
