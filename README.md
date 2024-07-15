# SSH Honeypot
<p>A simple SSH honeypot written in Python to log unauthorized login attempts. This project is intended for educational purposes and to help monitor unauthorized access attempts.</p>

<h2>Features</h2>
   <strong>‣ Listens on a configurable port for incoming SSH connections</strong><br>
   <strong>‣ Logs all login attempts with username and password</strong><br>
   <strong>‣ Logs the client's IP address of the connection attempt</strong><br>
   <strong>‣ Provides a fake SSH banner to connected clients</strong>
<h2>Installation</h2>
<h3>Clone the repository</h3>
<code>git clone https://github.com/3ngine/ssh-honeypot</code><br>
<code>cd ssh-honeypot</code><br>
<h3>Generate RSA key</h3>
<code>ssh-keygen -t rsa -f key_rsa.key</code>
<h3>Install requirements</h3>
<code>pip install -r requirements.txt</code>
