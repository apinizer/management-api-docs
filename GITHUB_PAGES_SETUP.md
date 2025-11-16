# GitHub Pages Ayarları - Adım Adım Kılavuz

## ⚠️ ÖNEMLİ: Bu adımları mutlaka yapın!

Site hala eski görünüyorsa, GitHub Pages ayarlarını kontrol etmeniz gerekiyor.

## Adım 1: GitHub Repository Ayarları

1. **GitHub repository'nize gidin:**
   - https://github.com/apinizer/management-api-docs

2. **Settings** sekmesine tıklayın (sağ üstte, repository adının yanında)

3. Sol menüden **Pages** seçeneğine tıklayın

4. **Source** bölümünde:
   - ❌ **"Deploy from a branch"** seçiliyse → **"GitHub Actions"** seçeneğine değiştirin
   - ✅ **"GitHub Actions"** seçili olmalı

5. **Save** butonuna tıklayın

## Adım 2: GitHub Actions Workflow'unu Kontrol Edin

1. **Actions** sekmesine gidin

2. Sol menüden **ci** workflow'unu seçin

3. En son çalışmayı kontrol edin:
   - ✅ **Yeşil tik**: Başarılı (birkaç dakika bekleyin)
   - 🟡 **Sarı daire**: Çalışıyor (bekleyin)
   - ❌ **Kırmızı X**: Hata var (hata mesajını kontrol edin)

4. Eğer workflow çalışmamışsa:
   - **"Run workflow"** butonuna tıklayın
   - **"Run workflow"** butonuna tekrar tıklayın

## Adım 3: Manuel Deployment (Alternatif)

Eğer GitHub Actions çalışmıyorsa, manuel olarak deploy edebilirsiniz:

### Yerel Bilgisayarınızda:

```bash
# 1. Bağımlılıkları yükleyin
python3 -m pip install --user -r requirements.txt

# 2. Siteyi deploy edin
python3 -m mkdocs gh-deploy --force
```

### Veya deploy script'ini kullanın:

```bash
./deploy.sh
```

## Adım 4: Siteyi Kontrol Edin

1. Birkaç dakika bekleyin (GitHub Pages güncellemesi zaman alabilir)

2. Tarayıcı cache'ini temizleyin:
   - **Chrome/Edge**: Ctrl+Shift+R (Windows) veya Cmd+Shift+R (Mac)
   - **Firefox**: Ctrl+F5 (Windows) veya Cmd+Shift+R (Mac)
   - Veya gizli modda açın

3. Siteyi kontrol edin:
   - https://apinizer.github.io/management-api-docs/
   - Sol tarafta menü görünmeli
   - Üstte arama kutusu olmalı
   - Modern bir tema görünmeli

## Sorun Giderme

### Site hala eski görünüyor
- ✅ GitHub Pages ayarlarında "GitHub Actions" seçili mi?
- ✅ GitHub Actions workflow'u başarılı mı?
- ✅ Tarayıcı cache'ini temizlediniz mi?
- ✅ Birkaç dakika beklediniz mi?

### GitHub Actions çalışmıyor
- Repository Settings → Actions → General
- "Workflow permissions" bölümünde "Read and write permissions" seçili olmalı
- "Allow GitHub Actions to create and approve pull requests" seçeneği işaretli olmalı

### 404 Hatası
- GitHub Actions workflow'unun başarılı bir şekilde tamamlandığını kontrol edin
- `gh-pages` branch'inin oluşturulduğunu kontrol edin

## Beklenen Sonuç

MkDocs Material teması uygulandığında şunları görmelisiniz:

- ✅ Sol tarafta sürekli görünen navigasyon menüsü
- ✅ Üst kısımda arama kutusu
- ✅ Sağ üstte dark/light mode toggle butonu
- ✅ Modern, profesyonel görünüm
- ✅ Responsive tasarım (mobil uyumlu)
- ✅ Kod bloklarında syntax highlighting
- ✅ Kod bloklarında kopyalama butonu

## Yardım

Eğer hala sorun yaşıyorsanız:
1. GitHub Actions log'larını kontrol edin
2. Hata mesajlarını okuyun
3. Manuel deployment deneyin

