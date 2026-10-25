# 🎞️ Inventory Animator

**Inventory Animator** — приложение для Windows, которое превращает обычное видео в анимированный ресурс-пак для инвентаря **Minecraft Java Edition**.

[![Windows](https://img.shields.io/badge/Platform-Windows-0078D4?logo=windows&logoColor=white)](https://github.com/M4ksR/Inventory-Animator/releases/tag/v0.1.0)
[![Release](https://img.shields.io/github/v/release/M4ksR/Inventory-Animator)](https://github.com/M4ksR/Inventory-Animator/releases)
[![Python checks](https://github.com/M4ksR/Inventory-Animator/actions/workflows/ci.yml/badge.svg)](https://github.com/M4ksR/Inventory-Animator/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**[⬇️ Скачать Inventory Animator v0.1.0](https://github.com/M4ksR/Inventory-Animator/releases/tag/v0.1.0)**

## 📸 Скриншот

![Интерфейс Inventory Animator](docs/screenshot.png)

## ✨ Возможности

- 🎬 Загрузка видео в форматах **MP4, AVI, MOV и MKV**.
- 🎨 Настройка **непрозрачности** изображения от 0 до 100%.
- 👁️ Простой предпросмотр непрозрачности на демонстрационной картинке с шаблоном инвентаря.
- 🎞️ Ограничение количества кадров: **500 по умолчанию**, до **2500** в расширенном режиме с предупреждением.
- 📊 Отображение количества обработанных кадров и прогресса генерации.
- 📦 Автоматическая сборка структуры ресурс-пака с анимированной текстурой инвентаря.
- 📁 Сохранение результата в `output` и кнопка быстрого открытия этой папки.

## 📥 Установка на Windows

1. Откройте [страницу релиза v0.1.0](https://github.com/M4ksR/Inventory-Animator/releases/tag/v0.1.0).
2. Скачайте файл **`InventoryAnimator.exe`** из раздела **Assets**.
3. Переместите `.exe` в папку, в которой хотите хранить результаты.
4. Запустите приложение.

**Python устанавливать не требуется.** Для сохранения ресурс-паков запускайте приложение из папки, доступной для записи (например, из собственной папки в «Документах»).

## 🚀 Как пользоваться

1. Введите название ресурс-пака.
2. Нажмите **«Выбрать файл»** и укажите видео.
3. Отрегулируйте **непрозрачность** и при необходимости измените **лимит кадров**.
4. Нажмите **«Создать Ресурс-Пак»**.
5. Дождитесь завершения обработки.
6. Нажмите **«Открыть папку»**, чтобы найти созданный ресурс-пак.

Результат сохраняется в папку `output/<название_ресурс-пака>/` рядом с исполняемым файлом. Готовую папку ресурс-пака можно поместить в `.minecraft/resourcepacks` и включить в настройках игры.

## 🎮 Совместимость и ограничения

- **Minecraft Java Edition** с поддержкой анимированных текстур **OptiFine**.
- Итоговая анимация может воспроизводиться с другой скоростью, чем исходное видео: длительность кадров определяется настройками анимации Minecraft.
- Рекомендуемый лимит — **500 кадров**. Очень длинные анимации требуют больше времени и памяти, а Minecraft может не загрузить слишком большой ресурс-пак.
- Совместимость метаданных ресурс-пака (`pack_format`) зависит от версии Minecraft.
- Приложение создаёт анимацию изображения, а не переносит в Minecraft звуковую дорожку видео.

## 🛠️ Запуск из исходного кода

Требуется Python 3.13 и Windows.

```powershell
git clone https://github.com/M4ksR/Inventory-Animator.git
cd Inventory-Animator
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Основные технологии: **Python, Flet, OpenCV, NumPy, Pillow и PyPNG**.

## 💬 Обратная связь

Сообщить об ошибке или предложить улучшение можно в [GitHub Issues](https://github.com/M4ksR/Inventory-Animator/issues).

**Автор:** [M4ksR](https://github.com/M4ksR)  
**Лицензия:** [MIT](LICENSE)
