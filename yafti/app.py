"""
Copyright 2023 Marco Ceppi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from gi.repository import Adw

from yafti.screen.window import Window
from yafti.parser import Config


class Yafti(Adw.Application):
    def __init__(self, cfg: Config = None):
        super().__init__(application_id="it.ublue.Yafti")
        self.config = cfg

    def do_activate(self):
        win = Window(application=self)
        win.present()
