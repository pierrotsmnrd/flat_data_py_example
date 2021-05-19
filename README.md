# Using python as postprocess script for Github's Flat Data actions


This repository demonstrates how to run a python script as postprocess step for Github's Flat Data actions.

The idea is basic : Use Deno to trigger the execution of a python script.

This example also shows how to install requirements and write a new file.


## Execution :

- the Flat Data action is scheduled daily, and download the BTC prices data (as seen in [Github Octo's example](https://github.com/githubocto/flat-demo-bitcoin-price/)) and stores it in `btc-price.json`

- the `postprocess.ts` script is then run, triggers the install of python packages, and runs the main python script `postprocess.py`. it also forwards the arguments.

- `postprocess.py` prints out its received arguments, and then generates a dummy output CSV file `df_output.csv`, for the sake of the example.


## Next steps, ideas and TODOs :
- make an example using conda

## Thanks

- Thanks to the Github Octo Team for [their friendly advices on Twitter](https://twitter.com/pierrotsmnrd/status/1394890851659177984?s=20) 

