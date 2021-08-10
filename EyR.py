import numpy
import matplotlib.pyplot as pl
def euler(t0, tf, presente, dt, ecuacion, *args):
    
    futuros = [] #lista vacía
    tiempos = []
    while True:
        futuros.append(presente)
        tiempos.append(t0)
        if t0 + dt > tf: # si sobrepasa el tf
            dt = tf - t0
        direccion = ecuacion(t0, presente, *args) #f(y,t)
        presente = presente + (direccion * dt)
        t0 = t0 + dt
        if(t0 >= tf):
            break
    return numpy.array(futuros),numpy.array(tiempos)
def RK4(t0, tf, presente, intervalo, pendiente, *args):
    futuros = []
    tiempos = []

    while True:
        futuros.append(presente)
        tiempos.append(t0)

        if(t0+intervalo) > tf:
            intervalo = tf-t0
        k1 = pendiente(t0, presente, *args)
        k2 = pendiente((t0 + (intervalo / 2)), presente + ((intervalo / 2) * k1), *args)
        k3 = pendiente(t0 + (intervalo / 2), presente + (intervalo / 2) * k2, *args)
        k4 = pendiente(t0 + intervalo, presente + (intervalo * k3), *args)
        direccion = (1/6) * (k1 + (2 * k2) + (2 * k3) + k4)
        presente = presente + direccion * intervalo
        t0 = t0+intervalo
        if t0 >= tf:
            break
    return numpy.array(futuros), numpy.array(tiempos)
