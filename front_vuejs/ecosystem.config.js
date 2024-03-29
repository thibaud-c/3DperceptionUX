module.exports = {
  apps : [{
    name: 'perc-front',
    script: 'serve -s dist -l 8080',

    // Options reference: https://pm2.keymetrics.io/docs/usage/application-declaration/
    args: 'one two',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production'
    }
  }],
};
