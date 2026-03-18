# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
block_cipher = None

added_files = [
    ('templates',  'templates'),
    ('static',     'static'),
    ('core',       'core'),
    ('blueprints', 'blueprints'),
]
added_files += collect_data_files('flask')
added_files += collect_data_files('jinja2')
added_files += collect_data_files('werkzeug')

hidden_imports = [
    'flask','flask.templating','flask.json','flask.json.provider',
    'jinja2','jinja2.ext','jinja2.loaders',
    'werkzeug','werkzeug.routing','werkzeug.security','werkzeug.serving',
    'click','itsdangerous','markupsafe',
    'blueprints.auth','blueprints.dashboard','blueprints.student_portal',
    'blueprints.students','blueprints.attendance','blueprints.examination',
    'blueprints.datesheet','blueprints.payments','blueprints.settings',
    'blueprints.notifications','blueprints.chatbot','blueprints.pdf',
    'blueprints.ai_insights',
    'core.database','core.helpers','core.qr_generator',
    'PIL','PIL.Image','PIL.ImageDraw','PIL.ImageFont',
    'PIL.PngImagePlugin','PIL.JpegImagePlugin',
    'reportlab','reportlab.pdfgen','reportlab.pdfgen.canvas',
    'reportlab.lib','reportlab.lib.pagesizes','reportlab.lib.colors',
    'reportlab.lib.styles','reportlab.lib.units',
    'reportlab.platypus','reportlab.platypus.tables',
    'sqlite3','_sqlite3','webview',
    'hashlib','io','threading','socket','datetime','base64','os','re','json',
]

a = Analysis(
    ['launcher.py'], pathex=['.'], binaries=[],
    datas=added_files, hiddenimports=hidden_imports,
    hookspath=[], hooksconfig={}, runtime_hooks=[], cipher=block_cipher,
    excludes=['matplotlib','numpy','pandas','scipy','tkinter','PyQt5','PyQt6','wx'],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz, a.scripts, a.binaries, a.zipfiles, a.datas, [],
    name='GCMS_CampusFlow', debug=False,
    strip=False, upx=True, upx_exclude=[],
    runtime_tmpdir=None, console=False,
    bootloader_ignore_signals=False, argv_emulation=False,
)
