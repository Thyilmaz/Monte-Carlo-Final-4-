import numpy as np
import time

# GEREKSİNİM: Rastgele sayı üreticisi öğrenci numarası ile beslenmelidir.
student_num = 20240082 # KENDİ NUMARANLA DEĞİŞTİR (Sonu 82)
np.random.seed(student_num)

# GEREKSİNİM: Y < 5 olduğu için n = 10^5
n = 10**5
k = 30 # Monte Carlo için sınır iterasyon sayısı

# Problem Tanımı: 1 ile 1000 arasında sayılardan oluşan n boyutlu dizi.
# Koşul: mod 7'ye göre 0 kalanı veren elemanı bulmak.
data = np.random.randint(1, 1001, n)

# Gerçek durumu analiz edelim (Teorik hesaplama için p değeri)
true_count = np.sum(data % 7 == 0)
p = true_count / n

print(f"--- TEORİK HESAPLAMALAR ---")
print(f"Veri setindeki 7'ye bölünen eleman oranı (p): {p:.4f}")
theoretical_error = (1 - p)**k
print(f"Teorik Hata Olasılığı P(error) = (1 - {p:.4f})^{k}: {theoretical_error:.6f}\n")

# Monte Carlo Algoritması
def monte_carlo_search(arr, k_iterations):
    for _ in range(k_iterations):
        # Rastgele indeks seçimi
        idx = np.random.randint(0, len(arr))
        if arr[idx] % 7 == 0:
            return True # Buldu (Kesin doğru sonuç)
    return False # Bulamadı (Hata yapma olasılığı var)

# Algoritmanın 100 kez çalıştırılması
errors = 0
times = []

for _ in range(100):
    start_time = time.perf_counter()
    result = monte_carlo_search(data, k)
    end_time = time.perf_counter()
    
    times.append(end_time - start_time)
    
    # Veri setinde aranan eleman varken (true_count > 0) algoritma False dönerse bu bir hatadır.
    if result == False and true_count > 0:
        errors += 1

exp_error_rate = errors / 100
mean_time = np.mean(times)
std_time = np.std(times)

print(f"--- DENEYSEL SONUÇLAR (100 Çalıştırma) ---")
print(f"Deneysel Hata Oranı: {exp_error_rate:.4f}")
print(f"Ortalama Çalışma Süresi: {mean_time:.8f} saniye")
print(f"Çalışma Süresi Standart Sapması: {std_time:.8f} saniye")