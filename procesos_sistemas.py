import networkx as nx
import matplotlib.pyplot as plt
import subprocess
import os


os.system('clear')
print ("¿Que Quieres Hacer?")
print ("1-Visualizar los procesos del sistema")
print ("2-Visualizar más info de un proceso en concreto")
opcion = int(input())


if opcion == 1:
   procesos = subprocess.run(["ps", "-aux"], capture_output=True, text=True)
   procesos = procesos.stdout.strip()
   print (procesos)


if opcion == 2:
   print("¿Cúal es el ID del proceso del cual quieres ver más información?")
   procesoID = int(input())

   infoprocesoMemory = subprocess.run(f"ps aux | sed -n {procesoID}p | sed 's/  */ /g' | cut -d ' ' -f 4", capture_output=True, text=True, shell=True)
   infoprocesoMemory = infoprocesoMemory.stdout.strip()

   infoprocesoTime = subprocess.run(f"ps aux | sed -n {procesoID}p | sed 's/  */ /g' | cut -d ' ' -f 10", capture_output=True, text=True, shell=True)
   infoprocesoTime = infoprocesoTime.stdout.strip()

   infoprocesoCpu = subprocess.run(f"ps aux | sed -n {procesoID}p | sed 's/  */ /g' | cut -d ' ' -f 3", capture_output=True, text=True, shell=True)
   infoprocesoCpu = infoprocesoCpu.stdout.strip()

   infoprocesoStat = subprocess.run(f"ps aux | sed -n {procesoID}p | sed 's/  */ /g' | cut -d ' ' -f 8", capture_output=True, text=True, shell=True)
   infoprocesoStat = infoprocesoStat.stdout.strip()



   print ("Memory:",infoprocesoMemory,'\n'"Time:",infoprocesoTime,'\n'"Cpu:",infoprocesoCpu,'\n'"Stat:",infoprocesoStat)



def get_process():
   f = open("ps.txt", "w")
   subprocess.call(["ps", "-aux"], stdout=f)


def read_process_file():
   with open("ps.txt") as file:
       lines = file.readlines()


       for l in lines:
           print(l)


get_process()
read_process_file()


G = nx.DiGraph()


G.add_node(1)
G.add_node(2)
G.add_edges_from([(1, 2)])
nx.draw(G, with_labels=True, font_weight='bold')


plt.show()

