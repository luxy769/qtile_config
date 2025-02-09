from libqtile import widget
import subprocess

class CmusWidget(widget.TextBox):
    def __init__(self, **config):
        super().__init__(**config)
        self.add_callbacks({
            'Button1': self.next_track,  # Левая кнопка мыши для следующего трека
        })
        self.update_cmus()  # Инициализация виджета
        self.timeout_add(1, self.update_cmus)  # Обновление каждые 1 секунду

    def next_track(self):
        subprocess.run(["cmus-remote", "-n"])  # Команда для переключения на следующий трек
        self.update_cmus()  # Обновить информацию о текущем треке

    def update_cmus(self):
        try:
            # Получаем текущий трек
            current_track = subprocess.check_output(["cmus-remote", "-Q"]).decode('utf-8')
            # Извлекаем название трека
            for line in current_track.splitlines():
                if line.startswith("tag title"):
                    title = line.split(" ", 2)[2]
                    self.text = f"🎵 {title}"  # Отображаем название трека
                    break
        except Exception as e:
            self.text = "cmus не запущен"  # Если cmus не запущен

# В вашем конфигурационном файле Qtile добавьте виджет
screens = [
    Screen(
        top=bar.Bar(
            [
                CmusWidget(),
                # Другие виджеты...
            ],
            24,
        ),
    ),
]
