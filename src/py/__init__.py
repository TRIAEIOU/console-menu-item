from aqt import mw, gui_hooks, QAction, debug_console
from .ankiutils import *

LBL = "Python debug console"
action: QAction
VER = "1.0.0"

# Add menu items ########################################################
def init():
	global action

	action = QAction(LBL)
	if sc := CFG.get('Shortcut'):
		action.setShortcut(sc)
	action.triggered.connect(debug_console.show_debug_console)
	mw.form.menuTools.addAction(action)

# Main ##################################################################
CFG = mw.addonManager.getConfig(__name__)
gui_hooks.main_window_did_init.append(init)

if strvercmp(VER, get_version()) > 0:
	set_version(VER)