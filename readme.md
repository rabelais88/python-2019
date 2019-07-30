# 2019 modern python
## setup
[reference](https://gist.github.com/simonw/4835a22c79a8d3c29dd155c716b19e16)
```bash
python3 -m venv ./venv/
. ./venv/bin/activate
pip3 install -r requirements.txt
# deactivate venv
deactivate
```
## installing & running *jupyter notebook* on venv
```bash
# (activate venv first)
pip3 install ipython
ipython kernel install --user --name=.venv
# running jupyter
jupyter notebook
```

## save
```bash
pip3 freeze > requirements.txt
```

## caveat
avoid using native Python names(def, lambda, decorator...) for project names. it'll crash jupyter notebook's kernel.