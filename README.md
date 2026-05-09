# Monte Carlo Yaklaşımı ile Olasılıksal Veri Analizi

Bu proje, büyük bir veri seti içerisindeki belirli bir koşulu sağlayan elemanların tespit edilmesinde **Monte Carlo** randomize algoritma yaklaşımının etkinliğini ve doğruluk payını deneysel olarak ispatlamak amacıyla geliştirilmiştir.

## 📋 Proje Parametreleri (Öğrenci No: 1240505082)

Ödev kriterlerine göre belirlenen özel çalışma parametreleri:

- **Algoritma Tipi:** Monte Carlo (Sınırlı iterasyonda olasılıksal sonuç)
- **Veri Hacmi ($n$):** 100,000 ($10^5$)
- **İterasyon Sayısı ($k$):** 30
- **Rastgelelik Kaynağı (Seed):** 1240505082
- **Hedef Koşul:** Rastgele üretilen dizide $mod(7) == 0$ olan elemanların tespiti.

## 🚀 Algoritma Mantığı

Monte Carlo algoritmaları, belirli bir zaman kısıtı altında (sabit $k$ iterasyonu) en iyi sonucu bulmaya çalışır. Las Vegas algoritmalarının aksine çalışma süresi garantidir ($O(k)$), ancak sonucun doğruluğu olasılıksaldır. 



### Matematiksel Hata Analizi
Bir elemanın hedef koşulu sağlama olasılığı $p$ ise, $k$ iterasyon sonunda hata yapma (hiçbir hedef elemanı bulamama) olasılığı şu formülle hesaplanır:
$$P(error) = (1 - p)^k$$

Bu projede $p \approx 0.142$ ve $k = 30$ için beklenen hata oranı **~%1.01**'dir.

