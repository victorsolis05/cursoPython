import os


tipo = lambda victoria : "superEstrella" if victoria > 50.0 else "aspirante"

def generarReporte(row):
    #nombre, indicadores  = row[:1], row[1:]
    #wrestler, wins, losses, draws = row
    #wins, losses, draws = list(map(int, [wins, losses, draws]))
    wrestler = row[:1]
    wins, losses, draws = list(map(int, row[1:]))
    total = wins + losses + draws
    wins = round((wins * 100) / total , 1)
    losses = round((losses * 100) / total , 1)
    draws = round((draws * 100) / total , 1)
    return f'''
======================Estadisticas luchador==============================
Nombre: {wrestler[0]}
Pct Victorias: {wins} %
Pct Derrotas: {losses}%
Pct Empates: {draws}%
Tipo de luchador: { tipo(wins)} 
'''

def generarReporteTxt(row):
    reporte = generarReporte(row)
    reportePath = os.path.join(".", "reportes", "reporte_" + row[0]+ ".txt" )
    if os.path.exists(reportePath):
        os.remove(reportePath)
    manejador_archivo = open(reportePath, mode= "x+", encoding="UTF-8")
    manejador_archivo.writelines(reporte)
    manejador_archivo.close()



