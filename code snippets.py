# https://www.mediawiki.org/wiki/Manual:Pywikibot
# https://www.mediawiki.org/wiki/Manual:Pywikibot/replace.py
# https://www.mediawiki.org/wiki/Manual:Pywikibot/listpages.py

# https://paws.wmflabs.org/paws/user/ianhussey/notebooks/Wiki%20suicide%20bot%20management.ipynb



# semi working

pwb.py replace \
-lang:en \
-ns:0 \
-simulate \
-search:"committed suicide" "committed suicide" "died by suicide" \
-summary:"Changed stigmatising language based on reccomended media guidelines" 

# -lang:en english language articles only
# -ns:0 articles only, no talk pages
# -simulate simulate the changes for the moment
# -search:"committed suicide" "committed suicide" "died by suicide" find pages that include the first string, then replace the second string with the third
# -summary saved summary
