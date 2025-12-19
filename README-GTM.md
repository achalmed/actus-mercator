# Instalación de Google Tag Manager en Quarto

Este repositorio incluye scripts para insertar Google Tag Manager (GTM) correctamente en todas las páginas de tu sitio Quarto.

## 🚀 Instalación Rápida

### Paso 1: Copiar archivos al proyecto

Copia estos archivos en la raíz de tu proyecto `actus-mercator`:

```
actus-mercator/
├── insert-gtm.py    ← Script Python
├── build.sh         ← Script de construcción automatizado
└── _quarto.yml      ← Tu configuración actual (sin cambios necesarios)
```

### Paso 2: Dar permisos de ejecución al script

```bash
chmod +x build.sh
chmod +x insert-gtm.py
```

### Paso 3: Construir tu sitio

En lugar de usar `quarto render`, ahora usa:

```bash
./build.sh
```

Este script hace dos cosas automáticamente:
1. Ejecuta `quarto render` para generar tu sitio
2. Ejecuta `insert-gtm.py` para insertar GTM en las posiciones correctas

## 📁 ¿Qué hace el script?

El script `insert-gtm.py`:
- Busca todos los archivos `.html` en `_site/`
- Inserta el código de GTM **justo después** de `<head>` (lo más arriba posible)
- Inserta el noscript **inmediatamente después** de `<body>`
- Evita duplicados si ya existe GTM en el archivo

## 🔄 Workflow de desarrollo

### Desarrollo local:
```bash
./build.sh           # Construir con GTM
quarto preview       # Previsualizar (opcional)
```

### Para publicar en Netlify:

Opción A - Usar el script en Netlify (Recomendado):
1. Asegúrate de que `insert-gtm.py` y `build.sh` estén en tu repo
2. En Netlify, cambia el comando de build a: `./build.sh`
3. Mantén el directorio de publicación como: `_site`

Opción B - Construir localmente:
```bash
./build.sh
git add _site/
git commit -m "Build con GTM"
git push
```

## ✅ Verificar instalación

Después de desplegar:

1. Ve a Google Tag Manager
2. Haz clic en **"Preview"** en la esquina superior derecha
3. Ingresa tu URL: `https://actus-mercator.netlify.app/`
4. Si se conecta y muestra "Connected", ¡está funcionando! ✨

También puedes verificar en el navegador:
- Abre tu sitio
- Presiona F12 (DevTools)
- Ve a la pestaña "Network"
- Busca `gtm.js` - debería aparecer cargándose
- Ve a "Console" - no debería haber errores de GTM

## 🛠️ Solución de problemas

### El script no se ejecuta:
```bash
# Verificar que Python 3 esté instalado
python3 --version

# Dar permisos
chmod +x insert-gtm.py build.sh
```

### GTM no se conecta en Preview:
1. Verifica que el código esté en el HTML generado (abre `_site/index.html`)
2. Busca `GTM-MN9MT747` - debería aparecer 2 veces
3. Verifica que esté justo después de `<head>` y `<body>`

### Para ejecutar manualmente:
```bash
quarto render
python3 insert-gtm.py
```

## 🔄 Actualizar el ID de GTM

Si necesitas cambiar el ID de GTM, edita estas líneas en `insert-gtm.py`:

```python
# Busca y reemplaza GTM-MN9MT747 por tu nuevo ID
GTM_HEAD = """...'GTM-TU-NUEVO-ID')...</script>"""
GTM_BODY = """...id=GTM-TU-NUEVO-ID"..."""
```

## 📝 Notas importantes

- **No modifiques** los archivos en `_site/` manualmente - se regeneran cada vez
- El script es **idempotente**: puedes ejecutarlo múltiples veces sin crear duplicados
- Si ya tienes GTM insertado manualmente, el script lo detectará y no duplicará el código

## 🎯 Ventajas de este método

✅ GTM se inserta en la posición óptima (lo más arriba posible)
✅ Funciona en todas las páginas automáticamente
✅ Compatible con el sistema de build de Netlify
✅ No requiere modificar el core de Quarto
✅ Evita duplicados automáticamente

---

¿Problemas? Revisa el output del script - te mostrará qué archivos modificó.
