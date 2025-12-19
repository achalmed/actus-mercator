#!/usr/bin/env python3
"""
Script para insertar Google Tag Manager en las posiciones correctas
de todos los archivos HTML generados por Quarto.
"""

import os
import re
from pathlib import Path

# Códigos de GTM
GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MN9MT747');</script>
<!-- End Google Tag Manager -->
"""

GTM_BODY = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MN9MT747"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

def insert_gtm_in_html(file_path):
    """Inserta GTM en un archivo HTML en las posiciones correctas."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar si GTM ya está insertado (evitar duplicados)
    if 'GTM-MN9MT747' in content:
        print(f"  ✓ GTM ya existe en {file_path}")
        return False
    
    # Insertar en <head> (lo más arriba posible, justo después de <head>)
    content = re.sub(
        r'(<head[^>]*>)',
        r'\1\n' + GTM_HEAD,
        content,
        count=1
    )
    
    # Insertar en <body> (inmediatamente después de <body>)
    content = re.sub(
        r'(<body[^>]*>)',
        r'\1\n' + GTM_BODY,
        content,
        count=1
    )
    
    # Guardar el archivo modificado
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ GTM insertado en {file_path}")
    return True

def process_directory(directory):
    """Procesa todos los archivos HTML en un directorio."""
    site_dir = Path(directory)
    
    if not site_dir.exists():
        print(f"❌ El directorio {directory} no existe")
        return
    
    html_files = list(site_dir.rglob('*.html'))
    
    if not html_files:
        print(f"❌ No se encontraron archivos HTML en {directory}")
        return
    
    print(f"📁 Procesando {len(html_files)} archivos HTML...\n")
    
    modified_count = 0
    for html_file in html_files:
        if insert_gtm_in_html(html_file):
            modified_count += 1
    
    print(f"\n✅ Proceso completado: {modified_count} archivos modificados")

if __name__ == "__main__":
    # Directorio donde Quarto genera los archivos (_site por defecto)
    site_directory = "_site"
    
    print("=" * 60)
    print("Google Tag Manager - Instalador para Quarto")
    print("=" * 60 + "\n")
    
    process_directory(site_directory)
