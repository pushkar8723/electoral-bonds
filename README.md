Electoral Bonds
===============

Ported electoral bonds data released by SBI to ECI to csv (to make it easier to read and analyse).

ECI disclosed this data [here](https://www.eci.gov.in/disclosure-of-electoral-bonds)

The intent of this is to make the data more accissible to analyse using MS Excel or similar tools.

### Data & Output

I included the PDFs release by ECI inside `data` directory and the corresponding CSVs in `output` directory.

### Script

I wrote `main.py` which converted the PDFs to CSVs.
Following are the prerequisite to run this python file.
- Python 3.8+
- Java 8+
- [Tabula Python module](https://github.com/tabulapdf/tabula)

To run the script simply run 
```sh
python main.py
```

This will
- convert `data/purchaser.pdf` to `output/purchase.pdf`
- convert `data/encasher.pdf` to `output/encash.pdf`  

##### Disclaimer

- I only changed the format of the data released by ECI and have not manipulated it in anyway.
- I have also included the script I wrote for conversion.
- I don't have any affiliation to any political party / individual. 
