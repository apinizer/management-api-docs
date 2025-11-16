# GitHub Pages Basit Ayarları

MkDocs ve GitHub Actions kaldırıldı. Şimdi GitHub Pages'i basit markdown render olarak kullanabilirsiniz.

## GitHub Pages Ayarları

1. **GitHub repository'nize gidin:**
   - https://github.com/apinizer/management-api-docs

2. **Settings** → **Pages** bölümüne gidin

3. **Source** kısmında:
   - **"Deploy from a branch"** seçin
   - **Branch**: `main` (veya `master`)
   - **Folder**: `/ (root)` veya `/docs` (eğer docs klasörü kullanıyorsanız)
   - **Save** butonuna tıklayın

4. Birkaç dakika bekleyin

5. Site hazır olacak: https://apinizer.github.io/management-api-docs/

## Notlar

- GitHub Pages basit markdown render kullanır
- Sol menü için Jekyll theme kullanabilirsiniz (opsiyonel)
- Veya başka bir dokümantasyon aracı kullanabilirsiniz

## Jekyll Theme Kullanmak İsterseniz

Eğer daha güzel bir görünüm istiyorsanız, `_config.yml` dosyası ekleyebilirsiniz:

```yaml
theme: jekyll-theme-minimal
```

Veya başka bir Jekyll theme kullanabilirsiniz.

