import sys
import traceback

assetPath = r'C:\Users\jerom\Documents\Projects\Heaj\3JV_Examen\Assets'
scenePath = r'Scenes\scene.unity'

#add the path of the project into python so we can import our module
path = r"C:\Users\jerom\Documents\Projects\Heaj\3JV_C1_Examen_solution"
if path not in sys.path:
	sys.path.append(path)

#delete previously loaded modules if any
#so we are sure to reload the latest update of the code
keys = [key for key in sys.modules.keys() if "unityTool" in key]
for key in keys:
	if "unityTool" in key:
		del sys.modules[key]
	
	
try:
    import unityTool.loader as ut
    ut.load( assetPath, scenePath )
except Exception:
    traceback.print_exc()