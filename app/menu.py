import curses

class Menu:

    
    
    def __init__(self):
        
        self.opciones = ['1.',
                         '2.',
                         '3.',
                         '4.']
        self.seleccionado = 0
        
        #--  Inicializamos la pentalla
        self.stdscr = curses.initscr() 
        self.stdscr.keypad(True)
        curses.curs_set(0)
        
        self.InitMenuExec()
        

    def MenuVista(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "¡Bienvenido al Menú!")
        for idx, opcion in enumerate(self.opciones):
            if idx == self.seleccionado:
                self.stdscr.addstr(idx + 2, 0, f"> {opcion}", curses.A_REVERSE)
            else:
                self.stdscr.addstr(idx + 2, 0, f"  {opcion}")
        self.stdscr.refresh()

    def ObtenerOpcion(self):
         while True:
            key = self.stdscr.getch()
            if key == curses.KEY_UP:
                self.seleccionado = max(0, self.seleccionado - 1)
            elif key == curses.KEY_DOWN:
                self.seleccionado = min(len(self.opciones) - 1, self.seleccionado + 1)
            elif key in [curses.KEY_ENTER, 10, 13]:
                return self.seleccionado
    
    def InitMenuExec(self):
        while True:
            self.MenuVista() 
            opcion = self.ObtenerOpcion()
           
            if opcion == len(self.opciones) - 1:
                self.stdscr.addstr(len(self.opciones) + 2, 0, "¡Hasta luego!")
                self.stdscr.refresh()
                self.stdscr.getch()
                break
            else:
                self.stdscr.addstr(len(self.opciones) + 2, 0, f"Elegiste la opción {opcion + 1}: {self.opciones[opcion]}")
                self.stdscr.refresh()
                self.stdscr.getch()
    
    def __del__(self):
        curses.endwin()