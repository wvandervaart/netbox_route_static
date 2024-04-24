from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

static = PluginMenuItem(
    link='plugins:netbox_route_static:staticroute_list',
    link_text='Static Route',
    permissions=['netbox_route_static.view_staticroute'],
    buttons=(
        PluginMenuButton('plugins:netbox_route_static:staticroute_add', 'Add', 'mdi mdi-plus', ButtonColorChoices.GREEN),
        PluginMenuButton(
            'plugins:netbox_route_static:staticroute_import',
            'Import',
            'mdi mdi-upload',
            ButtonColorChoices.CYAN
        ),
    )
)

menu = PluginMenu(
    label='Netbox Routing',
    groups=(
        ('Static Routing', (static,)),
    ),
    icon_class='mdi mdi-router'
)
