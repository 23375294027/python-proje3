# python-proje3
Proje 3: IMDb Film Veri Seti Analizi
Proje Raporu: IMDb Film Veri Seti Analizi
🎯 Projenin Amacı
Bu analizin temel hedefi, bir film veri setindeki ham verileri temizleyip sayısal formata dönüştürdükten sonra, filmlerin aldığı puanların dağılımını, oy sayısı ile puan arasındaki ilişkiyi ve veri setindeki en popüler film türlerini keşfetmektir.

1. Aşama: Veri Yükleme ve Hazırlık (Data Wrangling)
Bu aşama, veri setindeki farklı formatlardaki verilerin analize uygun standart sayısal formatlara dönüştürülmesini ve hatalı verilerin temizlenmesini içerir.

Veri Yükleme: movies_initial.csv dosyası Pandas kütüphanesi ile belleğe yüklendi.

Sayısal Dönüşümler: Filmlerin Yıl (year) ve Süre (runtime) sütunları, güvenilir sayısal verilere çevrildi.

Oy Sayısı (imdbVotes) Temizliği: Oy sayısı sütununda bulunan "1,234,567" formatındaki virgüller (,) kaldırıldı ve ardından bu değerler matematiksel işlemler için sayısal (numerik) değere dönüştürüldü.

Eksik Veri Temizliği: Analizin temelini oluşturan Puan (rating) ve Oy Sayısı (imdbVotes) sütunlarından herhangi birinde eksik değere sahip olan tüm satırlar veri setinden silinerek analizin güvenilirliği sağlandı.

Tür Verilerinin Ayrıştırılması: Bir filmde birden fazla tür ("Aksiyon, Macera") bulunabileceği için, her bir tür ayrı ayrı satırlara bölünerek, her türün ayrı ayrı sayılabilmesi için temiz bir liste oluşturuldu.

2. Aşama: Keşifsel Analiz ve Özet Bulgular
Veri temizliğinin ardından, veri setinin genel yapısını gösteren hızlı bir özet sunuldu.

En Popüler Türler: Veri setindeki film türlerinin görülme sıklığı hesaplanarak, en çok tekrar eden ilk 5 film türü listelendi.

3. Aşama: Veri Görselleştirme
Veri setindeki dağılımlar ve ilişkiler, Matplotlib kullanılarak üç farklı grafik türüyle görselleştirildi.

Grafik 1: Puan Dağılımı (Histogram)
Amaç: Veri setindeki filmlerin aldığı puanların (rating) hangi aralıklarda yoğunlaştığını göstermek. Bu grafik, filmlerin çoğunluğunun ortalama, yüksek veya düşük puan bandında toplandığını ortaya koyar.

<img width="1280" height="620" alt="yzt3" src="https://github.com/user-attachments/assets/379a983f-3443-4603-b9b1-2dd9066cae2d" />


Grafik 2: Oy Sayısı vs. Puan (Dağılım Grafiği - Scatter Plot)
Amaç: Bir filmin aldığı oy sayısı (imdbVotes) ile elde ettiği puan (rating) arasında bir ilişki olup olmadığını incelemek. Yatay eksen, çok geniş bir aralığı temsil edebilmek için logaritmik olarak ölçeklenmiştir. Grafikteki her nokta bir filmi temsil eder.


<img width="640" height="480" alt="res1" src="https://github.com/user-attachments/assets/917f7549-5468-4727-b9b9-64578adc506c" />

Grafik 3: En Sık Görülen Türler (Sütun Grafiği - Bar Chart)
Amaç: Veri setinde en çok temsil edilen film türlerinin görülme sayısını karşılaştırmak. Bu grafik, veri setinin hangi türlere odaklandığını gösterir.

<img width="640" height="480" alt="res2" src="https://github.com/user-attachments/assets/61c14bab-8d30-4ecc-b22c-099a5a9b68c8" />


4. Aşama: Analiz Sonucu
Tüm veri hazırlık ve görselleştirme adımları başarılı bir şekilde tamamlanmıştır. Oluşturulan grafikler, filmlerin puan dağılımı, popüler türleri ve oy sayısı ile puan arasındaki korelasyonu (ilişkiyi) görsel olarak onaylamaya hazır hale getirilmiştir. Analiz, veri setinin daha derinlemesine istatistiksel sorgulamalara hazır olduğunu göstermektedir.
