# GitHub Pages Deployment Guide

## Otomatik Deployment (GitHub Actions)

GitHub Actions workflow otomatik olarak her push'ta siteyi deploy eder. Kontrol etmek için:

1. GitHub repository'nize gidin: https://github.com/apinizer/management-api-docs
2. **Actions** sekmesine tıklayın
3. En son workflow'un başarılı olup olmadığını kontrol edin
4. Eğer hata varsa, hata mesajını kontrol edin

## GitHub Pages Ayarları

1. Repository Settings → Pages bölümüne gidin
2. **Source** kısmında **"GitHub Actions"** seçeneğini seçin
3. Eğer "Deploy from a branch" seçiliyse, bunu değiştirin

## Manuel Deployment (Gerekirse)

Eğer GitHub Actions çalışmıyorsa, manuel olarak deploy edebilirsiniz:

```bash
# MkDocs'u yükleyin
pip3 install -r requirements.txt

# Siteyi deploy edin
mkdocs gh-deploy --force
```

## Sorun Giderme

### Site hala eski görünüyor
- GitHub Actions workflow'unun tamamlanmasını bekleyin (birkaç dakika sürebilir)
- Tarayıcı cache'ini temizleyin (Ctrl+Shift+R veya Cmd+Shift+R)
- GitHub Pages ayarlarında "GitHub Actions" seçili olduğundan emin olun

### 404 Hatası
- GitHub Actions workflow'unun başarılı bir şekilde tamamlandığını kontrol edin
- Site URL'inin doğru olduğunu kontrol edin: https://apinizer.github.io/management-api-docs/

### Build Hatası
- GitHub Actions sekmesinde hata mesajlarını kontrol edin
- `mkdocs.yml` dosyasının syntax'ının doğru olduğundan emin olun

