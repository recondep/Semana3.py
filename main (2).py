class ClimaDiario:
    def _init_(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def obtener_temperatura(self):
        return self.__temperatura

    def obtener_humedad(self):
        return self.__humedad

    def obtener_presion(self):
        return self.__presion


class PromedioSemanalClima(ClimaDiario):
    def _init_(self):
        self.__lista_climas_diarios = []

    def agregar_clima_diario(self, clima_diario):
        self.__lista_climas_diarios.append(clima_diario)

    def calcular_promedio_semanal(self):
        total_temperatura = 0
        total_humedad = 0
        total_presion = 0

        for clima_diario in self.__lista_climas_diarios:
            total_temperatura += clima_diario.obtener_temperatura()
            total_humedad += clima_diario.obtener_humedad()
            total_presion += clima_diario.obtener_presion()

        promedio_temperatura = total_temperatura / len(self.__lista_climas_diarios)
        promedio_humedad = total_humedad / len(self.__lista_climas_diarios)
        promedio_presion = total_presion / len(self.__lista_climas_diarios)

        return promedio_temperatura, promedio_humedad, promedio_presion


# Ejemplo de uso del código

clima1 = ClimaDiario(25, 60, 1012)
clima2 = ClimaDiario(28, 65, 1010)
clima3 = ClimaDiario(23, 55, 1008)

promedio_semanal = PromedioSemanalClima()
promedio_semanal.agregar_clima_diario(clima1)
promedio_semanal.agregar_clima_diario(clima2)
promedio_semanal.agregar_clima_diario(clima3)

promedio_temperatura, promedio_humedad, promedio_presion = promedio_semanal.calcular_promedio_semanal()

print("Promedio semanal del clima:")
print("Temperatura:", promedio_temperatura)
print("Humedad:", promedio_humedad)
print("Presión:", promedio_presion)

