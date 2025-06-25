# 🚀 Apollo CI/CD Quest

Bienvenido/a a tu misión especial de CI/CD inspirada en el Programa Apollo. Tu tarea es construir correctamente el pipeline que permite ejecutar los pasos de una misión lunar… y al final, si lo logras, recibirás un **mensaje secreto enviado desde la Luna**.

---

## 🎯 Objetivo

- Comprender y editar un workflow de GitHub Actions.
- Verificar que una secuencia de pasos se cumpla correctamente en CI.
- Desplegar el resultado en `main` mediante un flujo de CD.
- Ejecutar y validar tests de Python.

---

## 🧩 El desafío

En este repositorio encontrarás un workflow CI (`apollo.yml`) con **los pasos de una misión lunar desordenados**.  
Tu misión es **ordenar los jobs en el orden correcto** agregando los campos `needs:` en el archivo YAML.

💡 Solo si los pasos están en el orden correcto se mostrará el **mensaje secreto**

## 🧠 Pasos para completar la misión

1. **Forkea** este repositorio en tu cuenta y clónalo localmente.
2. Crea una rama de trabajo, por ejemplo: `fix/apollo-sequence`
3. Instala las dependencias:
4. Abre el archivo .github/workflows/apollo.yml.
5. Ahí verás 4 jobs: launch, transposition_and_docking, lunar_orbit_insertion, splashdown.
6. Agrega los campos needs: en cada job para que se ejecuten en este orden:
7. Haz commit y push de tus cambios. Luego ve a la pestaña Actions en GitHub.
8. Si hiciste todo correctamente, en el job splashdown verás un mensaje como:
9. Abre un Pull Request para fusionar tu rama en main.
10. Al hacer merge en main, el workflow de CD se ejecutará y empaquetará el artefacto como apollo_artifact.zip.

---

## Orden de la mision

```bash
1. launch
2. transposition_and_docking
3. lunar_orbit_insertion
4. splashdown
```
