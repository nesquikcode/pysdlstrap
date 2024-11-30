# psdls.app include main App class for apps/games
# psdls.events include all events for app (like quit, keybutton down, etc.)
from psdls.app import App
from psdls.events import QUIT

# create app
# args: 
#   title: str, 
#   width: int,
#   height: int
# kwargs: 
#   fps: int = 60,
#   display: int = 0,
#   fullscreen: bool = False,
#   borderless: bool = False,
#   resizable: bool = False,
#   pos: tuple = ((self.screensize[0] // 2)-self.width//2, (self.screensize[1] // 2)-self.height//2)
#       **pos default on center of screen**
app = App("PySDLStrap Example", 800, 600, fps=800)

def fps(clock): print(clock.get_fps())

# run func on event
# app.addevent(event, func, `*args`, **kwargs)
app.addevent(QUIT, app.quit)

# run func every frame
# app.addhandler(func, `*args`, **kwargs)
app.addhandler(fps, (app.screen.clock,))

# run app
# app.run()
app.run()