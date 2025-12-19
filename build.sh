#!/bin/bash

# Script para renderizar Quarto e insertar GTM automáticamente

echo "🔨 Renderizando sitio con Quarto..."
quarto render

echo ""
echo "🏷️  Insertando Google Tag Manager..."
python3 insert-gtm.py

echo ""
echo "✅ ¡Proceso completado!"
echo "Puedes verificar los archivos en _site/"
