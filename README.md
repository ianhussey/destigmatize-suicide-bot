# Destigmatize suicide bot

*A bot to decrease stigmatising language around suicide on Wikipedia*



## Overview and purpose

The reporting and portrayal of suicide in the media are known to influence real world suicidal behaviour ([Biddle et al., 2008](http://www.bmj.com/content/336/7648/800)). Because of this, the World Health Organisation & International Association for Suicide Prevention provide simple [guidelines](http://www.who.int/mental_health/prevention/suicide/resource_media.pdf) for how to speak about suicide in the media and public discourse. A number of published articles suggesting these guidelines have had an impact on how the media reports and portrays suicide (e.g., [Wu & Yip, 2008](http://onlinelibrary.wiley.com/doi/10.1521/suli.2008.38.5.631/full)), and even the occurance of suicial behaviour in the real world (e.g., [Niederkrotenthaler & Sonneck, 2007](http://journals.sagepub.com/doi/abs/10.1080/00048670701266680)). This effort is also occuring internally within the academic literature on suicidology, although not as quickly as one might hope ([Nielsen, Padmanathan, & Knipe, 2017](https://wellcomeopenresearch.org/articles/1-21/v1)).

The internet is now an important source of information regarding suicide (Biddle et al., 2008), but these guidelines have not yet seen widespread use online. This is due in part to the distributed and decentralised nature of online content creation. However, some large sites provide a useful target. In particular, Wikipedia combines three useful properties: 1) it is used to access information by millions of people every day, 2) it allows users to create and alter its content, and 3) this editing is frequently performed automatically by bots. 

This repository is an attempt to build a wikipedia bot to automatically monitor and correct unhelpful language around suicide on Wikipedia, in line with the International Network of Early Career Researchers in Suicide and Self-harm's (netECR) [Commit to Change](https://netecr.wordpress.com/2017/09/07/commit-to-change-wikipedia-edit-a-thon/) Wikipedia edit-a-thon. This effort has a dual purpose: it's proximal goal is activism (i.e., an attempt to destigmatise suicide), and the more distal goal of indirectly influencing suicidal behaviour.

This repository is a working document for this work in progress. Ideally we would create a fully automated wiki bot that crawls and edits without needing supervision. In the first instance, I'll use Pywikibot (below) to scrape information from Wikipedia to potentially help organise manual editing activities. 



## Contributors and license

- Ian Hussey (ian.hussey@ugent.be)
- All content is distributed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) and code under [the Unlicense](http://unlicense.org/) - use as you please.



## Possible language to target on wikipedia

### Inspiration

From the WHO guidelines:

*"Such language should not sensationalize suicide. Terms like ‘increasing rates’ should be used in preference to hyperbolic phrases like ‘suicide epidemic’, and caution should be exercised in using the word ‘suicide’ in headlines. Language that misinforms the public about suicide or normalizes it should be avoided. Out-of-context use of the word ‘suicide’ – e.g., ‘political suicide’ – may serve to desensitize the community to its gravity. Terms like ‘unsuccessful suicide’ imply that death is a desirable outcome and should not be used; alternative phrases such as ‘non-fatal suicide attempt’ are more accurate and less open to misinterpretation. The phrase ‘committed suicide’ should not be used because it implies criminality, thereby contributing to the stigma experienced by those who have lost a loved one to suicide and discouraging suicidal individuals from seeking help. Rather, one should refer to ‘completed suicide’. Suicide remains a criminal offence in some countries around the world."* (pp. 7-8).

### Ideas for specific targets

- "commit suicide" to "die by suicide"
- "commits suicide" to "dies by suicide"
- "committed suicide" to "died by suicide"
  - Is it worth searching for common misspellings too? 
- "unsuccessful suicide" [attempt] to "non-fatal suicide" [attempt]
- "failed suicide" [attempt]  to "non-fatal suicide" [attempt]



## Pywikibot

Here I used [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot), a python library for editing wikipedia.

### Usage

#### Cloud based instances

Pywikibot can be run locally or in the cloud via PAWS (Pywikibot: A Web Shell). I'm using PAWS as it requires less setup. A guide is available [here](https://www.mediawiki.org/wiki/Manual:Pywikibot/PAWS).

*Note to self: my PAWS instance is available [here](https://paws.wmflabs.org/paws/user/ianhussey/notebooks/Wiki%20suicide%20bot%20management.ipynb).*

#### Local installations

To run locally, after installation:

1. Change to the directory of your local installation. For me, this is:

```shell
cd ~/Pywikibot/core 
```

2. Then simply make your function calls (using example from below):

```shell
python pwb.py listpages -lang:en -ns:0 -search:"committed suicide" | tee ~/git/destigmatize-suicide-bot/scraped_data/pages_commited_suicide.txt
```

Where `command | tee output.txt` shows the output in the terminal and also writes it to the specified file.

NB I'm still working on how to call this within a python script executed from within Atom, etc.

### Find list of pages that contain strings

Documentation for function [here](https://www.mediawiki.org/wiki/Manual:Pywikibot/listpages.py).

### Working examples:

PAWS:

~~~python
pwb.py listpages -lang:en -ns:0 -search:"committed suicide" 
~~~

Local:

```shell
python pwb.py listpages -format:3 -lang:en -ns:0 -search:"failed suicide" | tee ~/git/destigmatize-suicide-bot/data/scraped_data/pages_failed_suicide.txt
```

- `command | tee output.txt` shows the output in the terminal and also writes it to the specified file.


- `-lang:en` english language articles only


- `-ns:0` articles only, no talk pages etc.
- `-search` search for string 
- `-format:3` output only the name of the page, not the page count

Possibly useful additional parameters:

- `-limit:100` limit the number of results returned
- `-grep:"committed suicide"` search using regular expressions (throwing missing generator error?)




### Find and replace strings, provide summary of changes

Documentation for function [here](https://www.mediawiki.org/wiki/Manual:Pywikibot/replace.py).

(semi) working example:

```python
pwb.py replace \
-lang:en \
-ns:0 \
-simulate \
-search:"committed suicide" "committed suicide" "died by suicide" \
-summary:"Changed stigmatising language based on reccomended media guidelines" 
```

- `-lang:en` english language articles only
- `-ns:0` articles only, no talk pages etc.
- `-simulate` only simulate the changes, don't do them for real.
- `-search:"committed suicide" "committed suicide" "died by suicide"` find pages that include the first string, then replace the second string with the third
- `-summary` the summary saved


**IMPORTANT**: There are strict rules around editing wikipedia using bots. The above code is very easy to implement, but until we're confident that we know what we're doing here we should be cautious. Breaking the rules risks brining negative attention from the editors who might not favour future attempts, not to mention having all our changes undone and accounts banned.



## Scraped data

### Searches run

This data might be useful in 1) organising manual editing activities, and/or 2) choose targets for automated correction. An example of the former would be to use the (highly optimised) page search to find a list of candidate pages, and then use the (far slower) find and replace function to find and replace strings on these pages.  

Search terms that have been run (locally) and their code are listed below:

#### "failed suicide"

~~~shell
python pwb.py listpages -format:3 -lang:en -ns:0 -search:"failed suicide" | tee ~/git/destigmatize-suicide-bot/data/scraped_data/pages_failed_suicide.txt
~~~

#### "unsuccessful suicide"

```shell
python pwb.py listpages -format:3 -lang:en -ns:0 -search:"unsuccessful suicide" | tee ~/git/destigmatize-suicide-bot/data/scraped_data/pages_unsuccessful_suicide.txt
```

#### "committed suicide"

```shell
python pwb.py listpages -format:3 -lang:en -ns:0 -search:"committed suicide" | tee ~/git/destigmatize-suicide-bot/data/scraped_data/pages_committed_suicide.txt
```



### Data wrangling

I then use R to wrangle this data into a more meaningful format, using the `process data scraped from Wikipedia.Rmd` R markdown file.

This releals that when the page names for these three searches are combined and duplicates discarded, >17,000 pages still meet these searches (see `scraped_data/processed/unique pages meeting one or more criteria.csv`). 

If we retain only those pages that also include "suicid" in the title, this leaves 61 results (see `scraped_data/processed/pages with suicid in title.csv`). These could be a good place to start for manual editing or ideas for other strings to target with a bot. 



## To do

- Refine and test the get and replace strings code.
- Decide on a summary of changes test that is maximally informative to maximise the changes that our changes are not undone by other editors. E.g., reference to published literature showing that these guidelines are effective, rather than a call for language orthodoxy (which is sometimes seen as an instance of identity politics, and aversive to some audiences).
- Chose more specific targets.
- Get others from netECR involved, and/or provide data to netECR to aid others' efforts.
- Figure out execution of local python scripts from within Atom, etc. This would allow me to scrape directly to local files, increasing reproducability and cutting down on copy-pasting and associated issues. See https://www.mediawiki.org/wiki/Manual:Pywikibot/Create_your_own_script