import os
import requests
from datetime import datetime
from openai import OpenAI

# Configurazione
# Per GitHub Actions, usiamo l'API standard di OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1"
)

def generate_content():
    # 1. Generazione del testo dell'articolo
    prompt_testo = """
    Scrivi un articolo approfondito e professionale sul mondo del cosplay in lingua italiana.
    L'articolo deve essere lungo circa 1200-1500 parole (circa una pagina e mezza).
    Scegli un tema specifico (es. tutorial su materiali, storia di un personaggio, recensione di una fiera, consigli per il makeup).
    Usa un tono entusiasta ma tecnico. Dividi in paragrafi con titoli in grassetto.
    Includi una breve introduzione e una conclusione.
    Restituisci il risultato in questo formato:
    TITOLO: [Titolo dell'articolo]
    CONTENUTO: [Testo dell'articolo]
    PROMPT_IMMAGINE: [Un prompt dettagliato in inglese per generare un'immagine fotorealistica relativa all'articolo]
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt_testo}]
    )
    
    full_text = response.choices[0].message.content
    
    # Parsing semplice
    lines = full_text.split('\n')
    titolo = ""
    contenuto = []
    prompt_img = ""
    
    current_section = ""
    for line in lines:
        if line.startswith("TITOLO:"):
            titolo = line.replace("TITOLO:", "").strip()
        elif line.startswith("PROMPT_IMMAGINE:"):
            prompt_img = line.replace("PROMPT_IMMAGINE:", "").strip()
            current_section = "PROMPT"
        elif line.startswith("CONTENUTO:"):
            current_section = "CONTENUTO"
        elif current_section == "CONTENUTO":
            contenuto.append(line)
            
    return titolo, "\n".join(contenuto), prompt_img

def generate_image(prompt):
    # 2. Generazione dell'immagine con DALL-E 3
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    image_url = response.data[0].url
    return image_url

def save_post(titolo, contenuto, image_url):
    # 3. Salvataggio del file Markdown
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = titolo.lower().replace(" ", "-").replace("'", "-").replace("?", "").replace("!", "")[:50]
    filename = f"_posts/{date_str}-{slug}.md"
    
    # Scarichiamo l'immagine localmente per GitHub Pages
    img_data = requests.get(image_url).content
    img_name = f"assets/images/{date_str}-{slug}.jpg"
    with open(img_name, 'wb') as handler:
        handler.write(img_data)
    
    post_template = f"""---
layout: post
title: "{titolo}"
date: {date_str}
categories: cosplay
image: /{img_name}
---

![{titolo}](/{img_name})

{contenuto}
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(post_template)
    
    print(f"Post generato con successo: {filename}")

if __name__ == "__main__":
    try:
        print("Inizio generazione contenuto...")
        titolo, contenuto, prompt_img = generate_content()
        print(f"Generato titolo: {titolo}")
        print("Generazione immagine...")
        image_url = generate_image(prompt_img)
        print("Salvataggio post...")
        save_post(titolo, contenuto, image_url)
    except Exception as e:
        print(f"Errore durante la generazione: {e}")
