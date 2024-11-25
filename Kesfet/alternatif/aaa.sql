-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               9.1.0 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping data for table search.search: ~38 rows (approximately)
INSERT INTO `search` (`id`, `site_name`, `headline`, `timestamp`, `search_url`, `date_only`, `time_only`) VALUES
	(1, 'NTV Haber', 'Aç karnına 1 kaşık zeytinyağı! İçerseniz ne olur? Etkisini çok az kişi biliyor', '2024-11-11 08:11:11', 'https://www.ntv.com.tr/galeri/saglik/ac-karnina-1-kasik-zeytinyagi-icerseniz-ne-olur-etkisini-cok-az-kisi-biliyor,QRK30eA6OEaGJWt01f1iMg#:~:text=Her%20sabah%20a%C3%A7%20karn%C4%B1na%201,v%C3%BCcut%20sa%C4%9Fl%C4%B1%C4%9F%C4%B1n%C4%B1z%C4%B1n%20iyile%C5%9Ftirilmesinde%20olduk%C3%A7a%20etkilidir.', '2024-11-14', '15:07:07'),
	(2, 'Milliyet', '"Erkekler maçları izleyebilmek için benimle sevgili olmak istiyor"', '2024-11-11 08:21:51', 'https://www.milliyet.com.tr/dunya/erkekler-maclari-izleyebilmek-icin-benimle-sevgili-olmak-istiyor-7229845', '2024-11-14', '15:07:07'),
	(3, 'Milliyet', '"Bir gün hariç her gün sağanak: Meteoroloji\'den uyarı geldi"', '2024-11-11 08:21:51', 'https://www.sozcu.com.tr/akp-bahceli-nin-aciklamalarinin-sonuna-kadar-arkasindayiz-p98016', '2024-11-14', '15:07:07'),
	(4, 'Milliyet', '"Bakan Memişoğlu\'ndan ‘aile hekimi\' ve ‘reçete’ açıklaması"', '2024-11-11 08:21:51', 'https://www.milliyet.com.tr/gundem/bakan-memisoglundan-aile-hekimi-ve-recete-aciklamasi-7229870', '2024-11-14', '15:07:07'),
	(5, 'Sözcü', '"Cem Yılmaz duyurdu"', '2024-11-11 08:21:51', 'https://www.sozcu.com.tr/cem-yilmaz-duyurdu-p103190#:~:text=Komedyen%20Cem%20Y%C4%B1lmaz%2C%208%20Temmuz,duyulmam%C4%B1%C5%9F%20bir%20%C5%9Fark%C4%B1s%C4%B1n%C4%B1n%20yay%C4%B1nlanaca%C4%9F%C4%B1n%C4%B1%20a%C3%A7%C4%B1klad%C4%B1.&text=Oyuncu%20ve%20Mazhar%2DFuat%2D%C3%96zkan,tedavi%20g%C3%B6rd%C3%BC%C4%9F%C3%BC%20hastanede%20hayat%C4%B1n%C4%B1%20kaybetmi%C5%9Fti.', '2024-11-14', '15:07:07'),
	(6, 'Sözcü', '"GSM operatörü fiyatlarına zam yaptı: İşte yeni liste"', '2024-11-11 08:21:51', 'https://www.sozcu.com.tr/gsm-operatoru-fiyatlarina-zam-yapti-iste-yeni-liste-p103138', '2024-11-14', '15:07:07'),
	(7, 'Hürriyet', '"Sultangazi\'de duygulandıran anma töreni"', '2024-11-11 08:21:51', 'https://www.hurriyet.com.tr/gundem/sultangazide-duygulandiran-anma-toreni-42587660', '2024-11-14', '15:07:07'),
	(8, 'Hürriyet', '"Marmaray\'da güvenlik görevlisi kendisine saldıran kişiyi bacağından vurdu"', '2024-11-11 08:21:51', 'https://www.hurriyet.com.tr/gundem/marmarayda-guvenlik-gorevlisi-kendisine-saldiran-kisiyi-bacagindan-vurdu-42588262#:~:text=Al%C4%B1nan%20bilgiye%20g%C3%B6re%2C%20Bostanc%C4%B1%20%C4%B0stasyonu,arbedede%20zanl%C4%B1%20silahla%20baca%C4%9F%C4%B1ndan%20vuruldu.', '2024-11-14', '15:07:07'),
	(10, 'NTV Haber', 'Akciğeri 7 günde tertemiz yapıyor: 1 bardak iltihabı, balgamı kurutuyor', '2024-11-11 09:07:51', 'https://www.ntv.com.tr/galeri/saglik/akcigeri-7-gunde-tertemiz-yapiyor-1-bardagi-iltihabi-balgami-kurutuyor,c2JwQc6hn0-iKiO_x4U8dA', '2024-11-14', '15:07:07'),
	(11, 'Sözcü', '1 Aralık itibariyla başlayacak: Otomobilinde bulunmayan sürücüye 4 bin 69 TL ceza kesilecek', '2024-11-11 09:07:51', 'https://www.sozcu.com.tr/1-aralik-itibariyla-baslayacak-otomobilinde-bulunmayan-surucuye-2-bin-568-tl-ceza-kesilecek-p103182#:~:text=Zorunlu%20oldu%C4%9Fu%20halde%20ara%C3%A7lar%C4%B1na%20k%C4%B1%C5%9F,5%20bin%20856%20liraya%20y%C3%BCkselecek.', '2024-11-14', '15:07:07'),
	(12, 'Sözcü', 'Yeni salgın durdurulamıyor: O bölgelere giriş-çıkış kapatıldı', '2024-11-11 09:07:51', 'https://www.sozcu.com.tr/yeni-salgin-durdurulamiyor-o-bolgelere-giris-cikis-kapatildi-p103253', '2024-11-14', '15:07:07'),
	(13, 'Hürriyet', '9. YARGI PAKETİ SON DAKİKA HABERİ: Meclis\'te kabul edildi! 9. Yargı Paketi maddeleri ve içeriği neler, genel af ve ceza indirimi var mı?', '2024-11-11 09:07:51', 'https://www.hurriyet.com.tr/bilgi/galeri-9-yargi-paketi-son-dakika-4-4-ceza-indirimi-olacak-mi-9-yargi-paketi-resmi-gazetede-yayinlandi-mi-42584156', '2024-11-14', '15:07:07'),
	(14, 'Milliyet', '1 Aralık itibariyle başlayacak: Otomobilinde bulunmayan sürücüye 4 bin 69 TL ceza kesilecek', '2024-11-11 13:05:53', 'https://www.sozcu.com.tr/1-aralik-itibariyla-baslayacak-otomobilinde-bulunmayan-surucuye-2-bin-568-tl-ceza-kesilecek-p103182', '2024-11-14', '15:07:07'),
	(15, 'Sözcü', 'Müzede Atatürk’ün fotoğrafını gören Erdoğan, hemen Murat Bardakçı\'ya döndü', '2024-11-11 13:05:53', 'https://www.sozcu.com.tr/muzede-ataturk-un-fotografini-goren-erdogan-hemen-murat-bardakci-ya-dondu-p103431', '2024-11-14', '15:07:07'),
	(16, 'NTV Haber', 'Faylarda stres birikti: 6 il için deprem uyarısı geldi', '2024-11-11 13:05:53', 'https://www.ntv.com.tr/galeri/turkiye/faylarda-stres-birikti-6-il-icin-deprem-uyarisi-geldi,67R91jl2TkS4HaZRkWT6kA', '2024-11-14', '15:07:07'),
	(17, 'Sözcü', 'Memur ve emekli maaşı yüzde kaç zamlanacak? En düşük maaş ne kadar olacak?', '2024-11-11 13:05:53', 'https://www.sozcu.com.tr/memur-ve-emekli-maasi-yuzde-kac-zamlanacak-en-dusuk-maas-ne-kadar-olacak-p103404#:~:text=Yap%C4%B1lacak%20y%C3%BCzde%2012\'lik%20zam,bin%20697%20TL\'ye%20y%C3%BCkselecek.', '2024-11-14', '15:07:07'),
	(18, 'NTV Haber', 'Meğer doğal şeker ilacıymış: Yüksek kan şekerini anında düşürüyor', '2024-11-11 13:05:53', 'https://www.ntv.com.tr/galeri/saglik/meger-dogal-seker-ilaciymis-yuksek-kan-sekerini-aninda-dusuruyor,CmTGRMb0REWohZx3GBT9jw', '2024-11-14', '15:07:07'),
	(19, 'Sözcü', 'Türkiye\'nin en zengin müteahhidiydi: Hükümet deviren iş insanı böyle battı', '2024-11-11 13:05:53', 'https://www.sozcu.com.tr/turkiye-nin-en-zengin-muteahhidiydi-hukumet-deviren-is-insani-boyle-batti-p103134', '2024-11-14', '15:07:07'),
	(20, 'Sözcü', 'Ahmet Özer\'e yeni soruşturma', '2024-11-11 13:05:53', 'https://www.sozcu.com.tr/ahmet-ozer-e-yeni-sorusturma-p103510', '2024-11-14', '15:07:07'),
	(21, 'Sözcü', 'Sosyal medya Erdoğan\'ın bu mesajını tartışıyor', '2024-11-11 13:05:53', 'https://www.sozcu.com.tr/sosyal-medya-erdogan-in-bu-mesajini-tartisiyor-p103471', '2024-11-14', '15:07:07'),
	(22, 'Hürriyet', 'Barbaros Şansal gözaltına alındı', '2024-11-11 13:05:53', 'https://www.hurriyet.com.tr/gundem/barbaros-sansal-gozaltina-alindi-42588744', '2024-11-14', '15:07:07'),
	(23, 'Habertürk', 'İSKİ İstanbul su kesintileri 11 Kasım Pazartesi: İstanbul\'da sular ne zaman, saat kaçta gelecek?', '2024-11-11 13:05:53', 'https://www.haberturk.com/iski-istanbul-su-kesintileri-11-kasim-pazartesi-istanbul-da-sular-ne-zaman-saat-kacta-gelecek-3736662', '2024-11-14', '15:07:07'),
	(24, 'Sözcü', 'ATM‘den para çekenler için yeni dönem', '2024-11-13 06:30:21', 'https://www.sozcu.com.tr/1-ocak-tan-itibaren-gecerli-olacak-atm-den-para-cekenler-icin-yeni-donem-p103706', '2024-11-14', '15:07:07'),
	(25, 'Sözcü', 'Türkiye\'de hasadına başlandı, köylülerin geçim kaynağı! Olumsuzluğun simgesi olarak biliniyor', '2024-11-13 06:30:21', 'https://www.sozcu.com.tr/turkiye-de-hasadina-baslandi-koylulerin-gecim-kaynagi-olumsuzlugun-simgesi-olarak-biliniyor-p103417', '2024-11-14', '15:07:07'),
	(26, 'Sabah', 'Son dakika: Bahis batağı böyle işliyor! Para aktarımında kilit rol Aracılar: Sabah kumar sistemini araştırdı', '2024-11-13 06:30:21', 'https://www.sabah.com.tr/trend/galeri/yasam/son-dakika-bahis-batagi-boyle-isliyor-para-aktariminda-kilit-rol-aracilar-sabah-kumar-sistemini-arastirdi', '2024-11-14', '15:07:07'),
	(27, 'Sözcü', 'Jet Fadil\'in ‘Caprice ¢ Gold\'u rekor fiyata satışa ¢ıkarıldı', '2024-11-14 08:08:07', 'https://www.sozcu.com.tr/jet-fadil-in-caprice-gold-u-rekor-fiyata-satisa-cikarildi-p104131#:~:text=Bayrampa%C5%9Fa\'da%20Fad%C4%B1l%20Akg%C3%BCnd%C3%BCz%20taraf%C4%B1ndan,i%C3%A7in%20350%20milyon%20dolar%20isteniyor.', '2024-11-14', '15:07:07'),
	(28, 'Sözcü', '1 Ocak\'tan itibaren geçerli olacak: ATM\'den para çekenler için yeni dönem', '2024-11-14 08:08:07', 'https://www.sozcu.com.tr/1-ocak-tan-itibaren-gecerli-olacak-atm-den-para-cekenler-icin-yeni-donem-p103706', '2024-11-14', '15:07:07'),
	(29, 'NTV Haber', 'İstanbul Boğazı gemi trafiğine kapatıldı', '2024-11-14 08:08:07', 'https://www.ntv.com.tr/turkiye/istanbul-bogazi-gemi-trafigine-kapatildi,fRSWuEDc5EWDaDC75EFaAQ', '2024-11-14', '15:07:07'),
	(30, 'NTV Haber', 'Fay hattı kent merkezinin altından geçiyor! Prof. Dr. Seyitoğlu: Herkes Marmara’yı konuşuyor ama aynı risk b...', '2024-11-14 08:08:07', 'https://www.cumhuriyet.com.tr/turkiye/bu-kez-istanbul-degil-prof-dr-seyitoglundan-o-il-icin-deprem-2268155', '2024-11-14', '15:07:07'),
	(31, 'NTV Haber', 'SOK\'dan Mansur Yavaş\'a yanıt', '2024-11-14 10:37:00', 'https://www.ntv.com.tr/turkiye/son-dakika-haberiankara-buyuksehir-belediyesinin-konserleri-icin-inceleme-baslatildi,eQ00tikPqkSsmkVgGManEw', '2024-11-14', '15:07:07'),
	(32, 'Sözcü', 'CHP\'li belediyelere soruşturma: Özgür Özel açıklama yapacak', '2024-11-14 10:37:00', 'https://www.sozcu.com.tr/chp-li-belediyelere-sorusturma-ozgur-ozel-aciklama-yapacak-p104422', '2024-11-14', '15:07:07'),
	(33, 'Milliyet', 'Altında şelale düşüşü', '2024-11-14 11:01:26', 'https://bigpara.hurriyet.com.tr/altin/haber/altinda-selale-dususu_ID1603243/', '2024-11-14', '15:07:07'),
	(34, 'Sözcü', 'Satışa çıkarıldı', '2024-11-14 11:01:26', 'https://www.sozcu.com.tr/jet-fadil-in-caprice-gold-u-rekor-fiyata-satisa-cikarildi-p104131', '2024-11-14', '15:07:07'),
	(35, 'Milliyet', 'Altında şelale düşüşü', '2024-11-14 11:04:25', 'https://bigpara.hurriyet.com.tr/altin/haber/altinda-selale-dususu_ID1603243/', '2024-11-14', '15:07:07'),
	(36, 'Sözcü', 'Satışa çıkarıldı', '2024-11-14 11:04:25', 'https://www.sozcu.com.tr/jet-fadil-in-caprice-gold-u-rekor-fiyata-satisa-cikarildi-p104131', '2024-11-14', '15:07:07'),
	(37, 'Sözcü', 'Beş yıllık evlilikte üçüncü bebek geldi... Ünlü çift mutluluktan uçuyor', '2024-11-14 11:04:25', 'https://www.hurriyet.com.tr/kelebek/magazin/bes-yil-icinde-ucuncu-cocuk-dogdu-unlu-cift-mutluluktan-ucuyor-42589417', '2024-11-14', '15:07:07'),
	(38, 'NTV Haber', 'Elon Musk\'tan tarihi yatırım: Bir haftada 546 kat kazandı', '2024-11-14 11:04:25', 'https://www.ntv.com.tr/galeri/ntvpara/elon-musktan-tarihi-yatirim-bir-haftada-546-kat-kazandi,-_w-06E1ekmzXYOsaZ_rwA#:~:text=Elon%20Musk\'%C4%B1n%20se%C3%A7im%20yat%C4%B1r%C4%B1m%C4%B1,bir%20haftada%20546%20kat%20oldu.', '2024-11-14', '15:07:07'),
	(39, '- Site: Keşfet', 'Başlık: Patates filizlenmesini önleyen meyve! Aralarına 2 tane koyunca aylarca taş gibi kalıyor', '2024-11-14 11:05:13', 'https://www.milliyet.com.tr/galeri/patates-filizlenmesini-onleyen-meyve-aralarina-2-tane-koyunca-aylarca-tas-gibi-kaliyor-7232702#:~:text=PATATES%20F%C4%B0L%C4%B0ZLENMES%C4%B0N%C4%B0%20%C3%96NLEYEN%20MEYVE%3A%20ELMA', '2024-11-14', '15:07:07');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
