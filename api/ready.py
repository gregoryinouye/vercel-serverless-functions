from http.server import BaseHTTPRequestHandler
import os


commitSha = os.environ['VERCEL_GIT_COMMIT_SHA']
deployedHash = "dev" if commitSha == "" else commitSha


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(deployedHash.encode())
        return
