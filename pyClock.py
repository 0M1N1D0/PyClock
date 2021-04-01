from tkinter import *
from tkinter import ttk # contiene el separador
import time
import locale 

locale.setlocale(locale.LC_ALL, 'es') # hace que el nombre del mes aparezca en español


# declaración de variables globales para usarlas en la función cronometro()
horas = 0
minutos = 0
segundos = 0
s = 0
m = 0
h = 0
continuar = False
iniciar_de_nuevo = 0 # controla que al presionar más de una vez el boton iniciar no se acelere el tiempo


# establece la fecha y hora actual
def hora_actual():
    hora = time.strftime("%H")
    minutos = time.strftime("%M")
    segundos = time.strftime("%S")

    # establece la hora en el label_hora
    label_hora.config(text=hora + ":" + minutos + ":" + segundos)
    # actualiza el label_hora cada segundo
    label_hora.after(1000, hora_actual)


# establece la fecha actual
def fecha_actual():
    dia = time.strftime("%d")
    mes = time.strftime("%B")
    anio = time.strftime("%Y")
    
    # establece la fecha actual en el label_fecha
    label_fecha.config(text=dia + " de " + mes + " del " + anio)


# crea el cronometro
def cronometro():
    # especifica que las siguientes variables son de ámbito global
    global horas
    global minutos
    global segundos
    global h
    global m
    global s

    # centinela para iniciar o detener el cronometro
    global continuar

    # inicializa los segundos y va sumando 1 en cada iteración 
    s = s + 1

    # cada ves que s llegue a 60 suma 1 a minutos y reinicaliza los segundos a 0
    if s == 60:
        m = m + 1 
        s = 0

    # cada vez que minutos lleguen a 60 suma 1 a horas 
    if m == 60:
        h = h + 1
        m = 0

    # da el formato de 00:00:00 de las horas, minutos, segundo
    if s < 10:
        segundos = "0" + str(s)
    else:
        segundos = s
    if m < 10:
        minutos = "0" + str(m)
    else:
        minutos = m
    if h < 10:
        horas = "0" + str(h)
    else:
        horas = h

    
    # realiza la iteración cada segundo; 1 segundo = 1000 milisegundos
    # se manda llamar a sí misma para realizar otra iteración y así sucesivamente
    if continuar:
        label_crono.after(1000, cronometro)

    # muestra el cronometro en la interfaz
    label_crono.config(text=str(horas) + ":" + str(minutos) + ":" + str(segundos))

def iniciar():
    global continuar
    global iniciar_de_nuevo
    continuar = True

    iniciar_de_nuevo = iniciar_de_nuevo + 1
    if iniciar_de_nuevo == 1:
        # iniciar el cronometro
        cronometro()


# funcion que pausa el cronometro
def pausar():
    global continuar
    global iniciar_de_nuevo
    iniciar_de_nuevo = 0
    continuar = False


# funcion que reinicia el cronometro
def reiniciar():
    global continuar
    global horas 
    global minutos 
    global segundos 
    global h 
    global m 
    global s 
    global iniciar_de_nuevo

    s = 0
    segundos = 0
    m = 0
    minutos = 0
    h = 0
    horas = 0
    iniciar_de_nuevo = 0

    label_crono.config(text="00:00:00")


raiz = Tk()
raiz.title("PyClock")
raiz.geometry("220x150")
raiz.iconbitmap("clock.ico")
raiz.resizable(0,0)

# label = Label(raiz, text="Hora y fecha actual")
# label.grid(row=0, column=0)
# label.config(pady=10)

frame = Frame(raiz)
frame.grid(row=0, column=0)


# label para mostrar la hora
label_hora = Label(frame, text= "")
label_hora.grid(row=1, column=1, padx=15, pady=(10,0), columnspan=3)
# llamada a la función que establece la fecha y la hora y se actualiza cada segundo
hora_actual()


label_fecha = Label(frame, text="")
label_fecha.grid(row=2, column=1, columnspan=3, pady=(0,10))
fecha_actual()


separador = ttk.Separator(frame, orient=HORIZONTAL)
separador.grid(row=3, column=1, columnspan=3, sticky='we', padx= 5, pady=(0,5))

# botones para el cronometro
btn_iniciar = Button(frame, text="Iniciar", command=iniciar)
btn_iniciar.config(width=7)
btn_iniciar.grid(row=4, column=1, padx=8, pady=10)
btn_pausar = Button(frame, text="Pausar", command=pausar)
btn_pausar.config(width=7)
btn_pausar.grid(row=4, column=2, padx = 5, pady=10)
btn_reiniciar = Button(frame, text="Reiniciar", command=reiniciar)
btn_reiniciar.config(width=7)
btn_reiniciar.grid(row=4, column=3, padx=5, pady=10)

# label para el cronometro
label_crono = Label(frame, text="00:00:00") # muestra el cronómetro antes de iniciarlo
label_crono.grid(row=5, column=1, columnspan=3)
#cronometro()


raiz.mainloop()