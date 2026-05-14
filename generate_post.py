import os
import requests
import random
from datetime import datetime

def generate_content_free():
    # Poiché non abbiamo API key a pagamento, usiamo una lista di argomenti predefiniti 
    # e chiediamo a un servizio di generazione testo gratuito o usiamo un template avanzato.
    # Per rendere lo script autonomo e gratuito al 100%, useremo un sistema di "prompt" 
    # verso un'API pubblica gratuita se disponibile, altrimenti useremo un generatore locale.
    
    topics = [
        "L'arte del Worbla nelle armature",
        "Come scegliere la parrucca perfetta",
        "Makeup teatrale per il cosplay",
        "Creare armi realistiche con la schiuma EVA",
        "Storia del cosplay: dalle origini ad oggi",
        "Come prepararsi per la prima fiera",
        "Fotografia cosplay: consigli per pose epiche",
        "Sartoria avanzata per costumi complessi",
        "Lenti a contatto colorate: guida alla sicurezza",
        "Creare effetti speciali con il lattice"
    ]
    
    topic = random.choice(topics)
    
    # Usiamo un'API di testo gratuita (es. DuckDuckGo AI o simili tramite wrapper se possibile, 
    # o semplicemente generiamo un contenuto strutturato di alta qualità basato sul tema)
    # Per affidabilità totale senza chiavi, useremo Pollinations anche per il testo se supportato, 
    # o un servizio di mock-up di alta qualità.
    
    titolo = f"Guida Completa: {topic}"
    
    # Generiamo un testo lungo simulando un'analisi approfondita (per ora)
    # In un ambiente reale, potremmo usare Hugging Face (gratis con account)
    contenuto = f"""
Il mondo del cosplay è in continua evoluzione e oggi esploreremo un tema fondamentale: **{topic}**.

**Introduzione**
Il cosplay non è solo indossare un costume, è l'arte di dare vita a un personaggio. Che tu sia un principiante o un veterano, padroneggiare le tecniche di {topic.lower()} è essenziale per elevare la qualità dei tuoi lavori.

**Tecniche e Materiali**
Per ottenere risultati professionali, è necessario conoscere i materiali giusti. Spesso sottovalutiamo l'importanza della preparazione, ma è proprio lì che si vede la differenza tra un costume amatoriale e uno da competizione. 

*   **Pianificazione:** Prima di iniziare, studia ogni dettaglio del personaggio.
*   **Esecuzione:** Prenditi il tuo tempo. La fretta è la nemica della precisione.
*   **Rifinitura:** I dettagli fanno la differenza. Non aver paura di sperimentare con colori e texture.

**Consigli Pratici**
Molti cosplayer si scoraggiano davanti alle prime difficoltà. Il segreto è la costanza. Se stai lavorando su {topic.lower()}, ricorda di proteggere sempre la tua salute (usa maschere se usi colle o vernici!) e di divertirti durante il processo.

**Conclusione**
Speriamo che questa guida su {topic.lower()} ti sia stata utile. Il cosplay è una community meravigliosa fatta di condivisione e creatività. Continua a creare e a stupire!
"""
    
    prompt_img = f"High quality cosplay photo of a character related to {topic}, cinematic lighting, 8k, highly detailed, professional photography"
    
    return titolo, contenuto, prompt_img

def generate_image_free(prompt):
    # Usiamo Pollinations AI che è completamente gratuito e non richiede chiavi
    encoded_prompt = requests.utils.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed={random.randint(1, 100000)}"
    return image_url

def save_post(titolo, contenuto, image_url):
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = titolo.lower().replace(" ", "-").replace(":", "").replace("'", "-")[:50]
    filename = f"_posts/{date_str}-{slug}.md"
    
    # Scarichiamo l'immagine
    try:
        img_data = requests.get(image_url).content
        img_dir = "assets/images"
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        img_path = f"{img_dir}/{date_str}-{slug}.jpg"
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
        img_relative_path = f"/{img_path}"
    except:
        img_relative_path = image_url # Fallback all'URL diretto
    
    post_template = f"""---
layout: post
title: "{titolo}"
date: {date_str}
categories: cosplay
image: {img_relative_path}
---

![{titolo}]({img_relative_path})

{contenuto}
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(post_template)
    
    print(f"Post generato con successo: {filename}")

if __name__ == "__main__":
    print("Inizio generazione gratuita...")
    titolo, contenuto, prompt_img = generate_content_free()
    print(f"Argomento: {titolo}")
    img_url = generate_image_free(prompt_img)
    save_post(titolo, contenuto, img_url)
