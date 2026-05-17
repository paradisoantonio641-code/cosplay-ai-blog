# CosplayItalia AI Blog

Il primo blog cosplay italiano con articoli giornalieri automatici e foto generate dall'intelligenza artificiale.

## Caratteristiche

- **Articoli giornalieri automatici** tramite GitHub Actions
- **Foto cosplay AI** generate con Pollinations.ai
- **Donazioni PayPal** integrate in ogni articolo
- **Design responsive** ottimizzato per mobile e desktop
- **SEO ottimizzato** con meta tag, sitemap e feed RSS
- **Cookie banner** GDPR compliant
- **Privacy Policy** e pagine legali incluse

## Struttura del Progetto

```
cosplay-ai-blog/
├── _layouts/           # Template HTML
│   ├── default.html    # Layout principale
│   └── post.html       # Layout articoli
├── _posts/             # Articoli del blog
├── assets/
│   ├── css/main.css    # Stile principale
│   ├── js/main.js      # JavaScript
│   └── images/         # Foto AI
├── scripts/
│   └── generate_post.py # Script generazione automatica
├── .github/workflows/
│   ├── deploy.yml      # Deploy su GitHub Pages
│   └── daily_post.yml  # Generazione articolo giornaliero
└── _config.yml         # Configurazione Jekyll
```



## Come Configurare Google Analytics

1. Crea un account su [Google Analytics](https://analytics.google.com/)
2. Ottieni il tuo Measurement ID (es. `G-XXXXXXXXXX`)
3. Modifica `_config.yml` e inserisci il tuo ID nel campo `google_analytics`

## Donazioni PayPal

Le donazioni sono configurate per l'email `antoniored908@gmail.com`. Per modificarla, cerca e sostituisci questa email nei file `_layouts/default.html` e `_layouts/post.html`.

## Licenza

Contenuti generati con AI. Uso personale e commerciale consentito.
