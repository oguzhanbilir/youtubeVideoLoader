# YouTube Video İndirici

Modern ve kullanıcı dostu bir arayüze sahip YouTube video indirme uygulaması.

## Özellikler
- Kullanıcı dostu grafiksel arayüz (GUI)
- Farklı video kalitesi seçenekleri (720p, 480p, 360p, 240p, 144p)
- İndirme ilerleme çubuğu
- İndirme konumu seçme
- Hata yönetimi ve bilgilendirme mesajları

## Gereksinimler
- Python 3.x
- pytube
- tkinter (Python ile birlikte gelir)

## Kurulum
1. Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanım
1. Uygulamayı başlatın:
```bash
python downloader.py
```

2. YouTube video URL'sini yapıştırın
3. İstediğiniz video kalitesini seçin
4. İndirme konumunu seçin (varsayılan: Downloads klasörü)
5. "İndir" butonuna tıklayın

## Notlar
- İndirilen videolar MP4 formatında kaydedilir
- İndirme işlemi sırasında internet bağlantınızın kesilmemesi önemlidir
- Bazı videolar telif hakları nedeniyle indirilemeyebilir
