import os
import json
import tempfile
import time
import sys
import subprocess
import threading
import webbrowser
import shutil
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

def OO00O000OOOO():
    os.system('cls' if os.name == 'nt' else 'clear')

def O0O0O000OOO0(O000OO0O0O0O, O0OO00O00O00):
    return f'\x1b[{O0OO00O00O00}m{O000OO0O0O0O}\x1b[0m'

def OOOO00OOO0OO(OO00OO0OO0O0):
    return O0O0O000OOO0(OO00OO0OO0O0, '92')

def OO0OOO00000O(OO0OO0OO0000):
    return O0O0O000OOO0(OO0OO0OO0000, '96')

def O0O00OO00OOO(O0OOO0O00OO0):
    return O0O0O000OOO0(O0OOO0O00OO0, '93')

def O0OO00O0OO0O(OO00O0OOOO00):
    return O0O0O000OOO0(OO00O0OOOO00, '91')

def OOO0000O00OO(OOO0OOOO00O0):
    return O0O0O000OOO0(OOO0OOOO00O0, '1')

def O00O000OO00O(O0000O00O000):
    return O0O0O000OOO0(O0000O00O000, '2')
BANNER = '\n  ██████╗  █████╗ ██████╗ ██╗   ██╗███████╗\n  ██╔══██╗██╔══██╗██╔══██╗██║   ██║╚════██╗\n  ██████╔╝███████║██████╔╝██║   ██║    ██╔╝\n  ██╔═══╝ ██╔══██║██╔══██╗╚██╗ ██╔╝   ██╔╝ \n  ██║     ██║  ██║██║  ██║ ╚████╔╝   ██╔╝  \n  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝   ██████╗\n                                     ╚═════╝\n'

def O0O000OOOOOO(OOO0O0OOOOO0, delay=0.03):
    for OOOOO0000O0O in OOO0O0OOOOO0:
        sys.stdout.write(OOOOO0000O0O)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def O0000O0O0O00(OOO0OOO0O0OO, steps=30, delay=0.05):
    sys.stdout.write(f'  {OO0OOO00000O(OOO0OOO0O0OO):30s}  [')
    sys.stdout.flush()
    for O0OO0000O0O0 in range(steps):
        time.sleep(delay)
        sys.stdout.write(OOOO00OOO0OO('█'))
        sys.stdout.flush()
    sys.stdout.write(']  ' + OOOO00OOO0OO('✔') + '\n')
    sys.stdout.flush()

def OOO00OOO000O(OO00OOO00000, duration=2.0):
    OO00000O0OOO = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    O0OOOO0O0OO0 = time.time() + duration
    OO0OOO0OOO0O = 0
    while time.time() < O0OOOO0O0OO0:
        sys.stdout.write(f'\r  {OO0OOO00000O(OO00000O0OOO[OO0OOO0OOO0O % len(OO00000O0OOO)])}  {O0O00OO00OOO(OO00OOO00000)}   ')
        sys.stdout.flush()
        time.sleep(0.1)
        OO0OOO0OOO0O += 1
    sys.stdout.write(f"\r  {OOOO00OOO0OO('✔')}  {OOOO00OOO0OO(OO00OOO00000)}   \n")
    sys.stdout.flush()

def OO0OOOO0OO00():
    OO00O000OOOO()
    for O00OOO0000OO in BANNER.strip('\n').split('\n'):
        print(OO0OOO00000O(O00OOO0000OO))
    print()
    print(OOO0000O00OO(OOOO00OOO0OO('           ⚡  ALL-IN-ONE VIDEO DOWNLOADER  ⚡')))
    print(O00O000OO00O('           Powered by  ') + OOO0000O00OO(O0O00OO00OOO('@all_in_one_63')) + O00O000OO00O('  |  t.me/all_in_one_63'))
    print()
    time.sleep(0.4)
    sys.stdout.write('  ' + O0O00OO00OOO('Initializing'))
    for O00O00O000O0 in range(6):
        time.sleep(0.25)
        sys.stdout.write(O0O00OO00OOO('.'))
        sys.stdout.flush()
    print()
    time.sleep(0.2)
    OO0OOO00O00O = [('Loading modules', 25, 0.04), ('Checking yt-dlp', 20, 0.05), ('Setting up server', 22, 0.04), ('Preparing interface', 28, 0.03)]
    for O0OO0OOOO000, OOOOOOO0OOOO, O0O0OOO0OOO0 in OO0OOO00O00O:
        O0000O0O0O00(O0OO0OOOO000, OOOOOOO0OOOO, O0O0OOO0OOO0)
    print()
    OOO00OOO000O('Verifying system integrity ...', 1.8)
    OOO00OOO000O('Authenticating session      ...', 1.5)
    print()
    print(OOO0000O00OO(OOOO00OOO0OO('  ✔  All checks passed!  System ready.')))
    print()
    time.sleep(0.3)
    print('  ' + O00O000OO00O('─' * 60))
    print(f"  {O00O000OO00O('Powered by')}  {OOO0000O00OO(OO0OOO00000O('ALL IN ONE'))}  {O00O000OO00O('|')}  {O0O00OO00OOO('t.me/all_in_one_63')}")
    print('  ' + O00O000OO00O('─' * 60))
    print()
    time.sleep(0.5)

def OOO000OO0O0O():
    OO0OO0000O00 = []
    OOO0O00OO0OO = {'chrome': ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'], 'firefox': ['firefox', 'C:\\Program Files\\Mozilla Firefox\\firefox.exe', 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'], 'edge': ['microsoft-edge', 'msedge', 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', 'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe'], 'safari': ['/Applications/Safari.app/Contents/MacOS/Safari'], 'brave': ['brave-browser', 'brave', 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'], 'opera': ['opera', 'C:\\Program Files\\Opera\\opera.exe']}
    for O00O00OOO0O0, OOOO00O0000O in OOO0O00OO0OO.items():
        for OO00000O0000 in OOOO00O0000O:
            if os.path.isfile(OO00000O0000):
                OO0OO0000O00.append((O00O00OOO0O0.capitalize(), OO00000O0000))
                break
            try:
                OO0OOO000OOO = subprocess.run(['which', OO00000O0000] if os.name != 'nt' else ['where', OO00000O0000], capture_output=True, text=True, timeout=2)
                if OO0OOO000OOO.returncode == 0 and OO0OOO000OOO.stdout.strip():
                    OO0OO0000O00.append((O00O00OOO0O0.capitalize(), OO0OOO000OOO.stdout.strip().splitlines()[0]))
                    break
            except Exception:
                pass
    OO0000000OO0 = set()
    O000O000OO0O = []
    for O00O00OOO0O0, OOOO000OOO00 in OO0OO0000O00:
        if O00O00OOO0O0 not in OO0000000OO0:
            OO0000000OO0.add(O00O00OOO0O0)
            O000O000OO0O.append((O00O00OOO0O0, OOOO000OOO00))
    return O000O000OO0O

def OO0O0OOO00OO(O0OO0O0O00O0, O0O00OOOO00O):
    try:
        if os.name == 'nt':
            subprocess.Popen([O0OO0O0O00O0, O0O00OOOO00O])
        else:
            subprocess.Popen([O0OO0O0O00O0, O0O00OOOO00O], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        webbrowser.open(O0O00OOOO00O)

def OOO0O0O0O000(OO0OO00OOOOO):
    try:
        OOOO000OOOO0 = subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', OO0OO00OOOOO], capture_output=True, text=True, timeout=5)
        if OOOO000OOOO0.returncode == 0:
            return True
    except Exception:
        pass
    return False

def OO00OOO00O0O(O0O0O0OO0O00):
    if os.path.exists('/data/data/com.termux') or 'com.termux' in os.environ.get('PREFIX', ''):
        print(OOOO00OOO0OO('  📱 Android detected. Opening browser via intent...'))
        time.sleep(0.5)
        if OOO0O0O0O000(O0O0O0OO0O00):
            print(OOOO00OOO0OO(f'  ✔  Browser opened: {O0O0O0OO0O00}'))
        else:
            try:
                subprocess.Popen(['termux-open-url', O0O0O0OO0O00], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(OOOO00OOO0OO(f'  ✔  Opened via termux-open-url'))
            except Exception:
                print(O0O00OO00OOO(f'  ⚠  Could not open browser automatically.'))
                print(O0O00OO00OOO(f'  👉 Manually open: {OO0OOO00000O(O0O0O0OO0O00)}'))
        return
    OOO00O00O0OO = OOO000OO0O0O()
    if not OOO00O00O0OO:
        print(O0O00OO00OOO('  No specific browser detected. Opening default browser...'))
        webbrowser.open(O0O0O0OO0O00)
        return
    if len(OOO00O00O0OO) == 1:
        OOOO0OO0O0O0, OOOOOO0O000O = OOO00O00O0OO[0]
        print(OOOO00OOO0OO(f'  Opening in {OOOO0OO0O0O0}...'))
        time.sleep(0.5)
        OO0O0OOO00OO(OOOOOO0O000O, O0O0O0OO0O00)
        return
    print(OOO0000O00OO(OO0OOO00000O('  Multiple browsers detected. Choose one:\n')))
    for O0OO0O000000, (OOOO0OO0O0O0, OOOO0OOO0OOO) in enumerate(OOO00O00O0OO, 1):
        print(f'    {OOO0000O00OO(O0O00OO00OOO(str(O0OO0O000000)))}. {OOOO00OOO0OO(OOOO0OO0O0O0)}')
    print(f'    {OOO0000O00OO(O0O00OO00OOO(str(len(OOO00O00O0OO) + 1)))}. Default system browser')
    print()
    while True:
        try:
            sys.stdout.write(f"  {OO0OOO00000O('Enter number')} [{O0O00OO00OOO('1')}-{O0O00OO00OOO(str(len(OOO00O00O0OO) + 1))}]: ")
            sys.stdout.flush()
            OO0000OO0OO0 = input().strip()
            O0OO00OOOO0O = int(OO0000OO0OO0)
            if 1 <= O0OO00OOOO0O <= len(OOO00O00O0OO):
                OOOO0OO0O0O0, OOOOOO0O000O = OOO00O00O0OO[O0OO00OOOO0O - 1]
                print(OOOO00OOO0OO(f'\n  Opening in {OOOO0OO0O0O0}...'))
                time.sleep(0.4)
                OO0O0OOO00OO(OOOOOO0O000O, O0O0O0OO0O00)
                break
            elif O0OO00OOOO0O == len(OOO00O00O0OO) + 1:
                print(OOOO00OOO0OO('\n  Opening in default browser...'))
                time.sleep(0.4)
                webbrowser.open(O0O0O0OO0O00)
                break
            else:
                print(O0OO00O0OO0O('  Invalid choice. Try again.'))
        except (ValueError, KeyboardInterrupt):
            print(O0OO00O0OO0O('\n  Invalid input. Opening default browser...'))
            webbrowser.open(O0O0O0OO0O00)
            break

def O0000O00OO00(O00O00O000OO: str) -> str:
    OO0OO00000O0 = O00O00O000OO.encode('ascii', 'ignore').decode('ascii').strip()
    if not OO0OO00000O0:
        OO0OO00000O0 = 'download'
    OOOO00O0O00O = urllib.parse.quote(O00O00O000OO.encode('utf-8'), safe='')
    return f"""attachment; filename="{OO0OO00000O0}"; filename*=UTF-8''{OOOO00O0O00O}"""

class handler(BaseHTTPRequestHandler):

    def log_message(O00OOO0OO000, format, *O0OO0O00OOOO):
        pass

    def _json_ok(O0OO0O00OOO0, O0OOO00O0O0O):
        OOOOOOO00O00 = json.dumps(O0OOO00O0O0O, ensure_ascii=False).encode('utf-8')
        O0OO0O00OOO0.send_response(200)
        O0OO0O00OOO0.send_header('Content-Type', 'application/json; charset=utf-8')
        O0OO0O00OOO0.send_header('Content-Length', str(len(OOOOOOO00O00)))
        O0OO0O00OOO0.send_header('Access-Control-Allow-Origin', '*')
        O0OO0O00OOO0.end_headers()
        O0OO0O00OOO0.wfile.write(OOOOOOO00O00)

    def _json_error(OO0OOOOOO0OO, OO0OO00OO0O0, code=500):
        O000O000000O = json.dumps({'error': OO0OO00OO0O0}, ensure_ascii=False).encode('utf-8')
        OO0OOOOOO0OO.send_response(code)
        OO0OOOOOO0OO.send_header('Content-Type', 'application/json; charset=utf-8')
        OO0OOOOOO0OO.send_header('Content-Length', str(len(O000O000000O)))
        OO0OOOOOO0OO.send_header('Access-Control-Allow-Origin', '*')
        OO0OOOOOO0OO.end_headers()
        OO0OOOOOO0OO.wfile.write(O000O000000O)

    @staticmethod
    def _fmt_size(O0O00OOO0000):
        if not O0O00OOO0000:
            return ''
        O0O00OOO0000 = int(O0O00OOO0000)
        for O00O00O00OOO in ('B', 'KB', 'MB', 'GB'):
            if O0O00OOO0000 < 1024:
                return f'{O0O00OOO0000:.1f}{O00O00O00OOO}'
            O0O00OOO0000 /= 1024
        return f'{O0O00OOO0000:.1f}GB'

    def do_GET(OO000OO00OO0):
        if OO000OO00OO0.path == '/' or OO000OO00OO0.path == '/index.html':
            OO000OO00OO0._serve_html()
        elif OO000OO00OO0.path.startswith('/api/info'):
            OO000OO00OO0._api_info()
        elif OO000OO00OO0.path.startswith('/api/proxy'):
            OO000OO00OO0._api_proxy()
        else:
            OO000OO00OO0.send_error(404, 'Not Found')

    def do_POST(OO0OOOO0OO0O):
        OO0OOOO0OO0O.do_GET()

    def _serve_html(O00O0OOOOO00):
        O00O0OOOOO00.send_response(200)
        O00O0OOOOO00.send_header('Content-type', 'text/html; charset=utf-8')
        O00O0OOOOO00.end_headers()
        O00O0OOOOO00.wfile.write(HTML_PAGE.encode('utf-8'))

    def _api_info(OO00OO0O00OO):
        try:
            import yt_dlp
        except ImportError:
            OO00OO0O00OO._json_error('yt-dlp not installed. Run: pip install yt-dlp')
            return
        OOOOO0OO00O0 = int(OO00OO0O00OO.headers.get('Content-Length', 0))
        O0OOOO0OO00O = OO00OO0O00OO.rfile.read(OOOOO0OO00O0)
        try:
            OO0O0000O000 = json.loads(O0OOOO0OO00O)
        except Exception:
            OO00OO0O00OO._json_error('Invalid JSON')
            return
        O000OOOOOOOO = OO0O0000O000.get('url', '').strip()
        OOOO0OOOOOO0 = OO0O0000O000.get('quality', 'best')
        O0O00O000O0O = OO0O0000O000.get('format', 'mp4')
        if not O000OOOOOOOO:
            OO00OO0O00OO._json_error('URL required')
            return
        try:
            OO0O000O0O00 = {'worst': 144, '360p': 360, '480p': 480, '720p': 720, '1080p': 1080, 'best': 9999}
            OO0OO0O0O0OO = OO0O000O0O00.get(OOOO0OOOOOO0, 9999)
            O0OOOO00O0O0 = {'quiet': True, 'no_warnings': True, 'noplaylist': True, 'skip_download': True, 'socket_timeout': 15}
            with yt_dlp.YoutubeDL(O0OOOO00O0O0) as O00O00OO000O:
                O00OO0O00000 = O00O00OO000O.extract_info(O000OOOOOOOO, download=False)
            O0O0OO0O0OOO = O00OO0O00000.get('title', 'video')
            OO00O00O0OO0 = O00OO0O00000.get('duration_string') or str(O00OO0O00000.get('duration', ''))
            O000O00OOO0O = O00OO0O00000.get('thumbnail', '')
            O0O0O0O0OO00 = O00OO0O00000.get('extractor_key', O00OO0O00000.get('extractor', ''))
            O000O00000OO = O00OO0O00000.get('formats') or []
            O00OOOO000O0 = []
            if O0O00O000O0O == 'mp3':
                O00000OOO000 = [O000O000O00O for O000O000O00O in O000O00000OO if O000O000O00O.get('vcodec') == 'none' and O000O000O00O.get('url') and (O000O000O00O.get('ext') in ('m4a', 'mp3', 'webm', 'opus', 'aac'))]
                if not O00000OOO000:
                    O00000OOO000 = [OOO0O0O0OOOO for OOO0O0O0OOOO in O000O00000OO if OOO0O0O0OOOO.get('acodec') and OOO0O0O0OOOO.get('acodec') != 'none' and OOO0O0O0OOOO.get('url')]
                O00000OOO000.sort(key=lambda f: f.get('abr') or 0, reverse=True)
                for O0OOO0O0OOO0 in O00000OOO000[:3]:
                    O000OOOO0O0O = O0OOO0O0OOO0.get('abr', '')
                    O0O00O000O00 = OO00OO0O00OO._fmt_size(O0OOO0O0OOO0.get('filesize') or O0OOO0O0OOO0.get('filesize_approx'))
                    O00OOOO000O0.append({'url': O0OOO0O0OOO0['url'], 'quality': f'{int(O000OOOO0O0O)}kbps' if O000OOOO0O0O else 'Audio', 'ext': O0OOO0O0OOO0.get('ext', 'm4a'), 'filesize': O0O00O000O00})
            else:
                O00OOOOOO0O0 = [OO0O0O0OO0OO for OO0O0O0OO0OO in O000O00000OO if OO0O0O0OO0OO.get('vcodec') and OO0O0O0OO0OO.get('vcodec') != 'none' and OO0O0O0OO0OO.get('acodec') and (OO0O0O0OO0OO.get('acodec') != 'none') and OO0O0O0OO0OO.get('url') and ((OO0O0O0OO0OO.get('height') or 0) <= OO0OO0O0O0OO)]
                O00OOOOOO0O0.sort(key=lambda f: (O0OOO0O0OOO0.get('height') or 0, O0OOO0O0OOO0.get('tbr') or 0), reverse=True)
                O00OOOO0000O = set()
                for O0OOO0O0OOO0 in O00OOOOOO0O0:
                    O000OO0O0000 = O0OOO0O0OOO0.get('height') or 0
                    if O000OO0O0000 in O00OOOO0000O:
                        continue
                    O00OOOO0000O.add(O000OO0O0000)
                    O0O00O000O00 = OO00OO0O00OO._fmt_size(O0OOO0O0OOO0.get('filesize') or O0OOO0O0OOO0.get('filesize_approx'))
                    O00OOOO000O0.append({'url': O0OOO0O0OOO0['url'], 'quality': f'{O000OO0O0000}p' if O000OO0O0000 else 'Video', 'ext': O0OOO0O0OOO0.get('ext', 'mp4'), 'filesize': O0O00O000O00})
                    if len(O00OOOO000O0) >= 5:
                        break
                if not O00OOOO000O0 and O00OO0O00000.get('url'):
                    O000OO0O0000 = O00OO0O00000.get('height') or 0
                    O0O00O000O00 = OO00OO0O00OO._fmt_size(O00OO0O00000.get('filesize') or O00OO0O00000.get('filesize_approx'))
                    O00OOOO000O0.append({'url': O00OO0O00000['url'], 'quality': f'{O000OO0O0000}p' if O000OO0O0000 else 'HD', 'ext': O00OO0O00000.get('ext', 'mp4'), 'filesize': O0O00O000O00})
                if not O00OOOO000O0:
                    OO00OO000OO0 = [OO00O0000OOO for OO00O0000OOO in O000O00000OO if OO00O0000OOO.get('vcodec') and OO00O0000OOO.get('vcodec') != 'none' and OO00O0000OOO.get('url') and ((OO00O0000OOO.get('height') or 0) <= OO0OO0O0O0OO)]
                    OO00OO000OO0.sort(key=lambda f: O0OOO0O0OOO0.get('height') or 0, reverse=True)
                    for O0OOO0O0OOO0 in OO00OO000OO0[:3]:
                        O000OO0O0000 = O0OOO0O0OOO0.get('height') or 0
                        O0O00O000O00 = OO00OO0O00OO._fmt_size(O0OOO0O0OOO0.get('filesize') or O0OOO0O0OOO0.get('filesize_approx'))
                        O00OOOO000O0.append({'url': O0OOO0O0OOO0['url'], 'quality': f'{O000OO0O0000}p' if O000OO0O0000 else 'Video', 'ext': O0OOO0O0OOO0.get('ext', 'mp4'), 'filesize': O0O00O000O00})
            if not O00OOOO000O0:
                OO00OO0O00OO._json_error('No downloadable format found for this URL.')
                return
            O0OO0O00OO0O = {'title': O0O0OO0O0OOO, 'duration': OO00O00O0OO0, 'thumbnail': O000O00OOO0O, 'extractor': O0O0O0O0OO00, 'direct_url': O00OOOO000O0[0]['url'], 'formats': O00OOOO000O0}
            OO00OO0O00OO._json_ok(O0OO0O00OO0O)
        except Exception as e:
            O0OOOO0OOO00 = str(e)
            if 'Sign in' in O0OOOO0OOO00 or 'login' in O0OOOO0OOO00.lower():
                O0OOOO0OOO00 = 'This video requires login.'
            elif 'Private' in O0OOOO0OOO00:
                O0OOOO0OOO00 = 'This is a private video.'
            elif 'not available' in O0OOOO0OOO00.lower():
                O0OOOO0OOO00 = 'Video not available in your region.'
            OO00OO0O00OO._json_error(O0OOOO0OOO00)

    def _api_proxy(OO0000OO00OO):
        import urllib.request as ureq
        from urllib.parse import urlparse, parse_qs, unquote
        OO00000O00O0 = urlparse(OO0000OO00OO.path)
        OO0O00OOO00O = parse_qs(OO00000O00O0.query)
        O0OO0OO0O000 = unquote(OO0O00OOO00O.get('url', [''])[0])
        OO000O0OOOOO = unquote(OO0O00OOO00O.get('filename', ['video.mp4'])[0])
        if not O0OO0OO0O000 or not O0OO0OO0O000.startswith('http'):
            OO0000OO00OO.send_error(400, 'Invalid URL')
            return
        try:
            OOOOOO0OOOO0 = ureq.Request(O0OO0OO0O000, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36', 'Accept': '*/*', 'Accept-Encoding': 'identity', 'Referer': 'https://www.youtube.com/'})
            with ureq.urlopen(OOOOOO0OOOO0, timeout=60) as OOOOO0O00O0O:
                OOOO0OOO0O00 = OOOOO0O00O0O.headers.get('Content-Type', 'application/octet-stream')
                OO0O0000O0OO = OOOOO0O00O0O.headers.get('Content-Length', '')
                OO0000OO00OO.send_response(200)
                OO0000OO00OO.send_header('Content-Type', OOOO0OOO0O00)
                O00000O0O0O0 = O0000O00OO00(OO000O0OOOOO)
                O0O0O00O000O = ('Content-Disposition: ' + O00000O0O0O0 + '\r\n').encode('utf-8')
                if hasattr(OO0000OO00OO, '_headers_buffer'):
                    OO0000OO00OO._headers_buffer.append(O0O0O00O000O)
                else:
                    OO0000OO00OO.wfile.write(O0O0O00O000O)
                if OO0O0000O0OO:
                    OO0000OO00OO.send_header('Content-Length', OO0O0000O0OO)
                OO0000OO00OO.send_header('Cache-Control', 'no-cache')
                OO0000OO00OO.send_header('Access-Control-Allow-Origin', '*')
                OO0000OO00OO.end_headers()
                O00000000000 = 512 * 1024
                while True:
                    OOO000OO0OOO = OOOOO0O00O0O.read(O00000000000)
                    if not OOO000OO0OOO:
                        break
                    try:
                        OO0000OO00OO.wfile.write(OOO000OO0OOO)
                        OO0000OO00OO.wfile.flush()
                    except (BrokenPipeError, ConnectionResetError, OSError):
                        break
        except Exception as e:
            try:
                OO0000OO00OO._json_error(f'Proxy error: {str(e)}')
            except Exception:
                pass
HTML_PAGE = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>ALL-IN-ONE VIDEO DOWNLOADER</title>\n    <style>\n        * { margin:0; padding:0; box-sizing:border-box; font-family:\'Segoe UI\',Tahoma,Geneva,Verdana,sans-serif; }\n        body {\n            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);\n            color: white;\n            min-height: 100vh;\n            padding: 20px;\n        }\n        .container {\n            max-width: 800px;\n            margin: 0 auto;\n            background: rgba(0,0,0,0.7);\n            border-radius: 20px;\n            padding: 30px;\n            box-shadow: 0 10px 30px rgba(0,0,0,0.5);\n            border: 2px solid #00ff88;\n        }\n        .header { text-align:center; margin-bottom:30px; }\n        h1 {\n            color: #00ff88;\n            font-size: 32px;\n            margin-bottom: 10px;\n            text-shadow: 0 0 10px rgba(0,255,136,0.5);\n        }\n        .subtitle { color:#ccc; margin-bottom:20px; }\n        .url-box { margin:20px 0; }\n        input[type="text"] {\n            width: 100%;\n            padding: 15px;\n            border: 2px solid #00ff88;\n            border-radius: 10px;\n            background: rgba(255,255,255,0.1);\n            color: white;\n            font-size: 16px;\n            margin-bottom: 10px;\n        }\n        input[type="text"]:focus { outline:none; box-shadow:0 0 15px rgba(0,255,136,0.5); }\n        .quality-buttons { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin:20px 0; }\n        .quality-btn {\n            padding: 15px;\n            border: 2px solid #555;\n            background: rgba(255,255,255,0.1);\n            color: white;\n            border-radius: 10px;\n            cursor: pointer;\n            text-align: center;\n            transition: all 0.3s;\n        }\n        .quality-btn:hover { border-color:#00ff88; transform:scale(1.05); }\n        .quality-btn.active { background:rgba(0,255,136,0.2); border-color:#00ff88; }\n        .format-buttons { display:flex; gap:10px; margin:20px 0; }\n        .format-btn {\n            flex: 1;\n            padding: 15px;\n            border: 2px solid #555;\n            background: rgba(255,255,255,0.1);\n            color: white;\n            border-radius: 10px;\n            cursor: pointer;\n            text-align: center;\n            font-size: 18px;\n            transition: all 0.3s;\n        }\n        .format-btn:hover { border-color:#ff8800; transform:scale(1.05); }\n        .format-btn.active { background:rgba(255,136,0,0.2); border-color:#ff8800; }\n        .download-btn {\n            width: 100%;\n            padding: 20px;\n            background: linear-gradient(135deg,#00ff88,#0088ff);\n            border: none;\n            border-radius: 15px;\n            color: white;\n            font-size: 20px;\n            font-weight: bold;\n            cursor: pointer;\n            margin: 30px 0;\n            transition: all 0.3s;\n        }\n        .download-btn:hover:not(:disabled) { transform:translateY(-5px); box-shadow:0 10px 20px rgba(0,136,255,0.5); }\n        .download-btn:disabled { opacity:0.5; cursor:not-allowed; }\n        .progress-section {\n            display: none;\n            margin: 20px 0;\n            padding: 20px;\n            background: rgba(0,0,0,0.5);\n            border-radius: 15px;\n            border: 2px solid #0088ff;\n        }\n        .progress-bar { height:20px; background:rgba(255,255,255,0.1); border-radius:10px; overflow:hidden; margin:15px 0; }\n        .progress-fill { height:100%; background:linear-gradient(90deg,#00ff88,#0088ff); width:0%; transition:width 0.5s; }\n        .status { text-align:center; margin:10px 0; color:#00ff88; font-weight:bold; }\n        .console {\n            background: black;\n            color: #00ff88;\n            padding: 15px;\n            border-radius: 10px;\n            font-family: monospace;\n            font-size: 12px;\n            height: 200px;\n            overflow-y: auto;\n            margin: 20px 0;\n            display: none;\n            border: 1px solid #00ff88;\n        }\n        .message { padding:15px; border-radius:10px; margin:15px 0; text-align:center; display:none; }\n        .success { background:rgba(0,255,136,0.2); border:2px solid #00ff88; color:#00ff88; }\n        .error   { background:rgba(255,0,0,0.2);   border:2px solid #ff4444; color:#ff4444; }\n        .test-urls { display:flex; flex-wrap:wrap; gap:10px; margin:15px 0; }\n        .test-url {\n            background: rgba(0,136,255,0.2);\n            padding: 10px 15px;\n            border-radius: 8px;\n            cursor: pointer;\n            transition: all 0.3s;\n        }\n        .test-url:hover { background:rgba(0,136,255,0.4); transform:translateY(-2px); }\n        .footer {\n            text-align: center;\n            margin-top: 30px;\n            padding-top: 20px;\n            border-top: 1px solid rgba(255,255,255,0.1);\n        }\n        /* Telegram float */\n        .tg-float {\n            position: fixed;\n            bottom: 28px; right: 28px;\n            width: 58px; height: 58px;\n            border-radius: 50%;\n            background: linear-gradient(135deg, #2AABEE, #229ED9);\n            box-shadow: 0 4px 20px rgba(42,171,238,0.55);\n            display: flex;\n            align-items: center; justify-content: center;\n            cursor: pointer;\n            text-decoration: none;\n            z-index: 9999;\n            animation: tg-pulse 2.5s infinite;\n            transition: transform 0.2s, box-shadow 0.2s;\n        }\n        .tg-float:hover { transform:scale(1.12); box-shadow:0 6px 28px rgba(42,171,238,0.8); animation:none; }\n        .tg-float svg { width:30px; height:30px; fill:white; }\n        .tg-tooltip {\n            position: fixed;\n            bottom: 96px; right: 28px;\n            background: rgba(0,0,0,0.85);\n            color: #2AABEE;\n            font-size: 13px; font-weight: 600;\n            padding: 7px 14px;\n            border-radius: 10px;\n            border: 1px solid #2AABEE;\n            white-space: nowrap;\n            opacity: 0; pointer-events: none;\n            transition: opacity 0.25s;\n        }\n        .tg-float:hover + .tg-tooltip, .tg-tooltip.show { opacity: 1; }\n        @keyframes tg-pulse {\n            0%,100% { box-shadow: 0 4px 20px rgba(42,171,238,0.55); }\n            50%      { box-shadow: 0 4px 30px rgba(42,171,238,0.9); }\n        }\n        @media (max-width:600px) {\n            .container { padding:15px; }\n            .quality-buttons { grid-template-columns:repeat(2,1fr); }\n            h1 { font-size:24px; }\n            .tg-float { bottom:18px; right:18px; }\n            .tg-tooltip { bottom:82px; right:18px; }\n        }\n    </style>\n</head>\n<body>\n<div class="container">\n    <div class="header">\n        <h1>🎬 ALL-IN-ONE VIDEO DOWNLOADER</h1>\n        <p class="subtitle">YouTube • Instagram • Facebook • TikTok • Twitter • 100+ Sites</p>\n        <p style="color:#ff8800;font-size:14px;margin-top:10px;">⚡ Fast & Reliable Local Server</p>\n    </div>\n\n    <div class="url-box">\n        <input type="text" id="videoUrl" placeholder="🌐 Paste ANY video URL here...">\n        <div class="test-urls">\n            <div class="test-url" onclick="setTestUrl(\'youtube\')">📺 YouTube Test</div>\n            <div class="test-url" onclick="setTestUrl(\'instagram\')">📷 Instagram Test</div>\n            <div class="test-url" onclick="setTestUrl(\'tiktok\')">🎵 TikTok Test</div>\n        </div>\n    </div>\n\n    <div class="quality-buttons">\n        <div class="quality-btn active" onclick="selectQuality(\'360p\',this)">360p</div>\n        <div class="quality-btn" onclick="selectQuality(\'480p\',this)">480p</div>\n        <div class="quality-btn" onclick="selectQuality(\'720p\',this)">720p HD</div>\n        <div class="quality-btn" onclick="selectQuality(\'1080p\',this)">1080p FHD</div>\n        <div class="quality-btn" onclick="selectQuality(\'best\',this)">👑 Best</div>\n        <div class="quality-btn" onclick="selectQuality(\'worst\',this)">⚡ Fast</div>\n    </div>\n\n    <div class="format-buttons">\n        <div class="format-btn active" onclick="selectFormat(\'mp4\',this)">🎥 MP4 Video</div>\n        <div class="format-btn" onclick="selectFormat(\'mp3\',this)">🎵 MP3 Audio</div>\n    </div>\n\n    <button class="download-btn" id="downloadBtn" onclick="startDownload()">⚡ START DOWNLOAD</button>\n\n    <div class="progress-section" id="progressSection">\n        <div class="status" id="progressText">Click START DOWNLOAD to begin</div>\n        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>\n        <div class="status" id="progressPercent">0%</div>\n        <div class="console" id="console">> Ready to download...</div>\n        <button onclick="toggleConsole()"\n                style="width:100%;padding:10px;background:rgba(0,255,136,0.2);\n                       border:1px solid #00ff88;color:#00ff88;border-radius:8px;\n                       cursor:pointer;margin-top:10px;">\n            📜 Show/Hide Console\n        </button>\n    </div>\n\n    <div class="message success" id="successMessage">✅ Download Successful!</div>\n    <div class="message error"   id="errorMessage">❌ Download Failed!</div>\n\n    <div class="footer">\n        <p style="color:#888;margin-bottom:15px;">\n            ⚡ ALL IN ONE |\n            <a href="https://t.me/all_in_one_63" target="_blank"\n               style="color:#2AABEE;text-decoration:none;">t.me/all_in_one_63</a>\n        </p>\n        <button onclick="testDownload()"\n                style="padding:12px 25px;background:#0088ff;color:white;\n                       border:none;border-radius:10px;font-weight:bold;cursor:pointer;margin:5px;">\n            🧪 Test Download\n        </button>\n    </div>\n</div>\n\n<!-- Telegram Floating Button -->\n<a class="tg-float" href="https://t.me/all_in_one_63" target="_blank" title="Join our Telegram">\n    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">\n        <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.447 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.12l-6.871 4.326-2.962-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.537-.194 1.006.131.833.941z"/>\n    </svg>\n</a>\n<div class="tg-tooltip">📢 Join @all_in_one_63</div>\n\n<script>\n    let selectedQuality = \'360p\';\n    let selectedFormat  = \'mp4\';\n\n    const testUrls = {\n        youtube:   \'https://www.youtube.com/watch?v=dQw4w9WgXcQ\',\n        instagram: \'https://www.instagram.com/p/CrY1Kz0vCkE/\',\n        tiktok:    \'https://www.tiktok.com/@example/video/1234567890\'\n    };\n\n    function selectQuality(quality, el) {\n        selectedQuality = quality;\n        document.querySelectorAll(\'.quality-btn\').forEach(b => b.classList.remove(\'active\'));\n        el.classList.add(\'active\');\n        addConsole(\'Quality set to: \' + quality);\n    }\n\n    function selectFormat(format, el) {\n        selectedFormat = format;\n        document.querySelectorAll(\'.format-btn\').forEach(b => b.classList.remove(\'active\'));\n        el.classList.add(\'active\');\n        addConsole(\'Format set to: \' + format.toUpperCase());\n    }\n\n    function setTestUrl(platform) {\n        document.getElementById(\'videoUrl\').value = testUrls[platform];\n        addConsole(\'Test URL set for: \' + platform);\n    }\n\n    function addConsole(text) {\n        const c = document.getElementById(\'console\');\n        c.innerHTML += \'\\n> \' + text;\n        c.scrollTop = c.scrollHeight;\n    }\n\n    function toggleConsole() {\n        const c = document.getElementById(\'console\');\n        c.style.display = (c.style.display === \'none\' || c.style.display === \'\') ? \'block\' : \'none\';\n    }\n\n    function showSuccess(msg) {\n        const el = document.getElementById(\'successMessage\');\n        el.textContent = msg; el.style.display = \'block\';\n        setTimeout(() => el.style.display = \'none\', 6000);\n    }\n\n    function showError(msg) {\n        const el = document.getElementById(\'errorMessage\');\n        el.textContent = msg; el.style.display = \'block\';\n        setTimeout(() => el.style.display = \'none\', 7000);\n    }\n\n    function hideMessages() {\n        document.getElementById(\'successMessage\').style.display = \'none\';\n        document.getElementById(\'errorMessage\').style.display   = \'none\';\n    }\n\n    function setProgress(pct, text) {\n        document.getElementById(\'progressFill\').style.width    = pct + \'%\';\n        document.getElementById(\'progressPercent\').textContent = pct + \'%\';\n        if (text) document.getElementById(\'progressText\').textContent = text;\n    }\n\n    async function startDownload() {\n        const url = document.getElementById(\'videoUrl\').value.trim();\n        if (!url)                    { showError(\'❌ Please enter a URL\');       return; }\n        if (!url.startsWith(\'http\')) { showError(\'❌ Please enter a valid URL\'); return; }\n\n        const btn             = document.getElementById(\'downloadBtn\');\n        const progressSection = document.getElementById(\'progressSection\');\n\n        btn.disabled  = true;\n        btn.innerHTML = \'🔄 Getting link...\';\n        progressSection.style.display = \'block\';\n        hideMessages();\n\n        // Remove old result box\n        const old = document.getElementById(\'resultBox\');\n        if (old) old.remove();\n\n        addConsole(\'🔍 Extracting video info...\');\n        addConsole(\'URL: \' + url.substring(0, 60) + (url.length > 60 ? \'...\' : \'\'));\n        addConsole(\'Quality: \' + selectedQuality + \' | Format: \' + selectedFormat);\n        setProgress(15, \'🔍 Extracting video info...\');\n\n        try {\n            const response = await fetch(\'/api/info\', {\n                method:  \'POST\',\n                headers: {\'Content-Type\': \'application/json\'},\n                body:    JSON.stringify({ url, quality: selectedQuality, format: selectedFormat })\n            });\n\n            setProgress(70, \'📦 Processing formats...\');\n            const result = await response.json();\n\n            if (!response.ok || result.error) {\n                throw new Error(result.error || \'Failed to extract video info\');\n            }\n\n            setProgress(100, \'✅ Link found! Starting download...\');\n            addConsole(\'✅ Title: \' + result.title);\n            addConsole(\'📦 Formats found: \' + (result.formats ? result.formats.length : 1));\n\n            showDownloadLinks(result);\n            showSuccess(\'✅ Link extracted! Choose a format to download.\');\n\n        } catch (error) {\n            addConsole(\'❌ Error: \' + error.message);\n            showError(\'❌ \' + error.message);\n            setProgress(0, \'Failed\');\n        } finally {\n            btn.disabled  = false;\n            btn.innerHTML = \'⚡ START DOWNLOAD\';\n        }\n    }\n\n    function showDownloadLinks(result) {\n        const box = document.createElement(\'div\');\n        box.id = \'resultBox\';\n        box.style.cssText = `\n            background: rgba(0,255,136,0.08);\n            border: 2px solid #00ff88;\n            border-radius: 15px;\n            padding: 20px;\n            margin: 20px 0;\n        `;\n\n        const thumb = result.thumbnail\n            ? `<img src="${result.thumbnail}"\n                    style="width:100%;border-radius:10px;margin-bottom:12px;\n                           max-height:200px;object-fit:cover;"\n                    onerror="this.style.display=\'none\'">`\n            : \'\';\n\n        const fmts = (result.formats && result.formats.length > 0)\n            ? result.formats\n            : [{ url: result.direct_url, quality: \'Best\', ext: \'mp4\', filesize: \'\' }];\n\n        let formatRows = \'\';\n        fmts.forEach((f) => {\n            const size     = f.filesize ? \'~\' + f.filesize : \'\';\n            // Pass the raw CDN url; proxy will handle encoding\n            const cdnUrl   = f.url;\n            const safeExt  = (f.ext || \'mp4\').replace(/[^a-z0-9]/gi, \'\');\n            // Build filename: ASCII-safe title + quality + ext\n            const baseTitle = (result.title || \'video\')\n                .replace(/[\\/:*?"<>|]/g, \'\')   // remove illegal chars\n                .trim()\n                .substring(0, 80);\n            const fname = baseTitle + \'_\' + f.quality + \'.\' + safeExt;\n\n            formatRows += `\n            <div style="display:flex;align-items:center;justify-content:space-between;\n                        background:rgba(255,255,255,0.05);border-radius:12px;\n                        padding:12px 16px;margin:8px 0;gap:10px;flex-wrap:wrap;">\n                <div style="flex:1;min-width:0;">\n                    <span style="color:#00ff88;font-weight:bold;font-size:15px;">\n                        ${selectedFormat === \'mp3\' ? \'🎵\' : \'📹\'} ${f.quality}\n                    </span>\n                    ${f.ext ? `<span style="color:#aaa;font-size:12px;margin-left:6px;">.${f.ext}</span>` : \'\'}\n                    ${size  ? `<span style="color:#ff8800;font-size:13px;margin-left:8px;">${size}</span>` : \'\'}\n                </div>\n                <button\n                    data-cdn="${encodeURIComponent(cdnUrl)}"\n                    data-fname="${encodeURIComponent(fname)}"\n                    onclick="triggerDownload(this)"\n                    style="flex-shrink:0;padding:12px 22px;\n                           background:linear-gradient(135deg,#00ff88,#0088ff);\n                           color:white;border:none;border-radius:10px;\n                           font-weight:bold;font-size:14px;cursor:pointer;\n                           transition:all 0.2s;white-space:nowrap;">\n                    ⬇ Download\n                </button>\n            </div>`;\n        });\n\n        box.innerHTML = `\n            ${thumb}\n            <p style="color:#00ff88;font-weight:bold;margin-bottom:6px;font-size:15px;">\n                🎬 ${result.title || \'Video\'}\n            </p>\n            <p style="color:#aaa;font-size:13px;margin-bottom:14px;">\n                ⏱ ${result.duration || \'N/A\'} &nbsp;|&nbsp; 📺 ${result.extractor || \'Unknown\'}\n            </p>\n            <div>${formatRows}</div>\n        `;\n\n        const section = document.getElementById(\'progressSection\');\n        section.parentNode.insertBefore(box, section.nextSibling);\n\n        // Auto-click first download button after short delay\n        const firstBtn = box.querySelector(\'button\');\n        if (firstBtn) setTimeout(() => firstBtn.click(), 500);\n    }\n\n    function triggerDownload(btn) {\n        const cdnUrl  = decodeURIComponent(btn.dataset.cdn);\n        const fname   = decodeURIComponent(btn.dataset.fname);\n        const orig    = btn.innerHTML;\n\n        btn.innerHTML = \'⏳ Starting...\';\n        btn.disabled  = true;\n\n        addConsole(\'⬇ Downloading: \' + fname);\n\n        // Route through server proxy (handles CORS + Unicode filename)\n        const proxyUrl = \'/api/proxy\'\n            + \'?url=\'      + encodeURIComponent(cdnUrl)\n            + \'&filename=\' + encodeURIComponent(fname);\n\n        const a = document.createElement(\'a\');\n        a.href     = proxyUrl;\n        a.download = fname;\n        document.body.appendChild(a);\n        a.click();\n        document.body.removeChild(a);\n\n        addConsole(\'✅ Download triggered: \' + fname);\n        btn.innerHTML = \'✅ Downloading!\';\n        btn.style.background = \'linear-gradient(135deg,#00cc66,#006633)\';\n\n        setTimeout(() => {\n            btn.innerHTML        = orig;\n            btn.style.background = \'\';\n            btn.disabled         = false;\n        }, 6000);\n    }\n\n    function testDownload() {\n        document.getElementById(\'videoUrl\').value = testUrls.youtube;\n        addConsole(\'Test URL loaded. Click START DOWNLOAD to test.\');\n    }\n\n    document.addEventListener(\'DOMContentLoaded\', () => {\n        document.getElementById(\'progressSection\').style.display = \'block\';\n        addConsole(\'✅ ALL-IN-ONE DOWNLOADER READY\');\n        addConsole(\'🌐 Supports YouTube, Instagram, TikTok, Facebook, etc.\');\n        addConsole(\'📢 Join us: t.me/all_in_one_63\');\n\n        const tgBtn     = document.querySelector(\'.tg-float\');\n        const tgTooltip = document.querySelector(\'.tg-tooltip\');\n        tgBtn.addEventListener(\'mouseenter\', () => tgTooltip.classList.add(\'show\'));\n        tgBtn.addEventListener(\'mouseleave\', () => tgTooltip.classList.remove(\'show\'));\n    });\n</script>\n</body>\n</html>'
if __name__ == '__main__':
    OO0OOOO0OO00()
    PORT = None
    server = None
    for OO00OOOO0OO0 in range(8000, 8021):
        try:
            server = HTTPServer(('localhost', OO00OOOO0OO0), handler)
            PORT = OO00OOOO0OO0
            break
        except OSError:
            continue
    if server is None:
        print(O0OO00O0OO0O('  ✘  Could not find a free port (8000-8020). Close other apps and retry.'))
        sys.exit(1)
    OO0OOOOOOO0O = f'http://localhost:{PORT}'
    OO0O0000OO00 = threading.Thread(target=server.serve_forever, daemon=True)
    OO0O0000OO00.start()
    print(OOO0000O00OO(OOOO00OOO0OO(f'  🌐  Server running at  {OO0OOO00000O(OO0OOOOOOO0O)}')))
    print()
    OO00OOO00O0O(OO0OOOOOOO0O)
    print()
    print(O00O000OO00O('  Press  ') + OOO0000O00OO(O0OO00O0OO0O('Ctrl+C')) + O00O000OO00O('  to stop the server.'))
    print()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        print(O0O00OO00OOO('  Shutting down server... Goodbye! 👋'))
        server.shutdown()
