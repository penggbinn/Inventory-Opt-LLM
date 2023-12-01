# Results from Task-1

- For more generic questions, both models adopt a systematic approach to answering the question. The answers
have also been detailed and well explained.

- GPT-3.5 mentions that the interdependencies captured are conceptual and may vary based on real world data and 
information while BARD does not.

- BARD generated python code does not work. It is also unable to add visualization code. The changes had to be done
manually.

- GPT-3.5 code works 90% of the time and is bale to accommodate visualization code.

- BARD is good at understanding the user requirements and provides good answers, however unlike GPT-3.5 who remembers 
previous information to a certain extent, BARD is unable to do so. (Context: Different contextual queries)

- Both models generate very different results when the same query is run in another window, except when the API 
is used. (API Not Tested)

- Sometimes, the models generated dependencies involving self loops and produced code which did not accommodate 
self loops and did not know how to debug.

- Upon attempting to generate CPT tables, both models declare that the information is based on their understanding 
of the factors and that they may vary according to the real world data.

