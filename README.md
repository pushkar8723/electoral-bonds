Electoral Bonds
===============

Ported electoral bonds data released by SBI to ECI to CSV (to make it easier to read and analyze).

ECI disclosed this data [here](https://www.eci.gov.in/disclosure-of-electoral-bonds)

The intent of this is to make the data more accessible for analysis using MS Excel or similar tools.

---

### Data & Output

I included the PDFs released by ECI inside `data` directory and the corresponding CSVs in `output` directory.

#### Script

I wrote `main.py` which converted the PDFs to CSVs.
The following are the prerequisites to run this Python file.
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

---

### Dashboard

I also created dashboards using [Metabase](https://github.com/metabase). These dashboards can be easily run and accessed locally and it also supports a few filters.

[Instructions to run the dasbhoard](https://github.com/pushkar8723/electoral-bonds/tree/main/dashboard)

Note: Dashboard is independent from the Python script. Hence you can directly run the dashboard by following the instructions above.

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/e89a109f-4952-4380-8cc9-ce4053257ef7)

![image](https://github.com/pushkar8723/electoral-bonds/assets/2996493/31d341a2-d91c-4875-9448-fcc5ef19c99b)

---

### Future Plan

Currently, there is no link between who donated and to whom. This should be available once the bond ids are released by SBI.
I will update this repo one the data is available in the public domain.

---

##### Disclaimer

- I only changed the format of the data released by ECI and have not manipulated it in any way.
- I have also included the script I wrote for conversion.
- I don't have any affiliation to any political party/individual. 
