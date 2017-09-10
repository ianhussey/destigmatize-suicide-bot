# Destigmatize suicide bot

*A bot to decrease stigmatising language around suicide on Wikipedia*



## Overview and purpose

The reporting and portrayal of suicide in the media are known to influence real world suicidal behaviour ([Biddle et al., 2008](http://www.bmj.com/content/336/7648/800)). Because of this, the World Health Organisation & International Association for Suicide Prevention provide simple [guidelines](http://www.who.int/mental_health/prevention/suicide/resource_media.pdf) for how to speak about suicide in the media and public discourse. A number of published articles suggesting these guidelines have proven effective in combatting suicidal behaviour (e.g., [Wu & Yip, 2008](http://onlinelibrary.wiley.com/doi/10.1521/suli.2008.38.5.631/full)). This effort is also occuring internally within the academic literature on suicidology, although not as quickly as one might hope ([Nielsen, Padmanathan, & Knipe, 2017](https://wellcomeopenresearch.org/articles/1-21/v1)).

The internet is now an important source of information regarding suicide (Biddle et al., 2008), but these guidelines have not yet seen widespread use online. This is due in part to the distributed and decentralised nature of online content creation. However, some large sites provide a useful target. In particular, Wikipedia combines three useful properties: 1) it is used to access information by millions of people every day, 2) it allows users to create and alter its content, and 3) this editing is frequently performed automatically by bots. 

This repository is an attempt to build a wikipedia bot to automatically monitor and correct unhelpful language around suicide on Wikipedia, in line with the International Network of Early Career Researchers in Suicide and Self-harm's (netECR) [Commit to Change](https://netecr.wordpress.com/2017/09/07/commit-to-change-wikipedia-edit-a-thon/) Wikipedia edit-a-thon.

Ideally we would create a fully automated wiki bot that crawls and edits without needing supervision. In the first instance, I'll use Pywikibot (below) to scrape information from Wikipedia to potentially help organise manual editing activities. 



## Contributors and license

- Ian Hussey (ian.hussey@ugent.be)
- All content is distributed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) and code under [the Unlicense](http://unlicense.org/) - use as you please.



## Possible language to target on wikipedia

### Inspiration

From the WHO guidelines:

*"Such language should not sensationalize suicide. Terms like ‘increasing rates’ should be used in preference to hyperbolic phrases like ‘suicide epidemic’, and caution should be exercised in using the word ‘suicide’ in headlines. Language that misinforms the public about suicide or normalizes it should be avoided. Out-of-context use of the word ‘suicide’ – e.g., ‘political suicide’ – may serve to desensitize the community to its gravity. Terms like ‘unsuccessful suicide’ imply that death is a desirable outcome and should not be used; alternative phrases such as ‘non-fatal suicide attempt’ are more accurate and less open to misinterpretation. The phrase ‘committed suicide’ should not be used because it implies criminality, thereby contributing to the stigma experienced by those who have lost a loved one to suicide and discouraging suicidal individuals from seeking help. Rather, one should refer to ‘completed suicide’. Suicide remains a criminal offence in some countries around the world."* (pp. 7-8).

### Ideas for specific targets

- "commit suicide" to "die by suicide"
- "committed suicide" to "died by suicide"
- "unsuccessful suicide attempt" to "non-fatal suicide attempt"
- "failed suicide attempt" to "non-fatal suicide attempt"



## Pywikibot

Here I used [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot), a python library for editing wikipedia.

Pywikibot can be run locally or in the cloud via PAWS (Pywikibot: A Web Shell). I'm using PAWS as it requires less setup. A guide is available [here](https://www.mediawiki.org/wiki/Manual:Pywikibot/PAWS).

*Note to self: my PAWS instance is available [here](https://paws.wmflabs.org/paws/user/ianhussey/notebooks/Wiki%20suicide%20bot%20management.ipynb).*



### Find list of pages that contain strings

Documentation for function [here](https://www.mediawiki.org/wiki/Manual:Pywikibot/listpages.py).

Working example:

~~~python
pwb.py listpages -lang:en -ns:0 -search:"committed suicide" 
~~~

- `-lang:en` english language articles only
- `-ns:0` articles only, no talk pages etc.
- `-search` search for string 

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

This data might be useful in 1) organising manual editing activities, and/or 2) choose targets for automated correction.

File names are descriptive and can be found in the `scraped data` folder.

### list of pages containing "committed suicide".csv

- 9328 pages. Suggests this would be a huge amount of work by hand.

### list of pages containing "committed suicide" whose title contains "suicid".csv

- 49 pages. Possibly a useful starting point.



## To do

- Refine and test the get and replace strings code.
- Decide on a summary of changes test that is maximally informative to maximise the changes that our changes are not undone by other editors. E.g., reference to published literature showing that these guidelines are effective, rather than a call for language orthodoxy (which is sometimes seen as an instance of identity politics, and aversive to some audiences).
- Chose more specific targets.
- Get others from netECR involved, and/or provide data to netECR to aid others' efforts.