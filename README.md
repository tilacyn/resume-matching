# Resume and Vacancies Matching Tool

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

### BRAC University study

## Embeddings

We would like to work with numeric vectors rather than with word documents. 
There are multiple ways to interpret documents as vectors. 
They include **dense** vector representations as well as **sparse** ones. 

### TF-IDF

