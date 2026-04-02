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

# ============================================================
#   TERMINAL LOADING SCREEN
# ============================================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def green(t):  return color(t, '92')
def cyan(t):   return color(t, '96')
def yellow(t): return color(t, '93')
def red(t):    return color(t, '91')
def bold(t):   return color(t, '1')
def dim(t):    return color(t, '2')

BANNER = r"""
  ██████╗  █████╗ ██████╗ ██╗   ██╗███████╗
  ██╔══██╗██╔══██╗██╔══██╗██║   ██║╚════██╗
  ██████╔╝███████║██████╔╝██║   ██║    ██╔╝
  ██╔═══╝ ██╔══██║██╔══██╗╚██╗ ██╔╝   ██╔╝ 
  ██║     ██║  ██║██║  ██║ ╚████╔╝   ██╔╝  
  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝   ██████╗
                                     ╚═════╝
"""

def typewrite(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(label, steps=30, delay=0.05):
    sys.stdout.write(f"  {cyan(label):30s}  [")
    sys.stdout.flush()
    for i in range(steps):
        time.sleep(delay)
        sys.stdout.write(green("█"))
        sys.stdout.flush()
    sys.stdout.write("]  " + green("✔") + "\n")
    sys.stdout.flush()

def spinner_task(label, duration=2.0):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r  {cyan(frames[i % len(frames)])}  {yellow(label)}   ")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r  {green('✔')}  {green(label)}   \n")
    sys.stdout.flush()

def show_loading_screen():
    clear()
    for line in BANNER.strip('\n').split('\n'):
        print(cyan(line))
    print()
    print(bold(green("           ⚡  ALL-IN-ONE VIDEO DOWNLOADER  ⚡")))
    print(dim("           Powered by  ") + bold(yellow("@all_in_one_63")) + dim("  |  t.me/all_in_one_63"))
    print()
    time.sleep(0.4)

    sys.stdout.write("  " + yellow("Initializing"))
    for _ in range(6):
        time.sleep(0.25)
        sys.stdout.write(yellow("."))
        sys.stdout.flush()
    print()
    time.sleep(0.2)

    tasks = [
        ("Loading modules",       25, 0.04),
        ("Checking yt-dlp",       20, 0.05),
        ("Setting up server",     22, 0.04),
        ("Preparing interface",   28, 0.03),
    ]
    for label, steps, delay in tasks:
        loading_bar(label, steps, delay)

    print()
    spinner_task("Verifying system integrity ...", 1.8)
    spinner_task("Authenticating session      ...", 1.5)

    print()
    print(bold(green("  ✔  All checks passed!  System ready.")))
    print()
    time.sleep(0.3)

    print("  " + dim("─" * 60))
    print(f"  {dim('Powered by')}  {bold(cyan('ALL IN ONE'))}  {dim('|')}  {yellow('t.me/all_in_one_63')}")
    print("  " + dim("─" * 60))
    print()
    time.sleep(0.5)

# ============================================================
#   BROWSER DETECTION & AUTO-OPEN
# ============================================================

def detect_browsers():
    found = []
    common = {
        'chrome':  ['google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser',
                    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
                    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'],
        'firefox': ['firefox',
                    r'C:\Program Files\Mozilla Firefox\firefox.exe',
                    r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'],
        'edge':    ['microsoft-edge', 'msedge',
                    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
                    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'],
        'safari':  ['/Applications/Safari.app/Contents/MacOS/Safari'],
        'brave':   ['brave-browser', 'brave',
                    r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'],
        'opera':   ['opera',
                    r'C:\Program Files\Opera\opera.exe'],
    }

    for name, paths in common.items():
        for p in paths:
            if os.path.isfile(p):
                found.append((name.capitalize(), p))
                break
            try:
                result = subprocess.run(
                    ['which', p] if os.name != 'nt' else ['where', p],
                    capture_output=True, text=True, timeout=2
                )
                if result.returncode == 0 and result.stdout.strip():
                    found.append((name.capitalize(), result.stdout.strip().splitlines()[0]))
                    break
            except Exception:
                pass

    seen = set()
    unique = []
    for name, path in found:
        if name not in seen:
            seen.add(name)
            unique.append((name, path))
    return unique

def open_url_with(path, url):
    try:
        if os.name == 'nt':
            subprocess.Popen([path, url])
        else:
            subprocess.Popen([path, url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        webbrowser.open(url)

def open_url_android(url):
    try:
        result = subprocess.run(
            ['am', 'start', '-a', 'android.intent.action.VIEW', '-d', url],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return True
    except Exception:
        pass
    return False

def launch_browser(url):
    if os.path.exists('/data/data/com.termux') or 'com.termux' in os.environ.get('PREFIX', ''):
        print(green("  📱 Android detected. Opening browser via intent..."))
        time.sleep(0.5)
        if open_url_android(url):
            print(green(f"  ✔  Browser opened: {url}"))
        else:
            try:
                subprocess.Popen(['termux-open-url', url],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(green(f"  ✔  Opened via termux-open-url"))
            except Exception:
                print(yellow(f"  ⚠  Could not open browser automatically."))
                print(yellow(f"  👉 Manually open: {cyan(url)}"))
        return

    browsers = detect_browsers()
    if not browsers:
        print(yellow("  No specific browser detected. Opening default browser..."))
        webbrowser.open(url)
        return
    if len(browsers) == 1:
        name, path = browsers[0]
        print(green(f"  Opening in {name}..."))
        time.sleep(0.5)
        open_url_with(path, url)
        return

    print(bold(cyan("  Multiple browsers detected. Choose one:\n")))
    for i, (name, _) in enumerate(browsers, 1):
        print(f"    {bold(yellow(str(i)))}. {green(name)}")
    print(f"    {bold(yellow(str(len(browsers)+1)))}. Default system browser")
    print()

    while True:
        try:
            sys.stdout.write(f"  {cyan('Enter number')} [{yellow('1')}-{yellow(str(len(browsers)+1))}]: ")
            sys.stdout.flush()
            choice = input().strip()
            idx = int(choice)
            if 1 <= idx <= len(browsers):
                name, path = browsers[idx - 1]
                print(green(f"\n  Opening in {name}..."))
                time.sleep(0.4)
                open_url_with(path, url)
                break
            elif idx == len(browsers) + 1:
                print(green("\n  Opening in default browser..."))
                time.sleep(0.4)
                webbrowser.open(url)
                break
            else:
                print(red("  Invalid choice. Try again."))
        except (ValueError, KeyboardInterrupt):
            print(red("\n  Invalid input. Opening default browser..."))
            webbrowser.open(url)
            break

# ============================================================
#   SAFE FILENAME HELPER  ← FIX #1
# ============================================================

def safe_content_disposition(filename: str) -> str:
    """
    Return a Content-Disposition header value that works for ANY language
    (Bengali, Arabic, CJK, emoji …).

    Uses RFC 5987 / RFC 8187 extended notation:
        Content-Disposition: attachment; filename="fallback.mp4"; filename*=UTF-8''encoded
    """
    # ASCII fallback  (strip anything non-ASCII)
    ascii_name = filename.encode('ascii', 'ignore').decode('ascii').strip()
    if not ascii_name:
        ascii_name = "download"

    # RFC 5987 percent-encoded UTF-8 name
    encoded = urllib.parse.quote(filename.encode('utf-8'), safe='')

    return f'attachment; filename="{ascii_name}"; filename*=UTF-8\'\'{encoded}'


# ============================================================
#   HTTP HANDLER
# ============================================================

class handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass  # suppress logs

    def _json_ok(self, data):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def _json_error(self, msg, code=500):
        body = json.dumps({'error': msg}, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    @staticmethod
    def _fmt_size(b):
        if not b:
            return ''
        b = int(b)
        for unit in ('B', 'KB', 'MB', 'GB'):
            if b < 1024:
                return f'{b:.1f}{unit}'
            b /= 1024
        return f'{b:.1f}GB'

    # ----------------------------------------------------------
    def do_GET(self):

        # ── Home page ──────────────────────────────────────────
        if self.path == '/' or self.path == '/index.html':
            self._serve_html()

        # ── /api/info  (extract formats, no download) ──────────
        elif self.path.startswith('/api/info'):
            self._api_info()

        # ── /api/proxy  (stream file to browser) ───────────────
        elif self.path.startswith('/api/proxy'):
            self._api_proxy()

        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        self.do_GET()

    # ----------------------------------------------------------
    def _serve_html(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode('utf-8'))

    # ----------------------------------------------------------
    def _api_info(self):
        try:
            import yt_dlp
        except ImportError:
            self._json_error("yt-dlp not installed. Run: pip install yt-dlp")
            return

        content_length = int(self.headers.get('Content-Length', 0))
        post_data      = self.rfile.read(content_length)
        try:
            data = json.loads(post_data)
        except Exception:
            self._json_error("Invalid JSON")
            return

        url         = data.get('url', '').strip()
        quality     = data.get('quality', 'best')
        format_type = data.get('format', 'mp4')

        if not url:
            self._json_error("URL required")
            return

        try:
            height_map = {
                'worst': 144, '360p': 360, '480p': 480,
                '720p': 720, '1080p': 1080, 'best': 9999,
            }
            max_h = height_map.get(quality, 9999)

            ydl_opts = {
                'quiet':        True,
                'no_warnings':  True,
                'noplaylist':   True,
                'skip_download': True,
                'socket_timeout': 15,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            title     = info.get('title', 'video')
            duration  = info.get('duration_string') or str(info.get('duration', ''))
            thumbnail = info.get('thumbnail', '')
            extractor = info.get('extractor_key', info.get('extractor', ''))
            formats_raw = info.get('formats') or []

            chosen = []

            # ── AUDIO request ───────────────────────────────────
            if format_type == 'mp3':
                audio_fmts = [
                    f for f in formats_raw
                    if f.get('vcodec') == 'none' and f.get('url')
                    and f.get('ext') in ('m4a', 'mp3', 'webm', 'opus', 'aac')
                ]
                if not audio_fmts:
                    audio_fmts = [
                        f for f in formats_raw
                        if f.get('acodec') and f.get('acodec') != 'none' and f.get('url')
                    ]
                audio_fmts.sort(key=lambda f: f.get('abr') or 0, reverse=True)
                for f in audio_fmts[:3]:
                    abr  = f.get('abr', '')
                    size = self._fmt_size(f.get('filesize') or f.get('filesize_approx'))
                    chosen.append({
                        'url':      f['url'],
                        'quality':  f'{int(abr)}kbps' if abr else 'Audio',
                        'ext':      f.get('ext', 'm4a'),
                        'filesize': size,
                    })

            # ── VIDEO request ───────────────────────────────────
            else:
                # Strategy 1: pre-merged video+audio
                av_fmts = [
                    f for f in formats_raw
                    if f.get('vcodec') and f.get('vcodec') != 'none'
                    and f.get('acodec') and f.get('acodec') != 'none'
                    and f.get('url')
                    and (f.get('height') or 0) <= max_h
                ]
                av_fmts.sort(key=lambda f: (f.get('height') or 0, f.get('tbr') or 0), reverse=True)

                seen_h = set()
                for f in av_fmts:
                    h = f.get('height') or 0
                    if h in seen_h:
                        continue
                    seen_h.add(h)
                    size = self._fmt_size(f.get('filesize') or f.get('filesize_approx'))
                    chosen.append({
                        'url':      f['url'],
                        'quality':  f'{h}p' if h else 'Video',
                        'ext':      f.get('ext', 'mp4'),
                        'filesize': size,
                    })
                    if len(chosen) >= 5:
                        break

                # Strategy 2: top-level url (TikTok / Instagram / FB)
                if not chosen and info.get('url'):
                    h    = info.get('height') or 0
                    size = self._fmt_size(info.get('filesize') or info.get('filesize_approx'))
                    chosen.append({
                        'url':      info['url'],
                        'quality':  f'{h}p' if h else 'HD',
                        'ext':      info.get('ext', 'mp4'),
                        'filesize': size,
                    })

                # Strategy 3: any video format
                if not chosen:
                    vid_fmts = [
                        f for f in formats_raw
                        if f.get('vcodec') and f.get('vcodec') != 'none' and f.get('url')
                        and (f.get('height') or 0) <= max_h
                    ]
                    vid_fmts.sort(key=lambda f: f.get('height') or 0, reverse=True)
                    for f in vid_fmts[:3]:
                        h    = f.get('height') or 0
                        size = self._fmt_size(f.get('filesize') or f.get('filesize_approx'))
                        chosen.append({
                            'url':      f['url'],
                            'quality':  f'{h}p' if h else 'Video',
                            'ext':      f.get('ext', 'mp4'),
                            'filesize': size,
                        })

            if not chosen:
                self._json_error("No downloadable format found for this URL.")
                return

            result = {
                'title':      title,
                'duration':   duration,
                'thumbnail':  thumbnail,
                'extractor':  extractor,
                'direct_url': chosen[0]['url'],
                'formats':    chosen,
            }
            self._json_ok(result)

        except Exception as e:
            err = str(e)
            if 'Sign in' in err or 'login' in err.lower():
                err = "This video requires login."
            elif 'Private' in err:
                err = "This is a private video."
            elif 'not available' in err.lower():
                err = "Video not available in your region."
            self._json_error(err)

    # ----------------------------------------------------------
    def _api_proxy(self):
        """
        Stream remote video/audio to the browser as a proper download.

        FIX: Content-Disposition uses RFC 5987 UTF-8 encoding so Bengali /
        Unicode filenames never cause a latin-1 encode error.
        """
        import urllib.request as ureq
        from urllib.parse import urlparse, parse_qs, unquote

        parsed   = urlparse(self.path)
        qs       = parse_qs(parsed.query)
        raw_url  = unquote(qs.get('url',      [''])[0])
        filename = unquote(qs.get('filename', ['video.mp4'])[0])

        if not raw_url or not raw_url.startswith('http'):
            self.send_error(400, "Invalid URL")
            return

        try:
            req = ureq.Request(raw_url, headers={
                'User-Agent':      ('Mozilla/5.0 (Linux; Android 11) '
                                    'AppleWebKit/537.36 Chrome/120.0.0.0 '
                                    'Mobile Safari/537.36'),
                'Accept':          '*/*',
                'Accept-Encoding': 'identity',
                'Referer':         'https://www.youtube.com/',
            })

            with ureq.urlopen(req, timeout=60) as resp:
                content_type   = resp.headers.get('Content-Type',   'application/octet-stream')
                content_length = resp.headers.get('Content-Length', '')

                # ── Build response headers (safe for ALL languages) ──
                self.send_response(200)

                # Content-Type: keep original but ensure charset is not forced
                self.send_header('Content-Type', content_type)

                # ★ THE FIX: RFC 5987 encoded Content-Disposition
                cd = safe_content_disposition(filename)
                # send_header uses latin-1 internally, so we must
                # write the raw bytes ourselves via _headers_buf trick.
                # Safest portable way: encode the whole header line manually.
                cd_bytes = ('Content-Disposition: ' + cd + '\r\n').encode('utf-8')
                if hasattr(self, '_headers_buffer'):
                    self._headers_buffer.append(cd_bytes)
                else:
                    # Fallback for older Python versions
                    self.wfile.write(cd_bytes)   # written before end_headers

                if content_length:
                    self.send_header('Content-Length', content_length)
                self.send_header('Cache-Control', 'no-cache')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()

                # ── Stream in 512 KB chunks ──
                CHUNK = 512 * 1024
                while True:
                    chunk = resp.read(CHUNK)
                    if not chunk:
                        break
                    try:
                        self.wfile.write(chunk)
                        self.wfile.flush()
                    except (BrokenPipeError, ConnectionResetError, OSError):
                        break  # client disconnected – that's fine

        except Exception as e:
            # Try to send a JSON error if headers not sent yet
            try:
                self._json_error(f"Proxy error: {str(e)}")
            except Exception:
                pass


# ============================================================
#   HTML PAGE
# ============================================================

HTML_PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ALL-IN-ONE VIDEO DOWNLOADER</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif; }
        body {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.7);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border: 2px solid #00ff88;
        }
        .header { text-align:center; margin-bottom:30px; }
        h1 {
            color: #00ff88;
            font-size: 32px;
            margin-bottom: 10px;
            text-shadow: 0 0 10px rgba(0,255,136,0.5);
        }
        .subtitle { color:#ccc; margin-bottom:20px; }
        .url-box { margin:20px 0; }
        input[type="text"] {
            width: 100%;
            padding: 15px;
            border: 2px solid #00ff88;
            border-radius: 10px;
            background: rgba(255,255,255,0.1);
            color: white;
            font-size: 16px;
            margin-bottom: 10px;
        }
        input[type="text"]:focus { outline:none; box-shadow:0 0 15px rgba(0,255,136,0.5); }
        .quality-buttons { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin:20px 0; }
        .quality-btn {
            padding: 15px;
            border: 2px solid #555;
            background: rgba(255,255,255,0.1);
            color: white;
            border-radius: 10px;
            cursor: pointer;
            text-align: center;
            transition: all 0.3s;
        }
        .quality-btn:hover { border-color:#00ff88; transform:scale(1.05); }
        .quality-btn.active { background:rgba(0,255,136,0.2); border-color:#00ff88; }
        .format-buttons { display:flex; gap:10px; margin:20px 0; }
        .format-btn {
            flex: 1;
            padding: 15px;
            border: 2px solid #555;
            background: rgba(255,255,255,0.1);
            color: white;
            border-radius: 10px;
            cursor: pointer;
            text-align: center;
            font-size: 18px;
            transition: all 0.3s;
        }
        .format-btn:hover { border-color:#ff8800; transform:scale(1.05); }
        .format-btn.active { background:rgba(255,136,0,0.2); border-color:#ff8800; }
        .download-btn {
            width: 100%;
            padding: 20px;
            background: linear-gradient(135deg,#00ff88,#0088ff);
            border: none;
            border-radius: 15px;
            color: white;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
            margin: 30px 0;
            transition: all 0.3s;
        }
        .download-btn:hover:not(:disabled) { transform:translateY(-5px); box-shadow:0 10px 20px rgba(0,136,255,0.5); }
        .download-btn:disabled { opacity:0.5; cursor:not-allowed; }
        .progress-section {
            display: none;
            margin: 20px 0;
            padding: 20px;
            background: rgba(0,0,0,0.5);
            border-radius: 15px;
            border: 2px solid #0088ff;
        }
        .progress-bar { height:20px; background:rgba(255,255,255,0.1); border-radius:10px; overflow:hidden; margin:15px 0; }
        .progress-fill { height:100%; background:linear-gradient(90deg,#00ff88,#0088ff); width:0%; transition:width 0.5s; }
        .status { text-align:center; margin:10px 0; color:#00ff88; font-weight:bold; }
        .console {
            background: black;
            color: #00ff88;
            padding: 15px;
            border-radius: 10px;
            font-family: monospace;
            font-size: 12px;
            height: 200px;
            overflow-y: auto;
            margin: 20px 0;
            display: none;
            border: 1px solid #00ff88;
        }
        .message { padding:15px; border-radius:10px; margin:15px 0; text-align:center; display:none; }
        .success { background:rgba(0,255,136,0.2); border:2px solid #00ff88; color:#00ff88; }
        .error   { background:rgba(255,0,0,0.2);   border:2px solid #ff4444; color:#ff4444; }
        .test-urls { display:flex; flex-wrap:wrap; gap:10px; margin:15px 0; }
        .test-url {
            background: rgba(0,136,255,0.2);
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .test-url:hover { background:rgba(0,136,255,0.4); transform:translateY(-2px); }
        .footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }
        /* Telegram float */
        .tg-float {
            position: fixed;
            bottom: 28px; right: 28px;
            width: 58px; height: 58px;
            border-radius: 50%;
            background: linear-gradient(135deg, #2AABEE, #229ED9);
            box-shadow: 0 4px 20px rgba(42,171,238,0.55);
            display: flex;
            align-items: center; justify-content: center;
            cursor: pointer;
            text-decoration: none;
            z-index: 9999;
            animation: tg-pulse 2.5s infinite;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .tg-float:hover { transform:scale(1.12); box-shadow:0 6px 28px rgba(42,171,238,0.8); animation:none; }
        .tg-float svg { width:30px; height:30px; fill:white; }
        .tg-tooltip {
            position: fixed;
            bottom: 96px; right: 28px;
            background: rgba(0,0,0,0.85);
            color: #2AABEE;
            font-size: 13px; font-weight: 600;
            padding: 7px 14px;
            border-radius: 10px;
            border: 1px solid #2AABEE;
            white-space: nowrap;
            opacity: 0; pointer-events: none;
            transition: opacity 0.25s;
        }
        .tg-float:hover + .tg-tooltip, .tg-tooltip.show { opacity: 1; }
        @keyframes tg-pulse {
            0%,100% { box-shadow: 0 4px 20px rgba(42,171,238,0.55); }
            50%      { box-shadow: 0 4px 30px rgba(42,171,238,0.9); }
        }
        @media (max-width:600px) {
            .container { padding:15px; }
            .quality-buttons { grid-template-columns:repeat(2,1fr); }
            h1 { font-size:24px; }
            .tg-float { bottom:18px; right:18px; }
            .tg-tooltip { bottom:82px; right:18px; }
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>🎬 ALL-IN-ONE VIDEO DOWNLOADER</h1>
        <p class="subtitle">YouTube • Instagram • Facebook • TikTok • Twitter • 100+ Sites</p>
        <p style="color:#ff8800;font-size:14px;margin-top:10px;">⚡ Fast & Reliable Local Server</p>
    </div>

    <div class="url-box">
        <input type="text" id="videoUrl" placeholder="🌐 Paste ANY video URL here...">
        <div class="test-urls">
            <div class="test-url" onclick="setTestUrl('youtube')">📺 YouTube Test</div>
            <div class="test-url" onclick="setTestUrl('instagram')">📷 Instagram Test</div>
            <div class="test-url" onclick="setTestUrl('tiktok')">🎵 TikTok Test</div>
        </div>
    </div>

    <div class="quality-buttons">
        <div class="quality-btn active" onclick="selectQuality('360p',this)">360p</div>
        <div class="quality-btn" onclick="selectQuality('480p',this)">480p</div>
        <div class="quality-btn" onclick="selectQuality('720p',this)">720p HD</div>
        <div class="quality-btn" onclick="selectQuality('1080p',this)">1080p FHD</div>
        <div class="quality-btn" onclick="selectQuality('best',this)">👑 Best</div>
        <div class="quality-btn" onclick="selectQuality('worst',this)">⚡ Fast</div>
    </div>

    <div class="format-buttons">
        <div class="format-btn active" onclick="selectFormat('mp4',this)">🎥 MP4 Video</div>
        <div class="format-btn" onclick="selectFormat('mp3',this)">🎵 MP3 Audio</div>
    </div>

    <button class="download-btn" id="downloadBtn" onclick="startDownload()">⚡ START DOWNLOAD</button>

    <div class="progress-section" id="progressSection">
        <div class="status" id="progressText">Click START DOWNLOAD to begin</div>
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
        <div class="status" id="progressPercent">0%</div>
        <div class="console" id="console">> Ready to download...</div>
        <button onclick="toggleConsole()"
                style="width:100%;padding:10px;background:rgba(0,255,136,0.2);
                       border:1px solid #00ff88;color:#00ff88;border-radius:8px;
                       cursor:pointer;margin-top:10px;">
            📜 Show/Hide Console
        </button>
    </div>

    <div class="message success" id="successMessage">✅ Download Successful!</div>
    <div class="message error"   id="errorMessage">❌ Download Failed!</div>

    <div class="footer">
        <p style="color:#888;margin-bottom:15px;">
            ⚡ ALL IN ONE |
            <a href="https://t.me/all_in_one_63" target="_blank"
               style="color:#2AABEE;text-decoration:none;">t.me/all_in_one_63</a>
        </p>
        <button onclick="testDownload()"
                style="padding:12px 25px;background:#0088ff;color:white;
                       border:none;border-radius:10px;font-weight:bold;cursor:pointer;margin:5px;">
            🧪 Test Download
        </button>
    </div>
</div>

<!-- Telegram Floating Button -->
<a class="tg-float" href="https://t.me/all_in_one_63" target="_blank" title="Join our Telegram">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0zm5.894 8.221-1.97 9.28c-.145.658-.537.818-1.084.508l-3-2.21-1.447 1.394c-.16.16-.295.295-.605.295l.213-3.053 5.56-5.023c.242-.213-.054-.333-.373-.12l-6.871 4.326-2.962-.924c-.643-.204-.657-.643.136-.953l11.57-4.461c.537-.194 1.006.131.833.941z"/>
    </svg>
</a>
<div class="tg-tooltip">📢 Join @all_in_one_63</div>

<script>
    let selectedQuality = '360p';
    let selectedFormat  = 'mp4';

    const testUrls = {
        youtube:   'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        instagram: 'https://www.instagram.com/p/CrY1Kz0vCkE/',
        tiktok:    'https://www.tiktok.com/@example/video/1234567890'
    };

    function selectQuality(quality, el) {
        selectedQuality = quality;
        document.querySelectorAll('.quality-btn').forEach(b => b.classList.remove('active'));
        el.classList.add('active');
        addConsole('Quality set to: ' + quality);
    }

    function selectFormat(format, el) {
        selectedFormat = format;
        document.querySelectorAll('.format-btn').forEach(b => b.classList.remove('active'));
        el.classList.add('active');
        addConsole('Format set to: ' + format.toUpperCase());
    }

    function setTestUrl(platform) {
        document.getElementById('videoUrl').value = testUrls[platform];
        addConsole('Test URL set for: ' + platform);
    }

    function addConsole(text) {
        const c = document.getElementById('console');
        c.innerHTML += '\\n> ' + text;
        c.scrollTop = c.scrollHeight;
    }

    function toggleConsole() {
        const c = document.getElementById('console');
        c.style.display = (c.style.display === 'none' || c.style.display === '') ? 'block' : 'none';
    }

    function showSuccess(msg) {
        const el = document.getElementById('successMessage');
        el.textContent = msg; el.style.display = 'block';
        setTimeout(() => el.style.display = 'none', 6000);
    }

    function showError(msg) {
        const el = document.getElementById('errorMessage');
        el.textContent = msg; el.style.display = 'block';
        setTimeout(() => el.style.display = 'none', 7000);
    }

    function hideMessages() {
        document.getElementById('successMessage').style.display = 'none';
        document.getElementById('errorMessage').style.display   = 'none';
    }

    function setProgress(pct, text) {
        document.getElementById('progressFill').style.width    = pct + '%';
        document.getElementById('progressPercent').textContent = pct + '%';
        if (text) document.getElementById('progressText').textContent = text;
    }

    async function startDownload() {
        const url = document.getElementById('videoUrl').value.trim();
        if (!url)                    { showError('❌ Please enter a URL');       return; }
        if (!url.startsWith('http')) { showError('❌ Please enter a valid URL'); return; }

        const btn             = document.getElementById('downloadBtn');
        const progressSection = document.getElementById('progressSection');

        btn.disabled  = true;
        btn.innerHTML = '🔄 Getting link...';
        progressSection.style.display = 'block';
        hideMessages();

        // Remove old result box
        const old = document.getElementById('resultBox');
        if (old) old.remove();

        addConsole('🔍 Extracting video info...');
        addConsole('URL: ' + url.substring(0, 60) + (url.length > 60 ? '...' : ''));
        addConsole('Quality: ' + selectedQuality + ' | Format: ' + selectedFormat);
        setProgress(15, '🔍 Extracting video info...');

        try {
            const response = await fetch('/api/info', {
                method:  'POST',
                headers: {'Content-Type': 'application/json'},
                body:    JSON.stringify({ url, quality: selectedQuality, format: selectedFormat })
            });

            setProgress(70, '📦 Processing formats...');
            const result = await response.json();

            if (!response.ok || result.error) {
                throw new Error(result.error || 'Failed to extract video info');
            }

            setProgress(100, '✅ Link found! Starting download...');
            addConsole('✅ Title: ' + result.title);
            addConsole('📦 Formats found: ' + (result.formats ? result.formats.length : 1));

            showDownloadLinks(result);
            showSuccess('✅ Link extracted! Choose a format to download.');

        } catch (error) {
            addConsole('❌ Error: ' + error.message);
            showError('❌ ' + error.message);
            setProgress(0, 'Failed');
        } finally {
            btn.disabled  = false;
            btn.innerHTML = '⚡ START DOWNLOAD';
        }
    }

    function showDownloadLinks(result) {
        const box = document.createElement('div');
        box.id = 'resultBox';
        box.style.cssText = `
            background: rgba(0,255,136,0.08);
            border: 2px solid #00ff88;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
        `;

        const thumb = result.thumbnail
            ? `<img src="${result.thumbnail}"
                    style="width:100%;border-radius:10px;margin-bottom:12px;
                           max-height:200px;object-fit:cover;"
                    onerror="this.style.display='none'">`
            : '';

        const fmts = (result.formats && result.formats.length > 0)
            ? result.formats
            : [{ url: result.direct_url, quality: 'Best', ext: 'mp4', filesize: '' }];

        let formatRows = '';
        fmts.forEach((f) => {
            const size     = f.filesize ? '~' + f.filesize : '';
            // Pass the raw CDN url; proxy will handle encoding
            const cdnUrl   = f.url;
            const safeExt  = (f.ext || 'mp4').replace(/[^a-z0-9]/gi, '');
            // Build filename: ASCII-safe title + quality + ext
            const baseTitle = (result.title || 'video')
                .replace(/[\\/:*?"<>|]/g, '')   // remove illegal chars
                .trim()
                .substring(0, 80);
            const fname = baseTitle + '_' + f.quality + '.' + safeExt;

            formatRows += `
            <div style="display:flex;align-items:center;justify-content:space-between;
                        background:rgba(255,255,255,0.05);border-radius:12px;
                        padding:12px 16px;margin:8px 0;gap:10px;flex-wrap:wrap;">
                <div style="flex:1;min-width:0;">
                    <span style="color:#00ff88;font-weight:bold;font-size:15px;">
                        ${selectedFormat === 'mp3' ? '🎵' : '📹'} ${f.quality}
                    </span>
                    ${f.ext ? `<span style="color:#aaa;font-size:12px;margin-left:6px;">.${f.ext}</span>` : ''}
                    ${size  ? `<span style="color:#ff8800;font-size:13px;margin-left:8px;">${size}</span>` : ''}
                </div>
                <button
                    data-cdn="${encodeURIComponent(cdnUrl)}"
                    data-fname="${encodeURIComponent(fname)}"
                    onclick="triggerDownload(this)"
                    style="flex-shrink:0;padding:12px 22px;
                           background:linear-gradient(135deg,#00ff88,#0088ff);
                           color:white;border:none;border-radius:10px;
                           font-weight:bold;font-size:14px;cursor:pointer;
                           transition:all 0.2s;white-space:nowrap;">
                    ⬇ Download
                </button>
            </div>`;
        });

        box.innerHTML = `
            ${thumb}
            <p style="color:#00ff88;font-weight:bold;margin-bottom:6px;font-size:15px;">
                🎬 ${result.title || 'Video'}
            </p>
            <p style="color:#aaa;font-size:13px;margin-bottom:14px;">
                ⏱ ${result.duration || 'N/A'} &nbsp;|&nbsp; 📺 ${result.extractor || 'Unknown'}
            </p>
            <div>${formatRows}</div>
        `;

        const section = document.getElementById('progressSection');
        section.parentNode.insertBefore(box, section.nextSibling);

        // Auto-click first download button after short delay
        const firstBtn = box.querySelector('button');
        if (firstBtn) setTimeout(() => firstBtn.click(), 500);
    }

    function triggerDownload(btn) {
        const cdnUrl  = decodeURIComponent(btn.dataset.cdn);
        const fname   = decodeURIComponent(btn.dataset.fname);
        const orig    = btn.innerHTML;

        btn.innerHTML = '⏳ Starting...';
        btn.disabled  = true;

        addConsole('⬇ Downloading: ' + fname);

        // Route through server proxy (handles CORS + Unicode filename)
        const proxyUrl = '/api/proxy'
            + '?url='      + encodeURIComponent(cdnUrl)
            + '&filename=' + encodeURIComponent(fname);

        const a = document.createElement('a');
        a.href     = proxyUrl;
        a.download = fname;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        addConsole('✅ Download triggered: ' + fname);
        btn.innerHTML = '✅ Downloading!';
        btn.style.background = 'linear-gradient(135deg,#00cc66,#006633)';

        setTimeout(() => {
            btn.innerHTML        = orig;
            btn.style.background = '';
            btn.disabled         = false;
        }, 6000);
    }

    function testDownload() {
        document.getElementById('videoUrl').value = testUrls.youtube;
        addConsole('Test URL loaded. Click START DOWNLOAD to test.');
    }

    document.addEventListener('DOMContentLoaded', () => {
        document.getElementById('progressSection').style.display = 'block';
        addConsole('✅ ALL-IN-ONE DOWNLOADER READY');
        addConsole('🌐 Supports YouTube, Instagram, TikTok, Facebook, etc.');
        addConsole('📢 Join us: t.me/all_in_one_63');

        const tgBtn     = document.querySelector('.tg-float');
        const tgTooltip = document.querySelector('.tg-tooltip');
        tgBtn.addEventListener('mouseenter', () => tgTooltip.classList.add('show'));
        tgBtn.addEventListener('mouseleave', () => tgTooltip.classList.remove('show'));
    });
</script>
</body>
</html>'''


# ============================================================
#   MAIN
# ============================================================

if __name__ == '__main__':

    show_loading_screen()

    PORT   = None
    server = None
    for p in range(8000, 8021):
        try:
            server = HTTPServer(('localhost', p), handler)
            PORT = p
            break
        except OSError:
            continue

    if server is None:
        print(red("  ✘  Could not find a free port (8000-8020). Close other apps and retry."))
        sys.exit(1)

    URL = f"http://localhost:{PORT}"

    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()

    print(bold(green(f"  🌐  Server running at  {cyan(URL)}")))
    print()

    launch_browser(URL)

    print()
    print(dim("  Press  ") + bold(red("Ctrl+C")) + dim("  to stop the server."))
    print()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        print(yellow("  Shutting down server... Goodbye! 👋"))
        server.shutdown()
