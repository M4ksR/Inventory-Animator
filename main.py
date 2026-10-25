import flet as ft
import asyncio
import re

from pathlib import Path

from services.video_reader import get_video_metadata
from services.build_pipeline import create_resourcepack

def main(page: ft.Page):
    # параметры окна
    page.title = "Inventory Animator"
    page.window.width = 845
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.DARK

    # контейнер предпросмотра
    status_preview = ft.Text("Предпросмотр")
    preview = ft.Container(
        width=400,
        height=350,
        bgcolor="#263447",
        padding=20,
        border_radius=10,
        content=status_preview
    )

    # поле ввода для названия ресурс-пака
    resourcepack_name = ft.TextField(
        label="Название ресурспака",
        hint_text="created by github M4ksR"
    )

    # функция установки значения прозрачности рядом с ползунком
    def set_trans(e):
        trans_text.value = f"{e.control.value:.0f}%"

    # ползунок прозрачности и величина прозрачности
    slider = ft.Slider(
        min=0,
        max=100,
        value=100,
        divisions=100,
        label="{value}%",
        expand=True
    )
    slider.on_change = set_trans
    trans_text = ft.Text("100%")

    # выбор файла для раскадровки
    selected_video_path = None

    async def choose_video(e):
        nonlocal selected_video_path
        file = await file_picker.pick_files(allow_multiple=False,
                                            file_type=ft.FilePickerFileType.CUSTOM,
                                            allowed_extensions=["mp4",
                                                                "avi",
                                                                "mov",
                                                                "mkv"])
        if not file: return

        selected_video_name = file[0].name
        file_path = file[0].path

        try:
            metadata = await asyncio.to_thread(get_video_metadata, file_path)
            selected_video_path = file_path
            file_info.value = (f"Имя файла: {selected_video_name}\n"
                               f"Разрешение: {metadata['width']}x{metadata['height']}\n"
                               f"Длительность: {metadata['duration']} сек\n"
                               f"FPS: {metadata['fps']}\n"
                               f"Количество кадров: {metadata['frame_count']}")
        except ValueError as error:
            status_preview.value = f"Ошибка загрузки видео: {error}"

    file_picker = ft.FilePicker()
    file_info = ft.Text("Файл не выбран")

    # контейнер настроек
    settings = ft.Container(
        width=400,
        height=350,
        bgcolor="#263447",
        padding=20,
        border_radius=10,
        content=ft.Column(controls=[
            ft.Text("Настройки"),
            resourcepack_name,
            ft.Row(controls=[
                ft.Text("Непрозрачность"),
                slider,
                trans_text
            ]),
            ft.Row(controls=[
                ft.Text("Кадры"),
                ft.Button(
                    content="Выбрать файл",
                    on_click=choose_video,
                )
            ]),
            file_info
        ])
    )

    # добавление контейнеров
    page.add(ft.Row(controls=[preview,settings]))

    # кнопка сборки ресурс-пака
    async def on_build_click(e):
        if selected_video_path is None:
            return

        button.disabled = True

        status_preview.value = "Начинаем создание ресурспака"
        page.update()

        try:
            name = (resourcepack_name.value or "").strip()
            if not name or (re.search(r'[<>:"/\\|?*\x00-\x1f]', name) or name in (".", "..")
                            or name.endswith(".") or name.upper().split(".")[0] in
                            {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}):
                name = "github M4ksR"

            PROJECT_ROOT = Path(__file__).resolve().parent

            await asyncio.to_thread(create_resourcepack,
                                    selected_video_path,
                                    slider.value,
                                    PROJECT_ROOT / "output" / name)

            status_preview.value = "Ресурс-Пак собран"

        except (ValueError, OSError) as error:
            status_preview.value = f"Ошибка: {error}"

        finally:
            button.disabled = False
            page.update()

    button = ft.Button(width=815,
                       height=40,
                       content="Создать Ресурс-Пак",
                       on_click=on_build_click)
    page.add(button)

if __name__ == "__main__":
    ft.run(main)
