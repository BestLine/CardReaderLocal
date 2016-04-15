from tendo.singleton import SingleInstance
import tray_icon

me = SingleInstance() # защита от повторного запуска
tray_icon.start_icon()
