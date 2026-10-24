import flet as ft

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
        height=300,
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
        value=50,
        divisions=100,
        label="{value}%",
        expand=True
    )
    slider.on_change = set_trans
    trans_text = ft.Text("50%")

    # выбор файла для раскадровки
    selected_video_path = None

    async def choose_video(e):
        file = await file_picker.pick_files(allow_multiple=False,
                                            file_type=ft.FilePickerFileType.CUSTOM,
                                            allowed_extensions=["mp4",
                                                                "avi",
                                                                "mov",
                                                                "mkv"])
        if not file: return

        nonlocal selected_video_path
        selected_video_name = file[0].name
        selected_video_path = file[0].path

        file_info.value = f"Имя файла: {selected_video_name}"

    file_picker = ft.FilePicker()
    file_info = ft.Text("Файл не выбран")

    # контейнер настроек
    settings = ft.Container(
        width=400,
        height=300,
        bgcolor="#263447",
        padding=20,
        border_radius=10,
        content=ft.Column(controls=[
            ft.Text("Настройки"),
            resourcepack_name,
            ft.Row(controls=[
                ft.Text("Прозрачность"),
                slider,
                trans_text
            ]),
            ft.Row(controls=[
                ft.Text("Кадры"),
                file_info
            ]),
            ft.Button(
                content="Выбрать файл",
                on_click=choose_video,
            )
        ])
    )

    # добавление контейнеров
    page.add(ft.Row(controls=[preview,settings]))

    # кнопка сборки ресурс-пака
    def create_resourcepack(e): status_preview.value = "Начинаем создание ресурспака"

    button = ft.Button(width=815,
                       height=40,
                       content="Создать Ресурс-Пак",
                       on_click=create_resourcepack)
    page.add(button)

if __name__ == "__main__":
    ft.run(main)
