This repository contains data belonging to the REMINDS project, including datasets, scripts, and report documents.

Follow the instructions carefully in order to setup the local development environment. These instructions are intended for UNIX based systems. For Windows users, instructions might be a little different. All of the implemented code uses the 2.x version of the Python programming language and sometimes the Java programming language. So make sure these are environment are properly installed.

##### Install and create a virtual envinonment (required to install python packages later and keep them in a single place)

```bash
sudo pip install virtualenv
virutalenv venv
source venv/bin/activate
```

## Comparing the Performance of Different NLP Toolkits in Formal and Social Media Text ##############


The file run_evaluations.sh present in Experiments/Evaluation/ is the main script that evaluates the different toolkit and outputs the performance results.

It is a collection of calls from another python program called averaged_evaluation.py

```bash
usage: averaged_evaluation.py [-h] -r REFERENCE -p PREDICTED
	
NLP Evaluation
	
optional arguments:
	  -h, --help            show this help message and exit
	  -r REFERENCE, --reference REFERENCE
	                        Reference filename
	  -p PREDICTED, --predicted PREDICTED
	                        Predicted filename
```

Evaluation Program for generic NLP tasks. Each file is a collection of tagged
sentences. Each line has a word and a tag separated by space and each phrase
is separated by an empty line.

It is important to note that this program only evaluates results (predicted file) against a gold standard (reference file). The results are obtained using the NLP toolkits.

Each of the following folder contains the needed scripts and datasets to evaluate a specific tool. Each test dataset contains two nested folders: compare and results. The 'compare' folder contains the results obtained by the tool and the 'results' folder contains the performance evaluation results.  
```
├── apache_opennlp
│   ├── evaluate.sh
│   ├── opennlp_chunk.py
│   ├── opennlp_pos.py
│   ├── perform_nlp_taks.sh
├── aritter
│   ├── aritter_chunk.py
│   ├── aritter_ner.py
│   ├── aritter_pos.py
│   ├── nlp_tasks.sh
├── cmu_tweet_nlp
│   ├── cmu_tweetnlp.py
├── nltk_eval
│   ├── nltk_chunk.py
│   ├── nltk_ner.py
│   ├── nltk_pos.py
│   ├── nltk_report.py
│   ├── perform_nlp_tasks.sh
├── OntoText
│   ├── perform_nlp_tasks.sh
│   ├── twitie.py
├── pattern
│   ├── pattern_chunk.py
│   ├── pattern_pos.py
│   ├── perform_nlp_tasks.sh
├── spaCy
│   ├── perform_nlp_tasks.sh
│   ├── spacy_chunk.py
│   ├── spacy_ner.py
│   ├── spacy_pos.py
├── stanford_nlp
│   ├── cmu_tweetnlp.py
│   ├── nlp_tasks.sh
│   ├── stanford_nlp_ner.py
│   ├── stanford_nlp_pos.py
│   ├── stanford_nlp.py
```

The folder 'statistics' contains a script stats.py used to gather statistics from the datasets.
