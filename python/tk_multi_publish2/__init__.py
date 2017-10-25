# Copyright (c) 2017 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

from sgtk.platform.qt import QtCore, QtGui
import util

def show_dialog(app):
    """
    Show the main dialog ui

    :param app: The parent App
    """
    # defer imports so that the app works gracefully in batch modes
    from .dialog import AppDialog

    '''
    import sys, os

    paths = (
        '/opt/squeeze/PyCharm/helpers/pydev',
        '/opt/squeeze/PyCharm-2016.2.3/helpers/pydev',
        '/opt/squeeze/PyCharm-2016.3.2/helpers/pydev',
        '/opt/squeeze/PyCharm-2017.1.1/helpers/pydev',
        'C:/Program Files (x86)/JetBrains/PyCharm 2016.2.3/helpers/pydev',
        'C:/Program Files/JetBrains/PyCharm 2017.1.1/helpers/pydev',
        'C:/Program Files/JetBrains/PyCharm 2017.1.4/helpers/pydev',
        '/opt/pycharm-professional/helpers/pydev/'  # arch-linux
    )
    debug_path = next(iter(path for path in paths if os.path.exists(path)), None)
    if not debug_path or not os.path.exists(debug_path):
        raise Exception("Can't connect to pycharm, path doesn't exist: {0}".format(debug_path))
    if debug_path not in sys.path:
        sys.path.append(debug_path)
    import pydevd
    pydevd.settrace('localhost', port=64304, stdoutToServer=True, stderrToServer=True, suspend=False)
    '''

    # start ui
    app.engine.show_dialog("Shotgun Publish", app, AppDialog)




