import plotly.graph_objects as go
import numpy as np

# Fungsi membuat balok (box) dengan triangulasi segitiga
def create_box(size=(1, 1, 1), center=(0, 0, 0), color='lightgray', opacity=1):
    x0, y0, z0 = center
    dx, dy, dz = size

    x_unit = [0, 1, 1, 0, 0, 1, 1, 0]
    y_unit = [0, 0, 1, 1, 0, 0, 1, 1]
    z_unit = [0, 0, 0, 0, 1, 1, 1, 1]
    
    x = [dx*(i-0.5)+x0 for i in x_unit]
    y = [dy*(i-0.5)+y0 for i in y_unit]
    z = [dz*(i-0.5)+z0 for i in z_unit]
    
    vertices = list(zip(x, y, z))
    
    faces = [
        [0, 1, 2], [0, 2, 3], # Bottom face
        [4, 5, 6], [4, 6, 7], # Top face
        [0, 1, 5], [0, 5, 4], # Front face (y-negative)
        [1, 2, 6], [1, 6, 5], # Right face (x-positive)
        [2, 3, 7], [2, 7, 6], # Back face (y-positive)
        [3, 0, 4], [3, 4, 7], # Left face (x-negative)
    ]

    return go.Mesh3d(
        x=[v[0] for v in vertices],
        y=[v[1] for v in vertices],
        z=[v[2] for v in vertices],
        i=[f[0] for f in faces],
        j=[f[1] for f in faces],
        k=[f[2] for f in faces],
        color=color,
        opacity=opacity
    )

# Fungsi membuat silinder (untuk roda), dengan opsi orientasi sumbu
def create_cylinder(radius=0.5, height=1, center=(0, 0, 0), resolution=30, color='black', opacity=1, axis='z'):
    x_c, y_c, z_c = center # Pusat silinder
    theta = np.linspace(0, 2 * np.pi, resolution, endpoint=False)
    
    half_height = height / 2

    x_all, y_all, z_all = [], [], []

    if axis == 'z':
        # Lingkaran di bidang XY, tinggi sepanjang sumbu Z
        x_base = radius * np.cos(theta) + x_c
        y_base = radius * np.sin(theta) + y_c
        z_base = np.full_like(theta, z_c - half_height)
        x_top, y_top = x_base, y_base
        z_top = np.full_like(theta, z_c + half_height)
        
        x_all = np.concatenate([x_base, x_top, [x_c], [x_c]])
        y_all = np.concatenate([y_base, y_top, [y_c], [y_c]])
        z_all = np.concatenate([z_base, z_top, [z_c - half_height], [z_c + half_height]])
        
    elif axis == 'y':
        # Lingkaran di bidang XZ, tinggi sepanjang sumbu Y
        x_base = radius * np.cos(theta) + x_c
        z_base = radius * np.sin(theta) + z_c
        y_base = np.full_like(theta, y_c - half_height)
        x_top, z_top = x_base, z_base
        y_top = np.full_like(theta, y_c + half_height)

        x_all = np.concatenate([x_base, x_top, [x_c], [x_c]])
        y_all = np.concatenate([y_base, y_top, [y_c - half_height], [y_c + half_height]])
        z_all = np.concatenate([z_base, z_top, [z_c], [z_c]])

    elif axis == 'x':
        # Lingkaran di bidang YZ, tinggi sepanjang sumbu X
        y_base = radius * np.cos(theta) + y_c
        z_base = radius * np.sin(theta) + z_c
        x_base = np.full_like(theta, x_c - half_height)
        y_top, z_top = y_base, z_base
        x_top = np.full_like(theta, x_c + half_height)

        x_all = np.concatenate([x_base, x_top, [x_c - half_height], [x_c + half_height]])
        y_all = np.concatenate([y_base, y_top, [y_c], [y_c]])
        z_all = np.concatenate([z_base, z_top, [z_c], [z_c]])

    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'")

    # Indeks untuk pusat tutup bawah dan atas
    center_base_idx = resolution * 2
    center_top_idx = resolution * 2 + 1

    i_coords = []
    j_coords = []
    k_coords = []

    # Sisi silinder (persegi panjang yang terdiri dari dua segitiga)
    for t in range(resolution):
        v_base_curr = t
        v_base_next = (t + 1) % resolution
        v_top_curr = t + resolution
        v_top_next = (t + 1) % resolution + resolution

        # Segitiga 1: (base_curr, top_curr, base_next)
        i_coords.append(v_base_curr)
        j_coords.append(v_top_curr)
        k_coords.append(v_base_next)

        # Segitiga 2: (base_next, top_curr, top_next)
        i_coords.append(v_base_next)
        j_coords.append(v_top_curr)
        k_coords.append(v_top_next)
        
    # Tutup bawah (segitiga yang menyebar dari pusat)
    for t in range(resolution):
        i_coords.append(t)
        j_coords.append((t + 1) % resolution)
        k_coords.append(center_base_idx)
        
    # Tutup atas (segitiga yang menyebar dari pusat)
    for t in range(resolution):
        i_coords.append(t + resolution)
        j_coords.append(center_top_idx)
        k_coords.append((t + 1) % resolution + resolution)

    return go.Mesh3d(
        x=x_all,
        y=y_all,
        z=z_all,
        i=i_coords,
        j=j_coords,
        k=k_coords,
        color=color,
        opacity=opacity
    )

# Fungsi membuat bola (hiasan/lampu)
def create_sphere(radius=0.2, center=(0, 0, 0), resolution=20, color='skyblue', opacity=1):
    u, v = np.mgrid[0:2*np.pi:resolution*1j, 0:np.pi:resolution*1j]
    x = radius * np.cos(u) * np.sin(v) + center[0]
    y = radius * np.sin(u) * np.sin(v) + center[1]
    z = radius * np.cos(v) + center[2]
    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], showscale=False, opacity=opacity)

# Fungsi membuat piramida (representasi bentuk segitiga 3D)
def create_pyramid(base_size=(1,1), height=1, center=(0,0,0), color='brown', opacity=1):
    x0, y0, z0 = center
    base_dx, base_dy = base_size
    
    # Vertices dasar (persegi)
    v0 = (x0 - base_dx/2, y0 - base_dy/2, z0)
    v1 = (x0 + base_dx/2, y0 - base_dy/2, z0)
    v2 = (x0 + base_dx/2, y0 + base_dy/2, z0)
    v3 = (x0 - base_dx/2, y0 + base_dy/2, z0)
    
    # Vertices puncak
    apex = (x0, y0, z0 + height)
    
    vertices = [v0, v1, v2, v3, apex]
    
    # Faces (dasar persegi + 4 sisi segitiga)
    faces = [
        [0, 1, 2], [0, 2, 3], # Base (bottom)
        [0, 1, 4], # Side 1
        [1, 2, 4], # Side 2
        [2, 3, 4], # Side 3
        [3, 0, 4]  # Side 4
    ]
    
    x_coords = [v[0] for v in vertices]
    y_coords = [v[1] for v in vertices]
    z_coords = [v[2] for v in vertices]
    
    return go.Mesh3d(
        x=x_coords,
        y=y_coords,
        z=z_coords,
        i=[f[0] for f in faces],
        j=[f[1] for f in faces],
        k=[f[2] for f in faces],
        color=color,
        opacity=opacity
    )

# Scene Graph (struktur mobil)
def build_car_advanced():
    parts = []

    # 1. Body mobil (kubus)
    parts.append(create_box(size=(3.5, 1.6, 0.8), center=(0, 0, 0.4), color='royalblue'))

    # 2. Cabin/Atap mobil (kubus)
    parts.append(create_box(size=(2.2, 1.4, 0.7), center=(0.1, 0, 1.2), color='darkblue'))

    # 3. Windshield (kubus transparan tipis)
    parts.append(create_box(size=(0.05, 1.3, 0.6), center=(-0.8, 0, 1.35), color='skyblue', opacity=0.6))
    # 4. Rear Window (kubus transparan tipis)
    parts.append(create_box(size=(0.05, 1.3, 0.6), center=(1.0, 0, 1.35), color='skyblue', opacity=0.6))

    # 5. Side Windows (kubus transparan tipis)
    parts.append(create_box(size=(0.7, 0.05, 0.5), center=(-0.2, 0.7, 1.2), color='skyblue', opacity=0.6)) # Front Left
    parts.append(create_box(size=(0.7, 0.05, 0.5), center=(-0.2, -0.7, 1.2), color='skyblue', opacity=0.6)) # Front Right
    parts.append(create_box(size=(0.7, 0.05, 0.5), center=(0.6, 0.7, 1.2), color='skyblue', opacity=0.6))  # Rear Left
    parts.append(create_box(size=(0.7, 0.05, 0.5), center=(0.6, -0.7, 1.2), color='skyblue', opacity=0.6)) # Rear Right

    # 6. Roda (silinder - sekarang vertikal)
    # Roda kiri (Y positif)
    parts.append(create_cylinder(radius=0.4, height=0.3, center=(-1.2, 0.8, 0.2), color='black', axis='y')) # Front Left
    parts.append(create_cylinder(radius=0.4, height=0.3, center=(1.2, 0.8, 0.2), color='black', axis='y'))  # Rear Left
    # Roda kanan (Y negatif)
    parts.append(create_cylinder(radius=0.4, height=0.3, center=(-1.2, -0.8, 0.2), color='black', axis='y')) # Front Right
    parts.append(create_cylinder(radius=0.4, height=0.3, center=(1.2, -0.8, 0.2), color='black', axis='y')) # Rear Right

    # 7. Lampu Depan (bola)
    parts.append(create_sphere(radius=0.15, center=(-1.75, 0.5, 0.5), color='yellow'))
    parts.append(create_sphere(radius=0.15, center=(-1.75, -0.5, 0.5), color='yellow'))

    # 8. Lampu Belakang (kubus)
    parts.append(create_box(size=(0.1, 0.3, 0.2), center=(1.75, 0.5, 0.5), color='darkred'))
    parts.append(create_box(size=(0.1, 0.3, 0.2), center=(1.75, -0.5, 0.5), color='darkred'))

    # 9. Bumper Depan (kubus)
    parts.append(create_box(size=(0.3, 1.6, 0.4), center=(-1.9, 0, 0.3), color='darkgray'))
    # 10. Bumper Belakang (kubus)
    parts.append(create_box(size=(0.3, 1.6, 0.4), center=(1.9, 0, 0.3), color='darkgray'))

    # 11. Grill (kubus tipis)
    parts.append(create_box(size=(0.1, 1.0, 0.3), center=(-1.95, 0, 0.5), color='black'))

    # 12. Spoiler/Ornamen Atap (piramida untuk bentuk segitiga 3D)
    parts.append(create_pyramid(base_size=(0.5, 0.8), height=0.4, center=(1.5, 0, 1.0), color='darkred'))
    
    # 13. Spion Samping (kubus kecil)
    parts.append(create_box(size=(0.2, 0.1, 0.15), center=(-0.8, 0.85, 0.8), color='darkgray'))
    parts.append(create_box(size=(0.2, 0.1, 0.15), center=(-0.8, -0.85, 0.8), color='darkgray'))

    return parts

# Visualisasi Plotly
scene = build_car_advanced()
fig = go.Figure(data=scene)
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode='data'
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)
fig.show()