import click
import json
import os
from typing import Dict, List
import logging

class ConfigManager:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict:
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)

@click.group()
@click.option('--config', default='config.json', help='Configuration file path')
@click.pass_context
def cli(ctx, config):
    """시스템 관리를 위한 CLI 도구"""
    ctx.obj = ConfigManager(config)

@cli.command()
@click.argument('name')
@click.argument('value')
@click.pass_obj
def set_config(config_manager: ConfigManager, name: str, value: str):
    """설정 값을 저장합니다"""
    config_manager.config[name] = value
    config_manager.save_config()
    click.echo(f"설정 '{name}'이(가) '{value}'로 저장되었습니다.")

@cli.command()
@click.argument('name')
@click.pass_obj
def get_config(config_manager: ConfigManager, name: str):
    """설정 값을 조회합니다"""
    value = config_manager.config.get(name)
    if value is None:
        click.echo(f"설정 '{name}'을(를) 찾을 수 없습니다.")
    else:
        click.echo(f"{name}: {value}")

@cli.command()
@click.pass_obj
def list_config(config_manager: ConfigManager):
    """모든 설정을 조회합니다"""
    for name, value in config_manager.config.items():
        click.echo(f"{name}: {value}")

if __name__ == '__main__':
    cli()