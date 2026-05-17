import os
import json
import random
import requests
from datetime import datetime
import re

# Configurazione
POSTS_DIR = "_posts"
IMG_DIR = "assets/images"
TOPICS = [
    "Come creare armi in schiuma EVA",
    "Guida alla stampa 3D per il cosplay",
    "Sartoria cosplay: scegliere le stoffe giuste",
    "Fotografia cosplay: pose e illuminazione",
    "Come prepararsi per una gara cosplay",
    "Lenti a contatto colorate: guida sicura",
    "Creare effetti speciali con il lattice",
    "Come trasportare cosplay ingombranti in fiera",
    "Gestire il budget per un progetto cosplay",
    "Cosplay di coppia o di gruppo: consigli",
    "Come realizzare ali realistiche",
    "Lavorare con il Worbla trasparente",
    "Makeup per cosplay maschili (Crossplay)",
    "Come realizzare armature in pelle finta",
    "Elettronica nel cosplay: LED e motori base"
]

def generate_content(topic):
    """Genera il contenuto dell'articolo usando un'API gratuita o un template avanzato"""
    print(f"Generazione contenuto per: {topic}")
    
    # In un ambiente di produzione reale, qui si chiamerebbe l'API di OpenAI o simili.
    # Poiché questo script deve girare gratis su GitHub Actions, usiamo un generatore
    # basato su template molto avanzati o chiamate ad API pubbliche gratuite.
    
    # Per questo esempio, simuliamo una generazione di alta qualità
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    titolo = f"Guida Pratica: {topic}"
    
    contenuto = f"""
Il mondo del cosplay è fatto di creatività, ingegno e tanta passione. Oggi affrontiamo un argomento che molti di voi ci hanno richiesto: **{topic.lower()}**.

Che tu stia preparando il tuo primo costume o che tu sia un veterano delle fiere, padroneggiare queste tecniche ti permetterà di fare un salto di qualità incredibile.

## L'Importanza della Preparazione

Prima di tuffarci nei dettagli tecnici, è fondamentale capire che la fase di progettazione è importante quanto l'esecuzione stessa. Molti cosplayer si lanciano subito nella costruzione, per poi accorgersi a metà dell'opera di aver commesso errori strutturali.

Prenditi il tempo per:
1. Raccogliere reference (immagini del personaggio da ogni angolazione)
2. Fare un inventario dei materiali necessari
3. Stabilire un budget realistico
4. Creare una timeline dei lavori

## Tecniche Avanzate e Consigli Pratici

Quando si tratta di {topic.lower()}, il segreto sta nei dettagli. I materiali moderni ci offrono possibilità che fino a dieci anni fa erano impensabili.

*   **Sperimenta sempre:** Non aver paura di testare nuove tecniche su piccoli scarti di materiale prima di applicarle al pezzo finale.
*   **La sicurezza prima di tutto:** Usa sempre i DPI (Dispositivi di Protezione Individuale) come maschere per i vapori, occhiali protettivi e guanti quando usi colle, vernici o strumenti da taglio.
*   **Pazienza:** I migliori risultati si ottengono lavorando a strati, rispettando i tempi di asciugatura e non affrettando i passaggi.

## Risoluzione dei Problemi Comuni

È normale incontrare ostacoli durante la lavorazione. Se qualcosa va storto, non buttare via tutto! Spesso un errore può essere trasformato in un dettaglio "battle damage" (danno da battaglia) che aggiunge realismo al costume.

La community cosplay è meravigliosa proprio perché è sempre pronta ad aiutarsi. Se ti blocchi, cerca tutorial specifici o chiedi consiglio nei gruppi dedicati.

## Conclusione

Speriamo che questa guida su {topic.lower()} ti abbia fornito gli strumenti e l'ispirazione necessari per il tuo prossimo progetto. Ricorda che il cosplay non deve essere perfetto, deve essere divertente!

Continua a seguire CosplayItalia per nuovi articoli ogni giorno. E se questo articolo ti è stato utile, considera di supportarci con una piccola donazione tramite il pulsante PayPal qui sotto!
"""
    
    # Genera un prompt per l'immagine
    prompt_img = f"Professional cosplay photography, highly detailed, cinematic lighting, 8k resolution, related to {topic.replace(' ', '_')}"
    
    return titolo, contenuto, prompt_img

def generate_image_with_pollinations(prompt, slug):
    """Genera un'immagine usando l'API gratuita di Pollinations.ai"""
    print(f"Generazione immagine per prompt: {prompt}")
    
    # Pollinations.ai è un'API gratuita che non richiede chiavi
    encoded_prompt = requests.utils.quote(prompt)
    seed = random.randint(1, 1000000)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1200&height=800&nologo=true&seed={seed}"
    
    try:
        response = requests.get(url)
        if response.status_status_code == 200:
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = f"{date_str}-{slug}.jpg"
            filepath = os.path.join(IMG_DIR, filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            print(f"Immagine salvata: {filepath}")
            return f"/assets/images/{filename}"
    except Exception as e:
        print(f"Errore durante il download dell'immagine: {e}")
    
    # Fallback all'URL diretto se il download fallisce
    return url

def create_post():
    """Crea un nuovo post nel blog"""
    # Assicurati che le directory esistano
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMG_DIR, exist_ok=True)
    
    # Scegli un argomento casuale
    topic = random.choice(TOPICS)
    
    # Genera contenuto
    titolo, contenuto, prompt_img = generate_content(topic)
    
    # Crea slug e data
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H:%M:%S")
    
    # Pulisci il titolo per lo slug
    slug = re.sub(r'[^\w\s-]', '', titolo.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    
    # Genera immagine
    img_path = generate_image_with_pollinations(prompt_img, slug)
    
    # Crea il file Markdown
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)
    
    post_content = f"""---
layout: post
title: "{titolo}"
date: {date_str} {time_str} +0200
categories: tutorial
tags: [cosplay, guide, fai-da-te]
image: {img_path}
author: "CosplayItalia"
---

{contenuto}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(post_content)
        
    print(f"Post creato con successo: {filepath}")

if __name__ == "__main__":
    print("Avvio generazione post automatico...")
    create_post()
    print("Generazione completata.")
