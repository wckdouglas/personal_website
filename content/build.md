+++
title = "Building computing environment"
path = "build"
+++

This page contains the instruction for building my favourite computing environment on a Linux cluster.

The workflow greatly depends on [**conda**](http://conda.pydata.org/miniconda.html) and thus should not require root access.

Better solution is to download this [gist repository](https://gist.github.com/wckdouglas/9430411adf5ad312f75f681b371b14ff) and install by:

    conda install --file=${pacakge file}

Table of content:

- [Conda](#conda)
- [Python](#python)
- [R](#rstat)
- [Vim](#vim)
- [tmux](#tmux)
- [tinytex](#tex)
- [windows](#win)
- [apple silicon](#Apple)
- [docker](#docker)
- [poetry](#poetry)

<h1 id='conda'> Conda  </h1>

```bash
export LINK=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
curl -o miniconda_install.sh $LINK
sh miniconda_install.sh
```

# Add Channels

```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels anaconda
conda config --add channels conda-forge
```

<h1 id='python'> Python 3.6 & Packages </h1>

```bash
conda install -c bioconda -c defaults -c anaconda \
	python=3.6 scipy matplotlib numpy \
	seaborn pybedtools pysam pymc3 \
	biopython pandas scikit-learn pybigwig \
	jupyter	statsmodels h5py rpy2 bokeh \
	dask numexpr cython snakemake pytest xopen \
	ipykernel scikit-bio pyranges ujson
python -m ipykernel install --user --name miniconda3 --display-name "miniconda3"
```

# Bio-softwares

```bash
conda install -c bioconda hisat2 seqtk \
	bowtie2=2.2.5 atropos bedtools bowtie \
	bamtools samtools bwa seqkit \
	picard fastqc datamash csvtk \
	parallel bwameth pileometh \
	viennarna cutadapt blast \
	ucsc-wigtobigwig ucsc-bedtogenepred \
	ucsc-gtftogenepred ucsc-genepredtobed \
	ucsc-bigwigtobedgraph ucsc-bigwigtowig \
	ucsc-bedgraphtobigwig
```

## Developement environment for OSS contributions

`conda` has a nice feature allowing creation of [isolated virtual environments](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) for doing dirty experimental developmental work, so nothing will be broken in the day-time working environment.

```bash
conda create -n ${DEV_ENV_NAME} cython pytest ipython #create development envrionment
conda activate ${DEV_ENV_NAME}                           #activate development environment
### do something to break the software....
conda deactivate                                         #goes back to normal enviroment
```

## Deep learning with Keras/TensorFlow

Building environment for using [TensorFlow](https://www.tensorflow.org/install/install_linux) and [Keras](https://keras.io).

```bash
conda create -n tensorflow pip python3
conda activate tensorflow
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.6.0-cp36-cp36m-linux_x86_64.whl keras
conda install numpy scikit-learn \
			pandas ipykernel \
			matplotlib seaborn \
			pysam pybigwig \
			ujson cython
## add jupyter kernel
python -m ipykernel install --user --name tensorflow --display-name "tensorflow"
```

<h1 id='rstat'> Rstat </h1>

```bash
conda install r-tidyverse r-caret r-stringi \
	bioconductor-deseq2 r-bit64
```

## Probablistic modeling

```bash
conda create -n prob \
    pymc3 pandas arviz \
    matplotlib seaborn scipy \
    statsmodels ipykernel
```

```bash
conda create -n jax \
    jax flax optax matplotlib \
    scikit-learn pandas seaborn \
    funsor numpyro arviz
```

### To use conda R in Rstudio

On mac OSX, _Rstudio_ will not recognize _R_ from conda installation, since it only search $PATH from: **/usr/bin/R, /usr/local/bin/R** and **/opt/local/bin/R**.

To tell _Rstudio_ to use the _R_ installation from conda on OSX:

A. Put this line in **${HOME}/.profile**

```bash
export RSTUDIO_WHICH_R=/Users/wckdouglas/miniconda2/bin/R
```

B. Tell OSX to assign `$RSTUDIO_WHICH_R` to Rstudio (in Terminal, login shell)

```bash
launchctl setenv RSTUDIO_WHICH_R $RSTUDIO_WHICH_R
```

<h1 id='vim'> Vim </h1>

- pathogen
- nerdtree
- supertab
- solarized
- airline
- seiya (transparent background)

### install.sh

```bash
#!/bin/bash

#install pathogen
mkdir -p ~/.vim/autoload ~/.vim/bundle ~/.vim/syntax && \
	curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
cd ~/.vim/bundle &&

#install nerdTree
git clone https://github.com/scrooloose/nerdtree.git

#install superTab
git clone https://github.com/ervandew/supertab.git

#install solarized
git clone https://github.com/altercation/vim-colors-solarized.git

#install airline
git clone https://github.com/bling/vim-airline

#install seiya (transparent backgroun)
git clone https://github.com/miyakogi/seiya.vim.git


#install vim-one
git clone https://github.com/rakr/vim-one.git


#install snakemake syntax
cd ~/.vim/syntax
wget https://mstamenk.github.io/assets/files/snakemake.vim

#install mypy
git clone https://github.com/integralist/vim-mypy ~/.vim/bundle/vim-mypy
```

### .vimrc

```
execute pathogen#infect()
syntax on
filetype plugin indent on

map <C-n> :NERDTreeToggle<CR>
map <C-m> :set background=light<CR>
map <C-b> :set background=dark<CR>

"let g:airline#extensions#tabline#enabled = 1
"let g:airline#extensions#tabline#left_sep = ' '
"let g:airline#extensions#tabline#left_alt_sep = '|'
let g:AirLineTheme='one'

set t_Co=256
"let g:solarized_termcolors=256
set background=dark
colorscheme one

" space
set tabstop=4       " The width of a TAB is set to 4.
                    " Still it is a \t. It is just that
                    " Vim will interpret it to be having
                    " a width of 4.
set shiftwidth=4    " Indents will have a width of 4
set softtabstop=4   " Sets the number of columns for a TAB
set expandtab       " Expand TABs to spaces

"a combination of spaces and tabs are used to simulate tab stops at a width
"other than the (hard)tabstop
set hlsearch
set backspace=indent,eol,start
set number
au BufEnter /private/tmp/crontab.* setl backupcopy=yes
set laststatus=2
let g:seiya_auto_enable=1
""" prevent closing window when using VIM panes
nnoremap <C-e> <C-w>


au BufNewFile,BufRead Snakefile set syntax=snakemake
au BufNewFile,BufRead *.snake set syntax=snakemake
au BufNewFile,BufRead *.smk set syntax=snakemake
```

<h1 id='tmux'> TMUX </h1>

### Install powerline

```bash
conda install -c bioconda tmux  ncurses
pip3 install powerline-status
```

### configurate tmux

Copy and paste the following code to `~/.tmux.conf`

```bash
# change prefix, I like using ctrl + a, osx can also map ctrl to caps lock key
unbind-key C-b
set -g  prefix C-a
bind-key C-a send-prefix
set -g default-terminal "screen-256color"
#set-window-option -g xterm-keys on
#set-option -g renumber-windows on

# clear key for new bindings
unbind-key p
unbind-key t
unbind-key i
unbind-key s
unbind-key j
unbind-key l
unbind-key w
unbind-key f
unbind-key n
setw synchronize-panes off

# pane movements
bind-key s splitw -h -p 50  -c "#{pane_current_path}"
bind-key i splitw -v -p 50  -c "#{pane_current_path}"
bind-key f break-pane
bind-key j join-pane -h -p 50 -s !
bind-key w killp
bind-key t new-window  -c "#{pane_current_path}"
bind-key n new-window  -c "#{pane_current_path}"

set-window-option -g mode-keys vi
#bind-key -t vi-copy 'v' begin-selection
#bind-key -t vi-copy 'y' copy-selection
bind-key p paste-buffer


#vim integration
# Smart pane switching with awareness of vim splits
set-option -g status-interval 3
set-option -g status-justify centre
set-option -g status-left-length 90
set-option -g status-right-length 60
set-window-option -g window-status-current-format "#[fg=colour234, bg=colour234]#[fg=colour255, bg=colour4] ??? #I:#W #[fg=colour27, bg=colour234]"
set-window-option -g window-status-format  "#[fg=colour234, bg=colour234]#[fg=colour255, bg=colour234] #I:#W #[fg=colour234, bg=colour234]"
set -g status-bg colour234
set -g status-fg colour255
set -g status-right '#[fg=colour231,bg=colour234] %d/%m #[fg=colour231,bg=colour234] %H:%M:%S '
```

<h1 id='tex'> tinytex </h1>

A very lightweight latex (great for my chromebook) framework by [Yihui Xie](https://yihui.name/tinytex/). Great alternative to the 3Gb [MacTex](http://www.tug.org/mactex/) or [texlive-full](http://milq.github.io/install-latex-ubuntu-debian).

```bash
curl -sL "https://github.com/yihui/tinytex/raw/master/tools/install-unx.sh" | sh
```

<h1 id='win'> Windows Subsystem for Linux </h1>

- Open powershell as admin and type:

```bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

- Get OpenSUSE-42, and run it to install:

  1. Vim data

     ```bash
     sudo zypper install vim-data
     ```

  2. wsl-open

     ```bash
     sudo zypper install -yqq npm
     sudo npm install -g wsl-open
     ```

# SSHFS for windows

- Install WinFsp
- Install [SSHFS-Win](https://github.com/billziss-gh/sshfs-win)
- Mount root directory, from file explorer

```bash
\\sshfs\USERNAME@HOST\..\..\
```

# Useful alias

```bash
alias git-tree='git log --oneline --decorate --all --graph'
```

# Ipython

setting how many pandas columns showing in ipython

```python
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
```

<h1 id='Apple'> Apple Silicon </h1>

## conda

Conda can be installed with [miniforge](https://github.com/conda-forge/miniforge/releases) to accomodate the m1 ARM chip. However, many of the bio tools won't be able to install easily through conda (bioconda).

## python

```bash
mamba install python=3.9 scikit-learn dask  pandas numpy scipy
```

## JAX

```bash
pip install -U https://storage.googleapis.com/jax-releases/mac/jaxlib-0.1.74-cp39-none-macosx_11_0_arm64.whl
pip install jax
```

## numpyro

```bash
mamba install numpyro
```

## jupyter kernel

```bash
KERNEL_NAME=bfx
conda activate ${ENV}
python -m ipykernel install --user --name $KERNEL_NAME --display-name $KERNEL_NAME
```

<h2 id='docker'> Docker </h2>

```bash
# on apple silicon macs
export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```

shell into images:

```bash
docker run --entrypoint /bin/bash -i -t  ${image}
```

<h1 id='poetry'> Poetry </h1>

commands extracted from [[here]](https://python-poetry.org/docs)

- Installation:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

- oh-my-zsh completion:

```bash
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
```

- individual venv at repo:

```bash
poetry config virtualenvs.path .venv
```
