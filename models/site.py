from odoo import models, fields

from datetime import date

class Site(models.Model):
  """
  Clase que implementa una sede
  """

  _name = 'hairdresser.site'
  _description = 'Define cada una de las sedes de la cadena'

  code = fields.Char(string='Código', help ='Código de la sede', required = True, index = True)
  address = fields.Char(string='Dirección', required = True)
  city = fields.Char(string='Ciudad', required = True, default = 'Valencia') 

  capacity = fields.Integer(required = True)
  area = fields.Float(string='Superficie', help ='Superficie en m2', required = True)
  active = fields.Boolean(string='Activa')
  comments = fields.Text(string='Comentarios')

  def calcula_fecha(self):
    return date.today()
  
  opening_date = fields.Date(string='Fecha inauguración', default = date.today())

  