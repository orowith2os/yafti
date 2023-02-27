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

import yaml
from pydantic import BaseModel
from typing import Optional


class ActionConfig(BaseModel):
    pre: Optional[list[dict[str, str | dict]]]
    post: Optional[list[dict[str, str | dict]]]


class ScreenConfig(BaseModel):
    source: str
    values: Optional[dict]


class Config(BaseModel):
    title: str
    actions: Optional[ActionConfig]
    screens: Optional[dict[str, ScreenConfig]]  # Screens are parsed per plugin


def parse(config_file: str) -> Config:
    """Parse the YAML or JSON file passed and return a rendered Config object"""
    with open(config_file) as f:
        cfg = yaml.safe_load(f)
    return Config.parse_obj(cfg)
