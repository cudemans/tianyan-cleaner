# Tianyancha-cleaner

This package works with [tianyancha-scraper](https://github.com/simprisms/tianyancha-scraper) to clean scraped data.
It forms part of a project that to look at international investments by Chinese companies. As a result, the package subsets international investments.

It can take both CSV and JSONs as inputs

`from cleandata import CleanTianyanData`

`data = CleanTianyanData('data.json')`

To return a dataframe of cleaned data, run:

`data.process_internationals()`
