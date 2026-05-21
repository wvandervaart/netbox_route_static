from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu

static = PluginMenuItem(
    link='plugins:netbox_route_static:staticroute_list',
    link_text='Static Routes',
    permissions=['netbox_route_static.view_staticroute'],
    buttons=(
        PluginMenuButton(
            link='plugins:netbox_route_static:staticroute_add',
            title='Add',
            icon_class=COL_ADD,
            permissions=['netbox_route_static.add_staticroute'],
        ),
        PluginMenuButton(
            link='plugins:netbox_route_static:staticroute_bulk_import',
            title='Import',
            icon_class=COL_IMPORT,
            permissions=['netbox_route_static.import_staticroute'],
        ),
    ),
)

menu = PluginMenu(
    label='Netbox Routing',
    groups=(
        ('Static Routing', (static,)),
    ),
    icon_class='mdi mdi-router'
)
