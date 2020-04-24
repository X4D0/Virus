# Covid-19 Spreading Simulation
Covid-19 Spreading Simulation using Random Walk 2D with 4 Directions
## Random Walk
### Pengertian
Merupakan suatu cara dalam meng-generate bilangan acak untuk membentuk suatu trayek atau path.
Fenomena alami yang dapat dimodelkan sebagai Random Walk yaitu :
<li>Molekul Gas yang berterbangan</li>
<li>Pencarian jejak hewan</li>
<li>Memodelkan fluktuasi Saham, dll.</li>

### Jenis
#### Random Walk 1D
![image](https://user-images.githubusercontent.com/46711970/80188410-51b17c00-863b-11ea-80b3-951be71a842c.png)
Pada setiap Step yang dilakukan oleh Partikel ke arah kanan maka akan menghasilkan Probabilitas P dan apabila ke kiri akan menghasilkan probabilitas 1-P
#### Random Walk 2D - 4 Directions
![image](https://user-images.githubusercontent.com/46711970/80188332-35adda80-863b-11ea-8b37-9399ebe5c153.png)
#### Random Walk 2D - 8 Directions
![image](https://user-images.githubusercontent.com/46711970/80188616-a228d980-863b-11ea-9d6f-03b24238b8f9.png)
#### Random Walk 3D - 6 Directions
![image](https://user-images.githubusercontent.com/46711970/80188802-e6b47500-863b-11ea-883f-2332d5e51bfe.png)
![image](https://user-images.githubusercontent.com/46711970/80188879-00ee5300-863c-11ea-9a03-a98f7e2fda42.png)

### Random Walk Infinite Space dan Random Walk Finite Space
#### Random Walk Infinite Space
Merupakan simulasi Random Walk yang dilakukan di ruang tanpa batas, contohnya di tempat terbuka seperti Lapangan, Langit, Angkasa
#### Random Walk Finite Space
Merupakan simulasi Random Walk yang dilakukan di ruang terbatas, contohnya di dalam ruangan.

### Simulasi
Ada beberapa langkah yang harus dilakukan dalam membuat simulasi Random Walk :
<li>Menentukan Ukuran Ruangan (Bagi Random Walk Finite Space)</li>
<li>Menentukan Posisi Awal partikel/objek</li>
<li>Buat bilangan Random untuk posisi partikel dan dilakukan iterasi agar Partikel bergerak ke posisi lain</li>
<li>Implementasikan Periodic Boundary Conditions (PBC) agar jika Partikel/Objek bergerak keluar batas atau melebihi batar maka partikel/objek tersebut akan masuk lagi dari arah yang berlawanan</li>
