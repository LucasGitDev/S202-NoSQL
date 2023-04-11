import threading
import time
import random
from sensor_model import Sensor
from database import Database
from sensor_service import SensorServices
import uuid

COLLECTION = 'sensores'
db = Database()
TRIGGER_VALUE = 38


def setupCollection():
    collection = db.createCollectionIfNotExists(COLLECTION, Sensor.getSchema())
    return collection


# assim que o sensor for alarmado, o programa deve ser encerrado
def generateSensorData(sensor: Sensor, interval: float):
    try:
        while True:
            # gerar um valor entre 30 e 40
            sensor.valorSensor = random.randint(30, 40)
            print(f'{sensor.nomeSensor}: {sensor.valorSensor}')
            sensor.sensorAlarmado = sensor.valorSensor > TRIGGER_VALUE
            sensorServices.update(sensor)

            if sensor.sensorAlarmado:
                raise Exception(
                    f'Atenção! Temperatura muito alta! Verificar o Sensor {sensor.nomeSensor}')

            time.sleep(interval)
    except Exception as e:
        print(e.args[0])
        exit()


def main():
    global sensorServices
    sensorServices = SensorServices(setupCollection())

    qtdSensores = 3

    threads = []

    for i in range(qtdSensores):
        sensor = sensorServices.create(
            Sensor(f'ST {uuid.uuid4()}', 0, 'C', False))
        t = threading.Thread(target=generateSensorData, args=(sensor, 1))
        threads.append(t)

    t1, t2, t3 = threads

    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    main()
