import sdl2
import sdl2.ext as sdlext
from .clock import Clock

class Window:

    def __init__(self, title: str, width: int, height: int, **kwargs):
        """
        Initialize a window

        Parameters
        ----------
        title : str
            The title of the window
        width : int
            The width of the window
        height : int
            The height of the window
        **kwargs :
            Additional keyword arguments can be passed to set additional properties of the window. These include:

            fps : int (default=60)
                The target frames per second for the window
            display : int (default=0)
                The display to open the window on
            pos : tuple (default=((screen width // 2)-width//2, (screen height // 2)-height//2))
                The position of the window on the display
            fullscreen : bool (default=False)
                Whether the window should be opened in fullscreen mode
            borderless : bool (default=False)
                Whether the window should be opened in borderless mode
            resizable : bool (default=False)
                Whether the window should be opened with the ability to be resized
        """
        self.title = title
        self.width = width
        self.height = height
        self.kwargs = kwargs
        self.fullscreen = sdl2.SDL_WINDOW_FULLSCREEN
        self.fullscreen_desktop = sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
        self.bordeless = sdl2.SDL_WINDOW_BORDERLESS
        self.resizable = sdl2.SDL_WINDOW_RESIZABLE

        self.fps = self._getKwarg('fps', 60, int)
        self.display = self._getKwarg('display', 0, int)
        self.screensize = (sdlext.DisplayInfo(self.display).current_mode.w, sdlext.DisplayInfo(self.display).current_mode.h)
        defpos = ((self.screensize[0] // 2)-self.width//2, (self.screensize[1] // 2)-self.height//2)
        self.showpos = self._getKwarg('pos', defpos, tuple)
        self.flags = (
            self._getKwarg('flags', 0) | self.fullscreen_desktop if self._getKwarg('fullscreen', False) else 0 |
            self.bordeless if self._getKwarg('borderless', False) else 0 | 
            self.resizable if self._getKwarg('resizable', False) else 0
        )
        self.screen = sdlext.Window(title, (width, height), self.showpos, self.flags)
        self.clock = Clock(60)

    def _getKwarg(self, key, default, totype: None = None):
        q = self.kwargs.get(key, default)
        if totype is not None and q != default: q = totype(q)
        return q
    
    def show(self):
        """
        Show window.
        """
        self.screen.show()

    def minimize(self):
        """Minimize window."""
        self.screen.minimize()

    def hide(self):
        """
        Hide window.
        """
        self.screen.hide()

    def maximize(self):
        """
        Maximize window.
        """
        self.screen.maximize()

    def restore(self):
        """
        Restore window size to original size.
        """
        self.screen.restore()

    def close(self):
        """
        Close window.
        """
        self.screen.close()

    def create(self):
        """
        Create window if it doesn't exist.
        """
        self.screen.create()