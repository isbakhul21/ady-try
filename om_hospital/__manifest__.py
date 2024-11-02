{
  'name': 'Hospital Management',
    'summary': '""module to handle Hospital And Doctor',
    'description': """Module to handle:
    - Space
    - PAtient
    - Attendees Staff
    """,
    'sequence': 1,
    'author':'isbakhul lail',
    'website':'www.omhospital.com',
    'category':'Hospital',
    'depends':['mail','product',"base"],
    'data':[
      # security
      'security/ir.model.access.csv',


      # views
      'views/menu.xml',
      'views/patient_view.xml',
      'views/female_patient_view.xml',
      'views/appointment_view.xml',
      'views/playground_space.xml',
      'views/res_users.xml',

      #static
      'static/src/xml/page_product.xml',



      # data
      'data/sequence_data.xml',

    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}