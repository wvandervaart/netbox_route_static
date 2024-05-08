from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

static = PluginMenuItem(
    link='plugins:netbox_route_static:staticroute_list',
    link_text='Static Route',
    permissions=['netbox_route_static.view_staticroute'],
    buttons=(
        PluginMenuButton('plugins:netbox_route_static:staticroute_add', 'Add', 'mdi mdi-plus'),
        PluginMenuButton(
            'plugins:netbox_route_static:staticroute_import',
            'Import',
            'mdi mdi-upload'
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
