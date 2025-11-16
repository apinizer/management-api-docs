# Manuel Deployment Rehberi

GitHub Actions çalışmıyorsa veya workflow görünmüyorsa, manuel olarak deploy edebilirsiniz.

## Yöntem 1: Yerel Bilgisayardan Deploy

### Adım 1: Python ve pip'in yüklü olduğundan emin olun

```bash
python3 --version
pip3 --version
```

### Adım 2: Bağımlılıkları yükleyin

```bash
python3 -m pip install --user -r requirements.txt
```

### Adım 3: Siteyi deploy edin

```bash
python3 -m mkdocs gh-deploy --force
```

Bu komut:
- Siteyi build eder
- `gh-pages` branch'ini oluşturur/günceller
- GitHub'a push eder

### Adım 4: GitHub Pages Ayarlarını Kontrol Edin

1. GitHub repository → Settings → Pages
2. **Source** kısmında **"Deploy from a branch"** seçin
3. **Branch** kısmında:
   - Branch: `gh-pages`
   - Folder: `/ (root)`
4. **Save** butonuna tıklayın

## Yöntem 2: Deploy Script Kullanın

```bash
chmod +x deploy.sh
./deploy.sh
```

## Yöntem 3: GitHub Actions'ı Tetikleme

Eğer Actions sekmesinde workflow görünmüyorsa:

1. **Code** sekmesine gidin
2. `.github/workflows/ci.yml` dosyasını açın
3. Dosyanın doğru olduğundan emin olun
4. Bir değişiklik yapıp commit edin (workflow'u tetiklemek için)

Veya:

1. **Actions** sekmesine gidin
2. Sol üstte **"New workflow"** butonuna tıklayın
3. **"Set up a workflow yourself"** seçeneğini seçin
4. İçeriği silin ve `.github/workflows/ci.yml` dosyasının içeriğini yapıştırın
5. **"Start commit"** butonuna tıklayın

## Sorun Giderme

### "mkdocs: command not found" hatası
```bash
python3 -m pip install --user -r requirements.txt
python3 -m mkdocs --version
```

### "Permission denied" hatası
```bash
python3 -m pip install --user -r requirements.txt
```

### GitHub authentication hatası
- Personal Access Token oluşturun: Settings → Developer settings → Personal access tokens
- Token'ı kullanın: `git config --global credential.helper store`

## Beklenen Sonuç

Deployment başarılı olduğunda:
- `gh-pages` branch'i oluşturulur
- Birkaç dakika içinde site güncellenir
- https://apinizer.github.io/management-api-docs/ adresinde yeni tema görünür

