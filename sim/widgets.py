from enum import Enum
import random
import string

class WidgetType(Enum):
    NONE = 0
    INDICATOR_LIGHT = 1
    BATTERY = 2
    PORT = 3

class BatteryType(Enum):
    AA = 0
    D = 1

class IndicatorLightType(Enum):
    SND = 0
    CLR = 1
    CAR = 2
    IND = 3
    FRQ = 4
    SIG = 5
    NSA = 6
    MSA = 7
    TRN = 8
    BOB = 9
    FRK = 10

class PortType(Enum):
    DVI_D = 0
    PARALLEL = 1
    PS_2 = 2
    RJ_45 = 3
    SERIAL = 4
    STEREO_RCA = 5

class BatteryWidget:
    def __init__(self,type:BatteryType,count:int):
        self.type = type
        self.count = count

class IndicatorLight:
    def __init__(self,lit:bool,label:IndicatorLightType):
        self.lit = lit
        self.label = label
        
class Timer:
    def __init__(self,minutes:int,seconds:int):
        self.minutes = minutes
        self.seconds = seconds

    def step(self) -> bool:
        self.seconds -= 1
        if self.seconds < 0:
            self.minutes -= 1
            if self.minutes < 0:
                return False
            self.seconds = 59
        return True

    def in_future(self,minutes,seconds):
        return Timer(minutes,seconds)
    
    def __str__(self) -> str:
        return '[{minutes}:{seconds:0>2}]'.format(minutes=self.minutes,seconds=self.seconds)

    def contains_digit(self,digit:int):
        return str(digit) in str(self)

class Serial:
    min_len = 6
    max_len = 8
    def __init__(self):
        sample = string.ascii_letters.replace('y','').replace('Y','') + string.digits
        length = random.randint(Serial.min_len,Serial.max_len)
        self.__string = ''.join(random.choices(sample,k=length-1)) + random.choice(string.digits)
    
    def odd_digit_end(self) -> bool:
        return int(self.__string[-1]) % 2 == 1

    def has_vowel(self) -> bool:
        return not set(self.__string).isdisjoint(['a','e','i','o','u','A','E','I','O','U'])

    def __str__(self) -> str:
        return self.__string