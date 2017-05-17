# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem



class CoreConfig(AppConfig):
    name = 'core'


class SuitConfig(DjangoSuitConfig):
    name = 'suit'
    verbose_name = 'Django Suit'
    # Menu and header layout - horizontal or vertical
    layout = 'vertical'

    menu_show_home = False

    # Set default list per page
    list_per_page = 20

    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = True

    # Define menu
    #: :type: list of suit.menu.ParentItem
    menu = (
        ParentItem('Sales', children=[
            ChildItem('Dashboard', url='/admin/dash/'),
            ChildItem(model='core.order'),


        ]),
    )