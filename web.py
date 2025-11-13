#!/usr/bin/env python3
"""
single_file_webpage.py

Run this with: python3 single_file_webpage.py
Then open http://localhost:8000 in your browser.

This is a fully self-contained Python web server that serves a single-page
web application with embedded HTML, CSS and JavaScript (no external links
or files required).
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse

HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Single-file Python Webpage</title>
  <style>
    /* All CSS is embedded here (no external files) */
    :root{--bg:#f6f8fa;--card:#ffffff;--accent:#0b7285;--muted:#6b7280}
    html,body{height:100%;margin:0;font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial}
    body{background:linear-gradient(180deg,var(--bg),#eef2f7);display:flex;align-items:center;justify-content:center;padding:24px}
    .container{width:100%;max-width:980px;background:var(--card);box-shadow:0 8px 30px rgba(11,114,133,0.08);border-radius:12px;overflow:hidden}
    header{padding:28px 32px;border-bottom:1px solid #eef1f4;display:flex;align-items:center;gap:16px}
    .logo{width:48px;height:48px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#4cc9f0);display:flex;align-items:center;justify-content:center;color:white;font-weight:700}
    h1{font-size:20px;margin:0}
    p.lead{margin:4px 0 0;color:var(--muted);font-size:13px}
    main{display:grid;grid-template-columns:1fr 360px;gap:20px;padding:24px}
    .card{background:linear-gradient(180deg,rgba(255,255,255,0.85),rgba(255,255,255,0.9));padding:18px;border-radius:10px}

    /* Left column content */
    .hero{min-height:260px;display:flex;flex-direction:column;gap:12px}
    .hero h2{margin:0}
    .hero p{margin:0;color:var(--muted)}
    .buttons{display:flex;gap:12px;margin-top:12px}
    .btn{padding:10px 14px;border-radius:8px;border:none;cursor:pointer;font-weight:600}
    .btn-primary{background:var(--accent);color:white}
    .btn-outline{background:transparent;border:1px solid #dbe7ea;color:var(--accent)}

    /* Right column */
    .sidebar h3{margin:0 0 12px 0}
    .form-row{display:flex;flex-direction:column;margin-bottom:10px}
    .form-row label{font-size:13px;margin-bottom:6px}
    .form-row input, .form-row textarea{padding:10px;border-radius:8px;border:1px solid #e6edf0}
    .form-row textarea{resize:vertical;min-height:80px}

    footer{padding:16px 24px;border-top:1px solid #eef1f4;color:var(--muted);font-size:13px}

    @media (max-width:880px){
      main{grid-template-columns:1fr;}
      .sidebar{order:2}
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">Py</div>
      <div>
        <h1>Single-file Python Webpage</h1>
        <p class="lead">Served with Python's built-in web server — everything inline, no external links.</p>
      </div>
    </header>

    <main>
      <section class="card hero">
        <h2>Welcome 👋</h2>
        <p>This page is a demonstration of a single-file webpage using only Python's standard library. It includes embedded CSS and JavaScript, client-side interactivity, and a small example form that submits via JavaScript (no server round-trip required).</p>

        <div class="buttons">
          <button class="btn btn-primary" id="sayHello">Say Hello</button>
          <button class="btn btn-outline" id="themeToggle">Toggle Theme</button>
        </div>

        <div id="message" style="margin-top:14px;color:#0b7285;font-weight:600"></div>

        <h3 style="margin-top:18px;">Features</h3>
        <ul style="margin:8px 0 0 18px;color:var(--muted)">
          <li>No external CSS/JS — everything embedded</li>
          <li>Responsive layout that fits mobile and desktop</li>
          <li>Small interactive demo using vanilla JavaScript</li>
        </ul>
      </section>

      <aside class="card sidebar">
        <h3>Contact (demo)</h3>
        <form id="demoForm" onsubmit="return false;">
          <div class="form-row">
            <label for="name">Name</label>
            <input id="name" placeholder="Your name" required />
          </div>
          <div class="form-row">
            <label for="email">Email</label>
            <input id="email" placeholder="you@example.com" required />
          </div>
          <div class="form-row">
            <label for="message">Message</label>
            <textarea id="msg" placeholder="Write a short message"></textarea>
          </div>
          <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:10px">
            <button class="btn btn-outline" type="reset">Reset</button>
            <button class="btn btn-primary" id="submitBtn">Send</button>
          </div>
          <div id="formStatus" style="margin-top:10px;font-size:13px;color:var(--muted)"></div>
        </form>
      </aside>
    </main>

    <footer>
      This is a local demo page — edit the Python file to change content. No assets or CDNs required.
    </footer>
  </div>

  <script>
    // All JS embedded here
    const sayHello = document.getElementById('sayHello')
    const message = document.getElementById('message')
    const themeToggle = document.getElementById('themeToggle')
    const submitBtn = document.getElementById('submitBtn')
    const formStatus = document.getElementById('formStatus')

    sayHello.addEventListener('click', ()=>{
      const now = new Date().toLocaleString()
      message.textContent = `Hello! Current time: ${now}`
    })

    themeToggle.addEventListener('click', ()=>{
      document.documentElement.classList.toggle('dark')
      if(document.documentElement.classList.contains('dark')){
        document.documentElement.style.setProperty('--bg','#0f1724')
        document.documentElement.style.setProperty('--card','#0b1220')
        document.documentElement.style.setProperty('--accent','#7dd3fc')
        document.documentElement.style.setProperty('--muted','#94a3b8')
      } else {
        document.documentElement.style.removeProperty('--bg')
        document.documentElement.style.removeProperty('--card')
        document.documentElement.style.removeProperty('--accent')
        document.documentElement.style.removeProperty('--muted')
      }
    })

    submitBtn.addEventListener('click', ()=>{
      const name = document.getElementById('name').value.trim()
      const email = document.getElementById('email').value.trim()
      const msg = document.getElementById('msg').value.trim()
      if(!name || !email){
        formStatus.textContent = 'Please provide name and email.'
        return
      }
      // Demo: show the submitted data without sending to server
      formStatus.textContent = `Thanks, ${name}! (This demo doesn't send data to a server)`
    })
  </script>
</body>
</html>
"""

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the same page for any GET path (single-page app)
        if self.path.startswith('/favicon'):
            # Return a tiny empty favicon to avoid 404 in some browsers
            self.send_response(200)
            self.send_header('Content-Type','image/x-icon')
            self.end_headers()
            self.wfile.write(b'')
            return

        self.send_response(200)
        self.send_header('Content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML.encode('utf-8'))

    def log_message(self, format, *args):
        # Simple, cleaner logging
        print("[http] %s - - %s" % (self.address_string(), format%args))


def run(host='0.0.0.0', port=8000):
    server = HTTPServer((host, port), SimpleHandler)
    print(f"Serving on http://{host if host!='0.0.0.0' else 'localhost'}:{port} — press CTRL+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down...')
        server.server_close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run single-file Python webpage (no external files).')
    parser.add_argument('--host','-H',default='0.0.0.0',help='Host to listen on (default: 0.0.0.0)')
    parser.add_argument('--port','-p',type=int,default=8000,help='Port to listen on (default: 8000)')
    args = parser.parse_args()
    run(args.host, args.port)
