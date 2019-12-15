consul {
address = "con-agent-3:8500"
retry {
enabled = true
attempts = 12
backoff = "250ms"

}
template {
source      = "/opt/nginx/conf.d/load-balancer.conf.ctmpl"
destination = "/opt/nginx/conf.d/load-balancer.conf"
perms = 0600
command = "service nginx reload"
}
