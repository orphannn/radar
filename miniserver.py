import http.server
import socketserver
import webbrowser

# 设置默认端口
DEFAULT_PORT = 2333

# 获取用户输入端口，若无输入则使用默认端口
port_input = input(f"请输入端口号（默认 {DEFAULT_PORT}）：")
port = int(port_input) if port_input.isdigit() else DEFAULT_PORT

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    url = f"http://localhost:{port}"
    print(f"服务器已启动，访问地址：{url}")
    webbrowser.open(url)  # 弹出浏览器
    httpd.serve_forever()
