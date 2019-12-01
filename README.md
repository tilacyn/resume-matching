# Resume and Vacancies Matching Tool

## Introduction

Recruiters in the companies all around the world face the problem of having loads of resumes to be
looked through. This is a tedious and lingering task and that's why it probably could be automated.
Moreover obviously people tend to have mistakes and disregard some important features of the
applicants.

Many big companies nowadays design their own formats of application so that the information
could be processed easier. However this makes problems for the applicants because they have to
adjust their CV each time they apply for a new company instead of using a single document, which
would probably be constructed more attentively and carefully. Furthermore constructing your own
application form requires time and effort for the company. That's why we are looking for a way
to overcome the complexity of processing custom CV and create a tool which would allow companies
not to take care of their own way to handle applications. **Natural Language Processing** is a well known
set of technologies and it seems to be helpful in this case. We want to stick to the custom CV documents
and build an **NLP** and **Machine Learning** based tool for matching CVs and vacancies.

## Goals

By now the following goals are set:

0. Get a resume-vacancy database with **response history**.
0. Support different resume/vacancy formats (pdf, docx, etc) and create a proper parser
for each of the formats which probably be able to parse such features as highlighted words, headers, etc.
0. For the unified resume / vacancy models (for all the formats) create an embedding vector.
0. Implement a base-line (eg genetic algorithm) which is going to find pairs `<Resume, Vacancy>`, which match each other the best.
0. Learn the function `Resumes x Vacancies -> R`, where the output is considered to be a measure of how 
well do the resume and the vacancy match each other.

## Existing solutions

#### BRAC University study

The suggested approach includes CV segmentation, Data extraction and Data evaluation.

1. CV Segmentation is a process when the semi-structured CV form is parsed from a row file. This is
mostly done via Font processing, building syntax trees, etc.
2. Now when we have a segmented resume the goal is ti extract data. This can be done using syntax analysis
or simple pattern matching. Eg syntax analysis may help us to find sentences with projects / achievements /
education description. While less complicated data may be retrieved via simple pattern matching 
3. Then Data is evaluated using Decision Tree algorithm (or logistic regression)

The amount of data for system training still were very small (around 50? CVs).

#### Resume Parser with NLP (KIIT University, India)

A tool which just does resume parsing. Parsing consists of preprocessing (eg Tokenization) and NLP 
(Lexical, Syntactic and Semantic Analysis)

#### Aalto University

Objective: classifying resume data into 27 job industrial categories.

1. Embedding via word2vec (pre-trained?)
2. CNN as a classifier

Model has been trained on a dataset of job description because they lacked resumes.

#### Sovren

## Embeddings

We would like to work with numeric vectors rather than with word documents. 
There are multiple ways to interpret documents as vectors. 
They include **dense** vector representations as well as **sparse** ones. 

### TF-IDF

