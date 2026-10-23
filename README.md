# Demostración de GitHub Actions (CI/CD)

Proyecto de ejemplo para la exposición de la Sesión 12 – Desarrollo de Sistemas de Información (Instituto Khipu).

Contiene tres funciones en Python (`calculos.py`), sus pruebas con pytest (`test_calculos.py`) y un workflow
(`.github/workflows/ci.yml`) que, en cada push a `main` o pull request:

1. descarga el código,
2. instala Python 3.10, 3.11 y 3.12 (matriz de versiones),
3. revisa el estilo con flake8,
4. ejecuta las pruebas con pytest,
5. genera `dist/app.zip` y lo guarda como artefacto descargable.

## Pasos de la demostración

1. Crear un repositorio nuevo en GitHub (por ejemplo `demo-github-actions`) y subir todos estos archivos.
2. Abrir la pestaña **Actions**: el workflow **CI** se ejecuta solo tras el push.
3. Entrar a la ejecución y mostrar los jobs (uno por versión de Python), los pasos y los logs.
4. Al final de la ejecución, en **Artifacts**, descargar el paquete generado.
5. Hacer fallar el pipeline a propósito: en `calculos.py` cambiar `return a + b` por `return a - b`, hacer commit y ver el job en rojo con el test `test_suma_dos_numeros` fallando.
6. Corregir el cambio, hacer commit y mostrar que el pipeline vuelve a verde.
7. (Opcional) Abrir un Pull Request desde otra rama para mostrar los checks automáticos antes del merge.

## Probar localmente (sin GitHub)

```bash
pip install -r requirements.txt
flake8 . --max-line-length=100
pytest -v
```
