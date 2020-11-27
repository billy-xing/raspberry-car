# _*_ coding:utf-8 _*_

import threading
import Queue
import time
import random

leftSensorId=1
rightSensorId=2

class SensorEvent:
  def __init__(self, sensorId=0, isBlack=False):
    self.sensorId = sensorId
    self.occurTime=time.time()
    self.isBlack = isBlack


class SensorStatus:
  def __init__(self):
    self.sensorEvents = Queue()

  def addSensorEvent(self, event = SensorEvent()):
    """
    docstring
    """
    self.sensorEvents.put(event)






