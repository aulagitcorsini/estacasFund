from math import pi

def areaEstaca(diametro):

    area = pi * (diametro ** 2) / 4

    return area

def volumeEstaca(diametro, prof):

    volumeEst = areaEstaca(diametro) * prof

    return volumeEst