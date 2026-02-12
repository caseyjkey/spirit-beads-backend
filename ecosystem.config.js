module.exports = {
  apps: [{
    name: 'spirit-beads-service',
    script: './venv/bin/python',
    args: 'manage.py runserver 0.0.0.0:8000',
    cwd: '/var/www/spirit-beads-service',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production'
    }
  }]
};
