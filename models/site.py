from odoo import models, fields

class Site(models.Model):
  """
  Clase que implementa una sede
  """

  _name = 'hairdresser.site'
  _description = 'Define cada una de las sedes de la cadena'

  code = fields.Char()
  address = fields.Char()
  city = fields.Char() 