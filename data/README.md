# Major data resources for CS224u, Stanford, Spring 2019

Christopher Potts

2019-03-20


## glove.6B

Available from https://nlp.stanford.edu/projects/glove/

```
@inproceedings{pennington-socher-manning:2014:EMNLP2014,
	Address = {Doha, Qatar},
	Author = {Pennington, Jeffrey and Socher, Richard and Manning, Christopher D.},
	Booktitle = {Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
	Month = {October},
	Pages = {1532--1543},
	Publisher = {Association for Computational Linguistics},
	Title = {Glo{V}e: Global Vectors for Word Representation},
	Year = {2014}}
```


## nlidata

### SNLI

https://nlp.stanford.edu/projects/snli/

@inproceedings{Bowman:Angeli:Potts:Manning:2015,
  Author = {Bowman, Samuel R.  and  Angeli, Gabor  and  Potts, Christopher  and  Manning, Christopher D.},
  Booktitle = {Proceedings of the 2015 Conference on {E}mpirical {M}ethods in {N}atural {L}anguage {P}rocessing},
  Title = {Learning Natural Language Inference from a Large Annotated Corpus},
  Year = {2015},
  Pages = {632--642},
  Location = {Lisboa, Portugal},
  Publisher = {Association for Computational Linguistics},
  Address = {Stroudsburg, PA}}


### MultiNLI

https://www.nyu.edu/projects/bowman/multinli/

```
@inproceedings{Williams-etal:2018:MultiNLI,
	Author = {Williams, Adina and Nangia, Nikita and Bowman, Samuel},
	Booktitle = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)},
	Pages = {1112--1122},
	Publisher = {Association for Computational Linguistics},
	Title = {A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference},
	Year = {2018}}
```

### SICK

http://alt.qcri.org/semeval2014/task1/index.php?id=data-and-tools

The enclosed version was prepared by Sam Bowman to conform to the SNLI/MultiNLI format.


### nli_wordentail_bakeoff_data.json

This contains data used in the following papers:

```
@inproceedings{Baroni-etal:2012,
	Address = {Avignon, France},
	Author = {Baroni, Marco and Bernardi, Raffaella and Do, Ngoc-Quynh and Shan, Chung-chieh},
	Booktitle = {Proceedings of the 13th Conference of the {E}uropean Chapter of the Association for Computational Linguistics},
	Month = {April},
	Pages = {23--32},
	Publisher = {ACL},
	Title = {Entailment Above the Word Level in Distributional Semantics},
	Year = {2012}}

@inproceedings{W11-2501,
	Author = {Baroni, Marco and Lenci, Alessandro},
	Booktitle = {Proceedings of the GEMS 2011 Workshop on GEometrical Models of Natural Language Semantics},
	Pages = {1--10},
	Publisher = {Association for Computational Linguistics},
	Title = {How we {BLESSed} distributional semantic evaluation},
	Year = {2011}}

@article{Kotlerman-etal:2010,
	Author = {Kotlerman, Lili and Dagan, Ido and Szpektor, Idan and Zhitomirsky-geffet, Maayan},
	Journal = {Nat. Lang. Eng.},
	Month = oct,
	Number = {4},
	Pages = {359--389},
	Title = {Directional Distributional Similarity for Lexical Inference},
	Volume = {16},
	Year = {2010}}

@inproceedings{W14-1610,
	Author = {Levy, Omer and Dagan, Ido and Goldberger, Jacob},
	Booktitle = {Proceedings of the Eighteenth Conference on Computational Natural Language Learning},
	Pages = {87--97},
	Publisher = {Association for Computational Linguistics},
	Title = {Focused Entailment Graphs for {Open IE} Propositions},
	Year = {2014}}

@article{Turney:Mohammad:2014,
	Author = {Turney, Peter D.  and  Mohammad, Saif M.},
	Journal = {Journal of Natural Language Engineering},
	Number = {3},
	Pages = {437--476},
	Title = {Experiments with three Approaches to Recognizing Lexical Entailment},
	Volume = {21},
	Year = {2014}}

```

## negotiate

The Deal or No Deal? dataset from Facebook AI Research: https://github.com/facebookresearch/end-to-end-negotiator


## rel_ext_data

For details on this data, see GITHUB

## trees

https://nlp.stanford.edu/sentiment/

```
@inproceedings{Socher-etal:2013,
  Location = {Seattle, WA},
  Author = {Socher, Richard  and  Perelygin, Alex  and  Wu, Jean  and  Chuang, Jason  and  Manning, Christopher D.  and  Ng, Andrew Y.  and  Potts, Christopher},
  Booktitle = {Proceedings of the 2013 Conference on {E}mpirical {M}ethods in {N}atural {L}anguage {P}rocessing},
  Month = {October},
  Publisher = {Association for Computational Linguistics},
  Address = {Stroudsburg, PA},
  Title = {Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank},
  Pages = {1631--1642},
  Year = {2013},
  Url = {http://www.aclweb.org/anthology/D13-1170}}
```

## vsmdata

For details on this data, see GITHUB

## wordsim

### WordSim-353

http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/

```
@inproceedings{Finkelstein:2001:PSC:371920.372094,
	Address = {New York, NY, USA},
	Author = {Finkelstein, Lev and Gabrilovich, Evgeniy and Matias, Yossi and Rivlin, Ehud and Solan, Zach and Wolfman, Gadi and Ruppin, Eytan},
	Booktitle = {Proceedings of the 10th International Conference on World Wide Web},
	Pages = {406--414},
	Publisher = {ACM},
	Series = {WWW '01},
	Title = {Placing Search in Context: The Concept Revisited},
	Year = {2001}}
```

### MTURK-771

http://www2.mta.ac.il/~gideon/mturk771.html

```
@inproceedings{Halawi:2012:LLW:2339530.2339751,
	Address = {New York, NY, USA},
	Author = {Halawi, Guy and Dror, Gideon and Gabrilovich, Evgeniy and Koren, Yehuda},
	Booktitle = {Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
	Pages = {1406--1414},
	Publisher = {ACM},
	Series = {KDD '12},
	Title = {Large-scale Learning of Word Relatedness with Constraints},
	Year = {2012}}
```

### SimVerb-3500

http://people.ds.cam.ac.uk/dsg40/simverb.html

```
@inproceedings{D16-1235,
	Author = {Gerz, Daniela and Vuli{\'{c}}, Ivan and Hill, Felix and Reichart, Roi and Korhonen, Anna},
	Booktitle = {Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing},
	Pages = {2173--2182},
	Publisher = {Association for Computational Linguistics},
	Title = {SimVerb-3500: A Large-Scale Evaluation Set of Verb Similarity},
	Year = {2016}}
```

### MEN

http://clic.cimec.unitn.it/~elia.bruni/MEN

```
@article{Bruni:2014:MDS:2655713.2655714,
	Author = {Bruni, Elia and Tran, Nam Khanh and Baroni, Marco},
	Journal = {Journal of Artificial Intelligence Research},
	Month = jan,
	Number = {1},
	Pages = {1--47},
	Title = {Multimodal Distributional Semantics},
	Volume = {49},
	Year = {2014}}
```
