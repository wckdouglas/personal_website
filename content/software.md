+++
title = "software"
path = "software"
+++

As I do programming exclusively on RNA/DNA-seq experiments bioinformatics analysis, all of the softwares I wrote are mainly focus on this aspect.

# [Sequencing tools](https://github.com/wckdouglas/sequencing_tools) #

This is a python package that contains many of my day-to-day scripts and function for manuipulating SAM/BAM, Fastq, BED files from high-throughput genomic data. [[repo]](https://github.com/wckdouglas/sequencing_tools)

# [Stock profiler](https://stock-baseline.onrender.com/) #

<iframe src="https://stock-baseline.onrender.com/" style="border:none ; width: 100%; height: 400px"></iframe>

[[repo]](https://github.com/wckdouglas/wu-stock)

# UMI Design #

This is an [shiny app](https://wckdouglas.shinyapps.io/UMI_design/) to help designing unique molecular identifiers (UMI) primers. Backend of the app used poisson distribution to estimate how many times the barcode collision would occur. Idea from [Nicholas C. Wu](https://wchnicholas.github.io/)

<iframe src="https://wckdouglas.shinyapps.io/UMI_design/" style="border: none; width: 100%; height: 600px"></iframe>

[[repo]](https://github.com/wckdouglas/umi_design)



# [fdrcontrol](https://github.com/wckdouglas/fdrcontrol.git) #

This is a *R* package that I wrote to speed up FDR control in multiple hypothesis testing. Vignettes is available [here](http://rawgit.com/wckdouglas/fdrcontrol/master/vignettes/fdrcontrol.html).  [[repo]](https://github.com/wckdouglas/fdrcontrol.git)

<img src='/article_images/softwares/fdrcontrol.png'>

The package can be install via **devtools**.
```bash
devtools::install_github('wckdouglas/fdrcontrol')
```
