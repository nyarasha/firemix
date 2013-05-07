from PySide import QtGui, QtCore

from ui.ui_firemix import Ui_FireMixMain


class FireMixGUI(QtGui.QMainWindow, Ui_FireMixMain):

    def __init__(self, parent=None, mixer=None):
        super(FireMixGUI, self).__init__(parent)
        self._mixer = mixer
        self.setupUi(self)

        # Buttons
        self.btn_blackout.clicked.connect(self.on_btn_blackout)
        self.btn_runfreeze.clicked.connect(self.on_btn_runfreeze)
        self.btn_playpause.clicked.connect(self.on_btn_playpause)
        self.btn_next_preset.clicked.connect(self.on_btn_next_preset)
        self.btn_prev_preset.clicked.connect(self.on_btn_prev_preset)

        # File menu
        self.action_file_load_scene.triggered.connect(self.on_file_load_scene)
        self.action_file_reload_presets.triggered.connect(self.on_file_reload_presets)
        self.action_file_quit.triggered.connect(self.close)

        # Preset list
        self.lst_presets.itemDoubleClicked.connect(self.on_preset_double_clicked)

        self.update_preset_list()
        self._mixer.set_preset_changed_callback(self.on_mixer_preset_changed)

    def closeEvent(self, event):
        self._mixer.stop()
        event.accept()

    def on_btn_blackout(self):
        pass

    def on_btn_playpause(self):
        if self._mixer.is_paused():
            self._mixer.pause(False)
            self.btn_playpause.setText("Pause")
        else:
            self._mixer.pause()
            self.btn_playpause.setText("Play")

    def on_btn_runfreeze(self):
        if self._mixer.is_frozen():
            self._mixer.freeze(False)
            self.btn_runfreeze.setText("Freeze")
        else:
            self._mixer.freeze()
            self.btn_runfreeze.setText("Unfreeze")

    def on_btn_next_preset(self):
        self._mixer.next()

    def on_btn_prev_preset(self):
        self._mixer.prev()

    def update_preset_list(self):
        self.lst_presets.clear()
        presets = self._mixer.get_preset_playlist()
        current = self._mixer.get_active_preset()
        for preset in presets:
            item = QtGui.QListWidgetItem(preset.__class__.__name__)

            if preset == current:
                item.setBackground(QtGui.QColor(100, 255, 200))
            self.lst_presets.addItem(item)

    def on_mixer_preset_changed(self, new_preset):
        self.update_preset_list()

    def on_file_load_scene(self):
        pass

    def on_file_reload_presets(self):
        pass

    def on_preset_double_clicked(self, preset_item):
        self._mixer.set_active_preset_by_name(preset_item.text())
