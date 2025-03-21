# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.ElgatoKeyLight.SetButton import SetButton
from .actions.ElgatoKeyLight.ToggleButton import ToggleButton

from .actions.ElgatoKeyLight.Dial import Dial

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.set_light_action_holder = ActionHolder(
            plugin_base = self,
            action_base = SetButton,
            action_id = "com_memclash_elgatokeylight::SetButton", # Change this to your own plugin id
            action_name = "Set Light Properties",
        )

        self.toggle_light_action_holder = ActionHolder(
            plugin_base = self,
            action_base = ToggleButton,
            action_id = "com_memclash_elgatokeylight::ToggleButton", # Change this to your own plugin id
            action_name = "Toggle Light",
        )

        self.dial_action_holder = ActionHolder(
            plugin_base = self,
            action_base = Dial,
            action_id = "com_memclash_elgatokeylight::Dial", # Change this to your own plugin id
            action_name = "Dial Brightness Temperature",
        )

        self.add_action_holder(self.set_light_action_holder)
        self.add_action_holder(self.toggle_light_action_holder)
        self.add_action_holder(self.dial_action_holder)


        # Register plugin
        self.register(
            plugin_name = "Elgato Key Light",
            github_repo = "https://github.com/StreamController/PluginTemplate",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
