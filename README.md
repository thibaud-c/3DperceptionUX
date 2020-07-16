# 3DperceptionUX
 User Experiment on 3D perception


##### PROD FRONT
```
npm install
check the config in src/assets/config.json 
npm run build
pm2 start
```

##### PROD Back
```
check the cfg.py
pipenv install
pm2 start ecosystem.config.json
```

### 2 config files to activate (delete the "_example" and add your own data)
back_end/cfg.py
front_end/src/assets/config.json