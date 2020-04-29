import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Individu:
    def __init__(orang,i, posisix, posisiy, x, y, t_pulih, karantina):
        # ID tiap Individu
        orang.id = i
        
        # Penempatan Posisi Individu
        orang.x = x
        orang.y = y

        # Posisi individu saat ini
        orang.posisix = posisix
        orang.posisiy = posisiy
        
        # Status tiap Individu : Terinfeksi atau tidak dan Imun terhadap virus atau tidak
        orang.terinfeksi = False
        orang.imun = False
        orang.sembuh = False
        
        # Karantina atau tidak?
        orang.karantina = karantina

        # Pergerakan tiap Individu yang dikarantina dan tidak
        if orang.karantina:
            orang.deltax = 0
            orang.deltay = 0
        else:
            orang.deltax = (orang.x - orang.posisix)
            orang.deltay = (orang.y - orang.posisiy)

        # Waktu saat individu terinfeksi
        orang.t_terinfeksi = -1
        
        # Waktu pemulihan
        orang.t_pulih = t_pulih


    def __str__(orang):
        return "Individu "+orang.id+" berada di ("+str(orang.posisix)+", "+str(orang.posisiy)+")"

    def check_sehat(orang,i):
        # Mengubah status individu yang sakit menjadi Sehat apabila waktu terinfeksi melebihi waktu Pemulihan
        if orang.t_terinfeksi>-1:
            if i-orang.t_terinfeksi>orang.t_pulih:
                orang.pulih()
                
    def infeksi(orang,i):
        # Keadaan saat individu terinfeksi
        orang.terinfeksi = True
        orang.imun = False
        orang.sembuh = False
        orang.t_terinfeksi = i

    def pulih(orang):
        # Keadaan saat individu Pulih, Immune terhadap virus sehingga tidak dapat terkena lagi
        orang.imun = True
        orang.terinfeksi = False
        orang.sembuh = True

    def set_posisi(orang,x,y):
        # Menempatkan tiap individu ke posisi
        orang.x = x
        orang.y = y
        if orang.karantina:
            orang.deltax = 0
            orang.deltay = 0
        else:
            orang.deltax = (orang.x - orang.posisix)
            orang.deltay = (orang.y - orang.posisiy)
    def get_pos(orang):
        return (orang.posisix,orang.posisiy)
    
    def update_pos(orang, n_posx, n_posy):
        # Fungsi untuk membuat pergerakan
        if(n_posx==0 and n_posy==0):
            orang.posisix = orang.posisix + orang.deltax
            orang.posisiy = orang.posisiy + orang.deltay
        else:
            orang.posisix = n_posx
            orang.posisiy = n_posy

        #Generate Random
        rand = np.random.rand()
        #Right
        if(rand<=0.25):
            orang.posisix = orang.posisix + 1
        #Down
        elif(rand<=0.50):
            orang.posisiy = orang.posisiy - 1
        #Left
        elif(rand<=0.75):
            orang.posisix = orang.posisix - 1
        #Up
        else:
            orang.posisiy = orang.posisiy + 1
        
        #Perform PBC Correction
        if (orang.posisix > 20): 
            orang.posisix = orang.posisix - 20
        if (orang.posisix < 0): 
            orang.posisix = orang.posisix + 20
        if (orang.posisiy > 20):
            orang.posisiy = orang.posisiy - 20
        if (orang.posisiy < 0): 
            orang.posisiy = orang.posisiy + 20

    def get_warna(orang):
        if orang.terinfeksi:
            return 'red'
        else:
            return 'blue'


#INIT
n = 200  # Banyak nya Individu 200
r_infeksi = 5  # Rasio individu terinfeksi 5%
p_bergerak = 80  # Probabilitas individu bergerak 80%
t_pulih = 10   #Waktu pemulihan

terinfeksi = 0
individu = []

# Generate Individu di posisi Random dan Menginfeksinya sebagian
for i in range(n):
    p = Individu(i, np.random.randint(low=0, high=20), np.random.randint(low=0, high=20), 
                np.random.randint(low=0, high=20), np.random.randint(low=0, high=20),t_pulih, False)


    if np.random.rand()<r_infeksi/100:
        p.infeksi(0)
        terinfeksi = terinfeksi+1
    if np.random.rand()>p_bergerak/100:
        p.karantina = True

    individu.append(p)


# Fungsi membuat Plot/Visualisasi

fig = plt.figure(figsize=(18,9))
ax = fig.add_subplot(1,2,1)
cx = fig.add_subplot(1,2,2)
ax.axis('off')
cx.axis([0,50,0,n])

scatt = ax.scatter([p.posisix for p in individu], [p.posisiy for p in individu],c='blue',s=8)
ruang = plt.Rectangle((0,0),20,20,fill=False)
ax.add_patch(ruang)

grafik1,=cx.plot(terinfeksi,color="red",label="Terinfeksi")
grafik2,=cx.plot(terinfeksi,color="blue",label="Sembuh")
cx.legend(handles=[grafik2,grafik1])
cx.set_xlabel("Waktu")
cx.set_ylabel("Populasi")

inf = [terinfeksi]
smb = [0]
t = [0]


# Fungsi update Posisi tiap individu per Frame (Agar pergerakan dapat di trace)
def update(frame,smb,inf,t):
    infected = 0
    recover = 0
    warna = []
    sizes = [8 for p in individu]
    for p in individu:
        # Untuk mengetahui berapa lama individu sakit
        p.check_sehat(frame)

        # Animate pergerakan tiap individu
        p.update_pos(0,0)
        
        if p.sembuh:
            recover += 1 # Jumlah individu yang Pulih
        if p.terinfeksi:
            infected += 1 # Jumlah individu yang terinfeksi
            # Cek penyebaran virus
            for org in individu:
                if org.id==p.id or org.terinfeksi or org.sembuh or org.imun:
                    pass
                else:
                    pos1 = p.get_pos()
                    pos2 = org.get_pos()
                    if pos1==pos2:
                        org.infeksi(frame)

        warna.append(p.get_warna()) # Warna tiap individu menggambarkan status kesehatannya

    # print (infected);
    print("Hari ke",frame,":",int(infected),"Terinfeksi")

    
    # Update Plotting
    smb.append(recover)
    inf.append(infected)
    t.append(frame)

    # Visualisasi ke Matplotlib
    offsets = np.array([[p.posisix for p in individu], [p.posisiy for p in individu]])
    scatt.set_offsets(np.ndarray.transpose(offsets))
    scatt.set_color(warna)
    grafik1.set_data(t,inf)
    grafik2.set_data(t,smb)
    return scatt,grafik1,grafik2

#Menjalankan Animasi

animation = FuncAnimation(fig, update, interval=10,fargs=(smb,inf,t),blit=True)
plt.title("Penyebaran Virus")
plt.show()
