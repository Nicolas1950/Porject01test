{
    'name' : 'moduletest',
    'version' : '15.0.1', 
    'description' : 'Un module de test', 

    'depends' : [
        'base'
    ], 
    'data' : [
        'security/ir.model.access.csv',
        'views/auction.xml',
        'views/menu.xml', 
    ], 
    'installable' : True,
    'application' : True, 
    'auto_install' : True
}