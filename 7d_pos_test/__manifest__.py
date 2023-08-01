# -*- coding: utf-8 -*-
{
    'name': "7d_test_module",
    'summary': """PoS Customization App""",
    'description': """Long description of module's purpose""",
    'author': "Eng. Ahmet Alhendi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',
    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # POS
        'views/custom_assets.xml',
        # 'views/partner.xml',
        'views/pos_payment_method.xml',

        'views/pos_config.xml',
    ],

    'qweb': [
        'static/src/css/index.css',
        'static/src/xml/Popups/CreditAmountPopup.xml',

        'static/src/xml/Screens/ClientListScreen/ClientLine.xml',
        'static/src/xml/Screens/ClientListScreen/ClientListScreen.xml',

        'static/src/xml/Screens/InvoiceListScreen/InvoiceLine.xml',
        'static/src/xml/Screens/InvoiceListScreen/InvoiceListScreen.xml',

        'static/src/xml/Screens/ProductScreen/ControlButtons/CreditButton.xml',
        'static/src/xml/Screens/ProductScreen/ControlButtons/UnpaidInvoiceButton.xml',

        'static/src/xml/Screens/ReceiptScreen/WhatsappReceiptScreen.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            '7d_pos_test/static/src/css/style.css',
            'witforms_pos/static/src/css/theme.css',
            'witforms_pos/static/src/css/bootstrap.min.css',
            'witforms_pos/static/src/css/theme.css',
            '7d_pos_test/static/src/css/responsive.css.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
