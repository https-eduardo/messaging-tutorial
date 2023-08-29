from faker import Faker
import random

# Based on this copy and paste code
# 00020126440014BR.GOV.BCB.PIX0122kristine95@example.com5204000053039865802BR5913MATHEUS SOUZA6008LONDRINA62070503***6304E7D6


class PixGenerator:
    def __init__(self):
        self.__fake = Faker('pt_BR')

    def __get_random_city(self):
        CITIES = ['Cambe', 'Maringa', 'Curitiba']
        index = random.randint(0, 2)
        return CITIES[index]

    def generate(self):
        CODE_PREFIX = '00020126440014BR.GOV.BCB.PIX0122'
        CODE_MIDDLE = '5204000053039865802BR5913'
        CODE_END = '62070503***6304E7D6'

        name = self.__fake.name()
        email = self.__fake.email()
        city = self.__get_random_city()

        return f'{CODE_PREFIX}{email}{CODE_MIDDLE}{name}6008{city}{CODE_END}'
