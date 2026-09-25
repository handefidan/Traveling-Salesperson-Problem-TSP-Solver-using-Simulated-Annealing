import math
import random
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- AYARLAR ---
DOSYA_ADI = 'coordinates.csv'  # Dosya adınız
ZAMAN_SINIRI = 4000              # Saniye cinsinden çalışma süresi
BASLANGIC_SICAKLIK = 5000.0    # Başlangıç sıcaklığı
SOGUTMA_ORANI = 0.9999999        # Soğutma hızı

def read_data(filename):
    """Dosyayı okur; ID'leri ve koordinatları döndürür."""
    try:
        # Boşluk veya tab ile ayrılmış veriyi okumayı dene
        df = pd.read_csv(filename, delim_whitespace=True, header=None, names=['ID', 'X', 'Y'])
        # Eğer sadece tek sütun okuduysa veya hata varsa virgül dene
        if len(df.columns) < 3:
             df = pd.read_csv(filename, header=None, names=['ID', 'X', 'Y'])
    except:
        # Alternatif okuma
        df = pd.read_csv(filename, header=None, names=['ID', 'X', 'Y'])
        
    # Hem ID'leri hem Koordinatları döndür
    return df['ID'].values, df[['X', 'Y']].values

def calculate_distance_matrix(coords):
    """Tüm noktalar arası Öklid mesafesini hesaplar."""
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        # Vektörize öklid hesabı
        dists = np.sqrt(np.sum((coords - coords[i])**2, axis=1))
        dist_matrix[i] = dists
    return dist_matrix

def total_distance(tour, dist_matrix):
    """Bir turun toplam mesafesini hesaplar."""
    d = 0
    n = len(tour)
    for i in range(n):
        d += dist_matrix[tour[i]][tour[(i + 1) % n]]
    return d

def nearest_neighbor_init(dist_matrix, n):
    """Güçlü bir başlangıç için En Yakın Komşu algoritması."""
    start_node = random.randint(0, n - 1)
    tour = [start_node]
    unvisited = set(range(n))
    unvisited.remove(start_node)
    current = start_node
    while unvisited:
        # En yakın şehri bul
        nearest = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    return tour

def simulated_annealing(coords, time_limit=60):
    n = len(coords)
    dist_matrix = calculate_distance_matrix(coords)
    
    # 1. Başlangıç Çözümü (Greedy)
    print("Başlangıç çözümü oluşturuluyor (Nearest Neighbor)...")
    current_tour = nearest_neighbor_init(dist_matrix, n)
    current_dist = total_distance(current_tour, dist_matrix)
    
    best_tour = list(current_tour)
    best_dist = current_dist
    
    print(f"Başlangıç Mesafesi: {best_dist:.2f}")
    
    # 2. Simulated Annealing Döngüsü
    temp = BASLANGIC_SICAKLIK
    start_time = time.time()
    iter_count = 0
    
    print("Optimizasyon başladı...")
    while True:
        iter_count += 1
        
        # Süre kontrolü (Her 5000 adımda bir)
        if iter_count % 5000 == 0:
            if time.time() - start_time > time_limit:
                print("Süre doldu.")
                break
        
        # 2-Opt Hareketi
        a = random.randint(0, n - 2)
        b = random.randint(a + 1, n - 1)
        
        node_a = current_tour[a]
        node_a_next = current_tour[a+1]
        node_b = current_tour[b]
        node_b_next = current_tour[(b + 1) % n]
        
        # Hızlı Delta (Değişim) Hesabı
        removed = dist_matrix[node_a][node_a_next] + dist_matrix[node_b][node_b_next]
        added = dist_matrix[node_a][node_b] + dist_matrix[node_a_next][node_b_next]
        delta = added - removed
        
        # Metropolis Kriteri
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_tour[a+1:b+1] = reversed(current_tour[a+1:b+1])
            current_dist += delta
            
            if current_dist < best_dist:
                best_dist = current_dist
                best_tour = list(current_tour)
                print(f"Yeni En İyi: {best_dist:.2f} (Iter: {iter_count})")
        
        # Soğutma
        temp *= SOGUTMA_ORANI
        if temp < 0.001:
            print("Sıcaklık minimuma ulaştı.")
            break
            
    return best_tour, best_dist

# --- ANA PROGRAM ---
if __name__ == "__main__":
    # ID'leri ve koordinatları al
    ids, coords = read_data(DOSYA_ADI)
    
    if ids is not None:
        print(f"{len(coords)} nokta okundu.")
        
        best_route_indices, min_val = simulated_annealing(coords, time_limit=ZAMAN_SINIRI)
        
        # İndeksleri gerçek ID'lere dönüştür
        final_route_ids = [ids[i] for i in best_route_indices]
        
        print(f"\n" + "="*40)
        print(f"SONUÇ")
        print(f"Minimum Mesafe: {min_val:.4f}")
        print(f"="*40)
        
        print("\nZiyaret Sırasına Göre Şehir ID'leri:")
        # ID'leri yan yana yazdır
        print(*final_route_ids)
        
        # Görselleştirme
        plt.figure(figsize=(10, 6))
        tour_indices = best_route_indices + [best_route_indices[0]]
        tour_coords = coords[tour_indices]
        plt.plot(tour_coords[:, 0], tour_coords[:, 1], 'o-', markersize=3, linewidth=1, color='green')
        plt.title(f"TSP Sonuc (Mesafe: {min_val:.2f})")
        plt.show()
    else:
        print("Veri okunamadı, lütfen dosya adını kontrol edin.")