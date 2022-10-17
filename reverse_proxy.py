from pyngrok import ngrok

# open default port (80)
http_tunnel = ngrok.connect(8080)

# ssh tunnel
# ssh_tunnel = ngrok.connect(22, "tcp")

