from main import main, MooleanShell
import debugpy

if __name__ == "__main__":
    debugpy.listen(5678)
    debugpy.breakpoint()
    main()
