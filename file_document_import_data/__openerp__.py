# -*- coding: utf-8 -*-
##############################################################################
#
#   account_statement_file_document for OpenERP
#   Copyright (C) 2016-TODAY Akretion <http://www.akretion.com>.
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'File Document Import Data',
    'version': '0.1',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """
        Allow to make a native odoo import from a file document.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['base_import', 'file_document'],
    'init_xml': [],
    'update_xml': [
        'file_document_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
