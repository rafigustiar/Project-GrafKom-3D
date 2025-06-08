<<<<<<< HEAD
# Proyek Mobil Sederhana 3D

## Deskripsi

Proyek ini bertujuan untuk memodelkan sebuah **mobil sederhana** dalam bentuk komposisi dari beberapa **objek dasar 3D (primitive)** menggunakan bahasa pemrograman **Python** dan divisualisasikan dalam 3D menggunakan pustaka **Plotly** yang di-embed di HTML melalui **Pyodide**. Hasil akhir proyek ini dapat dijalankan langsung di browser.

## Objek dan Komposisinya

Model mobil ini tersusun dari bagian-bagian berikut:

* **Badan Mobil:** Dibangun dari satu objek **silinder** berwarna hijau tua, yang diposisikan horizontal untuk membentuk badan utama mobil.
* **Atap Mobil:** Dibangun dari satu objek **silinder** berwarna biru muda, yang di-skala dan diposisikan di atas badan mobil untuk memberikan bentuk atap yang sederhana.
* **Roda (4 buah):** Masing-masing roda dibangun dari satu objek **bola** berwarna abu-abu gelap, ditempatkan di empat sudut bawah badan mobil.
* **Kaca Depan & Belakang (2 buah):** Dibangun dari objek **kubus** berwarna biru langit yang di-skala tipis dan ditempatkan sebagai simulasi kaca depan dan belakang.

## Bentuk Dasar 3D yang Digunakan

Proyek ini menggunakan **minimal 3 jenis** bentuk dasar 3D yang berbeda:

1. **`Cylinder` (Silinder):** Digunakan untuk badan mobil dan atap mobil.
2. **`Sphere` (Bola):** Digunakan untuk roda mobil.
3. **`Cube` (Kubus):** Digunakan untuk kaca depan dan belakang.

## Transformasi yang Diterapkan

Setiap bentuk dasar yang digunakan telah mengalami **minimal 2 jenis transformasi** geometri:

* **Translasi (Pergeseran Posisi):** Semua bagian mobil (badan, atap, roda, kaca) digeser ke posisi yang tepat relatif satu sama lain untuk membentuk komposisi mobil yang utuh.
  * Contoh: Roda ditranslasikan ke bawah dan ke samping badan mobil.
* **Rotasi (Putaran):**
  * **Badan Mobil (`Cylinder`):** Dirotasi 90 derajat pada sumbu Z agar posisinya menjadi horizontal (memanjang).
  * **Atap Mobil (`Cylinder`):** Dirotasi 90 derajat pada sumbu Z agar sesuai dengan orientasi badan mobil.
* **Skala (Perbesar/Perkecil):**
  * **Atap Mobil (`Cylinder`):** Di-skala pada sumbu X, Y, dan Z untuk mengubah bentuk silinder menjadi lebih pipih dan lebar di satu sisi, menyerupai kemiringan atap.
  * **Kaca Depan/Belakang (`Cube`):** Di-skala sangat tipis pada satu sumbu untuk membentuk panel datar, dan di-skala pada sumbu lain untuk mendapatkan ukuran yang diinginkan.

## Struktur Scene Graph

Scene graph dalam proyek ini diimplementasikan secara sederhana dalam bentuk **list (`scene_objects`)** di `main.py`. Setiap elemen dalam list adalah sebuah objek `Shape` (atau turunannya seperti `Cylinder`, `Sphere`, `Cube`) yang telah mengalami serangkaian transformasi. Pendekatan ini memungkinkan penambahan dan pengelolaan objek secara modular, meskipun tidak menggunakan struktur hierarkis yang lebih kompleks (parent-child relationship) secara eksplisit, setiap objek dianggap sebagai bagian dari "scene" keseluruhan.

## Visualisasi 3D

Visualisasi dilakukan menggunakan pustaka **Plotly** dengan `plotly.graph_objects.Mesh3d`. Semua data vertex dan face dari setiap objek dalam `scene_objects` digabungkan menjadi satu set data besar yang kemudian dirender oleh Plotly. Pengaturan layout Plotly disesuaikan untuk memberikan judul, mengatur orientasi sumbu, dan memberikan tampilan visual yang jelas. Tambahan pengaturan kamera awal juga diberikan untuk tampilan default yang lebih baik.

## Cara Menjalankan Proyek dengan Live Server (VS Code)

Untuk menjalankan proyek ini di browser lokal Anda menggunakan ekstensi Live Server di VS Code:

1. **Pastikan Live Server Terinstal:** Buka VS Code, pergi ke bagian Extensions (Ctrl+Shift+X), cari "Live Server" oleh Ritwick Dey, dan instal jika Anda belum memilikinya.
2. **Buat Folder Proyek:** Buat folder baru (misalnya, `projek_mobil_sederhana`) di komputer Anda.
3. **Simpan File:**
   * Salin seluruh kode HTML di atas dan simpan sebagai `index.html` di dalam folder `projek_mobil_sederhana`.
   * Salin seluruh kode Python di atas dan simpan sebagai `main.py` di dalam folder `projek_mobil_sederhana`.
   * Salin seluruh teks README ini dan simpan sebagai `README.md` di dalam folder `proyek_mobil_sederhana`.
4. **Buka Folder di VS Code:** Buka folder `projek_mobil_sederhana` di VS Code (File > Open Folder...).
5. **Jalankan Live Server:** Klik kanan pada file `index.html` di Explorer VS Code, lalu pilih "Open with Live Server". Atau, klik ikon "Go Live" di status bar bawah VS Code.

Browser Anda akan otomatis terbuka (atau tab baru akan terbuka jika sudah ada) dan menampilkan model mobil 3D Anda. Live Server akan memantau perubahan pada file Anda, jadi setiap kali Anda menyimpan `index.py` atau `main.py`, browser akan otomatis me-refresh tampilan.

## Cara Mengunggah ke itch.io

1. **Masuk ke Akun:** Login ke akun itch.io Anda.
2. **Buat Proyek Baru:** Pilih "Upload new project" atau "Create new project".
3. **Konfigurasi Proyek:**
   * Berikan judul dan deskripsi yang sesuai untuk proyek Anda.
   * Pada bagian "Kind of project", pilih **"HTML"**.
   * Pastikan "WebGL" atau "HTML5" diaktifkan jika ada opsi serupa.
4. **Unggah File:**
   * Pada bagian "Uploads", klik "Upload file" dan pilih **folder `projek_mobil_sederhana` Anda (atau unggah file `index.html`, `main.py`, dan `README.md` secara terpisah, pastikan `index.html` menjadi file utama).**
   * **Penting:** Itch.io biasanya memerlukan file utama yang akan dijalankan. Pastikan `index.html` Anda dikenali sebagai file yang akan dibuka.
5. **Simpan & Publikasikan:** Setelah mengunggah, atur pengaturan lain sesuai keinginan (harga, kategori, dll.), lalu simpan draf dan publikasikan proyek Anda. Model mobil 3D Anda seharusnya akan berjalan di browser pada halaman itch.io Anda.

<!DOCTYPE html>

<html>
<head>
    <title>Mobil Sederhana 3D</title>
    <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script> 
    <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
    <style>
        body { 
            margin: 0; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            min-height: 100vh; 
            background-color: #f0f0f0; 
            font-family: sans-serif; 
        }
        #plotly-div { 
            width: 800px; 
            height: 600px; 
            background-color: #fff; 
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
            border-radius: 8px; 
            overflow: hidden; 
        }
    </style>
</head>
<body>
    <div id="plotly-div"></div>

    `<script type="text/javascript">`
        async function main() {
            console.log("STATUS: Memuat Pyodide...");
            let pyodide = await loadPyodide();
            console.log("STATUS: Pyodide berhasil dimuat.");

    console.log("STATUS: Menjalankan script Python yang di-embed...");

    try {
                const pythonScriptElement = document.getElementById('python-code-block');
                if (!pythonScriptElement) {
                    console.error("ERROR: Elemen script Python tidak ditemukan.");
                    return;
                }
                const pythonCode = pythonScriptElement.textContent.trim(); // Trim untuk menghilangkan spasi/newline di awal/akhir blok script

    await pyodide.runPythonAsync(`
                    import sys
                    import io
                    sys.stdout = io.StringIO()
                    sys.stderr = io.StringIO()

`+ pythonCode +`

    py_stdout = sys.stdout.getvalue()
                    py_stderr = sys.stderr.getvalue()

    if py_stderr) {
                        console.error("PYTHON_STDERR_ENCODED:" + JSON.stringify(py_stderr));
                    }
                `);

    console.log("STATUS: Script Python selesai dijalankan.");

    const captured_stdout = pyodide.runPython("sys.stdout.getvalue()");
                const captured_stderr = pyodide.runPython("sys.stderr.getvalue()");

    if (captured_stderr && captured_stderr.includes("PYTHON_STDERR_ENCODED:")) {
                    try {
                        const encodedErrorString = captured_stderr.split("PYTHON_STDERR_ENCODED:")[1];
                        const pythonError = JSON.parse(encodedErrorString);
                        console.error("ERROR: Python Runtime Error (dari stderr):", pythonError);
                    } catch (e) {
                        console.error("ERROR: Gagal parse encoded stderr:", e, "Raw:", captured_stderr);
                    }
                } else if (captured_stderr) {
                    console.error("ERROR: Python Runtime Error (raw stderr):", captured_stderr);
                }

    const jsonStartTag = "PLOTLY_FIGURE_JSON_START";
                const jsonEndTag = "PLOTLY_FIGURE_JSON_END";

    const startIndex = captured_stdout.indexOf(jsonStartTag);
                const endIndex = captured_stdout.indexOf(jsonEndTag);

    console.log(`DEBUG: Penanda JSON ditemukan di startIndex: ${startIndex}, endIndex: ${endIndex}`);

    if (startIndex !== -1 && endIndex !== -1 && endIndex > startIndex) {
                    const jsonString = captured_stdout.substring(
                        startIndex + jsonStartTag.length,
                        endIndex
                    ).trim();

    console.log("DEBUG: String JSON yang diekstrak (awal):", jsonString.substring(0, Math.min(jsonString.length, 500)) + "...");
                    console.log("DEBUG: Panjang string JSON:", jsonString.length);

    try {
                        const figure = JSON.parse(jsonString);
                        console.log("STATUS: JSON Plotly berhasil di-parse.");
                        console.log("DEBUG: Objek Figure Plotly setelah parse:", figure);

    Plotly.newPlot('plotly-div', figure.data, figure.layout)
                            .then(() => {
                                console.log("STATUS: Plotly grafik berhasil dirender.");
                            })
                            .catch((renderError) => {
                                console.error("ERROR: Gagal merender grafik Plotly:", renderError);
                            });

    } catch (jsonParseError) {
                        console.error("ERROR: Gagal mengurai JSON Plotly:", jsonParseError);
                        console.error("DEBUG: String JSON yang gagal di-parse (lengkap):", jsonString);
                    }
                } else {
                    console.error("ERROR: Penanda JSON Plotly tidak ditemukan atau tidak valid dalam output Python.");
                    console.log("DEBUG: Output Python (stdout) yang tidak mengandung JSON:", captured_stdout);
                }

    } catch (err) {
                console.error("FATAL ERROR: Terjadi error saat menjalankan Pyodide atau Python (catch utama):", err);
            }
        }

    window.onload = main;`</script>`

    `<script type="text/python" id="python-code-block">`

# main.py content goes here

# PASTIKAN TIDAK ADA SPASI ATAU BARIS KOSONG DI ATAS BARIS INI

# ATAU DI BAWAH BARIS TERAKHIR DARI KODE PYTHON ANDA.

import numpy as np
import plotly.graph_objects as go
import math
import json

# ==== Transformasi Geometri ====

def translate(xyz, dx, dy, dz):
    return xyz + np.array([dx, dy, dz])

def scale(xyz, sx, sy, sz):
    return xyz * np.array([sx, sy, sz])

def rotate_z(xyz, angle):
    c, s = np.cos(angle), np.sin(angle)
    x, y, z = xyz.T
    x_new = c * x - s * y
    y_new = s * x + c * y
    return np.stack([x_new, y_new, z], axis=-1)

def rotate_y(xyz, angle):
    c, s = np.cos(angle), np.sin(angle)
    x, y, z = xyz.T
    x_new = c * x + s * z
    z_new = -s * x + c * z
    return np.stack([x_new, y, z_new], axis=-1)

def rotate_x(xyz, angle):
    c, s = np.cos(angle), np.sin(angle)
    x, y, z = xyz.T
    y_new = c * y - s * z
    z_new = s * y + c * z
    return np.stack([x, y_new, z_new], axis=-1)

# ==== Primitive 3D ====

def make_cube(size=1.0, center=(0,0,0), color='blue'):
    s = size/2
    x = np.array([-s, s, s, -s, -s, s, s, -s])
    y = np.array([-s, -s, s, s, -s, -s, s, s])
    z = np.array([-s, -s, -s, -s, s, s, s, s])
    verts = np.stack([x, y, z], axis=1)
    verts += np.array(center)
    faces = np.array([
        [0,1,2], [0,2,3],
        [4,5,6], [4,6,7],
        [1,5,6], [1,6,2],
        [0,4,7], [0,7,3],
        [3,2,6], [3,6,7],
        [0,1,5], [0,5,4]
    ])
    return {'type':'cube', 'verts': verts, 'faces': faces, 'color': color}

def make_box(size=(2,1,1), center=(0,0,0), color='cyan'):
    sx, sy, sz = size
    s = np.array([sx/2, sy/2, sz/2])
    x = np.array([-s[0], s[0], s[0], -s[0], -s[0], s[0], s[0], -s[0]])
    y = np.array([-s[1], -s[1], s[1], s[1], -s[1], -s[1], s[1], s[1]])
    z = np.array([-s[2], -s[2], -s[2], -s[2], s[2], s[2], s[2], s[2]])
    verts = np.stack([x, y, z], axis=1)
    verts += np.array(center)
    faces = np.array([
        [0,1,2], [0,2,3],
        [4,5,6], [4,6,7],
        [1,5,6], [1,6,2],
        [0,4,7], [0,7,3],
        [3,2,6], [3,6,7],
        [0,1,5], [0,5,4]
    ])
    return {'type':'box', 'verts': verts, 'faces': faces, 'color': color}

def make_sphere(radius=1.0, center=(0,0,0), color='yellow', detail=25):
    u = np.linspace(0, np.pi, detail)
    v = np.linspace(0, 2*np.pi, detail*2)
    u, v = np.meshgrid(u, v)
    x = radius * np.sin(u) * np.cos(v) + center[0]
    y = radius * np.sin(u) * np.sin(v) + center[1]
    z = radius * np.cos(u) + center[2]
    return {'type':'sphere', 'x':x, 'y':y, 'z':z, 'color': color}

def make_cylinder(radius=0.3, height=1.0, center=(0,0,0), color='gray', detail=40):
    theta = np.linspace(0, 2*np.pi, detail)
    z = np.array([0, height])
    theta, z = np.meshgrid(theta, z)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = z - height/2
    x += center[0]
    y += center[1]
    z += center[2]
    return {'type':'cylinder', 'x':x, 'y':y, 'z':z, 'color': color}

def make_cone(radius=0.1, height=0.7, center=(0,0,0), color='red', detail=32):
    theta = np.linspace(0, 2*np.pi, detail)
    base_x = radius * np.cos(theta)
    base_y = radius * np.sin(theta)
    base_z = -height/2 * np.ones_like(theta)

    apex_x = 0
    apex_y = 0
    apex_z = height/2

    x_combined = np.append(base_x, apex_x)
    y_combined = np.append(base_y, apex_y)
    z_combined = np.append(base_z, apex_z)

    faces = []
    apex_idx = len(base_x)

    for i in range(detail):
        idx1 = i
        idx2 = (i + 1) % detail
        faces.append([idx1, idx2, apex_idx])

    base_center_idx = len(x_combined)
    x_combined = np.append(x_combined, 0)
    y_combined = np.append(y_combined, 0)
    z_combined = np.append(z_combined, -height/2)
    for i in range(detail):
        idx1 = i
        idx2 = (i + 1) % detail
        faces.append([idx1, base_center_idx, idx2])

    x_combined += center[0]
    y_combined += center[1]
    z_combined += center[2]

    return {'type':'cone', 'x':x_combined, 'y':y_combined, 'z':z_combined, 'faces': np.array(faces), 'color': color}

def make_torus(R=0.25, r=0.09, center=(0,0,0), color='black', detail=40):
    u = np.linspace(0, 2*np.pi, detail)
    v = np.linspace(0, 2*np.pi, detail)
    u, v = np.meshgrid(u, v)
    x = (R + r * np.cos(v)) * np.cos(u) + center[0]
    y = (R + r * np.cos(v)) * np.sin(u) + center[1]
    z = r * np.sin(v) + center[2]
    return {'type':'torus', 'x':x, 'y':y, 'z':z, 'color': color}

# ==== Scene Graph Node ====

class SceneNode:
    def __init__(self, name, primitive=None, transform=None, children=None):
        self.name = name
        self.primitive = primitive
        self.transform = transform
        self.children = children if children else []

    def get_all_primitives(self, parent_transform=None):
        primitives = []

    current_transform = self.transform if self.transform else (lambda xyz: xyz)

    if parent_transform:
            composed_transform = lambda xyz: current_transform(parent_transform(xyz))
        else:
            composed_transform = current_transform

    if self.primitive:
            primitives.append( (self.primitive, composed_transform) )

    for child in self.children:
            primitives += child.get_all_primitives(composed_transform)
        return primitives

# ==== Model Mobil Sederhana ====

# --- Root Node ---

mobil = SceneNode("Mobil", children=[])

# --- Badan Mobil (Balok) ---

badan = SceneNode(
    "Badan",
    primitive = make_box((2.5, 1.2, 0.6), center=(0,0,0), color='skyblue'),
    transform = lambda xyz: translate(xyz, 0, 0, 0.4)
)

# --- Kabin Mobil (Kubus) ---

kabin = SceneNode(
    "Kabin",
    primitive = make_cube(0.8, center=(0,0,0), color='dodgerblue'),
    transform = lambda xyz: translate(rotate_y(xyz, math.radians(-9)), 0.45, 0, 0.85)
)

# --- 4 Roda (Torus) ---

roda_pos = [
    (+0.9, +0.5, 0.1),
    (+0.9, -0.5, 0.1),
    (-0.9, +0.5, 0.1),
    (-0.9, -0.5, 0.1),
]
roda_nodes = []
for i, pos in enumerate(roda_pos):
    roda = SceneNode(
        f"Roda_{i+1}",
        primitive = make_torus(R=0.25, r=0.09, center=(0,0,0), color='black'),
        transform = lambda xyz, p=pos: translate(rotate_x(xyz, math.radians(90)), p[0], p[1], p[2])
    )
    roda_nodes.append(roda)

# --- Lampu Depan (Sphere) ---

lampu1 = SceneNode(
    "Lampu_Kanan",
    primitive = make_sphere(radius=0.08, center=(0,0,0), color='yellow'),
    transform = lambda xyz: translate(xyz, 1.35, 0.27, 0.5)
)
lampu2 = SceneNode(
    "Lampu_Kiri",
    primitive = make_sphere(radius=0.08, center=(0,0,0), color='yellow'),
    transform = lambda xyz: translate(xyz, 1.35, -0.27, 0.5)
)

# --- Knalpot (Cylinder) ---

knalpot = SceneNode(
    "Knalpot",
    primitive = make_cylinder(radius=0.05, height=0.25, center=(0,0,0), color='gray'),
    transform = lambda xyz: translate(rotate_y(xyz, math.radians(80)), -1.3, 0.25, 0.2)
)

# --- Antena (Cone) ---

antena = SceneNode(
    "Antena",
    primitive = make_cone(radius=0.03, height=0.45, center=(0,0,0), color='red'),
    transform = lambda xyz: translate(xyz, 0.8, 0.32, 1.13)
)

# --- Susun Scene Graph ---

mobil.children = [badan, kabin] + roda_nodes + [lampu1, lampu2, knalpot, antena]

# ==== Visualisasi Plotly ====

def plot_scenegraph(root):
    fig = go.Figure()

    prims = root.get_all_primitives()

    current_vertex_offset = 0
    all_mesh_x, all_mesh_y, all_mesh_z = [], [], []
    all_mesh_i, all_mesh_j, all_mesh_k = [], [], []
    all_mesh_colors = []

    for prim, transform in prims:
        if prim['type'] in ['cube', 'box', 'cone']:
            verts = prim['verts'] if 'verts' in prim else np.stack([prim['x'], prim['y'], prim['z']], axis=-1)

    if transform: verts = transform(verts)

    faces = prim['faces'] if 'faces' in prim else None

    if faces is not None:
                all_mesh_x.extend(verts[:,0].tolist())
                all_mesh_y.extend(verts[:,1].tolist())
                all_mesh_z.extend(verts[:,2].tolist())

    for f in faces:
                    if len(f) == 3: # Ensure faces are triangles
                        all_mesh_i.append(f[0] + current_vertex_offset)
                        all_mesh_j.append(f[1] + current_vertex_offset)
                        all_mesh_k.append(f[2] + current_vertex_offset)
                        all_mesh_colors.append(prim['color'])

    current_vertex_offset += len(verts)

    elif prim['type'] in ['sphere', 'cylinder', 'torus']:
            x, y, z = prim['x'], prim['y'], prim['z']
            xyz_grid = np.stack([x, y, z], axis=-1)
            if transform: xyz_grid = transform(xyz_grid)

    fig.add_trace(go.Surface(
                x=xyz_grid[:,:,0], y=xyz_grid[:,:,1], z=xyz_grid[:,:,2],
                colorscale=[[0, prim['color']], [1, prim['color']]],
                showscale=False, opacity=0.92,
                name=prim['type']
            ))

    if all_mesh_x:
        fig.add_trace(go.Mesh3d(
            x=all_mesh_x, y=all_mesh_y, z=all_mesh_z,
            i=all_mesh_i, j=all_mesh_j, k=all_mesh_k,
            facecolor=all_mesh_colors,
            opacity=0.95,
            name="Combined Mesh",
            flatshading=True
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False, showbackground=False, showgrid=False, zeroline=False),
            yaxis=dict(visible=False, showbackground=False, showgrid=False, zeroline=False),
            zaxis=dict(visible=False, showbackground=False, showgrid=False, zeroline=False),
            aspectmode='data',
            aspectratio=dict(x=2, y=1.2, z=0.8),
            camera=dict(
                eye=dict(x=2.2, y=1.6, z=1.2),
                up=dict(x=0, y=0, z=1)
            )
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
    )

    fig_json = fig.to_json()
    print("PLOTLY_FIGURE_JSON_START")
    print(fig_json)
    print("PLOTLY_FIGURE_JSON_END")

# Jalankan visualisasi mobil:

plot_scenegraph(mobil)
`</script>`

</body>
</html>
=======
# Project-GrafKom-3D
TUGAS GRAFIKA KOMPUTER
>>>>>>> 06e3bb0e94f4b2873f27a9afe37326c24dbddc98
