
.PHONY: env
env:
    mamba env create -f environment.yml -p ~/envs/ligo
    conda activate ~/envs/ligo
    python -m ipykernel install --user --name ligo --display-name "ligo"
    
    
    
    
.PHONY: html
html:
    jupyter-book build .


.PHONY html-hub
html-hub:
    jupyter-book config sphinx .
    sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
    cd _build/html
    python -m http.server


.PHONY : clean
clean :
    rm -rf figures/*
    rm -rf audio/*
    rm -rf _build/*
    
    
    

    


