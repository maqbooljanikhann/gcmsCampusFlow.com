"""
GCMS CampusFlow — Desktop Launcher
Starts Flask in background + opens native desktop window via PyWebView.
"""
import sys, os, threading, time, socket

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def get_bundle_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR   = get_base_dir()
BUNDLE_DIR = get_bundle_dir()

if BUNDLE_DIR not in sys.path: sys.path.insert(0, BUNDLE_DIR)
if BASE_DIR   not in sys.path: sys.path.insert(0, BASE_DIR)

os.environ['GCMS_DATA_DIR'] = BASE_DIR

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

PORT = find_free_port()

def start_flask():
    from app import create_app
    from core.database import init_db
    from jinja2 import FileSystemLoader
    flask_app = create_app()
    flask_app.root_path = BASE_DIR
    flask_app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')
    os.makedirs(flask_app.config['UPLOAD_FOLDER'], exist_ok=True)
    flask_app.jinja_loader = FileSystemLoader(os.path.join(BUNDLE_DIR, 'templates'))
    with flask_app.app_context():
        init_db()
    flask_app.run(host='127.0.0.1', port=PORT, debug=False, use_reloader=False, threaded=True)

def wait_for_flask(timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection(('127.0.0.1', PORT), timeout=1): return True
        except OSError: time.sleep(0.15)
    return False

def main():
    t = threading.Thread(target=start_flask, daemon=True)
    t.start()
    if not wait_for_flask():
        sys.exit(1)
    url = f'http://127.0.0.1:{PORT}'
    try:
        import webview
        webview.create_window(
            'GCMS CampusFlow — Government College of Management Sciences',
            url, width=1366, height=768, min_size=(1024,600), resizable=True)
        webview.start(debug=False)
    except ImportError:
        import webbrowser
        webbrowser.open(url)
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt: pass

if __name__ == '__main__':
    main()
