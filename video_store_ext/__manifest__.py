{
    'name': 'Tienda de video EXT',
    'summary': 'Módulo para alquiler de videos',
    'description': 'Módulo para alquiler de videos',
    'author': 'Freddy Portales - fportalesar@gmail.com',
    'website': 'http://www.colossusperu.com',
    'category': 'Tools',
    'version': '13.0.0.0.1',
    'depends': [
        'video_store',
    ],
    'data': [ # para cargar al sistema
        ## Archivo de seguridad
        # 'security/ir.model.access.csv',
        # # archivo
        # 'views/video_store_menu.xml',
        # 'views/pelicula_views.xml',
       # 'views/actor_views.xml',
       'views/pelicula_views.xml'
    ],
    'installable': True,
}