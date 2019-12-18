# Resume and Vacancies Matching Tool

## Objective

We want to create a resume-vacancy macher based on NLP embeddings and other ML technologiess with the following API

1. Given a vacancy, create a list of resumes which match it the best
2. Extending a resumes DB implies updating the model weights

## Goals

By now the following goals are set:

1. Get a resume-vacancy database with **response history**.
2. Support different resume/vacancy formats (pdf, docx, etc) and create a proper parser
for each of the formats which probably be able to parse such features as highlighted words, headers, etc.
3. For the unified resume / vacancy models (for all the formats) create an embedding vector.
4. Use a baseline StarSpace embeddings
5. Learn the function `Resumes x Vacancies -> R`, where the output is considered to be a measure of how 
well do the resume and the vacancy match each other.
6. Clusterize the resumes according to the industry domain



## Model

There are two notebook files `src/run.ipynb` and `src/clusterization.ipynb`. First one is about the main objective while the second is about clustering, which can be done without labeled resume-vacancy dataset.

																																					
