# -*- coding: utf-8 -*-
{
    'name': "My Tool Control",
    'summary': "Control de herramientas por usuarios",
    'description': "Aplicacion para el registro de herramientas en un taller comunitario. \n Registra las herramientas, sus marcas y categorias y controla quien la usa y a que hora.",
    'author': "Ismael Castiñeira Paz",
    'website': "https://www.osmeusproxectos.es",
    'category': 'Extra Tools',
    'version': '12.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/tool.xml',
        'views/tool_categ.xml',
        'views/tool_brand.xml',
        'views/tool_provider.xml'
    ],
}
